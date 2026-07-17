import uuid
from sqlalchemy import Column, String, Boolean, DateTime, Date, Time, Text, ForeignKey, DECIMAL, Integer 
from sqlalchemy.dialects.postgresql import UUID,JSONB
from sqlalchemy.sql import func
from app.database import Base
from sqlalchemy.orm import relationship

class Property(Base):
    __tablename__= "properties"
    id = Column(UUID(as_uuid=True), primary_key=True,default=uuid.uuid4)
    owner_id= Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)
    address_id= Column(UUID(as_uuid=True), ForeignKey("addresses.id"), nullable= False)
    property_name= Column(String(255), nullable=False)
    description= Column(Text, nullable=True)
    property_type= Column(String(255), nullable=False)
    star_rating= Column(Integer, nullable=True)
    contact_email= Column(String(255), nullable=False)
    contact_number= Column(String(20), nullable=False)
    cancellation_policy= Column(Text, nullable=True)
    house_rules= Column(JSONB, nullable= True)
    child_policy= Column(Text, nullable=True)
    pet_policy= Column(Text, nullable= True)
    smoking_policy= Column(Text, nullable=True)
    status= Column(String(100), nullable=False)
    is_verified= Column(Boolean, nullable= False, default=False)
    avg_rating= Column(DECIMAL(2,1), nullable=True)
    total_reviews= Column(Integer, nullable=False, default=0)
    check_in_time= Column(Time, nullable=False)
    check_out_time= Column(Time, nullable=False)
    created_at= Column(DateTime, server_default= func.now(), nullable=False)
    updated_at= Column(DateTime, server_default= func.now(), onupdate= func.now(), nullable=False)
    created_by= Column(String(100), nullable=True)
    updated_by= Column(String(100), nullable=True)

    address = relationship("Address", back_populates="property")
    owner= relationship("User", back_populates= "properties")


