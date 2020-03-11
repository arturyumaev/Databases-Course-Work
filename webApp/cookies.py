import random
import string
from flask import make_response

def has_cookies(request):
    return "userid" in list(request.cookies.keys())
        

def get_userid():
    N = 10
    # Verify that there are no that cookie in database
    return ''.join(random.choices(string.ascii_lowercase + string.ascii_uppercase + string.digits, k=N))


def validate_cookies(request, resp_obj):
    resp = make_response(resp_obj)
    if not has_cookies(request):
        print("No cookies")
        resp.set_cookie('userid', get_userid())
        print("New cookies set")
        # create database space
    else:
        print("Has cookies")

    return resp