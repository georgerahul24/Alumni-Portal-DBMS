from django.shortcuts import render, redirect
from django.views.generic import View
import mysql.connector

connection = mysql.connector.connect(user='gr', password='password', host='127.0.0.1', database='DocumentVerification',autocommit=True)


# Create your views here.
class YourProfileView(View):
    def get(self, request):
        if not request.user.is_authenticated:
            return redirect("login")
        else:
            user = request.user
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM student where rollNumber = %s", (user.username,))
                row = cursor.fetchall()[0]
                print(row)

                context = {"name": row[2],
                           "rollNumber": row[0],
                           "DOB":"mm dd yyyy",
                           "instituteEmailID": row[4],
                           "primaryEmailID": row[4],
                           "primaryPhoneNumber": row[1],
                           "secondaryPhoneNumber": row[1],
                           "batch": row[3]
                           }
                return render(request, 'yourProfileTemplate.html', context=context)
