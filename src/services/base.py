from typing import Generic, Type
from fastapi import status
from sqlalchemy.orm import Session

from src.utils.app_exceptions import AppException
from src.utils.service_result import ServiceResult
from src.utils.types import ModelDAL, CreateSchemaType, UpdateSchemaType, ModelType


class BaseService(Generic[ModelDAL, CreateSchemaType, UpdateSchemaType]):
    def __init__(self, dal: Type[ModelDAL], model: Type[ModelType]):
        self.dal = dal
        self.model = model

    def create(self, db: Session, obj_in: CreateSchemaType):
        data = self.dal(self.model).create_with_commit(db, obj_in)
        if not data:
            return ServiceResult(AppException.ServerError("Something went wrong"))
        return ServiceResult(data, status_code=status.HTTP_201_CREATED)

    def get_one_by_id(self, db: Session, id: int):
        data = self.dal(self.model).read_one_filtered_by_id(db, id)
        if not data:
            return ServiceResult(
                AppException.NotFound(
                    f"No {self.model.__name__.lower()} found with this id: {id}"
                )
            )
        return ServiceResult(data, status_code=status.HTTP_200_OK)

    def get_many(self, db: Session, skip: int = 0, limit: int = 10):
        data = self.dal(self.model).read_many_offset_limit(db, skip=skip, limit=limit)
        if not data:
            return ServiceResult(
                AppException.NotFound(f"No {self.model.__name__.lower()}s found")
            )
        return ServiceResult(data, status_code=status.HTTP_200_OK)

    def update_by_id(self, db: Session, obj_in: UpdateSchemaType):
        data = self.dal(self.model).update_one_filtered_by_id(db, id, obj_in)
        if not data:
            return ServiceResult(AppException.NotAccepted())
        return ServiceResult(data, status_code=status.HTTP_202_ACCEPTED)

    def remove_by_id(self, db: Session, id: int):
        ServiceResult(
            "Successfully deleted", status_code=status.HTTP_202_ACCEPTED
        ) if self.dal(self.model).delete_one_filtered_by_id(db, id) else ServiceResult(
            AppException.NotFound(f"Nothing matched with id: {id}")
        )
