from django.shortcuts import render, redirect
from django.views.generic import View
from .forms import LoginForm
from django.contrib.auth import authenticate, login, logout


# Create your views here.
class LoginView(View):
    def get(self, request):
        print(request.user)
        if request.user.is_authenticated:
            return redirect("yourProfile")
        else:
            print("User is not authenticated")
        context = {"loginFailed": False}
        return render(request, "LoginPage.html", context=context)

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            user = authenticate(username=email, password=password)
            if user is None:
                context = {"loginFailed": True}
                return render(request, "LoginPage.html", context=context)
            else:
                login(request, user)
                return redirect("yourProfile")



        else:
            context = {"loginFailed": True}
            return render(request, "LoginPage.html", context=context)


class ForgotPasswordEmailInputView(View):
    # TODO: Might have to create a database for this too to dynamically generate the links and all
    def get(self, request):
        return render(request, "ForgotPasswordEmailInput.html")


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect("login")
