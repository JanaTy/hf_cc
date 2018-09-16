# Welcome to hf_cc (hidden founders coding challeng)

This application was created in response to the hidden founders web challenge.
the application is divided to two parts, back-end made with python using flask micro-framework, and a front-end made with Angular 5.

## Setup the Backend
navigate to `codding_challenge_be` directory and run the command

> python codding_challenge.py migrate

to create and fill the database, when done run the command

>python codding_challenge.py server

to lunch the back-end server, by default the server runs on port `5000`

## Setup the Frondend
navigate to the `codding_challenge_fe` directory and run the command

>ng serve

to lunch the front-end server
then open a a browser to access the application on  `locahost:4200`

![Alt text](./img.png?raw=true "Title")

i set up two accounts, that were created when the database migration was lunched, these accounts are
`janatii:password` and `founders:hidden`.