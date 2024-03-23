
# class RequestStatusEnum(enum.Enum):
#     APPROVED = 'approved'
#     REJECTED = 'rejected'
#     RETURNED = 'returned'
#     PENDING = 'pending'

# class RequestTypeEnum(enum.Enum):
#     UNIT = 'unit'
#     SRT = 'srt'
#     DEPARTMENT = 'dept'
#     INDIVIDUAL = 'individual'

# class RoleNameEnum(enum.Enum):
#     UNIT_MEMBER = "unit_member"
#     PROGRAMS_LEAD = "programs_lead"
#     DEPT_LEAD = "dept_lead"
#     TECH_LEAD = "tech_lead"
#     STL = "stl"
#     ADMIN_LEAD = "admin_lead"
#     FLEET_TEAM = "fleet_team"
#     TENANT_ADMIN = "tenant_admin"
#     SUPER_ADMIN = "super_admin"


from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.gzip import GZipMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from routes import (
    tenancy_routes,
    srt_routes,
    role_routes,
    department_routes,
    workplantype_routes,
    location_routes,
    user_routes,
    employee_routes, 
    unit_routes
)

import uvicorn

app = FastAPI()

# CORS middleware
origins = ["*"]  
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# GZip Middleware to compress responses greater than or equal to 1000 bytes in size.
app.add_middleware(GZipMiddleware, minimum_size=1000)

# Trusted Host Middleware is added to only allow requests from the specified list of hosts.
#app.add_middleware(TrustedHostMiddleware, allowed_hosts=["example.com"])

# Include routes
app.include_router(tenancy_routes.router, prefix="/api/v1",tags=["Tenancies"])
app.include_router(srt_routes.router,prefix="/api/v1",tags=["SRTs"])
app.include_router(role_routes.router,prefix="/api/v1",tags=["UserRoles"])
app.include_router(department_routes.router,prefix="/api/v1",tags=["Departments"])
app.include_router(workplantype_routes.router,prefix="/api/v1",tags=["WorkPlan_Types"])
app.include_router(location_routes.router,prefix="/api/v1",tags=["Locations"])
app.include_router(user_routes.router,prefix="/api/v1",tags=["Users"])
app.include_router(employee_routes.router,prefix="/api/v1",tags=["Employees"])
app.include_router(unit_routes.router,prefix="/api/v1",tags=["Units"])
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

