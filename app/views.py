import random
from django.shortcuts import render, redirect
from django.core.mail import send_mail


def login_view(request):

        email = request.POST.get('email')

        # Generate OTP
        otp = str(random.randint(1000, 9999))

        # Store email and OTP in session
        request.session['email'] = email
        request.session['otp'] = otp

        # Send OTP to user's email
        send_mail(
            'Your otp code',
            f'Your OTP is: {otp}',
            'jeerusami@gmail.com',
            [email],
        )
        if request.method=='POST':

           return redirect('verify_otp')

        return render(request, 'app/login.html')


def verify_otp(request):

    if request.method == 'POST':

        user_otp = request.POST.get('user_otp')

        # Get OTP that was stored during login
        session_otp = request.session.get('otp')

        if user_otp == session_otp:
            return render(request, 'app/success.html')
        else:
            return render(request, 'app/failure.html')

    return render(request, 'app/verify_otp.html')