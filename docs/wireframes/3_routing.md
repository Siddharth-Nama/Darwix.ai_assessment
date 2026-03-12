## 3. Escalation and Routing UX Flow

**Goal**: Ensure customers with complex or high-emotion issues are seamlessly handed off to the right human agent, with no friction and full context preserved.

### Escalation Trigger Rules (Automated)
- Sentiment score drops below **0.3** (very negative) mid-conversation.
- Customer explicitly uses trigger phrases like "speak to a human", "manager", "this is unacceptable".
- AI confidence score for the current request falls below **80%**.
- The issue has been open for more than **2 AI turns** without resolution.

### Routing UX Flow

```
Customer sends message
        │
        ▼
  Intent & Sentiment Classifier
        │
        ├── Sentiment > 0.5 AND Confidence > 80%
        │         │
        │         ▼
        │    AI handles directly → Response sent
        │
        └── Sentiment < 0.3 OR Confidence < 80% OR Trigger Phrase Detected
                  │
                  ▼
         ESCALATION INITIATED
                  │
                  ▼
         AI generates TL;DR summary
         (e.g., "Customer frustrated about delayed refund for order #1234,
                  initiated on WhatsApp, pending 7 days")
                  │
                  ▼
         Smart Routing Engine
                  │
                  ├── Tag: "Billing" → Routes to Billing Specialist Queue
                  ├── Tag: "Technical" → Routes to Tech Support Queue
                  └── Tag: "General" → Routes to next available Agent
                  │
                  ▼
         Agent receives notification with:
         - TL;DR summary
         - Full cross-channel timeline
         - Current sentiment gauge
         - Pre-drafted response to start from
                  │
                  ▼
         Agent joins chat / calls back
                  │
                  ▼
         Resolution logged → Closes ticket → Updates KB if needed
```

### Agent Perspective During Escalation
- A prominent toast notification appears: `"New Escalation: Aarav S. — Refund Delay (Negative Sentiment)"`
- The conversation auto-opens with the AI summary already visible at the top.
- The agent is never starting cold; they always have context from the first second.
