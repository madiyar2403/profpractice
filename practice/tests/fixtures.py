import pytest

from ..factories import UserFactory, ContractFactory, CompanyFactory, ReportFactory


@pytest.fixture
def test_user(db):
    return UserFactory()


@pytest.fixture
def test_contract(db):
    return ContractFactory()


@pytest.fixture
def test_company(db):
    return CompanyFactory()


@pytest.fixture
def test_report(db):
    return ReportFactory()
