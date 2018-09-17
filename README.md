# Welcome to hf_cc (hidden founders coding challeng)

This application was created in response to the hidden founders web challenge.
The application is divided to two parts, a back-end made with python using flask micro-framework, and a front-end made with Angular 5.

## Setup the Backend
Navigate to `codding_challenge_be` directory and run the  following command to install all the dependencies for the backend application

> python setup.py

Then run the next command to create and fill the database

> python codding_challenge.py migrate

Finally, the following command runs the backend server

>python codding_challenge.py server


## Setup the Frondend
Navigate to the `codding_challenge_fe` directory and run the command below to start the front-end server

>ng serve

Then open  a browser to access the application on  `locahost:4200`

![Alt text](./img.png?raw=true "Title")

Two accounts were created when the database migration was lunched, these accounts are
`janatii:password` and `founders:hidden`.
