# AI-Powered Career and Branding Suite

## Overview

AI-Powered Career and Branding Suite is a comprehensive tool designed to assist users in their career development journey. It offers:

- 🧠 **Autonomous Job Application Agent**
- 📄 **AI-Driven Resume and Portfolio Builder**
- 🗣️ **AI-Powered Interview Intelligence for Recruiters**

This suite simplifies the career growth process with cutting-edge AI technologies, making job applications, resume building, and candidate evaluation seamless and efficient.

---

## Features

### 1. Autonomous Job Application Agent

The job application agent automates job discovery and applications:

- Matches jobs based on resume and skills.
- Automatically fills job applications.
- Tracks application statuses.

### 2. AI-Driven Resume and Portfolio Builder

- Helps create ATS-friendly resumes.
- Supports multimedia portfolios to portray users as a **personal brand**.
- Suggests role-specific enhancements.
- Enables quick customization based on job descriptions.

### 3. AI-Powered Interview Intelligence (Tech Interview Assistant)

Specifically designed for **recruiters**, this module assists in evaluating candidates:

- 📌 **Resume Evaluation** — Checks if a resume matches the job description.
- 💬 **Interview Questions** — Generates 10 questions (technical + non-technical).
- 🔁 **Follow-up Questions** — Dynamically created after candidate's answers.
- 💻 **Coding Section** — Provides a challenge and evaluates candidate's solution.
- 📊 **Final Evaluation** — Summarizes performance across all sections.

---

## Installation

### Prerequisites

- Python 3.8+
- pip package manager

### Create and Activate Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Set Up Environment Variables
Create a .env file in your project root.

### Run the App
```bash
streamlit run Home.py
```

### Project Structure
```
app
├── pages/
│    └── Autonomous Job Application Agent.py
│    └── AI Driven Resume & Portfolio Builder.py
│    └── AI-Powered Interview Intelligence.py
├── services/
│   └── genai_services.py
│   └── prompt.py
├── Home.py
├── .env
├── Dockerfile
├── requirements.txt
└── README.md
```
### Future Enhancements
- Text-to-Speech Evaluation for interview responses.
- Smart Agent Memory for personalized job matching.
- Branded Portfolio Templates with themes and animations.
- Automatic JD Parsing from URLs or job portals.

### Contributing
Contributions are welcome! Please fork the repository and submit a pull request. For major changes, open an issue first to discuss what you'd like to change.

## Contact
For inquiries or support, reach out to **yajatgrover@gmail.com**