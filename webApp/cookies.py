import random
import string
from flask import make_response, render_template


def hasCookies(request):
    return "userid" in list(request.cookies.keys())

def getUserSessionId():
    N = 10
    # Verify that there are no that cookie in database
    return ''.join([random.choice(string.ascii_lowercase + string.ascii_uppercase + string.digits) for _ in range(N)])
