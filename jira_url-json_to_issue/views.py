import json

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.utils import timezone
import requests
from .models import Issue
import pprint

from jira_integration.conf import jira_conf
from .forms import IssueForm
from jira_integration.Jira import Jira


def index(request):
    return HttpResponse("index jira_url-json_to_issue")


def jsonn(request, json1):
    # entry to the database
    iss = Issue(source="jsonn", json=json1)
    iss.save()

    # create issue
    response = Jira().jira_post(json1)

    # return HttpResponse("Here's the text of the Web page." + str(response.text))
    resp = json.loads(response.text)
    # resp = response.json
    # print("aaaa" + str(resp))
    # resp = {'issues': [{'id': '10286', 'key': 'TEST1-287', 'self': 'https://incident-integration-test.atlassian.net/rest/api/3/issue/10286'}], 'errors': []}
    date = {'response': resp}
    # date = {'response': {'issues': [{'id': '10286', 'key': 'TEST1-287', 'self': 'https://incident-integration-test.atlassian.net/rest/api/3/issue/10286'}], 'errors': []}}

    iss.issue_date_adding = timezone.now()
    iss.issue_id = resp['issues'][0]['id']
    iss.issue_key = resp['issues'][0]['key']
    iss.issue_url = resp['issues'][0]['self']
    iss.save()

    return render(request, 'after_create.html', date)


def gettt(request):
    json1 = "https://incident-integration-test.atlassian.net/rest/api/3/issue/10286"
    response = Jira().jira_get(json1)
    # print(str(response))
    # print(str(response.text))
    # print()

    dict_text_for_html = json.dumps(
        json.loads(response.text), indent=4
    ).replace(' ', '&nbsp').replace(',\n', ',\n<b>').replace(':', ',</b>:').replace(',\n', ',<br>').replace('\n', '<br>')

    return HttpResponse(dict_text_for_html)


def get_name(request):
    if request.method == 'POST':
        form = IssueForm(request.POST)
        if form.is_valid():

            payload = json.dumps(data)
            i1 = Jira()
            print(i1.jira_post(payload))
            return HttpResponseRedirect('/thanks/')

    else:
        form = IssueForm(request.GET)
        return render(request, 'name.html', {'form': form})

    return render(request, 'name.html', {'form': form})
