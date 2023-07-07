# Car service station

This site helps to manage the work of a car service center. With the help of this site, employees can create tasks and add cars. The site allows you to monitor the progress and deadline of tasks. 

The site has the following database structure:

![Database structure](static/img/Car-service-db-structure.png)

## Check it out!

[Car-Service-Station](there will be a link here)

## Installation

Python 3 must be already installed!

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

 - Authorization for the worker
 - Detailed information about tasks, vehicles, and workers
 - Ability to track and change task progress and deadlines
 - Easy switching between vehicles and tasks for them

## Demo

Use the following command to load prepared data from fixture to get demo access to the system:

 `python manage.py loaddata car_service_db_data.json
`

After loading data from fixture you can use following superuser (or create another one by yourself):

 - Login: Demo.user
 - Password: 5tgbvfr4

After cloning, you need to create your `.env` file and register your variables in it. After that, everything will work. For an example, see the file `.env.sample`
