"""Testing Practice"""

from faker import Faker

fake = Faker()


"""Testing Users"""


def test_view_users_status_ok(api_client):
    r = api_client.get('/user/')
    assert r.status_code == 200
    assert r.json() == r.json()


def test_view_users_status_not_found(api_client):
    r = api_client.get('/users/')
    assert r.status_code == 404


def test_create_user_status_bad_request(api_client):
    data = {}
    r = api_client.post('/user/', data)
    assert r.status_code == 400


def test_create_user_status_created(api_client):
    data = {
        "password": fake.password(),
        "username": fake.last_name(),
        "first_name": fake.first_name(),
        "last_name": fake.last_name(),
        "email": fake.email(),
        "is_staff": True,
        "is_active": True,
        "address": fake.address(),
        "birth_date": fake.date()
    }

    r = api_client.post('/user/', data)
    assert r.status_code == 201
    assert 'first_name' in r.json()
    assert 'last_name' in r.json()
    assert 'address' in r.json()


def test_create_user_status_bad_request_2(api_client):
    data = {
        "first_name": fake.first_name(),
        "last_name": fake.last_name(),
        "email": fake.email(),
        "is_staff": True,
        "is_active": True,
        "address": fake.address(),
        "birth_date": fake.date()
    }
    r = api_client.post('/user/', data)
    assert r.status_code == 400


def test_view_user_detail_status_ok(api_client, test_user):
    r = api_client.get(f'/user/{test_user.id}/')
    assert r.status_code == 200
    assert r.json() == r.json()


def test_view_user_detail_does_not_exist(api_client):
    r = api_client.get(f'/user/{10005000}/')
    assert r.status_code == 404


def test_update_user_detail_status_ok(api_client, test_user):
    r = api_client.put(f'/user/{test_user.id}/',
                       {
                           "password": fake.password(),
                           "username": fake.last_name(),
                           "first_name": 'Some name',
                           "last_name": fake.last_name(),
                           "email": 'some_email@example.com',
                           "is_staff": True,
                           "is_active": True,
                           "address": fake.address(),
                           "birth_date": fake.date()
                       })
    assert r.status_code == 200
    assert r.json().get('first_name') == 'Some name'
    assert r.json().get('email') == 'some_email@example.com'
    assert r.json().get('is_active') is True
    assert r.json().get('is_staff') is True


def test_update_user_detail_status_bad_request(api_client, test_user):
    r = api_client.put(f'/user/{test_user.id}/',
                       {
                           "first_name": 'Some name',
                           "last_name": fake.last_name(),
                           "email": 'some_email@example.com',
                           "is_staff": True,
                           "is_active": True,
                           "address": fake.address(),
                           "birth_date": fake.date()
                       })
    assert r.status_code == 400
    assert r.json()['username'] == ['This field is required.']


def test_partial_update_user_detail_status_ok(api_client, test_user):
    r = api_client.patch(f'/user/{test_user.id}/',
                         {"email": 'some_email@example.com'})
    assert r.status_code == 200
    assert r.json().get('email') == 'some_email@example.com'


def test_delete_user_detail_status_ok(api_client, test_user):
    r = api_client.delete(f'/user/{test_user.id}/')
    assert r.status_code == 204


"""Testing Contracts"""


def test_view_contracts_status_ok(api_client):
    r = api_client.get('/contract/')
    assert r.status_code == 200
    assert r.json() == r.json()


def test_view_contracts_status_not_found(api_client):
    r = api_client.get('/contracts/')
    assert r.status_code == 404


def test_create_contract_status_bad_request(api_client):
    data = {}
    r = api_client.post('/contract/', data)
    assert r.status_code == 400


def test_create_contract_status_bad_request_2(api_client, test_user):
    data = {
        "student": test_user.id,
        "contract_name": fake.word(),
        "contract_type": fake.word(),
        "contract_file": fake.file_name()
    }
    r = api_client.post('/contract/', data)
    assert r.status_code == 400
    assert r.json()['contract_file'] == \
           ['The submitted data was not a file. Check the encoding type on the form.']


def test_update_contract_detail_status_bad_request(api_client, test_user, test_contract):
    r = api_client.put(f'/contract/{test_contract.id}/',
                       {
                         "student": test_user.id,
                         "contract_name": fake.word(),
                         "contract_type": fake.word(),
                         "contract_file": fake.file_name()
                       })
    assert r.status_code == 400
    assert r.json()['contract_file'] == \
           ['The submitted data was not a file. Check the encoding type on the form.']


