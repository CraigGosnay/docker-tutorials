- [Module 1](#module-1)
  - [Basics](#basics)
    - [Images](#images)
      - [Layers](#layers)
    - [Containers](#containers)
      - [Running / Starting](#running--starting)
      - [Attached / Detached / Interactive / Logs](#attached--detached--interactive--logs)
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

### Images

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

Images are read-only! They are a snapshot of our source & deps at the time we create the image - so any subsequent edits will require creating a new image. (This is one of the major points of containerization).

#### Layers

Images are layer based. Docker inteprets each instruction in the file as a layer, and will cache these, so rebuiling an image with only a small change will update only that & subsequent layers. 

The container can be understood as another layer on top of the image, which provides i/o functionality etc.

With this in mind, the ordering of DOCKERFILE instructions can make significant difference in the time it takes to build an image after changes, e.g if we don't change package.json, we do not need to rerun npm install despite changing our code so we can place that run command prior to the code copy, and save rebuilding each time and pul from the cache.

### Containers

An instantiation of an image that actually 'runs'.

#### Running / Starting

`docker run` will run a command / an image in a new container, attached by default.

`docker start` will restart an existing contianer, detached by default.

#### Attached / Detached / Interactive / Logs

Running attached will mean the terminal will have the process in the foreground and any sys.out, console logs etc will be displayed.

This can be configured with the flag `-d` with `run`, or the opposite `-a` with `start`.

If already running, we can use `docker attach [container]`

To interact with a terminal stdin we can run with `-i`

`docker logs` will pull the logs from a continer, and with `-f` it will attach to listen to logs ongoing.

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
docker ps -a    # list all containers 
docker ps       # list running containers
docker images   # list images
docker build .  # build based on dockerfile in curr dir
docker run      # run a command in a new container
docker start    # restart a stopped container 
```