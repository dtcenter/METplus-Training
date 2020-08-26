.. _environment_docker:

Docker Container
================

.. raw:: html

  <iframe width="560" height="315" src="https://www.youtube.com/embed/KCISG0phmbw" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

Developed for **METplus Version 3.1**.

(*Introduction*)

In this video, we will setup the METplus training environment using a Docker Container.

We assume that you are working on a machine on which the Docker software has already been installed.
If you do not have Docker installed on your machine, please exit this video and proceed to the Docker
website at https://www.docker.com.

Installing Docker requires privileged user access to your machine. If you do not have that level of access,
please consider one of the other options for setting up a METplus training environment.

We will begin by launching a terminal window in which we can execute commands. Do this by running **xterm** on a Linux machine,
opening the **Terminal** app on a Mac, or launching a terminal emulator on Windows. Windows users are advised to
download and install a Linux xterm emulator such as `MobaXterm <https://mobaxterm.mobatek.net>`_
or `Cygwin <http://cygwin.com>`_ for use with containers.

After you have launched a terminal window, let's test that Docker is running properly on your machine.
Copy the command listed below and paste it into your terminal window. Hit enter to execute the command:

.. code-block::

  docker run --rm hello-world

All commands shown in code blocks like this may be copied and pasted in this way.

This **docker run** command first looks for an image named **hello-world** on your machine.
If found, it creates a software container from that image and executes the default command.
Or, more likely, if **hello-world** does not yet exist on your machine, Docker will automatically
download it from DockerHub at https://hub.docker.com prior to executing the default command.
We'll talk more about the **\-\-rm** option that we used later on.

If successful, you should see a **Hello from Docker!** message followed by some information and links.
If this command did not run succesfully, please exit this video and work on your Docker installation.

Launching
---------

Now that we've verified that Docker is running well, we only need to run one more command to
setup your METplus training environment:

.. code-block::

  docker run -it --rm --name metplus dtcenter/metplus-training /bin/bash

This automatically downloads the latest version of the **metplus-training** image from the
DTC organization on DockerHub, unless you have already done so.
This image is much larger than **hello-world** and will take much longer to retrieve.
Once the download is complete, it will execute the **/bin/bash** command inside the container,
effectively logging you into it. The **-it** options provide an interactive terminal session enabling
you to execute commands inside the container. Every **docker run** command creates a new software
container from the image being run, and those containers persist until they are removed. The
**\-\-rm** option automatically removes that container from your machine once you exit the container.
We recommend using the **\-\-rm** option to avoid stale containers consuming disk space.
However, if you'd like the container to persist after you exit, simply remove that **\-\-rm** option. 
The **\-\-name** option assigns a specific name to our container, rather than letting Docker choose
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
commands from inside this container.

Exiting
-------

Once you have finished running through some METplus training exercises from another module,
you will want to exit this container and cleanup. To exit the container, simply type:

.. code-block::

  exit

From outside the container, you can list both the **images** and **containers** on your machine
by running these commands.

.. code-block::

  docker images
  docker ps -a

At a minimum, we should see images for **hello-world** and **metplus-training**.
And **docker ps -a** should show us no containers since the **\-\-rm** option
automatically removed them once we exited. If you would like the container to
persist after exiting, omit the **\-\-rm** option.

Restarting
----------

To illustrate this, let's run the follow commands to relaunch a container without
the **\-\-rm** option, simply exit back out of it, and then list the containers on
your machine.

.. code-block::

  docker run -it --name metplus dtcenter/metplus-training /bin/bash
  exit
  docker ps -a

We should now see a container named **metplus** that exited a short time ago.
If you would like to log back into that container to do some more training exercises,
run the following commands to start it back up and launch the bash shell.

.. code-block::

  docker start metplus
  docker exec -it metplus /bin/bash

Cleaning up
-----------

Now let's say that you are all finished with the training exercises and want to
cleanup your machine. You can exit the **metplus** container and delete both the
containers and images from your machine by running these commands.

.. code-block::

  exit
  docker rm -f metplus
  docker rmi -f metplus-training hello-world 

The **metplus** container and images for **metplus-training** and **hello-world** should
no longer appear when you run the **docker ps -a** and **docker images** commands.

.. code-block::

  docker ps -a
  docker images

Thank you for watching this video. I hope you find running the METplus-Training exercises 
inside a Docker container to be useful.

