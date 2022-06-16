# sandra
from dataclasses import dataclass
from typing import List
from datetime import datetime


@dataclass
class Parcel:
    id: int
    name: str
    weight: float
    width: float
    height: float
    length: float
    date: datetime
    priority: str


@dataclass
class Truck:
    id: int
    name: str
    capacity: int
    weight_range: int
    trunk: List[Parcel]
