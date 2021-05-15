** docker-compose Examples **

*** 
node-hits-application : Sample Nodejs application that has Python and Redis. this application when accessed increments the hits counter and show on the screen
We can manually build the application using
docker build -t docker.io/jagadesh1982/hits:latest .

The Seconnd Container to run is the redis which store the hit count. just download redis:alpine image and run the image with name redis. We have the First application connecting to the redis container on default bridge network

docker run -d --name redis redis:alpine
docker run -d --name client --link redis:redis -p 5000:5000 node-hits-application_web 

***	



*** 

testing-service-application : The second application is the testing-service application. this testing-service application is 2 parts. one is the testing-service and other is the second-service. the second-service application pushes data into the testing-service application and we can consume the application using the link
http://localhost:9876/read

we need to create both container as
docker run -d -p 9876:9876 -v ${pwd):/demo ocker.io/jagadesh1982/testing-service
docker run -d -v ${pwd):/demo docker.io/jagadesh1982/second-service


***	

***	
Third application is a simple application. 
***	


***	
All Application have their respective docker-compose files available. We can run directly docker-compose build and docker-compose up
***	

