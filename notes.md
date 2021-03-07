- [Module 1](#module-1)
  - [Basics](#basics)
    - [Images Intro](#images-intro)
    - [Containers](#containers)
    - [Dockerfile](#dockerfile)
      - [FROM](#from)
      - [COPY](#copy)
      - [RUN](#run)
      - [WORKDIR](#workdir)
      - [EXPOSE](#expose)
      - [CMD](#cmd)
    - [Running from our own Image](#running-from-our-own-image)
      - [Build](#build)
      - [Run](#run-1)
- [Useful Commands](#useful-commands)

# Module 1

## Basics

### Images Intro

Template / blueprint for a container.

Contains definition of the code and required tools, libraries, runtimes etc.

Can find pre-defined images created by companies or open source etc. 

[Docker Hub](https://hub.docker.com)

For example, we could find the node image on dockerhub. We can use the docker cli even to do so:

```
docker run node
```
which will download the offical node image from dockerhub, and then create and run a container using it, which in this case will just run the node REPL. However this will just exit instantly because we haven't specified anything to be exposed from the container to the 'outside'.

If we run 

```
docker run -it node
```

then -i (-interactive) will force STDIN to be open and -t will attach a terminal for input.

Usually however we will use these premade images as a starting point to build up images for our own application.

### Containers

An instantiation of an image that actually 'runs'.

### Dockerfile

The commands inside the dockerfile are instructions for setting up the image, not for *running* the container. This is important. This is why we would run npp install in the image creation, but we wouldn't 'run node server.js', we'd use CMD instead which is used when container is started.

#### FROM

`FROM <image_name>`

The `image_name` can be a local or a dockerhub image. 

This specifies the base image we want to begin our image building from.

#### COPY

`COPY [flags] from ... to`

Which of our local files / directories do we want to copy across to our docker image.

#### RUN

`RUN cmd param` OR `RUN ["cmd", "arg1", "arg2"]`

This executes a shell command. The former literally in a shell as a string (so things like environment variables can be applied), and the latter directly. The latter is equivalent to exec command. Benefit is that you will receieve signals correctly to your process (e.g interrupts).

By default these commands are executed in root directory, unless set by `WORKDIR`.

#### WORKDIR

`WORKDIR path`

Sets the default location to execute `RUN` commands.

#### EXPOSE

`EXPOSE port`

Any ports exposed via the code (i.e `app.listen(80)`) will not be exposed outside of the docker container, only within it's own network. So to get access, we need to specify to docker which ports to expose to the outside world.

However this statement doesn't actually expose the port, just documents it.

#### CMD

`CMD ["executable", "arg1", "arg2"]`

Specifies commands to be run when a container, based on this image, is started.

If no CMD is specified, the CMD of the base image will be executed.

This should always be the last instruction.

### Running from our own Image

#### Build

We can run:

``docker build path``

where path is the location of the dockerfile, to build an image.

#### Run

``docker run -p 3000:80 image_hash``

The `-p` maps an external port exposure to an internal docker port. You can also use the image name instead of the image hash.

# Useful Commands

```
docker ps -a # list all containers 
```