def test_partial_update_contract_detail_status_ok(api_client, test_contract):
    r = api_client.patch(f'/contract/{test_contract.id}/',
                         {"contract_name": 'Some contract name'})
    assert r.status_code == 200
    assert r.json().get('contract_name') == 'Some contract name'


def test_delete_contract_detail_status_ok(api_client, test_contract):
    r = api_client.delete(f'/contract/{test_contract.id}/')
    assert r.status_code == 204


"""Testing Companies"""


def test_view_companies_status_ok(api_client):
    r = api_client.get('/company/')
    assert r.status_code == 200
    assert r.json() == r.json()


def test_view_companies_status_not_found(api_client):
    r = api_client.get('/companies/')
    assert r.status_code == 404


def test_create_company_status_bad_request(api_client):
    data = {}
    r = api_client.post('/company/', data)
    assert r.status_code == 400


def test_create_company_status_created(api_client, test_contract):
    data = {
        "contract": test_contract.id,
        "company_name": fake.company(),
        "telephone": fake.phone_number(),
        "address": fake.company()
    }

    r = api_client.post('/company/', data)
    assert r.status_code == 201
    assert 'company_name' in data
    assert 'telephone' in data
    assert 'address' in data


def test_view_company_detail_status_ok(api_client, test_company):
    r = api_client.get(f'/company/{test_company.id}/')
    assert r.status_code == 200
    assert r.json() == r.json()


def test_view_company_detail_does_not_exist(api_client):
    r = api_client.get(f'/company/{10005000}/')
    assert r.status_code == 404


def test_update_company_detail_status_ok(api_client, test_contract, test_company):
    r = api_client.put(f'/company/{test_company.id}/',
                       {
                         "contract": test_contract.id,
                         "company_name": fake.company(),
                         "telephone": fake.phone_number(),
                         "address": 'Abai, 123'
                       })
    assert r.status_code == 200
    assert 'company_name' in r.json()
    assert r.json().get('address') == 'Abai, 123'


def test_update_company_detail_status_bad_request(api_client, test_company):
    r = api_client.put(f'/company/{test_company.id}/',
                       {
                         "company_name": fake.company(),
                         "telephone": fake.phone_number(),
                         "address": 'Abai, 123'
                       })
    assert r.status_code == 400


def test_partial_update_company_detail_status_ok(api_client, test_company):
    r = api_client.patch(f'/company/{test_company.id}/',
                         {"company_name": 'Some company name'})
    assert r.status_code == 200
    assert r.json().get('company_name') == 'Some company name'


def test_delete_company_detail_status_ok(api_client, test_company):
    r = api_client.delete(f'/company/{test_company.id}/')
    assert r.status_code == 204


"""Testing Reports"""


def test_view_reports_status_ok(api_client):
    r = api_client.get('/report/')
    assert r.status_code == 200
    assert r.json() == r.json()


def test_view_reports_status_not_found(api_client):
    r = api_client.get('/reports/')
    assert r.status_code == 404


def test_create_report_status_created(api_client, test_contract):
    data = {
        "contract": test_contract.id,
        "report_name": fake.word(),
        "report_type": fake.word(),
        "report_description": fake.sentence(),
    }

    r = api_client.post('/report/', data)
    assert r.status_code == 201
    assert 'report_name' in r.json()
    assert 'report_type' in r.json()
    assert 'report_description' in r.json()


def test_view_report_detail_status_ok(api_client, test_report):
    r = api_client.get(f'/report/{test_report.id}/')
    assert r.status_code == 200
    assert r.json() == r.json()


def test_view_report_detail_does_not_exist(api_client):
    r = api_client.get(f'/report/{10005000}/')
    assert r.status_code == 404


def test_update_report_detail_status_ok(api_client, test_contract, test_report):
    r = api_client.put(f'/report/{test_report.id}/',
                       {
                         "contract": test_contract.id,
                         "report_name": 'Some report name',
                         "report_type": fake.word(),
                         "report_description": fake.sentence()
                       })
    assert r.status_code == 200
    assert 'report_type' in r.json()
    assert r.json().get('report_name') == 'Some report name'


def test_partial_update_report_detail_status_ok(api_client, test_report):
    r = api_client.patch(f'/report/{test_report.id}/',
                         {"report_type": 'Some report type'})
    assert r.status_code == 200
    assert r.json().get('report_type') == 'Some report type'


def test_delete_report_detail_status_ok(api_client, test_report):
    r = api_client.delete(f'/report/{test_report.id}/')
    assert r.status_code == 204
