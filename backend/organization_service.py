from fastapi import Depends
from sqlalchemy import select, update
from sqlalchemy.orm import Session
from database import db_session
from models import Organization
from entities import OrganizationEntity

class OrganizationService:
    """Service that performs all of the actions on the `Organization` table"""

    # Current SQLAlchemy Session
    _session: Session

    def __init__(self, session: Session = Depends(db_session)):
        """Initializes the `OrganizationService` session"""
        self._session = session

    def all(self) -> list[Organization]:
        """
        Retrieves all organizations from the table

        Returns:
            list[Organization]: List of all `Organization`
        """
        # Select all entries in `Organization` table
        query = select(OrganizationEntity)
        entities = self._session.scalars(query).all()

        # Convert entries to a model and return
        return [entity.to_model() for entity in entities]

    def create(self, organization: Organization) -> Organization:
        """
        Creates a organization based on the input object and adds it to the table.
        If the organization's ID is unique to the table, a new entry is added.
        If the organization's ID already exists in the table, the existing entry is updated.

        Parameters:
            organization (Organization): Organization to add to table
        Returns:
            Organization: Object added to table
        """

        # Checks if the role already exists in the table
        if self._session.get(OrganizationEntity, organization.id):

            # If so, update existing entry
            organization_entity = OrganizationEntity.from_model(organization)
            self._session.execute(
                update(OrganizationEntity)
                .where(OrganizationEntity.id == organization.id)
                .values(
                    id=organization_entity.id, 
                    name=organization_entity.name, 
                    logo=organization_entity.logo, 
                    short_description=organization_entity.short_description, 
                    long_description=organization_entity.long_description, 
                    website=organization_entity.website, 
                    email=organization_entity.email, 
                    instagram=organization_entity.instagram, 
                    linked_in=organization_entity.linked_in, 
                    youtube=organization_entity.youtube, 
                    heel_life=organization_entity.heel_life
            ))

            # Commit changes
            self._session.commit()

            # Return updated object
            return organization_entity.to_model()
        else:
            # Otherwise, create new object
            organization_entity = OrganizationEntity.from_model(organization)

            # Add new object to table and commit changes
            self._session.add(organization_entity)
            self._session.commit()

            # Return added object
            return organization_entity.to_model()

    def get_from_id(self, id: int) -> Organization:
        """
        Get the organization from an id
        If none retrieved, a debug description is displayed.

        Parameters:
            id (int): Unique organization ID
        Returns:
            Organization: Object with corresponding ID
        """

        # Query the organization with matching id
        organization = self._session.query(OrganizationEntity).get(id)

        # Check if result is null
        if organization:
            # Convert entry to a model and return
            return organization.to_model()
        else:
            # Raise exception
            raise Exception(f"No organization found with ID: {id}")

    def update(self, organization: Organization) -> Organization:
        """
        Update the organization
        If none found with that id, a debug description is displayed.

        Parameters:
            organization (Organization): Organization to add to table
        Returns:
            Organization: Updated organization object
        """

        # Query the organization with matching id
        obj = self._session.query(OrganizationEntity).get(organization.id)

        # Check if result is null
        if obj:
            # Update organization object
            obj.name=organization.name
            obj.logo=organization.logo
            obj.short_description=organization.short_description
            obj.long_description=organization.long_description
            obj.website=organization.website
            obj.email=organization.email
            obj.instagram=organization.instagram
            obj.linked_in=organization.linked_in
            obj.youtube=organization.youtube
            obj.heel_life=organization.heel_life
            self._session.commit()
            # Return updated object
            return obj.to_model()
        else:
            # Raise exception
            raise Exception(f"No organization found with ID: {organization.id}")

    
    def delete(self, id: int) -> None:
        """
        Delete the organization based on the provided ID.
        If no item exists to delete, a debug description is displayed.

        Parameters:
            id (int): Unique organization ID
        """

        # Find object to delete
        obj=self._session.query(OrganizationEntity).get(id)

        # Ensure object exists
        if obj:
            # Delete object and commit
            self._session.delete(obj)
            self._session.commit()
        else:
            # Raise exception
            raise Exception(f"No organization found with ID: {id}")