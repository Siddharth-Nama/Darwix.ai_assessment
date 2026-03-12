## 2. Agent/Customer Dashboard (UX Concept)

**Goal**: Give agents a single screen that eliminates all context-switching. Everything they need is in one place.

### Screen Layout (3-Column Design)

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  HEADER: Search customer | Active Queues: 14 | My Conversations: 3 | ⚙️     │
├──────────────┬──────────────────────────────────────┬───────────────────────┤
│              │                                      │                       │
│  LEFT PANEL  │          CENTER PANEL                │     RIGHT PANEL       │
│  Interaction │          Active Chat                 │     AI Copilot        │
│  Timeline    │                                      │                       │
│              │  Channel Icon | Customer Name        │  🧠 Intent:           │
│  10:15 AM    │  WhatsApp • Active Now               │  Refund Status        │
│  💬 WA       │                                      │                       │
│  "Where is   │  ┌──────────────────────────────┐   │  😟 Sentiment:        │
│  my refund?" │  │ Aarav: Where is my refund     │   │  Negative (0.72)      │
│              │  │ for order #1234? I ordered    │   │                       │
│  Yesterday   │  │ last week…                    │   │  📋 Suggested Reply:  │
│  📞 Voice    │  └──────────────────────────────┘   │  "Hi Aarav, I've      │
│  Return      │                                      │  located your return. │
│  requested   │  ┌──────────────────────────────┐   │  It will be credited  │
│  for #1234   │  │ Agent Types Here...           │   │  in 3-5 days. Can I  │
│              │  └──────────────────────────────┘   │  help with anything   │
│  Mon, Mar 4  │                                      │  else?" [Use Reply]   │
│  📧 Email    │  [ Send ]  [ Escalate ]  [ Close ]  │                       │
│  Shipping Q  │                                      │  🔮 Next Best Action: │
│              │                                      │  Offer 10% coupon     │
│              │                                      │  (Churn Risk: 🔴 High)│
└──────────────┴──────────────────────────────────────┴───────────────────────┘
```

### Key Components:
- **Left Panel (Timeline)**: Scrollable history of all cross-channel interactions (Task 1).
- **Center Panel (Live Chat)**: The active conversation window. Real-time WebSocket updates.
- **Right Panel (AI Copilot)**:
  - Displays detected **Intent** and **Sentiment score**.
  - Shows a **Draft Reply** AI generated from RAG pipeline, with a one-click "Use Reply" button.
  - Shows **Churn Risk Score** and a **Next Best Action** recommendation.
- **Escalation Button**: One-click escalation to supervisor with auto-generated summary.
