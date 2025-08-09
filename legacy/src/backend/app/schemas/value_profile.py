from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field, ConfigDict

class ValueProfileBase(BaseModel):
    name: str = Field(..., max_length=100)
    description: Optional[str] = Field(None, max_length=255)
    user_id: Optional[int] = None
    model_config = ConfigDict(from_attributes=True)

class ValueProfileCreate(ValueProfileBase):
    model_config = ConfigDict(from_attributes=True)

class ValueProfileUpdate(ValueProfileBase):
    model_config = ConfigDict(from_attributes=True)

class ValueProfileInDBBase(ValueProfileBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None
    model_config = ConfigDict(from_attributes=True)

class ValueProfile(ValueProfileInDBBase):
    model_config = ConfigDict(from_attributes=True)
