from conftest import login


def test_login_page_loads(client):
    assert client.get("/login").status_code == 200


def test_student_login_redirects_to_student_dashboard(client):
    response = login(client, "amina@handin.test")
    assert response.status_code == 302
    assert response.headers["Location"].endswith("/student/")


def test_lecturer_login_redirects_to_lecturer_dashboard(client):
    response = login(client, "achieng@handin.test")
    assert response.status_code == 302
    assert response.headers["Location"].endswith("/lecturer/")


def test_wrong_password_is_rejected(client):
    response = login(client, "amina@handin.test", "wrong-password")
    assert response.status_code == 200
    assert b"Incorrect email or password" in response.data


def test_dashboard_requires_login(client):
    response = client.get("/student/")
    assert response.status_code == 302
    assert "/login" in response.headers["Location"]


def test_lecturer_cannot_open_student_dashboard(client):
    login(client, "achieng@handin.test")
    assert client.get("/student/").status_code == 403


def test_student_sees_only_enrolled_courses(client):
    login(client, "amina@handin.test")
    page = client.get("/student/").data
    assert b"CS101" in page and b"DB201" in page
    assert b"WEB210" not in page
