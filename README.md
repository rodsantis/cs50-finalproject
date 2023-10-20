# Flask Productivity To do App

#### Video Demo:  https://youtu.be/8F2GsUtMKrI


#### Description:
In my final project I've created a Web App using Python, SQLite, HTML and CSS, with the help also of Flask and jinja syntax.

I wanted to created a productive app that could help anyone that needs to keep track of what needs to do.

This app could be used and could be helpfull by anyone that wants to add a Task that needs to be completed and could also remove or complete it on the go. It will only display the Tasks that needs to be yet completed so the removed and deleted tasks will be forever gone.

I thought about adding an edit button but I wanted for it to be responsive on the same page and as it was easy to remove and add a new task I yet didn't see the real need of editing it, so there will be no edit button.

I have started this project by creating the fundamentals files and folders that I would later use, for example: README.md, static/, templates/, todolist.db, helpers.py, app.py.

The static/ is where lives the .css and the templates/ is where the .html files lives.

I decided to create a solid base before that I could even start think of scailing the app, so I created the layout.html file, style.css file, app.py file, helpers.py file and from here I built up all the secondary pages, like: apology.html, feedback.html, index.html, login.html, register.html, thank.html, todo.html.

I have take inspiration on what I have learnt on cs50 while creating my layout.html so I could then reuse it with Jinja syntax on all of the other pages. The final P-Set (finance) helped me a lot to understand this web functionalities.

I started with all the basic HTMLs followed by the CSS and then have done the back end to glue it all together.

The app will work in a basic way but yet secure as it will ask you to be registered in order to use and will check if your username and password exists or are correct. It will ask users to login and make sure that all the information provided is correct.

The app will then have 2 functionalitis so far, the feedback form, so I as the develop can gather feedback from the users as in how to improve the app or if something is not working. And the app will have its main part that is the "TODO List".

In the "TODO List" the user will be able to use the bottom form in order to add a task and the task will stay there until it is either completed or removed. The app will know when it is completed only when the user interact by clicking in the respective buttons.

All of that is powered in the back end using Flask/Python, Jinja syntax, HTML and the SQLite data base in order to keep the task registered and then deleted accondingly to what was done in the front end by the user.

The Feedback Form was at first a simple input type of text and was inputing only what was written in it, but I though it was too simple and have created a proper form where the user can add their Name, Email address, age, how they heard about us.

Before submiting the project I thought that I could improve a bit more the feedback form. This way I decided to add one feedback form for when you are not logged in to the app so you can request our help, and the other feedback form is inside and you don't need to use your user ID as I will get it from your session, so making it more user friendly.

I'm submiting my project at this point.