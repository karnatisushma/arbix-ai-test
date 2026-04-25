# 🌾 SaakhSetu Scoring App (Arbix AI Practical Test)

---

## 🎯 Overview

This project is a simple end-to-end scoring application built as part of the Arbix AI Full-Stack AI Engineer practical exercise.

It consists of:

* A **Python backend (FastAPI)** for scoring logic
* A **React frontend** for user input and result display

The system evaluates basic agricultural and financial inputs to generate:

* A **score (0–100)**
* **3 explainable reason codes**

---

## ⚙️ Tech Stack

* Backend: Python, FastAPI
* Frontend: React (Vite), Axios
* Testing: Pytest

---

## 🚀 How to Run

### Backend

```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload
```

Backend runs at:

```
http://localhost:8000
```

---

### Frontend

```bash
cd frontend
npm install
npm run dev
```

Frontend runs at:

```
http://localhost:5173
```

---

## 🧠 Scoring Logic

The scoring is rule-based and designed for clarity and explainability:

* **Repayment History (50%)**

  * High → positive impact
  * Low → negative impact

* **Land Area**

  * > 5 acres → higher contribution
  * ≤5 acres → lower contribution

* **Income Band**

  * Higher income → higher score contribution

Final score is capped between **0 and 100**.

---

## 🧾 Reason Codes

The system returns exactly **3 reason codes**, representing key contributing factors:

* `good_repayment` / `poor_repayment`
* `large_landholding` / `small_landholding`
* `high_income` / `mid_income` / `lower_mid_income` / `low_income`

---

## ✅ Validation & Error Handling

Validation is handled using **Pydantic models**, ensuring:

* `land_area_acres > 0`
* `repayment_history_score ∈ [0, 100]`
* `crop_type` is non-empty
* `annual_income_band` is one of allowed values

Invalid inputs return appropriate **4xx errors**.

---

## 📊 Audit Logging

Each request is logged with:

* `request_id`
* input fields
* score
* reason codes
* timestamp

Logging is implemented using Python’s built-in `logging` module.

---

## 🧪 Tests

Basic unit tests included:

* ✅ Happy path test (valid input)
* ❌ Validation test (invalid input)

Run tests:

```bash
cd backend
pytest
```

---

## 🎨 Frontend Features

* Input form for all required fields
* API integration using Axios
* Loading state handling
* Error handling
* Clean result display with score and reason codes
* Improved UI with card-based result component

---

## ⚖️ Design Choices & Tradeoffs

* Chose **FastAPI** for fast development and built-in validation
* Used **rule-based scoring** instead of ML for simplicity and clarity
* Limited UI complexity to focus on functionality within time constraints
* Used **structured logging** instead of persistent storage to save time

---

## ❌ What I Skipped (and Why)

* Database integration → avoided to stay within time-box
* Advanced UI/UX → prioritized backend correctness
* Docker setup → not essential for core functionality

---

## 🔧 What I Would Improve (with 2 more hours)

* Add database (SQLite/Postgres) for storing requests
* Improve frontend UX with better validation feedback
* Add more comprehensive test coverage
* Introduce configurable scoring weights
* Add authentication and API security
* Implement basic model explainability enhancements

---

## 🤖 LLM / Tool Usage Disclosure

* Used ChatGPT for:

  * Structuring backend and frontend components
  * Generating initial boilerplate code
  * Refining validation and scoring logic

* All generated code was:

  * Reviewed
  * Tested manually
  * Modified to fit requirements

See `LLM_NOTES.md` for details.

---

## 🙌 Summary

This project focuses on:

* Clean engineering structure
* Validation and correctness
* Explainable outputs
* Practical, production-oriented thinking

---
