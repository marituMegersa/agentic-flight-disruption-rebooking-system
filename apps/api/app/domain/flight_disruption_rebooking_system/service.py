from sqlalchemy.orm import Session
import uuid
import datetime
from app.domain.flight_disruption_rebooking_system.models import AgenticFlightDisruptionRebookingSystemSession, AgenticFlightDisruptionRebookingSystemItem
from app.domain.flight_disruption_rebooking_system.schemas import AgenticFlightDisruptionRebookingSystemSessionCreate, AgenticFlightDisruptionRebookingSystemItemCreate

class AgenticFlightDisruptionRebookingSystemService:
    @staticmethod
    def create_session(db: Session, data: AgenticFlightDisruptionRebookingSystemSessionCreate) -> AgenticFlightDisruptionRebookingSystemSession:
        db_obj = AgenticFlightDisruptionRebookingSystemSession(
            id=f"SESS-{uuid.uuid4().hex[:8]}",
            task_prompt=data.task_prompt,
            status="COMPLETED",
            safety_tier="GREEN",
            confidence_score=0.98,
            metadata_json=data.metadata_json or {}
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    @staticmethod
    def get_session(db: Session, session_id: str) -> AgenticFlightDisruptionRebookingSystemSession:
        return db.query(AgenticFlightDisruptionRebookingSystemSession).filter(AgenticFlightDisruptionRebookingSystemSession.id == session_id).first()
