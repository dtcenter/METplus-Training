.. _metviewer_docker:

METviewer Docker Container
==========================

.. raw:: html

  <iframe width="560" height="315" src="https://www.youtube.com/embed/y0RTzEobYs8" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

.. note::

  Developed for **METplus Version 3.1** with **METviewer 3.1**.

.. note::

  **Follow Along!** with these exercises by downloading the **_`met-9.1 output data <https://dtcenter.ucar.edu/dfiles/code/METplus/METviewer/sample_data-met_out_v9.1.tgz>`_** tarfile.

.. note::

  Requires **docker**, **docker-compose**, **curl**, and **tar** commands.

*Preparation:*

* *Pull the metviewer image (docker pull dtcenter/metviewer)*
* *Download sample data tarfile (wget https://dtcenter.ucar.edu/dfiles/code/METplus/METviewer/sample_data-met_out_v9.1.tgz)*

(*Introduction*)

In this video, we will launch and run the METviewer database and display software using Docker containers.

Docker Software
---------------

We assume that you are working on a machine on which the Docker software has already been installed.
METviewer uses container orchestration provided by Docker-Compose. Let's make sure that both docker
and docker-compose are available in your path.

.. code-block::

  which docker
  which docker-compose

If you do not have Docker or Docker-Compose installed on your machine, please exit this video and proceed to the Docker
website at http://www.docker.com.

We will begin by launching a terminal window in which we can execute commands. Do this by running **xterm** on a Linux machine,
opening the **Terminal** app on a Mac, or launching a terminal emulator on Windows.

After you have launched a terminal window, let's test that Docker is running properly on your machine.
So we will start by running the Docker Hello World command:

.. code-block::

  docker run --rm hello-world

If you are following along with the script of this video, all commands shown in code blocks may be copied
and pasted into you terminal window. If hello-world was successful, you should see a **Hello from Docker!**
message followed by some information and links. If this command did not run succesfully, please exit this video
and work on your Docker installation.

Docker-Compose File 
-------------------

The METviewer software aggregates and plots statistical output from the Model Evaluation Tools, or MET, software.
Both MET and METviewer are components of a large suite of tools, named METplus. To learn more about MET, METviewer,
or any of the other METplus software components, please see the Developmental Testbed Center website at dtcenter.org.

Running METviewer through Docker requires two software images: one for the METviewer software itself and a second
for the MySQL database component. A Docker-Compose YML file defines how they work together to run the METviewer
application. So let's start by downloading that Docker-Compose file from the METviewer GitHub repository:

.. code-block::

  curl -SL https://raw.githubusercontent.com/dtcenter/METviewer/main_v3.1/docker/docker-compose.yml > docker-compose.yml

Let's take a look at the docker-compose.yml file.

.. code-block::

  cat docker-compose.yml

Notice that it references some environment variables:
- ${METVIEWER_DOCKER_IMAGE} is the name and version of METviewer that you'd like to run.
- ${METVIEWER_DATA} is directory on your machine where MET output files live that you'd like to load.
- ${MYSQL_DIR} is the directory on your machine where the MySQL database files should be written.
- ${METVIEWER_DIR} is the directory where METviewer should write its output files.

Environment
-----------

For this tutorial, we'll download some sample MET output files by pulling a sample data tarfile and untarring it.

.. code-block::

  curl -SL https://dtcenter.ucar.edu/dfiles/code/METplus/METviewer/sample_data-met_out_v9.1.tgz | tar -xzC .

This curl command creates a directory named **met_out** which contains the MET output files that are created
by running **make test** when compiling the MET software. Next, we'll setup directories for the METviewer
output and define the expected environment variables. Notice that I'm using `pwd` to reference your current
working directory and define full paths instead of relative paths.

.. code-block::

  mkdir MySQL METviewer
  export METVIEWER_DATA=`pwd`/met_out
  export MYSQL_DIR=`pwd`/MySQL
  export METVIEWER_DIR=`pwd`/METviewer
  export METVIEWER_DOCKER_IMAGE=dtcenter/metviewer

With this setting, Docker will pull the latest version of the METviewer image from the DTCenter organization
on `DockerHub <https://hub.docker.com/repository/docker/dtcenter/metviewer/tags?page=1>`_.

Launch METviewer
----------------

Now that our environment is setup, we can launch METviwer with a single command:

.. code-block::

  docker-compose up -d

If this your first time launching METviewer, this Docker-Compose command will automatically download the MySQL
and METviewer images from DockerHub prior to bringing up the METviewer application. The time required to
download these images will vary based on your network speed. Or if you have already launched METviewer previously,
as I have, Docker will use the images that already exist on your machine. Next, copy the follow URL into a web
browser on your machine to see the METviewer GUI:

**http://localhost:8080/metviewer/metviewer1.jsp**

So now METviewer is up and running on your machine and the GUI is accessible via a web browser. If you click
on the **Select Databases** button at the top of the GUI, you'll find that the list is empty.

Load Data
---------

So the next step is loading our sample MET output files into a METviewer database. METviewer requires that the
user create an XML file to define the location and type of data you'd like to load. This is a called a
load spec file. For convenience, we've included a load spec file in the sample data tarfile. On your machine,
this is in the **met_out** directory, but that directory is mapped in the METviewer software container to a directory
named **/data**. Since the METviewer load occurs inside the container, the load spec references that **/data** directory.

.. code-block::

  cat met_out/load_met_out.xml

JHG, start working here.
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

Notice that my prompt changed once I ran that command which is a good reminder that I'm now inside the
container. Now let's run the **point_stat** tool which is one of the MET verification tools.
The **which** command shows us where **point_stat** is installed.

.. code-block::

  which point_stat
  point_stat
  
And running **point_stat** with no arguments prints its usage statement.

All of the MET tools, as well as the METplus python wrappers, are readily available inside this container.

.. code-block::

  which master_metplus.py
  master_metplus.py

Here is where METplus is installed and here is the usage statement for **master_metplus.py**.

This container makes it very easy to get up and running with the METplus components.
For now, let's simply exit this container to return to your local machine.

.. code-block::

  exit

Notice that the prompt changed again, which tells me that I've exited this container.

Sample Input Datasets
---------------------

As I mentioned earlier, many training exercises require sample input datasets. We have provided these datsets as
data containers in the `dtcenter/metplus-data <https://hub.docker.com/repository/docker/dtcenter/metplus-data/general>`_
repository on DockerHub. The input datasets are differentiated by their tag name. Each tag begins with the
METplus version number followed by a description of the data.

If you are logged into a DockerHub account you can view the metplus-data repository tags here: 
https://hub.docker.com/repository/docker/dtcenter/metplus-data/tags

Otherwise, you can view the tags from the DockerHub registry here: 
https://registry.hub.docker.com/v1/repositories/dtcenter/metplus-data/tags

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

  docker run -it --rm --name metplus --volumes-from met_tool_wrapper dtcenter/metplus-training /bin/bash

Once inside the container, list out the input data directory.

.. code-block::

  ls /data/input/METplus_Data/met_test

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

At a minimum, you should see images for **hello-world**, **metplus-training**, and the **met-tool-wrapper** data.
And **docker ps -a** should only show the **met-tool-wrapper** data container. All of the other containers created
by **docker run** were automatically removed once you exited them since we used the **\-\-rm** option.
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

You should now see a container named **metplus** that exited a short time ago.
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
  docker rmi -f hello-world dtcenter/metplus-data:3.1-met_tool_wrapper dtcenter/metplus-training

The **metplus** software container, the **met_tool_wrapper** data container and images
for **hello-world**, **metplus-data**, and **metplus-training** should
no longer appear when you run the **docker ps -a** and **docker images** commands.

.. code-block::

  docker ps -a
  docker images

Thank you for watching this video. I hope you find running the METplus-Training exercises 
inside a Docker container to be useful.

