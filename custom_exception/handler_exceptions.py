from dataclasses import dataclass
from fastapi import HTTPException


@dataclass
class CuztomException(HTTPException):
    status_code: int
    detail: str


@dataclass
class PostException(HTTPException):
    status_code: int
    detail: str
