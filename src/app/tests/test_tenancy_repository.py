#test/repository_tests/test_tenancy_repository.py
# import unittest
# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker
# from app.repositories import tenancy_repository
# from app.db.models import all_models as models
# from app.schemas.tenancy_schema import TenancyCreate, TenancyUpdate



# class TenancyRepositoryTest(unittest.TestCase):
#     def setUp(self):
#         self.engine = create_engine('sqlite:///:memory:')
#         models.Base.metadata.create_all(bind=self.engine)
#         Session = sessionmaker(bind=self.engine)
#         self.db = Session()

#     def tearDown(self):
#         self.db.close()

#     def test_create_tenancy(self):
#         tenancy_data = TenancyCreate(tenant_name="Test Tenant")
#         created_tenancy = tenancy_repository.create_tenancy(self.db, tenancy_data)
#         self.assertEqual(created_tenancy.tenant_name, "Test Tenant")

#     def test_get_tenancy(self):
#         tenancy_data = TenancyCreate(tenant_name="Test Tenant")
#         created_tenancy = tenancy_repository.create_tenancy(self.db, tenancy_data)
#         retrieved_tenancy = tenancy_repository.get_tenancy(self.db, created_tenancy.id)
#         self.assertEqual(retrieved_tenancy.tenant_name, "Test Tenant")

#     def test_get_tenancies(self):
#         tenancy_data = TenancyCreate(tenant_name="Test Tenant")
#         tenancy_repository.create_tenancy(self.db, tenancy_data)
#         tenancies = tenancy_repository.get_tenancies(self.db)
#         self.assertEqual(len(tenancies), 1)

#     def test_update_tenancy(self):
#         tenancy_data = TenancyCreate(tenant_name="Test Tenant")
#         created_tenancy = tenancy_repository.create_tenancy(self.db, tenancy_data)
#         update_data = TenancyUpdate(tenant_name="Updated Tenant")
#         updated_tenancy = tenancy_repository.update_tenancy(self.db, created_tenancy.id, update_data)
#         self.assertEqual(updated_tenancy.tenant_name, "Updated Tenant")

#     def test_delete_tenancy(self):
#         tenancy_data = TenancyCreate(tenant_name="Test Tenant")
#         created_tenancy = tenancy_repository.create_tenancy(self.db, tenancy_data)
#         deleted_tenancy = tenancy_repository.delete_tenancy(self.db, created_tenancy.id)
#         self.assertIsNone(deleted_tenancy)


# if __name__ == '__main__':
#     unittest.main()


# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker
# import pytest
# from app.repositories import tenancy_repository
# from app.db.models import all_models as models
# from app.schemas.tenancy_schema import TenancyCreate, TenancyUpdate


# @pytest.fixture(scope="module")
# def db():
#     engine = create_engine('sqlite:///:memory:')
#     models.Base.metadata.create_all(bind=engine)
#     Session = sessionmaker(bind=engine)
#     db_session = Session()
#     yield db_session
#     db_session.close()


# def test_create_tenancy(db):
#     tenancy_data = TenancyCreate(tenant_name="Test Tenant")
#     created_tenancy = tenancy_repository.create_tenancy(db, tenancy_data)
#     assert created_tenancy.tenant_name == "Test Tenant"


# def test_get_tenancy(db):
#     tenancy_data = TenancyCreate(tenant_name="Test Tenant")
#     created_tenancy = tenancy_repository.create_tenancy(db, tenancy_data)
#     retrieved_tenancy = tenancy_repository.get_tenancy(db, created_tenancy.id)
#     assert retrieved_tenancy.tenant_name == "Test Tenant"


# def test_get_tenancies(db):
#     tenancy_data = TenancyCreate(tenant_name="Test Tenant 1")
#     tenancy_repository.create_tenancy(db, tenancy_data)
#     tenancy_data = TenancyCreate(tenant_name="Test Tenant 2")
#     tenancy_repository.create_tenancy(db, tenancy_data)

#     tenancies = tenancy_repository.get_tenancies(db)
#     assert len(tenancies) == 2
#     assert tenancies[0].tenant_name == "Test Tenant 1"
#     assert tenancies[1].tenant_name == "Test Tenant 2"


# def test_update_tenancy(db):
#     tenancy_data = TenancyCreate(tenant_name="Test Tenant")
#     created_tenancy = tenancy_repository.create_tenancy(db, tenancy_data)
#     update_data = TenancyUpdate(tenant_name="Updated Tenant")
#     updated_tenancy = tenancy_repository.update_tenancy(db, created_tenancy.id, update_data)
#     assert updated_tenancy.tenant_name == "Updated Tenant"


