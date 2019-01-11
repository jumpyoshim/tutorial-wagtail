import pytest

from django.core.management import CommandError, call_command
from django.test.client import Client


@pytest.mark.django_db
@pytest.mark.parametrize('email,password', [
    ('admin@iridge.jp', 'admin')
])
def test_success_case_createsuperuser_with_password(email, password):
    """正常系"""
    call_command(
        'createsuperuser_with_password',
        '--email', email,
        '--password', password
    )
    client = Client()
    response = client.login(email=email, password=password)
    assert response is True


@pytest.mark.django_db
@pytest.mark.parametrize('email', [
    ('admin@iridge.jp')
])
def test_failure_case_createsuperuser_with_password(email):
    """異常系"""
    with pytest.raises(CommandError):
        call_command(
            'createsuperuser_with_password',
            '--email', email
        )
