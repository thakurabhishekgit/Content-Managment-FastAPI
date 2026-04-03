from pydantic import BaseModel, EmailStr, Field
from datetime import datetime

class UserCreate(BaseModel):
    name: str = Field(..., min_length=3, max_length=50)
    email: EmailStr
    password: str = Field(..., min_length=6)

class UserResponse(BaseModel):
    id: str
    name: str
    email: EmailStr
    created_at: datetime

class UserUpdate(BaseModel):
    name: str = Field(None, min_length=3, max_length=50)
    email: EmailStr = None
    password: str = Field(None, min_length=6)



# 1. What is Pydantic?
#Pydantic is A library that validates, parses, and serializes data using Python type hints


# 2. What is BaseModel?
# class UserCreate(BaseModel):
# Meaning:
# BaseModel is the core class of Pydantic.
# It gives you:
# Automatic validation
# Type checking
# JSON conversion
# Error handling

# Example
# UserCreate(name="ab", email="wrong", password="123")

# This will automatically throw validation errors like:

# name too short
# invalid email
# password too short



# 3. What is Field()?
# name: str = Field(..., min_length=3, max_length=50)
# Purpose:

# Adds extra validation rules + metadata

# Breakdown
# ... → required field
# min_length=3 → validation
# max_length=50 → constraint