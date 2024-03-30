import os

from django.shortcuts import render, redirect
from django.views.generic import View
import mysql.connector
from AlumniPortal.credentialManager import CredentialManager as cm
import calendar

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


class AccomplishmentDetails:
    def __init__(self, title, description, month, year):
        self.title = title
        self.description = description
        self.month = calendar.month_name[month]
        self.year = year
class ExperienceDetails:
    def __init__(self, title, companyName, description, startMonth, startYear, endMonth, endYear):
        self.title = title
        self.company = companyName
        self.description = description
        self.startMonth = calendar.month_abbr[startMonth]
        self.startYear = startYear
        self.endMonth = calendar.month_abbr[endMonth] if endMonth else 'Present'
        self.endYear = endYear if endYear else ''


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
                    educations.append(
                        EducationDetails(educationRow[0], educationRow[1], educationRow[2], educationRow[3],
                                         educationRow[4], educationRow[5]))

                cursor.execute(
                    f"SELECT title,body,month,year FROM Accomplishments where rollNumber = {user.username};")

                accomplishments = []
                for accomplishmentRow in cursor.fetchall():
                    accomplishments.append(
                        AccomplishmentDetails(accomplishmentRow[0], accomplishmentRow[1], accomplishmentRow[2],
                                              accomplishmentRow[3]))

                cursor.execute(
                    f"SELECT title,companyName,description,startMonth,startYear,endMonth,endYear FROM Experiences where rollNumber = {user.username};")

                experiences = []
                for experienceRow in cursor.fetchall():
                    experiences.append(
                        ExperienceDetails(experienceRow[0], experienceRow[1], experienceRow[2], experienceRow[3],
                                          experienceRow[4], experienceRow[5], experienceRow[6]))

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
                           "accomplishments": accomplishments,
                           "experiences": experiences,
                           }
                return render(request, 'yourProfileTemplate.html', context=context)
