# Assignment-5_CS612

#RESTful webservice using Docker

Created a RESTful Web service that displays data of students in JSON format using four get routes:

/students

/students/year

/Student/year/class

/Student/year/class/Subject

Steps to run RESTful web service:

A Docker Image is created by running the following command: - "docker build -t flaskapp . "

Run the created students-image image inside a container using the following command "docker run -d -p 50:5001 flaskapp"

Check running docker container by "docker ps"

App will now be running at the following address: - http://0.0.0.0:5000/Students
