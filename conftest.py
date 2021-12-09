import pytest
from rest_framework.test import APIClient

from practice.factories import UserFactory
from practice.tests.fixtures import test_user, test_contract, test_company, test_report


@pytest.fixture()
def api_client(db):
    return APIClient()


@pytest.fixture
def admin_user_create(db):
    admin = UserFactory.create()
    admin.is_admin = True
    admin.is_superuser = True
    admin.username = 'admin'
    admin.set_password('password')
    admin.save()

    return admin
