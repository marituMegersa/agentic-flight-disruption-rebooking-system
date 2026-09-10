from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.domain.flight_disruption_rebooking_system.schemas import AgenticFlightDisruptionRebookingSystemSessionCreate, AgenticFlightDisruptionRebookingSystemSessionResponse
from app.domain.flight_disruption_rebooking_system.service import AgenticFlightDisruptionRebookingSystemService

router = APIRouter(prefix="/api/v1/flight_disruption_rebooking_system", tags=["Agentic Flight Disruption Rebooking System Domain"])

@router.post("/sessions", response_model=AgenticFlightDisruptionRebookingSystemSessionResponse, status_code=status.HTTP_201_CREATED)
def create_domain_session(data: AgenticFlightDisruptionRebookingSystemSessionCreate, db: Session = Depends(get_db)):
    """
    Creates a new FastAPI domain session for Agentic Flight Disruption Rebooking System.
    """
    return AgenticFlightDisruptionRebookingSystemService.create_session(db, data)

@router.get("/sessions/{session_id}", response_model=AgenticFlightDisruptionRebookingSystemSessionResponse)
def get_domain_session(session_id: str, db: Session = Depends(get_db)):
    obj = AgenticFlightDisruptionRebookingSystemService.get_session(db, session_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Domain session not found")
    return obj
