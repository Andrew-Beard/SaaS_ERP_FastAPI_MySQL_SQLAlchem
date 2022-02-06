from sqlalchemy.orm import Session
from typing import Optional

from .base import BaseDAL
from src.models import Medicine
from src.schemas import MedicineCreate, MedicineUpdate


class MedicineDAL(BaseDAL[Medicine, MedicineCreate, MedicineUpdate]):
    def read_many_filtered_by_brand_name_letters(
        self, db: Session, name_str: Optional[str], skip: int = 0, limit: int = 10
    ) -> Optional[Medicine]:
        return (
            db.query(self.model)
            .filter(self.model.brand_name.like(f"{name_str}%"))
            .offset(skip)
            .limit(limit)
            .all()
        )

    def read_many_filtered_by_generic_name_letters(
        self, db: Session, name_str: Optional[str], skip: int = 0, limit: int = 10
    ) -> Optional[Medicine]:
        return (
            db.query(self.model)
            .filter(self.model.generic_name.like(f"{name_str}%"))
            .offset(skip)
            .limit(limit)
            .all()
        )
