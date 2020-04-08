## The following doc includes instructions on how to navigate the project - particularly changing and dealing with the front end.

#Directory Structure (zsheet v1.1)

In the folder are 5 items:

1 - db.sqlite3 : this is where the database of users and their information are stored, I’m not really sure how to access it directly but there is a way using Django which I’ll explain below

2- manage.py : used to run majority of the django commands

3- zsheets : the main folder where important stuff are kept like settings and urls

4- zapp : the main app where most of the work will be done and where the model is stored

5- templates: where html templates are stored


#Current web pages

From what I figured out, the way django works is that it has a list of urls (zsheets/urls.py file). When a url is typed in the address bar, django looks through this list (parts of the list import other url lists so it will also look in zapp/url.py for example). 

Once it finds a match with the url, it will call the view for that url found in views.py (for urls in zapp/urls.py it will look at zapp/views.py - the view will return a HttpResponse and show the user what it needs to see.

The current web pages along with their views are

/zapp/ - with view in zapp.views.login (the login method in zapp/views.py)

This page redirects to /accounts/login/

/accounts/login/ - this is provided by Django and so we don’t really have access to the view

This page is a login page, after logging in successfully it will redirect to the users dashboard

/zapp/dashboard/ - with view in zapp.views.user_dashboard

This page shows a users dashboard and can only be viewed if the user is logged in.

There are other web pages but they do not really have anything atm so I have left them out of this list, you can find them in zapp/urls.py with their views in zapp/views.py

#Templates

The views themselves are in python and so you can’t just put html there directly as far as I’m aware.

The way this is done is through templates. By telling the view to use its corresponding template it will then go to the corresponding file in the templates directory.

The login and logout templates are in templates/registration - the rest of the templates should go in templates/zapp. There should be one there for the user_dashboard page already, but it is very simple.

The templates are all html, they get access to whatever you pass on to them in the view, if you need access to a specific thing, for example the database of all schedules - let me know, I should be able to pass it on as an argument and I’ll tell you what the name of the variable will be.

There is one thing that always looks like it’s passed, which is user. This is the current user of the session assuming they are logged in - you can assume for other than the login page that they are logged in.

user is of type User which has the following fields

* username
* password
* email
* first_name
* last_name

And one other field:

employee - each User has an associated Employee account, an employee has access to its associated user account as well, employee has also one other field

manager


So for example, if we wanted to access an employees manager and we only had access to the user account because of how the html is, we could write

{{ user.employee.manager }} and this will give the manager object converted into a string  (I think) (which for now just returns the manager’s username). You can see this in the dashboard.html template.

There are also other objects but for now I’d recommend playing around with this and improving the login and dashboard pages. Remember the html files are all in templates. It’s probably worth mentioning I have no idea how the login and logout pages work so I don’t recommend changing them unless you know what all of it means - I suspect there's extra lines of codes in the associated views but those views are kind of hidden files so not sure how to access them and it's not really recommended to tamper with imported stuff.

# Admin

Django also includes an admin interface, there is currently one admin user

Username = MuneerAdmin
Password = password

In order to login, go to /admin/
This page will allow you to create users fairly easily and check existing users. In order to create an employee or a manager, you must first create a user and then link an employee object with that user object.

Some accounts are already there (unless the sql file has been changed), the usernames can be found from the admin page, the passwords are all t3stp4ss


# Testing

In order to test the project, make sure you have python and django install (version 3 I think).
Be in the directory with manage.py and run (you might have to write python3 instead of python)

python manage.py runserver

And then go to http://127.0.0.1:8000/zapp/ on your browser, that’ll take you to the login page. Try testing the app, go to the dashboard page without logging in, login with different accounts etc.

# CSS

I’m not really sure where css files would go or how they would work, I’d recommend looking at this link

https://tutorial.djangogirls.org/en/css/

Wherever you see ‘blog’ just replace that with ‘zapp’

Let me know if you need help, I’d focus on the login and dashboard pages for now. I’m going to add object methods to the model that approves/denies timesheets etc.
