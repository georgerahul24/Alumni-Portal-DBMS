from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import View
from .forms import AboutMeForm, SocialMediaForm, ProfileDetailsForm, PasswordForm
import mysql.connector
from AlumniPortal.credentialManager import CredentialManager as cm

connection = mysql.connector.connect(user=cm.user, password=cm.password, host=cm.host, database=cm.database,
                                     autocommit=True)


# Create your views here.
class SettingsView(View):
    def get(self, request):
        if not request.user.is_authenticated:
            return redirect("login")
        else:
            user = request.user
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT name,rollNumber,DOB,instituteEmail,primaryEmail,primaryPhoneNumber,secondaryPhoneNumber,degree FROM profileStatic where rollNumber = %s",
                    (user.username,))
                row = cursor.fetchall()[0]
                print(row)

                context = {"name": row[0],
                           "rollNumber": row[1],
                           "DOB": row[2],
                           "instituteEmailID": row[3],
                           "batch": row[7]
                           }
                return render(request, 'SignUp.html', context=context)


class AboutMeView(View):
    def post(self, request):
        if request.user.is_authenticated:
            user = request.user
            form = AboutMeForm(request.POST)
            if form.is_valid():
                permanentCity = form.cleaned_data['permanentCity']
                permanentState = form.cleaned_data['permanentState']
                permanentCountry = form.cleaned_data['permanentCountry']

                rollNumber = user.username
                with connection.cursor() as cursor:
                    cursor.execute(
                        f"UPDATE  ProfileStatic SET permanentCity = '{permanentCity}' WHERE rollNumber = {rollNumber};")
                    cursor.execute(
                        f"UPDATE  ProfileStatic SET permanentState = '{permanentState}' WHERE rollNumber = {rollNumber};")
                    cursor.execute(
                        f"UPDATE  ProfileStatic SET permanentCountry = '{permanentCountry}' WHERE rollNumber = {rollNumber};")
                    connection.commit()
                    return redirect("yourProfile")

            else:
                print(form.errors)
                return redirect("settings")
        else:
            return redirect("login")


class SocialMediaView(View):
    def post(self, request):
        if request.user.is_authenticated:
            user = request.user
            form = SocialMediaForm(request.POST)
            if form.is_valid():
                linkedIn = form.cleaned_data['linkedin']
                github = form.cleaned_data['github']
                twitter = form.cleaned_data['twitter']

                rollNumber = user.username
                with connection.cursor() as cursor:
                    cursor.execute(
                        f"UPDATE  ProfileStatic SET linkedin = '{linkedIn}' WHERE rollNumber = {rollNumber};")
                    cursor.execute(
                        f"UPDATE  ProfileStatic SET github = '{github}' WHERE rollNumber = {rollNumber};")
                    cursor.execute(
                        f"UPDATE  ProfileStatic SET twitter = '{twitter}' WHERE rollNumber = {rollNumber};")
                    connection.commit()
                    return redirect("yourProfile")

            else:
                print(form.errors)
                return redirect("settings")
        else:
            return redirect("login")


class PasswordView(View):
    def post(self, request):
        if request.user.is_authenticated:
            user = request.user
            form = PasswordForm(request.POST)
            if form.is_valid():
                password = form.cleaned_data['password']

                rollNumber = user.username
                with connection.cursor() as cursor:
                    cursor.execute(
                        f"UPDATE  ProfileStatic SET Password = '{password}' WHERE rollNumber = {rollNumber};")
                    connection.commit()
                    return redirect("yourProfile")

            else:
                print(form.errors)
                return redirect("settings")
        else:
            return redirect("login")


class ProfileView(View):
    def post(self, request):
        if request.user.is_authenticated:
            user = request.user
            form = ProfileDetailsForm(request.POST)
            if form.is_valid():
                primaryEmail = form.cleaned_data['primaryEmail']
                primaryPhoneNumber = form.cleaned_data['primaryPhone']
                secondaryPhoneNumber = form.cleaned_data['secondaryPhone']
                showPhone = form.cleaned_data['showPhone']
                showEmail = form.cleaned_data['showEmail']

                rollNumber = user.username
                with connection.cursor() as cursor:
                    cursor.execute(
                        f"UPDATE  ProfileStatic SET primaryEmail = '{primaryEmail}' WHERE rollNumber = {rollNumber};")
                    cursor.execute(
                        f"UPDATE  ProfileStatic SET primaryPhoneNumber = '{primaryPhoneNumber}' WHERE rollNumber = {rollNumber};")
                    cursor.execute(
                        f"UPDATE  ProfileStatic SET secondaryPhoneNumber = '{secondaryPhoneNumber}' WHERE rollNumber = {rollNumber};")
                    cursor.execute(
                        f"UPDATE  ProfileStatic SET showEmail = '{1 if showEmail else 0}' WHERE rollNumber = {rollNumber};")
                    cursor.execute(
                        f"UPDATE  ProfileStatic SET showPhoneNumber = '{1 if showPhone else 0}' WHERE rollNumber = {rollNumber};")

                    connection.commit()
                    return redirect("yourProfile")

            else:
                print(form.errors)
                return redirect("settings")
        else:
            return redirect("login")
