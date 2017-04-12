# webapp_testing
Docker Container for Testing of the Web Application

## Prerequisites ##
* Docker is installed
* Your device is connected to the internet

## Build and Run a Docker Container ##
1. Clone this repository to your local machine, and navigate to its folder
2. Run `docker build -t selwd:v1 .`, where `selwd` is the name of the image and `v1` is a tag associated with this name
3. After building, run `# docker run --rm selwd:v1` to run through a single container. It should output to console and terminate automatically when finished.

## Tools and Tutorials Used ##
* Selenium
* ** [**Dockerizing Selenium Tutorial**](<https://medium.com/@griggheo/running-headless-selenium-webdriver-tests-in-docker-containers-342fdbabf756/>)