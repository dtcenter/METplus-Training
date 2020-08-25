.. _environment_docker:

Docker Container
================

.. raw:: html

  <iframe width="560" height="315" src="https://www.youtube.com/embed/MlVI2YAa6Ok" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

Developed for **METplus Version 3.1**.

In this video, we will setup the METplus training environment using a Docker Container.

We assume that you are working on a machine on which the Docker software has already been installed.
If you do not have Docker installed on your machine, please exit this video and proceed to the Docker
website at https://www.docker.com.

Installing Docker requires privileged user access to your machine. If you do not have that level of access,
please consider one of the other options for setting up a METplus Training environment.

We will begin by launching a terminal window in which we can execute commands. Do this by opening the
**Terminal** app on a Mac or launching a terminal emulator on Windows, such as (TODO: state recommended terminal emulators here).

Let's test that Docker is running properly on your machine. Copy the command listed below and
paste it into your terminal window. Hit enter to execute the command:

.. code-block::

  docker run --rm hello-world

All commands shown in code blocks like this may be copied and pasted in this way.

This **docker run** command first looks for an image named **hello-world** on your machine.
If found, it creates a software container from that image and executes the default command.
Or, more likely, if **hello-world** does not yet exist on your machine, Docker will automatically
download it from DockerHub at https://hub.docker.com prior to executing the default command.
We'll talk more about the **--rm** option that we used later on.

If successful, you should see a **Hello from Docker!** message followed by some information and links.
If this command did not run succesfully, please exit this video and work on your Docker installation.

Now that we've verified that Docker is running well, we only need to run one more command to
setup your METplus Training Environment:

.. code-block::

  docker run -it --rm --name metplus dtcenter/metplus-training /bin/bash

This automatically downloads the latest version of the **metplus-training** image from the
DTC organization on DockerHub, unless you have already done so.
This image is much larger than **hello-world** and will take much longer to retrieve.
Once the download is complete, it will execute the **/bin/bash** command inside the container,
effectively logging you into it. The **-it** options provide an interactive terminal session enabling
you to execute commands inside the container. Every **docker run** command creates a new software
container from the image being run, and those containers persist until they are removed. The
**--rm** option automatically removes that container from your machine once you exit the container.
We recommend using the **--rm** option to avoid stale containers consuming disk space.
However, if you'd like the container to persist after you exit, simply remove that **--rm** option. 
The **--name** option assigns a specific name to our container, rather than letting Docker choose
one for us.

Now that we've successfully downloaded and logged into the METplus-Training container, let's
review a few important environment variables that will be used in the training modules.
Execute the following commands to see the values for METPLUS_TUTORIAL_DIR, METPLUS_BUILD_BASE,
MET_BUILD_BASE, and METPLUS_DATA.

.. code-block::

  echo ${METPLUS_TUTORIAL_DIR}
  echo ${METPLUS_BUILD_BASE}
  echo ${MET_BUILD_BASE}
  echo ${METPLUS_DATA} 

You are now ready to proceed to the training modules! Just execute all future training module
commands from inside this container. When you are all finished and ready to exit this container,
simply type:

.. code-block::

  exit

Beware that when you exit a container created using the **--rm** option, it will automatically be
deleted, along with any data you may have created inside of it. If you would like the container to
persist, omit the **--rm** option. After exiting the container, run the following commands to start
it back up and log back into it with the bash shell.

.. code-block::

  docker start metplus
  docker exec -it metplus /bin/bash


