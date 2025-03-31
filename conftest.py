import pytest

@pytest.fixture(scope='session')
def django_db_setup():
    return {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }