import calendar

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import View
from .forms import *
import mysql.connector
from AlumniPortal.credentialManager import CredentialManager as cm

connection = mysql.connector.connect(user=cm.user, password=cm.password, host=cm.host, database=cm.database,
                                     autocommit=True)


class EducationDetails:
    def __init__(self, degree, fieldOfStudy, institute, description, startYear, endYear, educationID):
        self.educationID = educationID
        self.degree = degree
        self.fieldOfStudy = fieldOfStudy
        self.instituteName = institute
        self.description = description
        self.startYear = startYear
        self.endYear = endYear


class AccomplishmentDetails:
    def __init__(self, title, description, month, year, accomplishmentID):
        self.accomplishmentID = accomplishmentID
        self.title = title
        self.description = description
        self.month = calendar.month_name[month]
        self.year = year


class ExperienceDetails:
    def __init__(self, title, companyName, description, startMonth, startYear, endMonth, endYear, experienceID):
        self.experienceID = experienceID
        self.title = title
        self.company = companyName
        self.description = description
        self.startMonth = calendar.month_abbr[startMonth]
        self.startYear = startYear
        self.endMonth = calendar.month_abbr[endMonth] if endMonth else 'Present'
        self.endYear = endYear if endYear else ''


# Create your views here.
class SettingsView(View):
    def get(self, request):
        if not request.user.is_authenticated:
            return redirect("login")
        else:
            user = request.user
            with connection.cursor() as cursor:

                cursor.execute(
                    "SELECT name,rollNumber,DOB,instituteEmail,primaryEmail,primaryPhoneNumber,secondaryPhoneNumber,degree,graduationYear,department,permanentCity,permanentState,permanentCountry,linkedin,github,twitter FROM profileStatic where rollNumber = %s",
                    (user.username,))
                row = cursor.fetchone()
                print(row)

                cursor.execute(
                    f"SELECT degree,fieldOfStudy,institute,description,startYear,endYear,educationID FROM Education where rollNumber = {user.username};")
                educations = []
                for educationRow in cursor.fetchall():
                    educations.append(
                        EducationDetails(educationRow[0], educationRow[1], educationRow[2], educationRow[3],
                                         educationRow[4], educationRow[5], educationRow[6]))

                cursor.execute(
                    f"SELECT title,body,month,year,accomplishmentID FROM Accomplishments where rollNumber = {user.username};")

                accomplishments = []
                for accomplishmentRow in cursor.fetchall():
                    accomplishments.append(
                        AccomplishmentDetails(accomplishmentRow[0], accomplishmentRow[1], accomplishmentRow[2],
                                              accomplishmentRow[3], accomplishmentRow[4]))

                cursor.execute(
                    f"SELECT title,companyName,description,startMonth,startYear,endMonth,endYear,experienceID FROM Experiences where rollNumber = {user.username};")

                experiences = []
                for experienceRow in cursor.fetchall():
                    experiences.append(
                        ExperienceDetails(experienceRow[0], experienceRow[1], experienceRow[2], experienceRow[3],
                                          experienceRow[4], experienceRow[5], experienceRow[6], experienceRow[7]))

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
                showAddress = form.cleaned_data['showAddress']

                rollNumber = user.username
                with connection.cursor() as cursor:
                    cursor.execute(
                        f"UPDATE  ProfileStatic SET permanentCity = '{permanentCity}' WHERE rollNumber = {rollNumber};")
                    cursor.execute(
                        f"UPDATE  ProfileStatic SET permanentState = '{permanentState}' WHERE rollNumber = {rollNumber};")
                    cursor.execute(
                        f"UPDATE  ProfileStatic SET permanentCountry = '{permanentCountry}' WHERE rollNumber = {rollNumber};")
                    cursor.execute(
                        f"UPDATE  ProfileStatic SET showAddress = '{1 if showAddress else 0}' WHERE rollNumber = {rollNumber};")

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
            print(form)
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


