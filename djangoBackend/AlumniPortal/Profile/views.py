import os

from django.shortcuts import render, redirect
from django.views.generic import View
import mysql.connector
from AlumniPortal.credentialManager import CredentialManager as cm

connection = mysql.connector.connect(user=cm.user, password=cm.password, host=cm.host, database=cm.database,
                                     autocommit=True)


class EducationDetails:
    def __init__(self, degree, fieldOfStudy, institute, description, startYear, endYear):
        self.degree = degree
        self.fieldOfStudy = fieldOfStudy
        self.instituteName = institute
        self.description = description
        self.startYear = startYear
        self.endYear = endYear


# Create your views here.
class YourProfileView(View):
    def get(self, request):
        if not request.user.is_authenticated:
            return redirect("login")
        else:
            user = request.user
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT name,rollNumber,DOB,instituteEmail,primaryEmail,primaryPhoneNumber,secondaryPhoneNumber,degree,graduationYear,department,permanentCity,permanentState,permanentCountry,linkedin,github,twitter FROM profileStatic where rollNumber = %s",
                    (user.username,))
                row = cursor.fetchall()[0]
                print(row)
                cursor.execute(
                    f"SELECT degree,fieldOfStudy,institute,description,startYear,endYear FROM Education where rollNumber = {user.username};")
                educations = []
                for educationRow in cursor.fetchall():
                    educations.append(EducationDetails(educationRow[0], educationRow[1], educationRow[2], educationRow[3], educationRow[4], educationRow[5]))

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
                           "educations": educations,
                           }
                return render(request, 'yourProfileTemplate.html', context=context)
