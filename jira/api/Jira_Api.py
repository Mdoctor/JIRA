from .curl import Curl
from urllib import parse
import json

"""
request token url:JIRA_BASE_URL + "/plugins/servlet/oauth/request-token"
authorization url:JIRA_BASE_URL + "/plugins/servlet/oauth/authorize""
access token url:JIRA_BASE_URL + "/plugins/servlet/oauth/access-token"
oauth signing type:RSA-SHA1
consumer key
as configured in Step 1
"""


class Jira_Api(object):
    def __init__(self):
        self.curl = Curl()

    def jira_login(self, username, pwd):
        url = 'http://localhost:8080/jira/rest/api/2/issue/'
        # decrqto = lambda x:hashlib.md5(x.encode()).hexdigest()
        # mdpwd = decrqto(pwd)
        data = {
            "username": username,
            "password": pwd
        }
        endata = parse.urlencode(data).encode()
        result = self.curl.post(url, endata)
        print(result, self.curl.cj)
        return result, self.curl.cj

    def jire_submit(self, parms):
        """http://hostname/rest/<api-name>/<api-version>/<resource-name>"""
        url = "http://localhost:8080/jira/rest/api/2/issue/"
        data = {
            "fields": {
                "project": {"id": "10000"},
                "summary": "No REST for the Wicked.",
                "description": "Creating of an issue using ids for projects and issue types using the REST API",
                "issuetype": {"id": "3"}
            }
        }
        endata = parse.urlencode(json.dumps(data, ensure_ascii=True)).encode()
        result, self.curl.cj = self.curl.post(url, endata)
        return result, self.curl.cj

    def test(self):
        url = "http://www.baidu.com"
        result = self.curl.post(url)
        return result, self.curl.cj
