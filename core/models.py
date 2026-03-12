from django.db import models
import uuid


class Customer(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200)
    email = models.EmailField(unique=True, null=True, blank=True)
    phone = models.CharField(max_length=20, unique=True, null=True, blank=True)
    lifetime_value = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    churn_risk = models.FloatField(default=0.0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Interaction(models.Model):
    CHANNEL_WHATSAPP = 'whatsapp'
    CHANNEL_WEB = 'web'
    CHANNEL_EMAIL = 'email'
    CHANNEL_VOICE = 'voice'

    CHANNEL_CHOICES = [
        (CHANNEL_WHATSAPP, 'WhatsApp'),
        (CHANNEL_WEB, 'Web Chat'),
        (CHANNEL_EMAIL, 'Email'),
        (CHANNEL_VOICE, 'Voice'),
    ]

    STATUS_OPEN = 'open'
    STATUS_AI_RESOLVED = 'ai_resolved'
    STATUS_ESCALATED = 'escalated'
    STATUS_CLOSED = 'closed'

    STATUS_CHOICES = [
        (STATUS_OPEN, 'Open'),
        (STATUS_AI_RESOLVED, 'AI Resolved'),
        (STATUS_ESCALATED, 'Escalated to Agent'),
        (STATUS_CLOSED, 'Closed'),
    ]

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='interactions')
    channel = models.CharField(max_length=20, choices=CHANNEL_CHOICES)
    content = models.TextField()
    intent_label = models.CharField(max_length=100, null=True, blank=True)
    sentiment_score = models.FloatField(null=True, blank=True)
    ai_confidence = models.FloatField(null=True, blank=True)
    suggested_reply = models.TextField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=STATUS_OPEN)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return f"{self.customer.name} via {self.channel} — {self.intent_label}"
