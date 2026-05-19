# 🛍️ Flipkart Product Recommender Chatbot

> AI-powered product recommendation chatbot using RAG (Retrieval-Augmented Generation) with Groq's Llama 3 model and AstraDB vector database.

![Python](https://img.shields.io/badge/Python-3.11-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-green)
![LangChain](https://img.shields.io/badge/LangChain-RAG-orange)
![Groq](https://img.shields.io/badge/Groq-Llama3-purple)
![AstraDB](https://img.shields.io/badge/AstraDB-VectorDB-blue)
![Docker](https://img.shields.io/badge/Docker-Containerized-blue)
![Kubernetes](https://img.shields.io/badge/Kubernetes-Minikube-blue)

---

## 🚀 Live Demo
[(https://flipkart-product-recommender-chatbot-hsgp.onrender.com/)]

---

## 📌 Problem Statement

Online shoppers struggle to find the right products among millions of listings. Manual searching is time-consuming and overwhelming. This AI chatbot provides instant, personalized product recommendations based on natural language queries.

---

## ✅ Features

- Natural language product search
- RAG-powered accurate recommendations
- Real-time chat with conversation history
- Product source attribution
- Quick suggestion buttons
- Responsive Flipkart-styled UI
- Containerized with Docker
- Deployed on Kubernetes (Minikube)
- Prometheus + Grafana monitoring

---

## 🛠️ Tech Stack

| Technology | Purpose |
|-----------|---------|
| Python 3.11 | Core language |
| FastAPI | Backend REST API |
| HTML + CSS + JS | Frontend UI |
| LangChain | RAG pipeline |
| Groq API (Llama 3) | AI language model |
| HuggingFace | Text embeddings |
| AstraDB | Vector database |
| Docker | Containerization |
| Kubernetes (Minikube) | Orchestration |
| Prometheus | Metrics collection |
| Grafana | Monitoring dashboard |
| GitHub | Version control |

---

## 📁 Project Structure

```
flipkart-chatbot/
├── backend/
│   ├── main.py              # FastAPI server
│   ├── rag_pipeline.py      # RAG + Groq AI logic
│   ├── data_ingestion.py    # AstraDB data upload
│   └── logger.py            # Custom logging
├── frontend/
│   ├── index.html           # Chat UI
│   ├── style.css            # Flipkart styling
│   └── script.js            # Chat logic
├── data/
│   └── flipkart_products.csv # Product dataset
├── k8s/
│   ├── deployment.yaml      # K8s deployment
│   ├── service.yaml         # K8s service
│   ├── prometheus.yaml      # Prometheus config
│   └── grafana.yaml         # Grafana dashboard
├── requirements.txt         # Dependencies
├── Dockerfile               # Container config
├── ingest.py                # Data ingestion script
├── .env.example             # Environment template
└── README.md                # Documentation
```

---

## 📊 System Architecture

```
User (Browser)
      ↓
HTML/CSS/JS Frontend
      ↓
FastAPI Backend
      ↓
LangChain RAG Pipeline
      ↓
HuggingFace Embeddings
      ↓
AstraDB Vector Search
      ↓
Groq LLM (Llama 3)
      ↓
Product Recommendations
```

---

## ⚙️ How to Run Locally

### Prerequisites
- Python 3.11+
- Groq API key — free at console.groq.com
- HuggingFace token — free at huggingface.co
- AstraDB account — free at astra.datastax.com

### Setup

```bash
# 1. Clone repo
git clone https://github.com/your-username/flipkart-chatbot.git
cd flipkart-chatbot

# 2. Create virtual environment
python -m venv .venv
.venv\Scripts\activate  # Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Add your API keys
cp .env.example .env
# Edit .env and add all keys

# 5. Upload products to AstraDB
python ingest.py

# 6. Start server
uvicorn backend.main:app --reload
```

Open browser: `http://localhost:8000`

---

## 🐳 Docker

```bash
# Build image
docker build -t flipkart-chatbot .

# Run container
docker run -p 8000:8000 --env-file .env flipkart-chatbot

# Open browser
# http://localhost:8000
```

---

## ☸️ Kubernetes (Minikube)

```bash
# Start Minikube
minikube start

# Create secrets
kubectl create secret generic chatbot-secret \
  --from-literal=groq-key=your_groq_key \
  --from-literal=astra-token=your_astra_token

# Deploy app
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml

# Get app URL
minikube service flipkart-chatbot --url
```

---

## 📊 Monitoring

```bash
# Deploy Prometheus + Grafana
kubectl apply -f k8s/prometheus.yaml
kubectl apply -f k8s/grafana.yaml

# Access Grafana
# http://localhost:3000
```

---

## 🌍 Environment Variables

Create a `.env` file:

```
GROQ_API_KEY=your_groq_api_key_here
HUGGINGFACE_TOKEN=your_huggingface_token_here
ASTRA_DB_API_ENDPOINT=your_astra_endpoint_here
ASTRA_DB_APPLICATION_TOKEN=your_astra_token_here
ASTRA_DB_COLLECTION=flipkart_products
```

---

## 🔄 How RAG Works

```
User asks: "Best mobile under 20000"
        ↓
HuggingFace converts query to vector
        ↓
AstraDB finds similar product vectors
        ↓
Top 4 relevant products retrieved
        ↓
Groq LLM generates recommendation
        ↓
"Samsung Galaxy M34 5G at Rs.18999..."
```

---

## 📈 What I Learned

- Building RAG pipelines with LangChain
- Vector database setup with AstraDB
- Text embeddings with HuggingFace
- FastAPI backend development
- Docker containerization
- Kubernetes deployment with Minikube
- Prometheus + Grafana monitoring
- Frontend development with HTML/CSS/JS

---

## 🔮 Future Improvements

- Add user authentication
- Price comparison feature
- Product image display
- Order tracking integration
- Multi-language support
- Voice search capability
- Mobile app version

---

## 👤 Author

**Your Name**
- GitHub: [github.com/your-username](https://github.com/your-username)
- LinkedIn: [linkedin.com/in/your-profile](https://linkedin.com/in/your-profile)

---

## ⭐ Star this repo if you found it helpful!
