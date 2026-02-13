# CS50 WEB PROGRAMMING FINAL PROJECT: VAULT

The project video is: https://youtu.be/9UKB8SYxhKE

## Main idea
I made a web application which will enable a class students in college to collaborate easily and share their thoughts and ideas with one another also share the study materials and chat in real time with django channels:

* Home page
* Login/Logout/Register
* Home page have all the routes to the things which you can do on this app
* A individual page for Chatting which is running on ASGI interface and is on real time
* You have the options to share notes, books and Assignments deadlines and details to the other users
* Most the things which we have learned are used here like javascript and animation etc.


## Distinctiveness and Complexity
The page is not similar to anything we have already created. It's not a social media app nor an e-commerce. It's not similar to other years projects either it's a combination of most the things we learned with Django channels and ASGI Interface. 

In terms of complexity, I used Django with more than one model (explained below) and Django channels and a little bit of Javascript. 
Moreover, all of the web application is responsive to the different screen sizes (mainly mobile phones and computers).

Some of the features which distinguishes this project from other ones are below:
* The Chat Interface of the application helps to communicate with other users in real time, This alone is a top notch feature which distinguishes it from other applications Some of its more helpful things are:
    * This will allow the users to real time share data and links
    * If a person is needing any help then he could directly contact to the whole group 
    * It would help the users being connected with the group
    * It would be very safe as it is developed within the Django framework

* Users can share links of required documents like books and decorate it with its cover pages 

* People would be able to check the assignment dates and due assignments of their own 

The important terms and tools which are used are given and explained below:

* ASGI: Think of ASGI as an upgrade to Django’s usual way of handling requests. It allows Django to manage real-time communication like chat messages.

* Consumers: These are like special functions that handle different types of connections, such as WebSockets (for real-time chat) or HTTP requests. They can work both synchronously and asynchronously.

* Channel Layers: Imagine a messaging system inside your app. Channel layers help different parts of your app talk to each other. Redis is often used to manage this messaging.

* WebSockets: This is a technology that lets your app send and receive messages instantly, perfect for chat-rooms.

* Daphne: This is a server that helps run your Django Channels app, handling different types of connections like HTTP and WebSockets.

* Redis: A tool often used to manage the messaging system (channel layers) in your app, ensuring smooth communication between different parts.

* Routing: This is like a map that directs different types of connections (like WebSockets) to the right place in your app.


## Files information

* In views.py there is all of the backend code. The main functions are:
    * We have our usual routes like the login/register and logout to enter in our app
    * Then I have included data and info which is passed on consumer.py file to include some of the user data which is saved on real time 
    * Index page simply is the routes page which will take us to the other facilities which are provided in the app
    * Room is the place where we will chat and the saved data will be taken from the Chat model (explained down)
    * Books is the place where you can find books as well as you will be redirected to the website of that particular book
    * Subjects are there for the notes and all of the stuff plus there will one feature of self notes which I will be updating which will use markdown like we did in the wiki project
    * Book Update is the thing where we can add the book links and all of that stuff
    * Assignment is the area where we can add our assignment which is given to us as well as we can see the assignments


* Models.py. The different models are:
    * A users model
    * A model for Chats to store all the chats data which is stored in real time
    * All the other models to store Person(right now of no use but will update later), Books and Assignments
    * Notes also have a separate model

* Consumers.py :
    * This thing will help in communicating the data in real time
    * For backing memory redis is used and to run that I have used docker and the command is written in help.txt
    * Daphne is also installed and is being used to run the ASGI server

* Script is used to communicate with real time data
* Javascript is also used for the block hiding and showing and some other stuffs like this

* A css file with all of the css used in the web application. Techniques like Animation and Responsiveness are used
* Other less important files like urls, admin, settings, static images...

## Things which will be updated
* A dedicated page which will record our own notes in the form of markdown and will display it on notes page
* More real time features like who is currently logged in and followers and etc.
* Better chat room facilities

## How to run the application
* Install project dependencies like django channels, django, docker, redis, daphne etc.
* Make and apply migrations by running python manage.py makemigrations and python manage.py migrate.