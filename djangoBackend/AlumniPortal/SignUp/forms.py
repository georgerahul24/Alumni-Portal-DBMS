from django import forms


class SignupForm(forms.Form):
    name = forms.CharField(max_length=100,required=True)
    rollNumber = forms.CharField(max_length=100,required=True)

    instituteEmail = forms.CharField(max_length=100, required=True)
    primaryEmail = forms.CharField(max_length=100, required=False)
    showEmail = forms.BooleanField(required=True)

    primaryPhone = forms.CharField(max_length=15, required=True)
    secondaryPhone = forms.CharField(max_length=15, required=False)
    showPhone = forms.BooleanField(required=True)

    graduationYear = forms.IntegerField(required=True)
    degree = forms.CharField(max_length=100, required=True)
    department = forms.CharField(max_length=100, required=True)
    DOB = forms.DateField(required=True)

    permanentCity = forms.CharField(max_length=100, required=True)
    permanentState = forms.CharField(max_length=100, required=True)
    permanentCountry = forms.CharField(max_length=100, required=True)

    linkedin = forms.CharField(max_length=1000, required=True)
    twitter = forms.CharField(max_length=1000, required=True)
    github = forms.CharField(max_length=1000, required=True)

    password = forms.CharField(max_length=100, required=True)








