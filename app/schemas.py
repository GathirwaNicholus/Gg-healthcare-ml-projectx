from pydantic import BaseModel, Field
from typing import Literal

class PatientInput(BaseModel):
    age:                int    = Field(..., gt=0, lt=150, example=45)
    gender:             str    = Field(..., example="Male")
    blood_type:         str    = Field(..., example="A+")
    medical_condition:  str    = Field(..., example="Diabetes")
    insurance_provider: str    = Field(..., example="Medicare")
    billing_amount:     float  = Field(..., ge=0, example=25000.0)
    room_number:        int    = Field(..., example=205)
    admission_type:     str    = Field(..., example="Elective")
    medication:         str    = Field(..., example="Aspirin")
    length_of_stay:     int    = Field(..., ge=0, example=5)
    admission_month:    int    = Field(..., ge=1, le=12, example=6)
    admission_year:     int    = Field(..., example=2023)

class PredictionResponse(BaseModel):
    prediction: Literal["Normal", "Abnormal", "Inconclusive"]
    status:     str = "success"
