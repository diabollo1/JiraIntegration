import json

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from datetime import datetime
import requests

from jira_integration.conf import jira_conf
from .forms import IssueForm
from jira_integration.Jira import Jira


def index(request):
    return HttpResponse("index jira_url-json_to_issue")


def jsonn(request, json1):
    response = Jira().create_issue(json1)
    return HttpResponse("Here's the text of the Web page." + str(response.text))


def get_name(request):
    if request.method == 'POST':
        form = IssueForm(request.POST)
        if form.is_valid():

            payload = json.dumps(data)
            i1 = Jira()
            print(i1.create_issue(payload))
            return HttpResponseRedirect('/thanks/')

    else:
        form = IssueForm(request.GET)
        return render(request, 'name.html', {'form': form})

    return render(request, 'name.html', {'form': form})
