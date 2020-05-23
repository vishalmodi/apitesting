"""
Users class to add/update/delete/query using RESTapi call.
"""
from RestApiLib.base_lib import BaseLib


class Users(BaseLib):
    """Users Class for  Add/Edit/Delete/List."""

    def __init__(self):
        super().__init__(base_rul='https://reqres.in/api/')
        self.users_url = '{}users'.format(self.base_url)

    def get_users(self):
        """Return list of Users.

        :return: list of users.
        :rtype: (status code, [users])
        Example:
        (200,
        [
          {
            "id": 1,
            "name": "Leanne Graham",
            "username": "Bret",
            "email": "Sincere@april.biz",
            "address": {
              "street": "Kulas Light",
              "suite": "Apt. 556",
              "city": "Gwenborough",
              "zipcode": "92998-3874",
              "geo": {
                "lat": "-37.3159",
                "lng": "81.1496"
              }
            }]
        """
        return self.get(self.users_url)

    def get_user(self, user_id):
        """Return user based on user id.
        :param user_id: user id
        :rtype: (status code, [users])
        Example:
        (200,
          {
            "id": 1,
            "name": "Leanne Graham",
            "username": "Bret",
            "email": "Sincere@april.biz",
            "address": {
              "street": "Kulas Light",
              "suite": "Apt. 556",
              "city": "Gwenborough",
              "zipcode": "92998-3874",
              "geo": {
                "lat": "-37.3159",
                "lng": "81.1496"
              }
            }
        """
        single_user_url = '{}/{}'.format(self.users_url, user_id)
        return self.get(single_user_url)

    def add_user(self, name, job_title):
        """Add User.

        :param str name: User name.
        :param str job_title: Job title of user
        :return: API call status and result.
        :rtype: (status code, user)
        """
        # TODO - Add check for invalid parameter

        json_payload = {'name': name, 'job': job_title}
        return self.post(self.users_url, json=json_payload)

    def update_user(self, user_id, name, job_title):
        """Update User.

        :param int name: User id
        :param str name: User name.
        :param str job_title: Job title of user
        :return: API call status and result.
        :rtype: (status code, user)
        """
        # TODO - Add check for invalid parameter

        single_user_url = '{}/{}'.format(self.users_url, user_id)
        json_payload = {'name': name, 'job': job_title}
        return self.push(single_user_url, json=json_payload)
