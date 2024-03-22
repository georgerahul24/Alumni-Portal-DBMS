from django.shortcuts import render, redirect
from django.views.generic import View
from .forms import SignupForm
from django.contrib.auth import authenticate, login, logout


# Create your views here.
class SignUpView(View):
    def get(self, request):
        print(SignupForm())
        return render(request, "SignUp.html")

    def post(self, request):
        form = SignupForm(request.POST)
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
