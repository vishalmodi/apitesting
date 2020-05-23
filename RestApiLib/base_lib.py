"""
Base class for lib.
"""
import requests


class BaseLib:
    STATUS_200 = 200
    STATUS_201 = 201
    STATUS_404 = 404

    def __init__(self, base_rul):
        self.base_url = base_rul

    def get(self, url, params=None):
        """Call Rest API using Get.

        :param url: API url
        :param params: Parameter to call API
        :return: API call status and result.
        :rtype: (status code, [result])
        """
        response = requests.get(url, params)
        if response.ok:
            return response.status_code, response.json()['data']
        else:
            return response.status_code, []

    def post(self, url, json):
        """Call Rest API using Get.

        :param url: API url
        :param json: Parameter as json
        :return: API call status and result.
        :rtype: (status code, [result])
        """
        response = requests.post(url, json=json)
        if response.ok:
            return response.status_code, response.json()
        else:
            return response.status_code, []

    def push(self, url, json):
        """Call Rest API using Get.

        :param url: API url
        :param json: Parameter as json
        :return: API call status and result.
        :rtype: (status code, [result])
        """
        response = requests.post(url, json=json)
        if response.ok:
            return response.status_code, response.json()
        else:
            return response.status_code, []
