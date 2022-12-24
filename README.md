# Flask Docker Template

This template python project was built to demo easy flask app which can be deployed to cloud via docker containers

## Features:


## Requirements:
- docker

## Get started:

#### Clone the repository:
```bash
git clone https://github.com/erfankashani/docker_flask_app.git
cd docker_flask_app
```

####  Option: Use docker-compose to build image and run the app
```bash
docker-compose up
```

####  Option: Use docker to build image and run the app
```bash
docker image build ./
docker container run --rm --name flask-app -d -p 8888:5000 <image_id>
```

####  check the resulting flask page on your host [0.0.0.0:8888](0.0.0.0:8888)

####  Check all docker containers (running or stopped):
```bash
docker ps -a
```

####  Check all docker images:
```bash
docker image list
```

####  Delete all docker containers (running or stopped):
```bash
docker kill $(docker ps -aq)
docker rm $(docker ps -aq)
```

####  Delete a given docker image:
```bash
docker rmi <image_id>
```

####  run test cases
```bash
pytest
```


## Issue Tracking:
If you feel like there are more parts to be added to this project please refer to [issue_tracker](https://github.com/erfankashani/docker_flask_app/issues). 