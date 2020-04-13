import random
import string
from flask import make_response, render_template

def has_cookies(request):
    return "userid" in list(request.cookies.keys())
        

def get_userid():
    N = 10
    # Verify that there are no that cookie in database
    return ''.join([random.choice(string.ascii_lowercase + string.ascii_uppercase + string.digits) for _ in range(N)])
