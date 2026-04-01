# AI Code Reviewer

An AI-powered code review tool built with Python and Reflex framework.

## Live Demo

Deployed App: https://ai-code-reviewer-gold-moon.reflex.run

## Features

- Automated code analysis using Python AST
- AI-powered suggestions using Groq LLM
- Code quality scoring (0-100)
- Bug and issue detection
- Corrected code generation
- Analysis history tracking

## Tech Stack

- Frontend and Backend: Reflex (Python)
- AI Model: Groq LLaMA
- Database: PostgreSQL (Neon.tech)
- Deployment: Reflex Cloud

## Project Structure
AI_Code_Reviewer/
├── components/
│   ├── analyze.py
│   ├── history.py
│   ├── navbar.py
│   ├── hero.py
│   ├── about.py
│   └── footer.py
├── state.py
├── models.py
├── code_analyzer.py
└── AI_Code_Reviewer.py
## Setup and Installation
pip install -r requirements.txt
reflex run