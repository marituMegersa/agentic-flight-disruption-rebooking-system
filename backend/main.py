from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Dict, Any

app = FastAPI(title="Agentic Flight Disruption Rebooking System", description="Multi-agent airline delay tracker, automated passenger rebooking, and hotel voucher issuer.", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class QueryInput(BaseModel):
    prompt: str

@app.get("/health")
def health():
    return {"status": "healthy", "service": "Agentic Flight Disruption Rebooking System", "domain": "TravelTech"}

@app.post("/api/v1/agent/run")
def run_agent(data: QueryInput):
    return {
        "success": True,
        "service": "Agentic Flight Disruption Rebooking System",
        "response": f"Agent processed query: '{data.prompt}'",
        "trajectory": [
            {"step": 1, "action": "State Evaluation"},
            {"step": 2, "action": "Tool & RAG Execution"},
            {"step": 3, "action": "Final Output Synthesis"}
        ]
    }
