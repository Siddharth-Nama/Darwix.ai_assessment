## AI Model Usage

To balance speed, cost, and accuracy, the system employs a multi-model routing strategy rather than relying on a single massive LLM for every task.

### 1. Intent & Sentiment Routing (The "Smart Triage")
- **Model**: Fine-tuned lightweight models (e.g., Llama-3-8B or customized BERT).
- **Function**: Processes every incoming message to extract an intent taxonomy tag (Refund, Inquiry, Complaint) and a sentiment valence (Positive, Neutral, Negative, Urgent).
- **Why**: Low-latency and highly cost-effective for millions of messages a day.

### 2. Retrieval-Augmented Generation (RAG) Engine
- **Model**: Large Language Models (e.g., GPT-4o, Claude 3.5 Sonnet, or Llama-3-70B).
- **Function**: Drafts personalized replies based on the `Intent`, reading from the vector database (KB articles) and the SQL database (order history).
- **Usage**: Used only when the Intent router determines the query requires a generative response.

### 3. Embeddings Model
- **Model**: BGE-M3 (or OpenAI `text-embedding-3-large`).
- **Function**: Converts company policies, FAQs, and product manuals into semantic vectors for the vector database. Allows the RAG engine to pull the correct paragraphs when answering a question.

### 4. Next Best Action (Predictive AI)
- **Model**: Classical Machine Learning (XGBoost/Random Forest).
- **Function**: Examines the customer's purchase frequency and current sentiment to predict if offering a discount or free shipping will save a churning customer. Used specifically by the Agent Copilot to display recommendations on the dashboard.
