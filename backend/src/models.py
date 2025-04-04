from dataclasses import dataclass
from typing import List, Optional
from datetime import datetime

@dataclass
class Deal:
    id: str
    account_id: str
    service_line: str
    value: float
    status: str
    date: str

@dataclass
class Account:
    id: str
    name: str
    industry: str
    current_tech_stack: List[str]
    pain_points: List[str]

@dataclass
class AccountManager:
    id: str
    name: str
    accounts: List[str] 