import React, { useState } from 'react';
import './App.css';
import axios from 'axios';

interface QueryResponse {
  query: string;
  drugs_identified: string[];
  query_type: string;
  response: string;
  sources_used: number;
}

interface DrugInteractionResponse {
  drug1: string;
  drug2: string;
  interaction_found: boolean;
  interactions: any[];
  response: string;
  sources: string[];
}

const API_BASE_URL = 'http://localhost:8000';

function App() {
  const [query, setQuery] = useState('');
  const [drug1, setDrug1] = useState('');
  const [drug2, setDrug2] = useState('');
  const [loading, setLoading] = useState(false);
  const [response, setResponse] = useState<QueryResponse | DrugInteractionResponse | null>(null);
  const [activeTab, setActiveTab] = useState<'general' | 'interaction'>('general');
  const [error, setError] = useState('');

  const handleGeneralQuery = async () => {
    if (!query.trim()) return;
    
    setLoading(true);
    setError('');
    try {
      const res = await axios.post<QueryResponse>(`${API_BASE_URL}/query`, {
        query: query
      });
      setResponse(res.data);
    } catch (err: any) {
      setError(err.response?.data?.detail || 'An error occurred');
    }
    setLoading(false);
  };

  const handleInteractionCheck = async () => {
    if (!drug1.trim() || !drug2.trim()) return;
    
    setLoading(true);
    setError('');
    try {
      const res = await axios.post<DrugInteractionResponse>(`${API_BASE_URL}/check-interaction`, {
        drug1: drug1,
        drug2: drug2
      });
      setResponse(res.data);
    } catch (err: any) {
      setError(err.response?.data?.detail || 'An error occurred');
    }
    setLoading(false);
  };

  return (
    <div className="App">
      <header className="App-header">
        <h1>Medicine & Drug Interaction Advisor</h1>
        <p>Get instant answers about medications, interactions, and side effects</p>
      </header>

      <div className="container">
        <div className="tabs">
          <button 
            className={`tab ${activeTab === 'general' ? 'active' : ''}`}
            onClick={() => {setActiveTab('general'); setResponse(null); setError('');}}>
            General Query
          </button>
          <button 
            className={`tab ${activeTab === 'interaction' ? 'active' : ''}`}
            onClick={() => {setActiveTab('interaction'); setResponse(null); setError('');}}>
            Check Drug Interaction
          </button>
        </div>

        {activeTab === 'general' ? (
          <div className="query-section">
            <h2>Ask About Medications</h2>
            <div className="input-group">
              <input
                type="text"
                placeholder="e.g., What are the side effects of metformin?"
                value={query}
                onChange={(e) => setQuery(e.target.value)}
                onKeyPress={(e) => e.key === 'Enter' && handleGeneralQuery()}
              />
              <button onClick={handleGeneralQuery} disabled={loading}>
                {loading ? 'Searching...' : 'Ask'}
              </button>
            </div>
            <div className="examples">
              <p>Example queries:</p>
              <ul>
                <li>What is ibuprofen used for?</li>
                <li>Side effects of amoxicillin</li>
                <li>How much acetaminophen can I take?</li>
                <li>Metformin warnings and precautions</li>
              </ul>
            </div>
          </div>
        ) : (
          <div className="interaction-section">
            <h2>Check Drug Interactions</h2>
            <div className="interaction-inputs">
              <input
                type="text"
                placeholder="First drug (e.g., ibuprofen)"
                value={drug1}
                onChange={(e) => setDrug1(e.target.value)}
              />
              <span className="and">AND</span>
              <input
                type="text"
                placeholder="Second drug (e.g., amoxicillin)"
                value={drug2}
                onChange={(e) => setDrug2(e.target.value)}
              />
              <button onClick={handleInteractionCheck} disabled={loading}>
                {loading ? 'Checking...' : 'Check Interaction'}
              </button>
            </div>
          </div>
        )}

        {error && (
          <div className="error">
            <p>{error}</p>
          </div>
        )}

        {response && (
          <div className="response-section">
            <h3>Response</h3>
            <div className="response-content">
              <p>{response.response}</p>
              
              {'drugs_identified' in response && response.drugs_identified.length > 0 && (
                <div className="metadata">
                  <p><strong>Drugs identified:</strong> {response.drugs_identified.join(', ')}</p>
                  <p><strong>Query type:</strong> {response.query_type}</p>
                  <p><strong>Sources used:</strong> {response.sources_used}</p>
                </div>
              )}
              
              {'interaction_found' in response && (
                <div className="metadata">
                  <p><strong>Interaction found:</strong> {response.interaction_found ? 'Yes' : 'No'}</p>
                  <p><strong>Sources:</strong> {response.sources.join(', ')}</p>
                </div>
              )}
            </div>
            <div className="disclaimer">
              <p><strong>Disclaimer:</strong> This information is for educational purposes only. Always consult with a healthcare professional before making any decisions about medications.</p>
            </div>
          </div>
        )}
      </div>
    </div>
  );
}

export default App;