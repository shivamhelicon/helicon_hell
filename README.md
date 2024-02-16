# Helicon Hell Project 2

## Part One: Admin interface

You have been tasked with creating a simple API to handle and analyze sensor data from various locations. The client is well-informed and has requested that we start with an MVP so that they can commence testing and receive feedback from other departments early. You’ve identified Django as the best tool for the job as the platform aligns nicely with the requirements.



## Installation

1. Clone the repository:

https://github.com/shivamhelicon/helicon_hell.git

2. Docker compose to build and run

   docker-compose up --build

   docker-compose up

3. Migrations

    docker-compose run sensor-web python manage.py makemigrations

    docker-compose run sensor-web python manage.py migrate


4. Create superuser

    docker-compose run sensor-web python manage.py createsuperuser
   
   