class NewEducationView(View):
    def get(self, request):
        return render(request, "insertEducationDetails.html")

    def post(self, request):
        if request.user.is_authenticated:
            user = request.user
            form = NewEducationForm(request.POST)
            if form.is_valid():
                instituteName = form.cleaned_data['instituteName']
                degree = form.cleaned_data['degree']
                fieldOfStudy = form.cleaned_data['fieldOfStudy']
                startYear = form.cleaned_data['startYear']
                endYear = form.cleaned_data['endYear']
                description = form.cleaned_data['description']

                with connection.cursor() as cursor:
                    cursor.execute(
                        f"INSERT INTO Education (rollNumber,institute,degree,fieldOfStudy,startYear,endYear,description) VALUES ({user.username},'{instituteName}','{degree}','{fieldOfStudy}',{startYear},{endYear},'{description}');")

                return redirect("yourProfile")
            else:
                return redirect("settings")
        else:
            return redirect("login")


class NewAccomplishmentView(View):
    def get(self, request):
        return render(request, "insertAccomplismentDetails.html")

    def post(self, request):
        if request.user.is_authenticated:
            user = request.user
            form = NewAccomplishmentForm(request.POST)
            if form.is_valid():
                title = form.cleaned_data['title']
                description = form.cleaned_data['description']
                month = form.cleaned_data['month']
                year = form.cleaned_data['year']
                print("sdfkbashjklfgblihasfbvlhjkabsf")
                with connection.cursor() as cursor:
                    cursor.execute(
                        f"INSERT INTO Accomplishments (rollNumber,title,body,month,year) VALUES ({user.username},'{title}','{description}',{month},{year});")

                return redirect("yourProfile")
            else:
                return redirect("settings")
        else:
            return redirect("login")


class NewExperienceView(View):
    pass


class editEducationView(View):

    def get(self, request, educationID):
        if request.user.is_authenticated:
            user = request.user
            with connection.cursor() as cursor:
                cursor.execute(
                    f"select educationID,rollNumber,degree,fieldOfStudy,institute,description,startYear,endYear from Education where educationID={educationID};")
                row = cursor.fetchone()
                if int(user.username) != int(row[1]):
                    return redirect("settings")
                context = {
                    'educationID': row[0],
                    'degree': row[2],
                    'fieldOfStudy': row[3],
                    'institute': row[4],
                    'description': row[5],
                    'startYear': row[6],
                    'endYear': row[7],
                }

                return render(request, "editEducationDetails.html", context)

        else:
            return redirect("login")

    def post(self, request, educationID):
        if request.user.is_authenticated:
            user = request.user
            with connection.cursor() as cursor:
                cursor.execute(
                    f"select rollNumber from Education where educationID={educationID};")
                row = cursor.fetchone()
                if int(user.username) != int(row[0]):
                    return redirect("settings")
                form = NewEducationForm(request.POST)
                if form.is_valid():
                    degree = form.cleaned_data['degree']
                    fieldOfStudy = form.cleaned_data['fieldOfStudy']
                    institute = form.cleaned_data['instituteName']

                    startYear = form.cleaned_data['startYear']
                    endYear = form.cleaned_data['endYear']
                    description = form.cleaned_data['description']

                    cursor.execute(f"UPDATE Education SET degree = '{degree}' WHERE educationID = {educationID};")
                    cursor.execute(
                        f"UPDATE Education SET fieldOfStudy = '{fieldOfStudy}' WHERE educationID = {educationID};")
                    cursor.execute(f"UPDATE Education SET institute = '{institute}' WHERE educationID = {educationID};")
                    cursor.execute(
                        f"UPDATE Education SET description = '{description}' WHERE educationID = {educationID};")
                    cursor.execute(f"UPDATE Education SET startYear = '{startYear}' WHERE educationID = {educationID};")
                    cursor.execute(f"UPDATE Education SET endYear = '{endYear}' WHERE educationID = {educationID};")

                    return redirect("settings")


                else:
                    return redirect("editEducation", educationID)





        else:
            return redirect("login")


class editExperienceView(View):
    def post(self, request, experienceID):
        pass


class editAccomplishmentsView(View):
    def post(self, request, accomplishmentID):
        pass


class deleteEducationView(View):
    def get(self, request, educationID):
        if request.user.is_authenticated:
            user = request.user
            with connection.cursor() as cursor:
                cursor.execute("select rollNumber from Education where educationID={}".format(educationID))
                row = cursor.fetchone()
                if int(user.username) != int(row[0]):
                    return redirect("settings")
                else:
                    cursor.execute("delete from Education where educationID={}".format(educationID))
                    return redirect("settings")

    pass


class deleteAccomplishmentView(View):
    def get(self, request, accomplishmentID):
        pass


class deleteExperienceView(View):
    def get(self, request, experienceID):
        pass
