# COVID Relevant Articles Finder

## Project Overview

This project is an answer to the call to action from the COVID-19 Open Research Dataset Challenge (CORD-19) to leverage our expertise to help the medical community in the fight against coronarivuses.

We created a smart search engine that suggests relevant academic articles related to coronavirus based on user's request (semantic-like search engine).
This could help to generate insights and corelations among over 400k articles about COVID-19, SARS-CoV-2, and related coronaviruses.

High-level steps of the projects:
- data cleaning: refine the articles' abstracts to make them usable
- modelling: vectorize the abstracts and define an Unsupervised learning algorithm
- productionizing: build a Flask API and graphical user interface (web-app)





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
