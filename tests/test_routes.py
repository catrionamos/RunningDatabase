import pytest
from werkzeug.security import generate_password_hash

#home page loads
def test_index_page(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"Welcome to Running Database" in response.data
    assert b"Find a Program" in response.data

#about page loads
def test_about_page(client):
    response = client.get('/about')
    assert response.status_code == 200
    assert b"About Running Database" in response.data

#programs page lists every program
def test_programs_page(client, mock_db):
    mock_db.fetchall.return_value = [("Couch to 5K","Beginner",9,"Walk run plan"),("Half Marathon Plan","Intermediate",12,"Build up to 21km")]

    response = client.get("/programs")
    assert response.status_code == 200
    assert b"Couch to 5K" in response.data
    assert b"Half Marathon Plan" in response.data
    assert b"2 programs found." in response.data

#programs page filters by fitness level
def test_programs_filter(client, mock_db):
    mock_db.fetchall.return_value = [("Couch to 5K","Beginner",9,"Walk run plan")]

    response = client.post("/programs", data={"level":"Beginner"})
    assert response.status_code == 200
    assert b"Couch to 5K" in response.data
    #check the sql sent to the database only asks for Beginner programs
    sql = mock_db.execute.call_args[0][0]
    assert "where target_level ='Beginner'" in sql

#shop page shows the products
def test_shop_page(client, mock_db):
    mock_db.fetchall.return_value = [("Trail Running Shoes","Shoes",89.99,15)]

    response = client.get("/shop")
    assert response.status_code == 200
    assert b"Running Gear Store" in response.data
    assert b"Trail Running Shoes" in response.data
    assert b"89.99" in response.data

#login page loads
def test_login_page_loads(client):
    response = client.get("/login")
    assert response.status_code == 200
    assert b"Sign In" in response.data

#correct login creates a session
def test_login_success(client, mock_db):
    hashed_pw = generate_password_hash("Running2026")
    mock_db.fetchone.return_value = (hashed_pw,)
    mock_db.fetchall.return_value = []

    response = client.post("/login",data={"username":"CatrionaRuns", "password":"Running2026"},follow_redirects=True)

    assert response.status_code == 200
    assert b"Logged in successfully!" in response.data
    with client.session_transaction() as test_session:
        assert test_session["user_id"] == "CatrionaRuns"

#wrong password is refused
def test_login_invalid_password(client, mock_db):
    hashed_pw = generate_password_hash("Running2026")
    mock_db.fetchone.return_value = (hashed_pw,)

    response = client.post("/login", data={"username":"CatrionaRuns", "password":"wrongpassword"},follow_redirects=True)

    assert response.status_code == 200
    assert b"Invalid username or password." in response.data
    with client.session_transaction() as test_session:
        assert "user_id" not in test_session

#unknown user is refused
def test_login_unknown_user(client, mock_db):
    mock_db.fetchone.return_value = None

    response = client.post("/login",data= {"username":"nouser", "password":"Running2026"},follow_redirects=True)
    assert response.status_code == 200
    assert b"Invalid username or password." in response.data

#log a run sends users who are not logged in to the login page
def test_log_run_requires_login(client):
    response = client.get("/log_run",follow_redirects=True)

    assert response.status_code == 200
    assert b"Please log in to log a run." in response.data
    assert b"Sign In" in response.data

#log a run page shows the user's runs
def test_log_run_page(client, mock_db):
    with client.session_transaction() as test_session:
        test_session["user_id"] = "CatrionaRuns"
    mock_db.fetchall.return_value = [("2026-11-01",5.0,24,"Parkrun")]

    response = client.get("/log_run")
    assert response.status_code == 200
    assert b"Logged in as" in response.data
    assert b"Parkrun" in response.data

#a new run is saved
def test_log_run_save(client, mock_db):
    with client.session_transaction() as test_session:
        test_session["user_id"] = "CatrionaRuns"
    mock_db.fetchall.return_value = []

    response = client.post("/log_run",data={"run_date":"2026-11-20", "distance_km":"5.5", "duration_minutes":"28", "notes":"Felt good"},follow_redirects=True)

    assert response.status_code == 200
    assert b"Run saved!" in response.data
    #check an insert statement was sent to the runs table
    sqls = [call[0][0] for call in mock_db.execute.call_args_list]
    assert any("insert into runs" in sql for sql in sqls)

#logout clears the session
def test_logout(client):
    with client.session_transaction() as test_session:
        test_session["user_id"] = "CatrionaRuns"

    response = client.get("/logout",follow_redirects=True)

    assert response.status_code == 200
    assert b"You have been logged out." in response.data
    with client.session_transaction() as test_session:
        assert "user_id" not in test_session
