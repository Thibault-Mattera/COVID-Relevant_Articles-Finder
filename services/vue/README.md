# build the container
docker build -t vuejs-cookbook/dockerize-vuejs-app .

# run the container
docker run -it -p 8080:8080 --rm --name dockerize-vuejs-app-1 vuejs-cookbook/dockerize-vuejs-app

# access to application on:
http://localhost:8080/