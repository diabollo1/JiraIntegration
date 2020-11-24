from django import forms


class IssueForm(forms.Form):
    summary = forms.CharField(label='Podsumowanie', max_length=200)
    project_key = forms.CharField(label='Projekt', max_length=200)
    issuetype = forms.CharField(label='Zadanie', max_length=200)
    # TODO: creating a full form with functionality
