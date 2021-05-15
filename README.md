** docker-compose Examples **

*** 
node-hits-application : Sample Nodejs application that has Python and Redis. this application when accessed increments the hits counter and show on the screen
We can manually build the application using
docker build -t docker.io/jagadesh1982/hits:latest .

The Seconnd Container to run is the redis which store the hit count. just download redis:alpine image and run the image with name redis. We have the First application connecting to the redis container on default bridge network

docker run -d -p 5000:5000 docker.io/jagadesh1982/hits:latest
docker run -d redis:alpine




***	
