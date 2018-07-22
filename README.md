# Caller ID Service

This is a caller ID service implemented as a part of the interview process at Truly for Andrew Taeoalii. It allows users to add phone numbers to the service and retrieve existing records in the service by number.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

This project is intended to be run inside a docker container, so docker must be installed prior to running. Access to [DockerHub](https://www.hub.docker.com) is also needed in order to download the official `python` container.

```
brew install docker
```

### Installing

Once docker is installed, you can build the docker image from the root directory of the project by running `docker build -t <app-name> .`. An example shown below:

```
docker build -t caller-id .
```

This may take a while to download the python image depending on connection speed. After the first time downloading, subsequent downloads will be much faster. Once built, you can run the application with any port specified by executing the command `docker run -d -p <port>:5000 --name <container-name> <app-name>`. Example below for running on port 8080 with a container name of `bruce`.

```
docker run -d -p 8080:5000 --name bruce caller-id
```

At this point, you may navigate in your browser to `http://localhost:8080` and view the swagger documentation for the application. The API endpoints specified in the project description are found in the `number` namespace and can be tested at `http://localhost:8080/api/query` and `http://localhost:8080/api/number`  respectively.

### Testing

No tests were created for this sample project, but the code was written in a modularized fashion using dependency injection to allow for easy unit testing.

## Built With

* [Docker](https://www.docker.com) - Container technology
* [Python](https://www.python.org) - Language used
* [Pip](https://pypi.org/project/pip/) - Used to install python dependencies
* [Flask](http://flask.pocoo.org/) - Microframework for building web applications
* [Flask-RESTPlus](http://flask-restplus.readthedocs.io/en/stable/) - Extension for Flask that adds support for quickly building REST APIs

## Authors

* **Andrew Taeoalii** - *Initial work* - [ulu5](https://github.com/ulu5)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Thanks Truly for an interesting challenge!