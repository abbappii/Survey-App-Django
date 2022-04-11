Django Survey app


Setup:

LinuxOS

active virtualenv
source env/bin/activate

install requirements:
pip install -r requirements.txt

run:
python manage.py runserver 

home page: /survey/home/

Ex: http://127.0.0.1:8000/survey/home/



windows 

create a virtualenvironment:
python -m venv env

install requirements:
pip install -r requirements.txt

run -> python manage.py runserver 

home page: /survey/home/

Ex: http://127.0.0.1:8000/survey/home/



User and login

users:
{
    user1 {
        name: impelit
        pass: impelit
    },
    user2 {
        name: test
        pass: test
    }
}

login example:

username: impelit
password: impelit
