from django import forms


class SignupForm(forms.Form):
    name = forms.CharField(max_length=100, required=True)
    rollNumber = forms.CharField(max_length=100, required=True)

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


class AboutMeForm(forms.Form):
    permanentCity = forms.CharField(max_length=100, required=True)
    permanentState = forms.CharField(max_length=100, required=True)
    permanentCountry = forms.CharField(max_length=100, required=True)
    showAddress = forms.BooleanField(required=False)


class SocialMediaForm(forms.Form):
    linkedin = forms.CharField(max_length=1000, required=False)
    twitter = forms.CharField(max_length=1000, required=False)
    github = forms.CharField(max_length=1000, required=False)


class PasswordForm(forms.Form):
    password = forms.CharField(max_length=100, required=True)


class ProfileDetailsForm(forms.Form):
    primaryEmail = forms.CharField(max_length=100, required=False)
    showEmail = forms.BooleanField(required=False)

    primaryPhone = forms.CharField(max_length=15, required=True)
    secondaryPhone = forms.CharField(max_length=15, required=False)
    showPhone = forms.BooleanField(required=False)


class NewEducationForm(forms.Form):
    instituteName = forms.CharField(max_length=100, required=True)
    degree = forms.CharField(max_length=100, required=True)
    fieldOfStudy = forms.CharField(max_length=100, required=True)
    startYear = forms.IntegerField(required=True)
    endYear = forms.IntegerField(required=True)

    description = forms.CharField(max_length=1000, required=False)


class NewExperienceForm(forms.Form):
    title = forms.CharField(max_length=100, required=True)
    companyName = forms.CharField(max_length=100, required=True)
    description = forms.CharField(max_length=1000, required=False)
    startMonth = forms.IntegerField(required=True)
    startYear = forms.IntegerField(required=True)
    endMonth = forms.IntegerField(required=False)
    endYear = forms.IntegerField(required=False)


class NewAccomplishmentForm(forms.Form):
    title = forms.CharField(max_length=100, required=True)
    description = forms.CharField(max_length=1000, required=False)
    month = forms.IntegerField(required=True)
    year = forms.IntegerField(required=True)
