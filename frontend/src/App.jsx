import { useState } from "react";
import "./App.css";

function App() {
  const [file, setFile] = useState(null);
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const analyzeDocument = async () => {
    if (!file) {
      setError("Please select a PDF file.");
      return;
    }

    setLoading(true);
    setError("");
    setResult(null);

    const formData = new FormData();
    formData.append("file", file);

    try {
      const response = await fetch("http://127.0.0.1:8000/analyze", {
        method: "POST",
        body: formData,
      });

      if (!response.ok) {
        throw new Error("Document analysis failed.");
      }

      const data = await response.json();
      setResult(data);
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="container">
      <h1>OCR Document AI</h1>
      <p>Upload a PDF and let AI analyze your document.</p>

      <input
        type="file"
        accept=".pdf"
        onChange={(event) => {
          setFile(event.target.files[0]);
          setResult(null);
          setError("");
        }}
      />

      <button onClick={analyzeDocument} disabled={loading}>
        {loading ? "Analyzing..." : "Analyze Document"}
      </button>

      {error && <p className="error">{error}</p>}

      {result && (
        <div className="result">
          <h2>Analysis Result</h2>

          <h3>Document Type</h3>
          <p>{result.analysis.document_type}</p>

          <h3>Summary</h3>
          <p>{result.analysis.summary}</p>

          <h3>Important Information</h3>

          <div className="information">
            {Object.entries(
              result.analysis.important_information || {}
            ).map(([key, value]) => (
              <p key={key}>
                <strong>{key}:</strong>{" "}
                {typeof value === "object"
                  ? JSON.stringify(value)
                  : String(value)}
              </p>
            ))}
          </div>

          <h3>Extracted OCR Text</h3>
          <pre>{result.extracted_text}</pre>
        </div>
      )}
    </div>
  );
}

export default App;