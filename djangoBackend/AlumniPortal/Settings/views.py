from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View
from .forms import SignupForm
import mysql.connector
from AlumniPortal.credentialManager import CredentialManager as cm

connection = mysql.connector.connect(user=cm.user, password=cm.password, host=cm.host, database=cm.database,
                                     autocommit=True)


# Create your views here.
class SettingsView(View):
    def get(self, request):
        return render(request, "SignUp.html")


