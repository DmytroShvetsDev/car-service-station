# Car service station

This site helps to manage the work of a car service center. With the help of this site, employees can create tasks and add cars. The site allows you to monitor the progress and deadline of tasks. 

The site has the following database structure:

![Database structure](static/img/Car-service-db-structure.png)

## Check it out!

[Car-Service-Station](Link)

## Installation

Python 3 must be already installed

```shell
git clone https://github.com/dirolius/car-service-station
cd car-service-station
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

## Features

Authorization for the worker
Detailed information about tasks, vehicles, and workers
Ability to track and change task progress and deadlines
Easy switching between vehicles and tasks for them

## Demo

You can log in to the site using the following user:

 - Login: Demo.user
 - Password: 5tgbvfr4