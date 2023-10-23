# eiland_collective_app

Interactive Map to work with the Eiland Data. 

This project is part of the [Eiland Collective](https://eilands.design/) research project into the history of flemish moated Eilands. 

It's a very simple prototype that runs a flask instance with a Postgresql database.
The app is mainly used for workshops to collect data that will then be used for Machine Learning Applications to automate the detection of moated homesteads. 

THe Leaflet frontend is connected to different API endpoints that allow to add, edit and delete data. You can also change basemaps. For each inputed Eiland, You can add basic metadata like the Eiland's name, and moat preservation status (complete, incomplete, disapeared). You can also add a description of the Eiland, and add a picture. 

SocketIO allos all the users to see the changes in real time, and are notified when other users add or edit data. THis way an Eiland is less likely to be added twice. 

The app is currently hosted on Heroku, and can be accessed [here](https://eiland-collective-app.herokuapp.com/).


![Welcome Page](doc_images/onboarding0.png)

![Onboarding](doc_images/onboarding1.png)

![Alt text](doc_images/onboarding2.png)

![Alt text](doc_images/onboarding3.png)

![Alt text](doc_images\journey.gif)

