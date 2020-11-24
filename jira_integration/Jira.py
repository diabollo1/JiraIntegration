import json
import sys
from aifc import Error

import requests

from jira_integration.conf import jira_conf


class Jira:
    def __init__(self):
        self.url = jira_conf.url
        self.auth = jira_conf.auth
        self.headers = jira_conf.headers

    def create_issue(self, json1):
        try:
            response = requests.request(
                "POST",
                self.url,
                data=json1,
                headers=self.headers,
                auth=self.auth
            )
            # print("++++++++++++++++++++++++++++" + str(response.text))
            # print("+++" + str(json.loads(response.text)["issues"]))

        except Error as e:
            print("Error creating issue" + str(e))

        return response
