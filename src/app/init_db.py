# init_db.py
from db.database import reset_database, create_tables
from models.all_models import User, UserRole, Department, Unit, SRT, WorkPlan, WorkPlanRequest
from models.all_models import RequestStatus, WorkPlanType, Vehicle, VehicleMaintenance, MaintenanceType
from models.all_models import FuelPurchase, Driver, Location, Tenancy, Trip

def main():
    # Reset the database (drop if exists, then create)
    reset_database()
    
    # Create tables
    create_tables()

if __name__ == "__main__":
    main()
