# Chatbuddy ( A Django Chat APP )

This is a chat application built with help of with Django Channels. It also features a user login/registration system using the inbuilt django user model. 

# How to setup Locally:

#### Frontend Setup:

1.  Navigate to main directory (the one with manage.py file) , open up CMD and run the following command
```
python manage.py makemigrations
python manage.py migrate
```
2. Now that migrations are complete, simply run
```
python manage.py runserver
```
This will run a server locally. Now you can acces the app through a browser using URL in the terminal.

#### Backend Setup:

1.  Install Docker for desktop 

2.  Once Docker is up and running open up CMD and run the following command.
```
docker run -p 6379:6379 -d redis:5
```
This will pull a image of Redist:5 application and run it locally on port 6379.

### NOTE:
   Please note this is a demo project of the concepts used in building a chat app. It is simply not production ready. For example, when the backend receives a message, it'll broadcast to everyone in the room including the sender. This means when you demo the sender role, be aware you'll see every outbound message duplicated. The project is setup for deployment however work is being done to get this up and running.
 

  


