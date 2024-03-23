#app/models/all_models.py
from sqlalchemy import Column, Integer, String, Text, Boolean, Date, DateTime, Enum, DECIMAL, ForeignKey
from sqlalchemy.orm import relationship
from db.database import Base
import datetime


class BaseTable(Base):
    __abstract__ = True

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    is_active = Column(Boolean, default=True)  # Soft delete
    date_created = Column(DateTime(timezone=True), default=datetime.datetime.utcnow)
    date_updated = Column(DateTime(timezone=True), default=None, onupdate=datetime.datetime.utcnow)

 
class User(BaseTable):
    __tablename__ = 'user'
    user_name = Column(String(50))
    employee_id = Column(Integer, ForeignKey('employee.id'))
    user_role_id = Column(Integer, ForeignKey('user_role.id'))
    hashed_password = Column(String(50))
    jwt_token = Column(String(255))  # Field for storing JWT token
    is_superuser = Column(Boolean, default=False)  # Flag to identify superuser/admin


class Employee(BaseTable):
    __tablename__ = 'employee'

    first_name = Column(String(255))
    last_name = Column(String(255))
    phone_number = Column(String(20))
    email = Column(String(255), unique=True)
    address = Column(Text)
    employee_code = Column(String(50), unique=True)
    unit_id = Column(Integer, ForeignKey('unit.id'))
    tenancy_id = Column(Integer, ForeignKey('tenancy.id'))
    srt_id = Column(Integer, ForeignKey('srt.id'),nullable=True)
    dept_id = Column(Integer, ForeignKey('department.id'))
    is_unit_lead = Column(Boolean)
    is_dept_lead = Column(Boolean)
    is_srt_lead = Column(Boolean)
    is_stl = Column(Boolean)
    is_technical_lead = Column(Boolean)


class UserRole(BaseTable):
    __tablename__ = 'user_role'

    role_name = Column(String(50),unique=True)

class Unit(BaseTable):
    __tablename__ = 'unit'

    unit_name = Column(String(100), unique=True)
    dept_id = Column(Integer, ForeignKey('department.id'))

class Department(BaseTable):
    __tablename__ = 'department'

    dept_name = Column(String(255),unique=True)

class SRT(BaseTable):
    __tablename__ = 'srt'

    srt_name = Column(String(50))
    tenancy_id = Column(Integer, ForeignKey('tenancy.id'))

class WorkPlanType(BaseTable):
    __tablename__ ='workplan_type'

    workplan_type_name =Column(String(100), unique=True)

class WorkPlan(BaseTable):
    __tablename__ = 'work_plan'

    title = Column(String(255))
    description = Column(Text)
    workplan_type_id = Column(Integer, ForeignKey('workplan_type.id'))#Unit, SRT, Individual, Dept
    user_id = Column(Integer, ForeignKey('user.id'))
    modified_by_id = Column(Integer, ForeignKey('user.id'))
    tenancy_id = Column(Integer, ForeignKey('tenancy.id'))

class WorkPlanRequest(BaseTable):
    __tablename__ = 'work_plan_request'

    status_id = Column(Integer, ForeignKey('request_status.id'))
    plan_id = Column(Integer, ForeignKey('work_plan.id'))
    tenancy_id = Column(Integer, ForeignKey('tenancy.id'))

class RequestStatus(BaseTable):
    __tablename__ = 'request_status'

    status_name = Column(String(50), unique=True)

class Vehicle(BaseTable):
    __tablename__ = 'vehicle'

    vehicle_name = Column(String(255))
    licence_plate = Column(String(20),unique=True)
    make = Column(String(100))
    year = Column(Integer)
    fuel_type = Column(String(50))
    current_mileage = Column(Integer)
    is_available = Column(Boolean)
    seat_capacity = Column(Integer)

class VehicleMaintenance(BaseTable):
    __tablename__ = 'vehicle_maintenance'

    vehicle_id = Column(Integer, ForeignKey('vehicle.id'))
    maintenance_type_id = Column(Integer, ForeignKey('maintenance_type.id'))
    description = Column(Text)
    cost = Column(DECIMAL(10, 2))
    status = Column(String(50))
    maintenance_date = Column(Date)

class MaintenanceType(BaseTable):
    __tablename__ = 'maintenance_type'

    maintenance_type_name = Column(String(100))

class FuelPurchase(BaseTable):
    __tablename__ = 'fuel_purchase'

    vehicle_id = Column(Integer, ForeignKey('vehicle.id'))
    quantity = Column(DECIMAL(10, 2))
    unit_cost = Column(DECIMAL(10, 2))
    total_cost = Column(DECIMAL(10, 2))
    purchase = Column(Date)

class Driver(BaseTable):
    __tablename__ = 'driver'

    user_id = Column(Integer, ForeignKey('user.id'))
    licence_number = Column(String(50))
    licence_exp_date = Column(Date)

class Trip(BaseTable):
    __tablename__ = 'trip'

    vehicle_id = Column(Integer, ForeignKey('vehicle.id'))
    driver_id = Column(Integer, ForeignKey('driver.id'))
    work_plan_id = Column(Integer, ForeignKey('work_plan.id'))
    start_location =Column(Integer, ForeignKey('location.id')) #Column(Enum('Aba', 'Arochukwu', 'Ohafia'))
    end_location = Column(Integer, ForeignKey('location.id')) #Column(Enum('Aba', 'Arochukwu', 'Ohafia'))
    start_time = Column(DateTime)
    end_time = Column(DateTime)
    distance = Column(DECIMAL(10, 2))
    fuel_consumed = Column(DECIMAL(10, 2))

class Location(BaseTable):
    __tablename__ = 'location'
    #location_name = Column(Enum('Aba', 'Arochukwu', 'Ohafia'))
    location_name = Column(String(255))
    tenancy_id = Column(Integer, ForeignKey('tenancy.id'))

class Tenancy(BaseTable):
    __tablename__ = 'tenancy'
    tenant_name = Column(String(255))
