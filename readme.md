New version

API Documentation

https://docs.google.com/document/d/1JGKP--ybNL6q0yLEqrxEkdSND5Jxl-HwVnZsXQ6rSac/edit?usp=sharing

MyResume
=============


A webapp for generating e-resume

# Installation

This project is running on Ubuntu, so this is
probably the easiest environment in which to get things running, but other
distributions of linux should be fine as well.

### Virtual environment (if your system doesn't have it already):

The development environment relies on using a Python [virtual environment][venv]
for tools and portability across platforms. Ensure that you have Python Pip
installed for your platform before proceeding with these instructions.

Windows users can use the [following guide][windows venv]. Specifically, get
Python installed and then use the get-pip.py installer once Python is working

OSX users can use the built in version of Python as long as Pip is available,
or better, install [Brew and Python][osx venv].

Linux users should have Python already installed. Ensure Pip is installed via
your package manager and you should be all set.


## Linux based Setup for MyResume development

Note: Ubuntu 14.04 LTS is recommended to use for the development environment.

1. Run the following git clone (specify a directory of your choosing if you like):

        git clone https://github.com/Small-Start/myresume.git

2. Run virtualenv on the git cloned directory to setup the Python virtual environment:

        virtualenv nse

3. cd into the name of the directory into which you cloned the git repository

        cd myresume

4. After activating the virtual environment, install the dependencies

        pip install -r requirements.txt

5. Migrate database so that django built essential database structure

        python manage.py migrate
        
6. You are all set. Run the final command

        python manage.py runserver

10. Its time to rock. Visit [http://localhost:8000][localhost] in your browser and you should be all set.


[localhost]: http://localhost:8000/

