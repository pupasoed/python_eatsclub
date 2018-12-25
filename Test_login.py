import pytest
from application import Application

# def is_alert_present(driver):

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_login(app):
    app.open_home()
    app.nav_linc("ВХОД")
    app.enter_email_and_pass(email="vitia.88@mail.ru", password="123456")

def test_login1(app):
    app.open_home()
    app.nav_linc("ВХОД")
    app.enter_email_and_pass(email=" ", password=' ')


# app = Application()
# app.open_home()
# app.nav_linc("ВХОД")
# app.enter_email(emai="vitia.88@mail.ru", password="123456")
# app.destroy()