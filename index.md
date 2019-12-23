# Python-flask App

For setting virtualenv find the location of project folder in command prompt, powershell:

Then install Python in the folder and create Virtual enviroment:

On Windows:
 
 > python -m venv venv

Before you work on your project, activate the corresponding environment:

On linux:

> $venv/bin/activate


On Windows Command prompt:

> venv\Scripts\activate.bat

On Windows powershell:
> venv\Scripts\Activate.ps1

Once enviroment is activated, install from requirements.txt

> pip install -r requirements.txt

** Open project folder in vsCode and run the app.py:

on Windows powershell:

>$env:FLASK_APP="app.py"

>$env:FLASK_DEBUG =1

>flask run

On command prompt:

>set FLASK_APP=app.py

>flask run

On Linux:

>export FLASK_APP=app.py

>export FLASK_DEBUG=1

>flask run



