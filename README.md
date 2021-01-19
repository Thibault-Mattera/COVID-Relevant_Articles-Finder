The data comes from the COVID-19 Open Research Dataset Challenge (CORD-19):
https://www.kaggle.com/allen-institute-for-ai/CORD-19-research-challenge

TO use the web app, Clone github repository and run the following Docker commands:

![](/images/covid-app-demo.gif)


## Build the images 
docker-compose build

## run the containers
docker-compose up

## access to webapp:
http://localhost:8080/

## Test flask api:
http://127.0.0.1:5000/task

## Stop containers
docker-compose stop
