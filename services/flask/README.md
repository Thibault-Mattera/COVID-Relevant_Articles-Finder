# build the container
docker build -t my_docker_flask:latest .

# run the container
docker run -p 5000:5000 my_docker_flask:latest

# test api on:
http://127.0.0.1:5000/task