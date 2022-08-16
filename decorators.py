######  E X E R C I S E S ########
# Exercise 1: In file app.py, show the welcome page at /welcome
# Exercise 2: Let's decorate the home route
# Exercise 3: Show the welcome page only once at /
# Exercise 4: In app.py, add the welcome screen to post page as well.
# Bonus: In template/welcome.html, Add a link to go to blog in welcome page.
##################################
from functools import wraps
from flask import session, url_for, render_template

def welcome_screen(original_function):
    @wraps(original_function)
    def decorated_function(*args, **kwargs):
        if session.get('visited'):
            return original_function(*args, **kwargs)
        else:
            session['visited'] = True
            return render_template('welcome.html')

    return decorated_function
