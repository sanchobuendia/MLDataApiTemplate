from models.db import db
from models.serializer import Serializer
from sqlalchemy.dialects.postgresql import UUID

class Collectors(db.Model,Serializer):
    __tablename__ = "examples"
    id = db.Column(UUID(as_uuid=True), primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    enabled = db.Column(db.Boolean(), default = False)

    def __repr__(self):
        return f"<{self.name} Example>"
