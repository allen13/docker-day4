docker day 4
------------

* docker networking
* docker storage
* docker compose
* run docker compose app
* wrapping up

docker networking
-----------------

One of the reasons Docker containers and services are so powerful is that you can connect them together, or connect them to non-Docker workloads. Docker containers and services do not even need to be aware that they are deployed on Docker, or whether their peers are also Docker workloads or not. Whether your Docker hosts run Linux, Windows, or a mix of the two, you can use Docker to manage them in a platform-agnostic way.

* [docker networking](https://docs.docker.com/network/)

Complete this docker networking lab:

* [network basics](https://github.com/docker/labs/blob/master/networking/A1-network-basics.md)

docker storage
--------------

By default all files created inside a container are stored on a writable container layer. This means that:

* The data doesn’t persist when that container no longer exists, and it can be difficult to get the data out of the container if another process needs it.

* A container’s writable layer is tightly coupled to the host machine where the container is running. You can’t easily move the data somewhere else.

* Writing into a container’s writable layer requires a storage driver to manage the filesystem. The storage driver provides a union filesystem, using the Linux kernel. This extra abstraction reduces performance as compared to using data volumes, which write directly to the host filesystem.

In order to get around these two limitations you can use [volumes](https://docs.docker.com/storage/volumes/) or [bind mounts](https://docs.docker.com/storage/bind-mounts/).


* [docker storage](https://docs.docker.com/storage/)

docker compose
--------------

Compose is a tool for defining and running multi-container Docker applications. With Compose, you use a YAML file to configure your application’s services. Then, with a single command, you create and start all the services from your configuration.

* [docker compose](https://docs.docker.com/compose/)

*docker compose networking*

By default Compose sets up a single network for your app. Each container for a service joins the default network and is both reachable by other containers on that network, and discoverable by them at a hostname identical to the container name.

* [docker compose networking](https://docs.docker.com/compose/networking/)

run docker compose app
----------------------

Now that you have an understanding of docker compose, checkout this repository and run the [docker-compose.yml](docker-compose.yml) file contained in this repo. It will also build the python [Dockerfile](Dockerfile)

    docker-compose up

* It will have some errors you need to fix before it can serve traffic
* Once it runs without errors navigate to localhost:5000 and refresh a few times
* Stop and restart docker compose. Reload the webpage.
* Why did the refresh count pick up where it left off previously?

wrapping up
-----------

Containers offer numerous benefits over older IT models such as virtual machines. Containers make it easy to integrate into DevOps. Containers also standardize the deployment and runtime model for applications and services in production (and test/staging). Containers are an enabling technology for microservice architecture and DevOps.

While there are definitely higher level abstractions that can replace containers like AWS Lambda (FAAS) these services come with many restrictions and are usually locked to a single cloud. Which leads to a very important point: Kubernetes and containers are a cloud abstraction layer.

Embracing this abstraction makes your stack a lot more portable and adds flexibility along with building a much needed future-ready architecture.

* [top 7 benefits of containers](https://blog.kumina.nl/2017/04/the-benefits-of-containers-and-container-technology/)




