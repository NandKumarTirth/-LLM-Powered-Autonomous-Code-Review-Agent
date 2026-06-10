# 🤖 LLM-Powered Autonomous Code Review Agent

An intelligent code review platform that combines Python static code analysis with Gemini LLM to evaluate source code quality, identify potential issues, generate contextual recommendations, and produce automated review reports.

The project was developed to explore software quality assessment, static code analysis, Large Language Models (LLMs), and interactive dashboard development using Streamlit.

---

## 🚀 Features

- Upload and analyze Python source code files
- Static code analysis using Python AST
- Detect missing docstrings and maintainability issues
- Calculate code quality score and grade
- Generate AI-powered code reviews using Gemini LLM
- Provide contextual recommendations for code improvement
- Interactive Streamlit dashboard
- Generate downloadable PDF review reports
- Automated review status and final verdict generation

---

## 🛠️ Tech Stack

- Python
- Streamlit
- Gemini API
- AST (Abstract Syntax Tree)
- ReportLab
- Git & GitHub

---

## ⚙️ How It Works

```text
Upload Python File
        ↓
Static Analysis (AST)
        ↓
Code Quality Assessment
        ↓
Gemini LLM Review
        ↓
Recommendations & Insights
        ↓
PDF Report Generation
```

---

## 📊 Analysis Metrics

The system evaluates:

- Total Lines of Code
- Number of Functions
- Number of Classes
- Missing Docstrings
- Function Complexity Indicators
- Code Quality Score
- Overall Grade
- Review Status

---

## 🤖 Gemini AI Review

The application integrates Google's Gemini model to provide:

- Code quality assessment
- Potential issue identification
- Best practice recommendations
- Readability improvements
- Final code review verdict

Unlike rule-based suggestions, the LLM generates contextual feedback based on the uploaded source code.

---

## 📄 PDF Report

Generated reports include:

- Review Summary
- Quality Score
- Grade
- Status
- Detected Issues
- AI Recommendations
- Final Verdict

---

## 📂 Project Structure

```text
LLM-Powered-Autonomous-Code-Review-Agent
│
├── app.py
├── analyzer.py
├── llm_reviewer.py
├── report_generator.py
├── test.py
├── README.md
└── requirements.txt
```

---

## ▶️ Installation

Clone the repository:

```bash
git clone https://github.com/NandKumarTirth/LLM-Powered-Autonomous-Code-Review-Agent.git
```

Move to the project directory:

```bash
cd LLM-Powered-Autonomous-Code-Review-Agent
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run app.py
```

---

## 🔑 Environment Setup

Create a Gemini API key from Google AI Studio and configure it before running the application.

```python
API_KEY = "YOUR_GEMINI_API_KEY"
```

For production usage, storing API keys in environment variables is recommended.

---

## 🎯 Future Enhancements

- Multi-language code support
- Pylint integration
- Code complexity analysis
- GitHub repository review support
- Advanced analytics dashboard
- LLM-powered PDF insights

---

## 👨‍💻 Author

**Nand Kumar Tirth**

MCA Student | Artificial Intelligence & Machine Learning Enthusiast

GitHub: https://github.com/NandKumarTirth
