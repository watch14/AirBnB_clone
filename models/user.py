#!/usr/bin/python3
"""User class"""
from models.base_model import BaseModel


class User(BaseModel):
    """User class addr@ / pass / F.N / L.N"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
