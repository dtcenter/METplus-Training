.. _environment_docker:

Docker Container
================

.. raw:: html

  <iframe width="560" height="315" src="https://www.youtube.com/embed/KCISG0phmbw" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

.. note::

  Developed for **METplus Version 3.1**.

.. note::

  **Follow Along!** with these exercises using **met_tool_wrapper** data.

*Preparation:*

* *Pull the metplus-training image (docker pull dtcenter/metplus-training)*
* *Pull the metplus-data image (docker pull dtcenter/metplus-data:3.1-met_tool_wrapper)*

(*Introduction*)

In this video, we will setup the METplus training environment using Docker containers.

Docker Software
---------------

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

METplus Software 
----------------

Docker containers are provided for both the METplus software and sample input datasets.
Many training exercises require that a sample input dataset container be mounted when the
software container is run. We will start by running the METplus container without sample input data,
but we will cover that topic later on in this video.
 
Now that we've verified that Docker is running well, we only need to run one more command to
launch a METplus container:

.. code-block::

  docker run -it --rm --name metplus dtcenter/metplus-training /bin/bash

This automatically downloads the latest version of the **metplus-training** image from the
DTC organization on DockerHub, unless you have already done so, which I have.
This image is much larger than **hello-world** and will take much longer to retrieve.
Once the download is complete, it will execute the **/bin/bash** command inside the container,
effectively logging you into it. The **-it** options provide an interactive terminal session enabling
you to execute commands inside the container. Every **docker run** command creates a new software
*container* from the *image* being run, and those containers persist until they are removed. The
**\-\-rm** option that we used automatically removes that container from your machine once you exit out of it.
We recommend using the **\-\-rm** option to avoid stale containers consuming disk space.
However, if you'd like the container to persist after you exit, simply remove that **\-\-rm** option. 
The **\-\-name** option assigns a specific name to our container, rather than letting Docker choose
one for us.

For now, simply exit the container to return to your local machine.

.. code-block::

  exit

Sample Input Datasets
---------------------

As I mentioned earlier, many training exercises require sample input datasets. We have provided these datsets as
data containers in the `dtcenter/metplus-data <https://hub.docker.com/repository/docker/dtcenter/metplus-data/general>`_
repository on DockerHub. The input datasets are differentiated by their tag name. Each tag begins with the
METplus version number followed by a description of the data. Run the following command to see the tags
currently available in the metplus-data repository.

.. code-block::

  curl https://registry.hub.docker.com/v1/repositories/dtcenter/metplus-data/tags 

For example, the **3.1-met_tool_wrapper** tag contains data for the MET tool wrappers in METplus version 3.1.
Let's pull that image and use it to create a data container that we'll name **met_tool_wrapper**.
I have already pulled this image, so don't worry if your commands take much longer to run.

.. code-block::

  docker pull dtcenter/metplus-data:3.1-met_tool_wrapper
  docker create --name met_tool_wrapper dtcenter/metplus-data:3.1-met_tool_wrapper 

The **docker pull** command retrieves the image from DockerHub, while the **docker create** command instantiates
that image as a data container locally. Next, we'll relaunch a METplus software container, but this time
using the **\-\-volumes-from** option to mount the **met_tool_wrapper** sample data container.

.. code-block::

  docker run -it --rm --name metplus --volumes-from met_tool_wrapper dtcenter/metplus-training:develop /bin/bash

Once inside the container, list out the input data directory.

.. code-block::

  ls /data/input/METplus_Data

The **met_test** dirctory contains the sample input data that we mounted using the **\-\-volumes-from** option.
If you'd like to mount multiple input datasets, just use the **\-\-volumes-from** option multiple times to
specify each one.

Environment Variables
---------------------

While we are still inside the METplus container, let's review a few important environment variables that
are used during the `METplus Online Tutorial <http://dtcenter.org/community-code/metplus/online-tutorial>`_.
Execute the following commands to see the values for METPLUS_TUTORIAL_DIR, METPLUS_BUILD_BASE,
MET_BUILD_BASE, and METPLUS_DATA.

.. code-block::

  echo ${METPLUS_TUTORIAL_DIR}
  echo ${METPLUS_BUILD_BASE}
  echo ${MET_BUILD_BASE}
  echo ${METPLUS_DATA} 

These are used throughout the online tutorial to simplify the commands you'll run.

You are now ready to proceed to the training exercises! Just execute all future training exercise 
commands from inside this container. Each training exercise should indicate the required input data at the top.
For example, the **Follow Along!** note at the top of this page tells you that the **met_tool_wrapper** input
data is required.

.. note::

  **Follow Along!** with these exercises using **met_tool_wrapper** data.

Be sure to run **docker pull** and **docker create** to retrieve that input data and use the **\-\-volumes-from**
option to mount it into your **docker run** container.

Exiting a Container
-------------------

Once you have finished running through some METplus training exercises from another module,
you will want to exit this container and cleanup. To exit the container, simply type:

.. code-block::

  exit

From outside the container, you can list both the **images** and **containers** on your machine
by running these commands.

.. code-block::

  docker images
  docker ps -a

At a minimum, we should see images for **hello-world**, **metplus-training**, and the **met-tool-wrapper** data.
And **docker ps -a** should only show the **met-tool-wrapper** data container. All of the other containers created
by **docker run** were automatically removed once we exited them since we used the **\-\-rm** option.
If you would like the container to persist after exiting, omit the **\-\-rm** option.

Restarting a Container
----------------------

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
cleanup your machine. You can exit the **metplus** container and delete all of the
containers and images from your machine by running these commands.

.. code-block::

  exit
  docker rm -f metplus met_tool_wrapper
  docker rmi -f hello-world metplus-data:3.1-met_tool_wrapper metplus-training

The **metplus** software container, the **met_tool_wrapper** data container and images
for **hello-world**, **metplus-data**, and **metplus-training** should
no longer appear when you run the **docker ps -a** and **docker images** commands.

.. code-block::

  docker ps -a
  docker images

Thank you for watching this video. I hope you find running the METplus-Training exercises 
inside a Docker container to be useful.

