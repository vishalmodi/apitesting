from RestApiLib.users import Users


def test_get_users():
    """This test verify whether the get call is returning the Users or not."""
    users = Users()

    # Call API
    status_code, user_list = users.get_users()

    # Verify Call Status
    assert status_code == users.STATUS_200, "Status code should be 200"
    assert len(user_list) > 0, "User list is empty."


def test_get_single_user():
    """This test verify whether the API return the single user or not"""
    users = Users()
    status_code, user_list = users.get_users()

    # Call API
    status_code, user = users.get_user(user_id=user_list[0]['id'])

    # Verify Call Status
    assert status_code == users.STATUS_200, "Status code should be 200"
    assert user == user_list[0], 'API is returning wrong user.'


def test_get_invalid_user():
    """This test verify whether the API return 404 when user not found."""
    users = Users()

    # Call API
    status_code, user = users.get_user(user_id=23)

    # Verify Call Status
    assert status_code == users.STATUS_404, "API is not returning error message when user not found."


def test_add_valid_user():
    """This test verify whether the API can add new user or not."""
    users = Users()
    name = 'Vishal'
    job_title = 'SDET'

    # Call API to add user
    status_code, user = users.add_user(name, job_title)

    # Verify Call Status and User info.
    assert status_code == users.STATUS_201, "Failed to add new user"
    assert name == user['name'], 'Wrong user is added.'
    assert job_title == user['job'], 'Wrong job title is added.'


def test_update_valid_user():
    """This test verify whether the API can update existing user or not."""
    users = Users()
    name = 'Vishal'
    job_title = 'SDET'

    # Add new user and verify status
    status_code, user = users.add_user(name, job_title)
    assert status_code == users.STATUS_201, "Failed to add new user"
    user_id = user['id']

    # Update name and job title
    name = 'Vishal-Updated'
    job_title = 'SDET-Updated'
    status_code, user_updated = users.update_user(user_id, name, job_title)
    assert status_code == users.STATUS_201, "Failed to update existing user."

    # Verify updated user name and title
    # TODO - Can't verify newly add/update using get
    # status_code, user = users.get_user(user_id)
    assert user_updated['name'] == name, 'Wrong user is updated.'
    assert user_updated['job'] == job_title, 'Wrong job title is updated.'
