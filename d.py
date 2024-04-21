import random
def Generateotp():
    return ''.join(random.choices('0123456789',k=6))
otp=Generateotp()
print("your OTP",otp)