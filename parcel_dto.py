# sandra
from dataclasses import dataclass
from typing import List, Optional
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
    priority: bool


@dataclass
class Truck:
    id: int
    name: str
    capacity: int
    weight_range: float
    used_weight_range: Optional[float] #defult na 0 ustaw
    trunk: List[Parcel]

    def add_parcel_to_trunk(self, parcel: Parcel) -> None:
        self.trunk.append(parcel)
