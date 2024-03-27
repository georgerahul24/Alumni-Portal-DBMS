import mysql.connector
from django.shortcuts import render, redirect
from django.views import View
from AlumniPortal.credentialManager import CredentialManager as cm

from .forms import SearchBarForm

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
class SearchProfileView(View):
    def get(self, request, rollNumber):
        if request.user.is_authenticated:

            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT name,rollNumber,DOB,instituteEmail,primaryEmail,primaryPhoneNumber,secondaryPhoneNumber,degree,graduationYear,department,permanentCity,permanentState,permanentCountry,linkedin,github,twitter,showPhoneNumber,showEmail,showAddress FROM profileStatic where rollNumber = %s",
                    (rollNumber,))
                row = cursor.fetchall()[0]
                print(row)
                cursor.execute(
                    f"SELECT degree,fieldOfStudy,institute,description,startYear,endYear FROM Education where rollNumber = {rollNumber};")
                educations = []
                for educationRow in cursor.fetchall():
                    educations.append(
                        EducationDetails(educationRow[0], educationRow[1], educationRow[2], educationRow[3],
                                         educationRow[4], educationRow[5]))

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
                           "showAddress": row[18],
                           "educations": educations,
                           }
                return render(request, 'searchProfileTemplate.html', context=context)
        else:
            return redirect("login")


class SearchBarView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return render(request, "searchBarForSearch.html")
        else:
            return redirect("login")


class Result:
    def __init__(self, name, rollNumber, graduationYear, degree, department):
        self.name = name
        self.rollNumber = rollNumber
        self.graduationYear = graduationYear
        self.degree = degree
        self.department = department


class SearchResultsView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect("searchbar")
        else:
            return redirect("login")

    def post(self, request):
        if request.user.is_authenticated:
            form = SearchBarForm(request.POST)
            if form.is_valid():
                searchText = form.cleaned_data['searchText']
                rows = []
                if searchText.isnumeric():
                    # Then this is a roll number
                    with connection.cursor() as cursor:
                        cursor.execute(
                            f"SELECT name,rollNumber,graduationYear,degree,department FROM profileStatic where rollNumber = {searchText} ")
                        rows = cursor.fetchall()
                else:
                    # This is a string to search
                    # TODO: Try searching companies and institutes also
                    with connection.cursor() as cursor:
                        cursor.execute(
                            f"SELECT name,rollNumber,graduationYear,degree,department FROM profileStatic where name like '%{searchText}%'")
                        rows = cursor.fetchall()

                if len(rows) == 0:
                    return redirect("searchbar")
                print(rows)
                resultRows = []
                for row in rows:
                    resultRows.append(Result(row[0], row[1], row[2], row[3], row[4]))
                context = {"resultRows": resultRows}
                return render(request, "searchResultPageForProfile.html", context)
            else:
                print(form.errors)
                return redirect("searchbar")

        else:
            return redirect("login")
