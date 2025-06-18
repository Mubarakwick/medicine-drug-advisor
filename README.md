# 🏥 Medicine & Drug Interaction Advisor

An AI-powered comprehensive medicine database and drug interaction checker with special focus on Indian medicines and mental health medications. Built with FastAPI, React, and RAG (Retrieval-Augmented Generation) architecture.

![Python](https://img.shields.io/badge/python-v3.8+-blue.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-0.104.1-green.svg)
![React](https://img.shields.io/badge/React-18.2.0-blue.svg)
![License](https://img.shields.io/badge/license-MIT-blue.svg)

## 🌟 Features

### 🔍 Comprehensive Drug Database
- **45+ Medications** including Indian brands
- **20+ Mental Health Drugs**: Antidepressants, Anti-anxiety, Antipsychotics, Mood stabilizers
- **Indian Medicines**: Crocin, Combiflam, Pan 40, Ecosprin, and more
- **Ayurvedic Options**: Ashwagandha, Triphala, Tulsi

### 💊 Advanced Features
- **Drug Interaction Checker**: Check safety of drug combinations
- **Pill Identifier**: Identify pills by appearance
- **Medicine by Condition**: Browse drugs by health condition
- **Voice Search**: Search medicines using voice
- **Price Information**: Indian market prices in INR
- **Prescription Status**: Know which drugs need prescription

### 🧠 Mental Health Focus
- Comprehensive information on psychotropic medications
- Controlled substance warnings
- Detailed side effects and interactions
- Dosage guidelines

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- Node.js 14+
- Git

### Backend Setup

1. Clone the repository:
```bash
git clone https://github.com/yourusername/medicine-drug-advisor.git
cd medicine-drug-advisor
```

2. Set up Python virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install backend dependencies:
```bash
cd backend
pip install -r requirements.txt
```

4. Set up environment variables:
```bash
cp .env.example .env
# Add your OpenAI API key to .env (optional for enhanced features)
```

5. Run the backend server:
```bash
python enhanced_main.py
```

The API will be available at `http://localhost:8000`

### Frontend Setup

1. Navigate to frontend directory:
```bash
cd ../frontend
npm install
```

2. Start the development server:
```bash
# Open the enhanced HTML file in your browser
open enhanced-index.html  # On Mac
# Or simply double-click the enhanced-index.html file
```

## 📋 API Endpoints

### Core Endpoints

- `POST /query` - Process natural language queries about medicines
- `POST /check-interaction` - Check interactions between two drugs
- `GET /drug/{drug_name}` - Get detailed information about a specific drug
- `GET /mental-health-drugs` - List all mental health medications
- `GET /search/{category}` - Search drugs by category
- `GET /all-drugs` - Get complete drug list

### Example Queries

```bash
# Check drug information
curl -X POST http://localhost:8000/query \
  -H "Content-Type: application/json" \
  -d '{"query": "What are the side effects of sertraline?"}'

# Check drug interaction
curl -X POST http://localhost:8000/check-interaction \
  -H "Content-Type: application/json" \
  -d '{"drug1": "alprazolam", "drug2": "alcohol"}'
```

## 🧪 Sample Medications

### Mental Health Drugs
- **Antidepressants**: Sertraline (Zoloft), Fluoxetine (Prozac), Escitalopram (Lexapro)
- **Anti-anxiety**: Alprazolam (Xanax), Clonazepam (Klonopin), Lorazepam (Ativan)
- **Antipsychotics**: Quetiapine (Seroquel), Olanzapine (Zyprexa), Risperidone (Risperdal)
- **Mood Stabilizers**: Lithium, Valproate (Depakote), Carbamazepine (Tegretol)

### Common Indian Medicines
- **Pain/Fever**: Crocin, Dolo 650, Combiflam
- **Acid/Gastric**: Pan 40, Omez
- **Antibiotics**: Azithral, Augmentin
- **Heart/BP**: Ecosprin, Amlodipine

## 🏗️ Architecture

```
medicine-drug-advisor/
├── backend/
│   ├── enhanced_main.py          # FastAPI application
│   ├── comprehensive_drug_database.py  # Drug database
│   ├── rag_pipeline.py          # RAG implementation
│   ├── vector_db.py            # FAISS vector database
│   └── requirements.txt
├── frontend/
│   ├── enhanced-index.html     # Main UI (dark theme)
│   └── index.html             # Alternative UI
└── README.md
```

## 🔧 Technology Stack

- **Backend**: FastAPI, Python, LangChain, FAISS
- **Frontend**: HTML5, Tailwind CSS, JavaScript
- **Database**: In-memory comprehensive drug database
- **APIs**: FDA OpenFDA, RxNorm (optional)

## 🚨 Important Notes

### Medical Disclaimer
This tool is for educational and informational purposes only. Always consult with qualified healthcare professionals before making any medical decisions.

### Controlled Substances
Some medications in the database are controlled substances. These require special prescriptions and have strict regulations.

### Data Sources
- FDA approved drug information
- Indian pharmaceutical databases
- Clinical drug interaction databases

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- FDA OpenFDA for drug label data
- RxNorm for drug interaction data
- Indian pharmaceutical companies for drug information
- Open source community for amazing tools

## 📧 Contact

Your Name - [@yourtwitter](https://twitter.com/yourtwitter)

Project Link: [https://github.com/yourusername/medicine-drug-advisor](https://github.com/yourusername/medicine-drug-advisor)

---

**⚠️ Medical Disclaimer**: This application provides general information only. It is not intended as medical advice. Always consult healthcare professionals for medical decisions.