import os

from django.shortcuts import render, redirect
from django.views.generic import View
import mysql.connector
from AlumniPortal.credentialManager import CredentialManager as cm

connection = mysql.connector.connect(user=cm.user, password=cm.password, host=cm.host, database=cm.database,
                                     autocommit=True)


# Create your views here.
class YourProfileView(View):
    def get(self, request):
        if not request.user.is_authenticated:
            return redirect("login")
        else:
            user = request.user
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT name,rollNumber,DOB,instituteEmail,primaryEmail,primaryPhoneNumber,secondaryPhoneNumber,degree,graduationYear,department,permanentCity,permanentState,permanentCountry FROM profileStatic where rollNumber = %s",
                    (user.username,))
                row = cursor.fetchall()[0]
                print(row)

                context = {"name": row[0],
                           "rollNumber": row[1],
                           "DOB": row[2],
                           "instituteEmailID": row[3],
                           "primaryEmailID": row[4] if row[4] is not None else None,
                           "primaryPhoneNumber": row[5],
                           "secondaryPhoneNumber": row[6] if row[6] is not None else " ",
                           "batch": row[7] + " " + str(row[8]) + " " + row[9],
                           "permanentCity": row[10],
                           "permanentState": row[11],
                           "permanentCountry": row[12],
                           }
                return render(request, 'yourProfileTemplate.html', context=context)
