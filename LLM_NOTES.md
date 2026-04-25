# LLM Usage Notes

## 🛠 Tools Used

* ChatGPT

---

## 💬 Example Prompts (Paraphrased)

1. "How to build a FastAPI POST endpoint with validation using Pydantic?"
2. "Simple rule-based scoring logic for loan eligibility system"
3. "React form submission with API call using Axios"
4. "How to structure a full-stack project with backend and frontend separation"
5. "How to write basic pytest unit tests for FastAPI endpoints"

---

## 🔍 How LLM Was Used

* Generated initial boilerplate code for:

  * FastAPI backend
  * React frontend
* Assisted in designing scoring logic structure
* Helped with validation rules and test cases
* Suggested improvements for UI and code organization

---

## ✏️ What I Reviewed / Modified

* Adjusted scoring weights to ensure output stays within 0–100
* Ensured exactly 3 reason codes are returned
* Improved validation constraints using Pydantic fields
* Fixed frontend API integration issues
* Enhanced UI for better readability (score card layout)

---

## ⚠️ Example Correction

Initial LLM output did not strictly enforce:

* Returning exactly 3 reason codes

Fix:

* Explicitly limited output using slicing:

```python
reasons[:3]
```

---

## 🧠 Key Takeaway

LLM tools were used as assistants for speed, but all outputs were:

* Reviewed critically
* Tested manually
* Adapted to meet problem constraints

---
