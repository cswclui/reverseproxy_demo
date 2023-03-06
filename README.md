# README
Launch a terminal in VSCode.

First, build the Docker image for the Flask application:

`docker build . -t myflaskapp`

Run the following command to start the Docker containers defined in the docker-compose.yaml file:

`docker-compose up` # run docker compose in foreground

Wait for all the containers to start.

- Once the containers are all running, you can access the application in your web browser at http://localhost:10080. In the PolyU Virtual lab platform, you can use the show port function and input 10080.
- You can append /about to access the `/about` endpoint.

You may press Ctrl+C to stop the docker-compose stack.

 
