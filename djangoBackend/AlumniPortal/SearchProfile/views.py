import mysql.connector
from django.shortcuts import render, redirect
from django.views import View
from AlumniPortal.credentialManager import CredentialManager as cm

connection = mysql.connector.connect(user=cm.user, password=cm.password, host=cm.host, database=cm.database,
                                     autocommit=True)


# Create your views here.
class SearchProfileView(View):
    def get(self, request, rollNumber):
        if request.user.is_authenticated:

            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT name,rollNumber,DOB,instituteEmail,primaryEmail,primaryPhoneNumber,secondaryPhoneNumber,degree,graduationYear,department,permanentCity,permanentState,permanentCountry,linkedin,github,twitter,showPhoneNumber,showEmail FROM profileStatic where rollNumber = %s",
                    (rollNumber,))
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
                           "linkedin": row[13],
                           "github": row[14],
                           "twitter": row[15],
                           "showPhone": row[16],
                           "showEmail": row[17],
                           }
                return render(request, 'searchProfileTemplate.html', context=context)
        else:
            return redirect("login")
