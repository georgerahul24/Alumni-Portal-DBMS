from django import forms


class SearchBarForm(forms.Form):
    searchText = forms.CharField(max_length=100, required=False)
    startYear = forms.IntegerField(required=False)
    endYear = forms.IntegerField(required=False)
    cse = forms.BooleanField(required=False)
    ece = forms.BooleanField(required=False)
