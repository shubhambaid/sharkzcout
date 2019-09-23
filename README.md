# Sharkzcout: Scapy based Network Traffic Analyzer
 #### A basic but less boring network traffic analyzer
 
 ## Setup
 
 Setup a PIPENV and run these commands under
 
 ```sh
 pipenv shell
 ```
 
 ```sh
pipenv install scapy[basic]
pipenv install flask
```
## Running

For running this app, make sure you're on admin mode 
then give 

```sh
export FLASK_APP=app.py
```
this specifies, how to load the application

Then Run 
```sh
export FLASK_ENV=development flask run
```
this makes the program run with DEBUG mode - ON.

### Since the software is in development stage, imperfection exists.