# def test_delete_tenancy(db):
#     tenancy_data = TenancyCreate(tenant_name="Test Tenant")
#     created_tenancy = tenancy_repository.create_tenancy(db, tenancy_data)
#     deleted_tenancy = tenancy_repository.delete_tenancy(db, created_tenancy.id)
#     assert deleted_tenancy is not None
#     assert deleted_tenancy.is_active is False
#     assert tenancy_repository.get_tenancy(db, created_tenancy.id) is None


# if __name__ == '__main__':
#     pytest.main()

import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.repositories import tenancy_repository
from app.models import all_models as models
from app.schemas.tenancy_schema import TenancyCreate, TenancyUpdate
from app.db.database import Base, get_db, reset_database, DATABASE_URL
from app.init_db import main as init_db_main


@pytest.fixture(scope="module")
def db():
    # Create a separate database for testing
    TESTING_DATABASE_URL = DATABASE_URL + '_test'
    engine = create_engine(TESTING_DATABASE_URL)
    TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    models.Base.metadata.create_all(bind=engine)
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()
        # Clean up the testing database after the tests
        Base.metadata.drop_all(bind=engine)


@pytest.fixture(scope="session", autouse=True)
def initialize_test_db():
    # Initialize the test database before running tests
    TESTING_DATABASE_URL = DATABASE_URL + '_test'
    engine = create_engine(TESTING_DATABASE_URL)
    Base.metadata.create_all(bind=engine)
    reset_database()


def test_create_tenancy(db):
    # Test creating a new tenancy
    tenancy_data = TenancyCreate(tenant_name="Test Tenant")
    created_tenancy = tenancy_repository.create_tenancy(db, tenancy_data)
    assert created_tenancy.tenant_name == "Test Tenant"

    # Test creating a tenancy with empty name
    with pytest.raises(ValueError):
        tenancy_data = TenancyCreate(tenant_name="")
        tenancy_repository.create_tenancy(db, tenancy_data)

def test_get_tenancy(db):
    # Test retrieving an existing tenancy
    tenancy_data = TenancyCreate(tenant_name="Test Tenant")
    created_tenancy = tenancy_repository.create_tenancy(db, tenancy_data)
    retrieved_tenancy = tenancy_repository.get_tenancy(db, created_tenancy.id)
    assert retrieved_tenancy.tenant_name == "Test Tenant"

    # Test retrieving a non-existent tenancy
    non_existent_tenancy = tenancy_repository.get_tenancy(db, 999)
    assert non_existent_tenancy is None


def test_get_tenancies(db):
    # Test retrieving multiple tenancies
    tenancy_data1 = TenancyCreate(tenant_name="Test Tenant 1")
    tenancy_repository.create_tenancy(db, tenancy_data1)
    tenancy_data2 = TenancyCreate(tenant_name="Test Tenant 2")
    tenancy_repository.create_tenancy(db, tenancy_data2)

    tenancies = tenancy_repository.get_tenancies(db)
    assert len(tenancies) == 2
    assert tenancies[0].tenant_name == "Test Tenant 1"
    assert tenancies[1].tenant_name == "Test Tenant 2"


def test_update_tenancy(db):
    # Test updating an existing tenancy
    tenancy_data = TenancyCreate(tenant_name="Test Tenant")
    created_tenancy = tenancy_repository.create_tenancy(db, tenancy_data)
    update_data = TenancyUpdate(tenant_name="Updated Tenant")
    updated_tenancy = tenancy_repository.update_tenancy(db, created_tenancy.id, update_data)
    assert updated_tenancy.tenant_name == "Updated Tenant"

    # Test updating a non-existent tenancy
    with pytest.raises(ValueError):
        update_data = TenancyUpdate(tenant_name="Updated Tenant")
        tenancy_repository.update_tenancy(db, 999, update_data)


def test_delete_tenancy(db):
    # Test soft deleting an existing tenancy
    tenancy_data = TenancyCreate(tenant_name="Test Tenant")
    created_tenancy = tenancy_repository.create_tenancy(db, tenancy_data)
    deleted_tenancy = tenancy_repository.delete_tenancy(db, created_tenancy.id)
    assert deleted_tenancy is not None
    assert deleted_tenancy.is_active is False

    # Test soft deleting a non-existent tenancy
    non_existent_tenancy = tenancy_repository.delete_tenancy(db, 999)
    assert non_existent_tenancy is None


if __name__ == '__main__':
    init_db_main()
    pytest.main()
