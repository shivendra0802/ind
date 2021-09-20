from django.http import request
from accounts.models import CustomUser, Employer, Jobseeker
from django.forms import forms
from django.http.response import HttpResponse
from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.core.exceptions import ValidationError
# from validate_email import validate_email
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.core.validators import validate_email
from django.views.generic import View
from django.contrib.auth import logout





def userlogin(request):
	return render(request, 'accounts/login.html')

def index(request):
	return render(request, 'accounts/home.html')


class RegistrationView(View):
    def get(self, request):
        return render(request, 'accounts/register.html')

    def post(self, request):
        context = {

            'data': request.POST,
            'has_error': False
        }

        email = request.POST.get('email')
        role = request.POST.get('name')
        password = request.POST.get('password')
        password2 = request.POST.get("confirm-password")

        print(email,role,password,password2)
	
        if len(password) < 6:
            messages.add_message(request, messages.ERROR,
                                 'passwords should be atleast 6 characters long')
            context['has_error'] = True
        if password != password2:
            messages.add_message(request, messages.ERROR,
                                 'passwords dont match')
            context['has_error'] = True

        # if not validate_email(email):
        #     messages.add_message(request, messages.ERROR,
        #                          'Please provide a valid email')
        #     context['has_error'] = True

        try:
            if CustomUser.objects.get(email=email):
                messages.add_message(request, messages.ERROR, 'Email is taken')
                context['has_error'] = True

        except Exception as identifier:
            pass

        if context['has_error']:
            return render(request, 'accounts/register.html', context, status=400)

        user = CustomUser.objects.create_user(email=email,password=password)
        user.set_password(password)
        user.email = email
        # user.role = role
        user.is_active = False
        user.save()
		# print(user)
        
        return redirect('login')





class LoginView(View):
    def get(self, request):
        return render(request, 'accounts/login.html')

    def post(self, request):
        context = {
            'data': request.POST,
            'has_error': False
        }
        email = request.POST.get('email')
		# print(email)
        password = request.POST.get('password')
        if email == '':
            messages.add_message(request, messages.ERROR,
                                 'email is required')
            context['has_error'] = True
        if password == '':
            messages.add_message(request, messages.ERROR,
                                 'Password is required')
            context['has_error'] = True
        user = authenticate(request, email=email, password=password)

        if not user and not context['has_error']:
            messages.add_message(request, messages.ERROR, 'Invalid login')
            context['has_error'] = True

        # if context['has_error']:
        #     return render(request, 'accounts/login.html', status=401, context=context)
        login(request, user)
        return redirect('home')


class LogoutView(View):
    def post(self, request):
        logout(request)
        messages.add_message(request, messages.SUCCESS, 'Logout successfully')
        return redirect('login')

























 

		# if role == 'Employer':
		# 	user = Employer.objects.create_user(email=email)
		# 	user.set_password(password)
		# 	user.email = email
		# 	user.is_active = True
		# 	user.save()

		# else:
		# 	user = Jobseeker.objects.create_user(email=email)
		# 	user.set_password(password)
		# 	user.email = email
		# 	# user.last_name = full_name
		# 	user.is_active = True
		# 	user.save()







