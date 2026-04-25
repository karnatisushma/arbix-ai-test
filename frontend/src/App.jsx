import { useState } from "react";
import { api } from "./api";
import "./App.css";

function App() {
  const [form, setForm] = useState({
    land_area_acres: "",
    crop_type: "",
    repayment_history_score: "",
    annual_income_band: "<2L"
  });

  const [result, setResult] = useState(null);
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(false);

  const handleChange = (e) => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  const handleSubmit = async () => {
    setLoading(true);
    setError("");
    setResult(null);

    try {
      const res = await api.post("/score", {
        ...form,
        land_area_acres: Number(form.land_area_acres),
        repayment_history_score: Number(form.repayment_history_score)
      });
      setResult(res.data);
    } catch (err) {
      setError("Something went wrong. Check inputs.");
    }

    setLoading(false);
  };

  return (
    <div className="container">
      <h2>🌾 SaakhSetu Scoring</h2>

      <input name="land_area_acres" placeholder="Land Area (acres)" onChange={handleChange} />
      <input name="crop_type" placeholder="Crop Type" onChange={handleChange} />
      <input name="repayment_history_score" placeholder="Repayment Score (0-100)" onChange={handleChange} />

      <select name="annual_income_band" onChange={handleChange}>
        <option>&lt;2L</option>
        <option>2-5L</option>
        <option>5-10L</option>
        <option>&gt;10L</option>
      </select>

      <button onClick={handleSubmit} disabled={loading}>
        {loading ? "Processing..." : "Get Score"}
      </button>

      {error && <p className="error">{error}</p>}

      {result && (
        <div className="result-card">
            <h2 className="score-title">Your Score</h2>
            
            <div className="score-value">
            {result.score}
            </div>

            <div className="reasons">
            <h4>Key Factors</h4>
            <ul>
                {result.reason_codes.map((r, i) => (
                <li key={i} className="reason-item">{r}</li>
                ))}
            </ul>
            </div>
        </div>
        )}
    </div>
  );
}

export default App;