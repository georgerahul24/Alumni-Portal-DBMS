from django.contrib.auth.models import User
import mysql.connector

connection = mysql.connector.connect(user='gr', passwd='password', host='127.0.0.1', database='DocumentVerification',
                                     autocommit=True) #Autocommit is true so that the connection gets updated with the latest data always


class loginBackend():
    def authenticate(self, request, username=None, password=None, **kwargs):
        with  connection.cursor() as cursor:
            if username is not None and password is not None:
                cursor.execute("SELECT Password,RollNumber FROM Student WHERE Email = %s", (username,))
                records = cursor.fetchall()
                print(records, password)
                if len(records) == 0:
                    return None
                if records[0][0] != password:
                    return None
                else:

                    user, created = User.objects.get_or_create(username=records[0][1])
                    if created:  # If the user is created, set unusable password and save
                        user.set_unusable_password()
                        user.save()
                    return user
            return None

    def get_user(self, uid):
        try:
            user = User.objects.get(pk=uid)
            return user
        except:
            return None
