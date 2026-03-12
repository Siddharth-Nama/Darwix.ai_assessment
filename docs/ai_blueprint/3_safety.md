## Safety, Accuracy, and HITL (Human-in-the-Loop) Plan

To deploy AI in a customer-facing environment safely, strict guardrails are implemented.

### 1. Data Privacy & PII Masking
- **Mechanism**: Before any customer message is sent to an external generative LLM, a local Presidio-based Named Entity Recognition (NER) model scrubs Personally Identifiable Information (PII) such as credit card numbers, social security numbers, and precise addresses.
- **Benefit**: Ensures GDPR/CCPA compliance and prevents data leaks to third-party AI vendors.

### 2. Guardrails Against Hallucination
- **Retrieval-Augmented Integrity**: The primary LLM is restricted via system prompts to *only* use facts present in the retrieved Knowledge Base chunks.
- **Verification Step (Self-Correction)**: A secondary lightweight LLM grades the output of the primary LLM against the source documents. If the alignment score is below 95%, the output is blocked from reaching the user.

### 3. Human-in-the-Loop (HITL) Thresholds
- **Confidence Scoring**: Every AI action prediction generates a confidence score based on historical training data.
- **Threshold Policy**:
  - `> 95% Confidence`: Automatic execution (e.g., answering "What are your business hours?").
  - `80% - 94% Confidence`: Drafted response is shown to the human agent on the dashboard for approval and one-click sending (Agent Copilot mode).
  - `< 80% Confidence`: The AI skips generation and strictly routes the interaction to a specialized human agent.
- **Continuous Learning**: Every time a human agent edits a drafted response, that diff is logged. This data is periodically used to fine-tune the Intent and RAG models.
