from django import forms


class SearchBarForm(forms.Form):
    searchText = forms.CharField(max_length=100, required=True)
