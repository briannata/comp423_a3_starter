from fastapi import Depends
from sqlalchemy import select, update, values
from sqlalchemy import insert
from sqlalchemy.orm import Session
from database import db_session
from models import Role
from entities import RoleEntity

class RoleService:

    _session: Session

    def __init__(self, session: Session = Depends(db_session)):
        self._session = session

    def all(self) -> list[Role]:
        query = select(RoleEntity)
        entities = self._session.scalars(query).all()
        return [entity.to_model() for entity in entities]

    def create(self, role: Role) -> Role:
        if self._session.get(RoleEntity, role.id):
            
            role_entity = RoleEntity.from_model(role)
            self._session.execute(
                update(RoleEntity)
                .where(RoleEntity.id == role.id)
                .values(
                    id = role_entity.id,
                    user_id = role_entity.user_id,
                    org_id = role_entity.org_id,
                    membership_type = role_entity.membership_type
            ))

            self._session.commit()
            return role_entity.to_model()
        else:
            role_entity = RoleEntity.from_model(role)
            self._session.add(role_entity)
            self._session.commit()
            return role_entity.to_model()

    def get_from_userid(self, user_id: int) -> list[Role]:
        roles = self._session.query(RoleEntity).filter(RoleEntity.user_id == user_id).all()
        if roles:
            models: list[Role] = []
            for role in roles:
                models.append(role.to_model())
            return models
        else:
            raise Exception(f"No role found with User ID: {user_id}")

    def get_from_orgid(self, org_id: int) -> list[Role]:
        roles = self._session.query(RoleEntity).filter(RoleEntity.org_id == org_id).all()
        if roles:
            models: list[Role] = []
            for role in roles:
                models.append(role.to_model())
            return models
        else:
            raise Exception(f"No role found with Organization ID: {org_id}")

    def delete(self, id: int) -> None:
        obj=self._session.query(RoleEntity).filter(RoleEntity.id == id).first()
        if obj:
            self._session.delete(obj)
            self._session.commit()
        else:
            raise Exception(f"No role found with ID: {id}")