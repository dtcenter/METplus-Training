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

  Requires commands: **docker**, **docker-compose**, **curl**, **tar**
*Preparation:*

* *Pull the metviewer image (docker pull dtcenter/metviewer)*
* *Download sample data tarfile (wget https://dtcenter.ucar.edu/dfiles/code/METplus/METviewer/sample_data-met_out_v9.1.tgz)*

(*Introduction*)

In this video, we will launch and run the METviewer database and display software using Docker containers.

Docker Software
---------------

We will begin by launching a terminal window in which we can execute commands. Do this by running **xterm** on a Linux machine,
launching a terminal emulator on Windows, or opening the **Terminal** application on a Mac, as I've done here. 

We assume that you are working on a machine on which the Docker software has already been installed.
METviewer uses container orchestration provided by Docker-Compose. Let's make sure that both **docker**
and **docker-compose** are available in your path.

.. code-block::

  which docker
  which docker-compose

If you do not have Docker or Docker-Compose installed on your machine, please exit this video and proceed to the Docker
website at http://www.docker.com.

Next, let's test that Docker is running properly on your machine by running the Docker **Hello World** command:

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
or any of the other METplus components, please see the Developmental Testbed Center website at dtcenter.org.

Running METviewer through Docker requires two software images: one for the METviewer software itself and a second
for the MySQL database component. A Docker-Compose YML file defines how they work together to run the METviewer
application. So let's start by downloading that Docker-Compose file from the METviewer GitHub repository:

.. code-block::

  curl -SL https://raw.githubusercontent.com/dtcenter/METviewer/main_v3.1/docker/docker-compose.yml > docker-compose.yml

Let's take a look at the **docker-compose.yml** file.

.. code-block::

  cat docker-compose.yml

Notice that it references some environment variables:

* **${METVIEWER_DOCKER_IMAGE}** is the name and version of METviewer that you'd like to run.
* **${METVIEWER_DATA}** is the directory on your machine where the MET output files that you'd like to analyze live.
* **${MYSQL_DIR}** is the directory on your machine where the MySQL database files should be written.
* **${METVIEWER_DIR}** is the directory on your machine where METviewer should write its output files.

Environment
-----------

For this tutorial, we'll get some MET output files by downloading a sample data tarfile from the DTC website.

.. code-block::

  curl -SL https://dtcenter.ucar.edu/dfiles/code/METplus/METviewer/sample_data-met_out_v9.1.tgz | tar -xzC .

This *curl* command creates a directory named **met_out** which contains the MET output files that are created
by running **make test** when compiling the MET software. Next, we'll setup directories for the METviewer
output and define the expected environment variables. Notice that I'm using *pwd* to reference your current
working directory and define full paths instead of relative ones.

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

Now that our environment is setup, we can launch METviwer with a single command from the directory that
contains the docker-compose.yml file:

.. code-block::

  docker-compose up -d

If this your first time launching METviewer, this Docker-Compose command will automatically download the MySQL
and METviewer images from DockerHub prior to bringing up the METviewer application. The time required to
download these images will vary based on your network speed. Or if you have launched METviewer previously,
as I have, Docker will use the images that already exist on your machine.

Let's check to see what containers are now running through Docker.

.. code-block::

  docker ps -a

You should see two containers up and running named **metviewer_1** and **mysql_mv**.

Next, copy and paste the following URL into a web browser to see the METviewer GUI:

**http://localhost:8080/metviewer/metviewer1.jsp**

METviewer is now up and running on your machine and the GUI is accessible via a web browser. But if you click
on the **Select Databases** button at the top of the GUI, you'll find that the list of databases is empty.

Load Data
---------

The next step is loading our sample MET output files into a METviewer database. METviewer requires that the
user create an XML file to define the location and type of data you'd like to load. This is a called a
*load spec* file. For convenience, we've included a load spec in the sample data tarfile. On your machine,
the sample data is in the **met_out** directory, but that directory is mounted inside the METviewer container
to a directory named **/data**. Since the METviewer load occurs *inside* the container, the load spec references
that **/data** directory.

.. code-block::

  cat met_out/load_met_out.xml

The **<folder_tmpl>*** tag is important to note. It defines the directories that contain MET output files that
should be loaded into METviewer. And notice that the **<database>** tag indicates that we want to load
data into a database named **mv_met_out**. But before we're able to do that, we'll need to run commands
to first *create* that database and then second apply the METviewer *schema* to it.

We run *docker exec* to execute commands inside of a container that's already up and running. We'll launch an
interactive *bash* shell inside the container to effectively log into it. The *-it* option provides an
interactive terminal session.

.. code-block::

  docker exec -it metviewer_1 /bin/bash

Once inside the container, run the following commands to create a new database named **mv_met_out** and apply
the METviewer schema to it. These two steps are required prior to loading data into any new database.

.. code-block::

  mysql -hmysql_mv -uroot -pmvuser -e"create database mv_met_out;"
  mysql -hmysql_mv -uroot -pmvuser mv_met_out < /METviewer/sql/mv_mysql.sql

The last step is running the **mv_load.sh** script to load the MET output into this database.
Let's first make sure that that shell script is executable.

.. code-block::

  chmod +x /METviewer/bin/mv_load.sh
  /METviewer/bin/mv_load.sh /data/load_met_out.xml

The load script requires a single argument which is the load XML file. The load may include some
*WARNING* messages but is complete with when you see the line that reads:

**----  MVLoad Done  ----**

Scrolling up, you'll see that it lists information about how much MET output was loaded and how
long it took to load. Next, type *exit* to log out of the container.
web browser.

.. code-block::

  exit

Then, go back to your web browser. Whenever adding a new database, you need to click the
**Reload Databases** button in the upper-right corner to tell the GUI to re-query the list of databases.
Also, clear the browser cache by holding down the shift key and clicking the refresh button. This works
on the Chrome browser, but the process for clearing your cache may differ on other browsers.

Checking the list of databases, we now see one named **mv_met_out** in a group named **METplus-Training**.
Note that this tutorial does not describe how to actually make plots with METviewer, just launching it
through Docker.

You can follow these steps to load your own MET output data into METviewer. Be sure to create a new load
spec XML file to describe the location of your data. You can either load all of your data into a single
database or organize you data into multiple databases.

.. note::

  If you want to overwrite the contents of an existing database, be sure to run a **mysql** drop command
  before recreating the database, similar to the following:
  **mysql -hmysql_mv -uroot -pmvuser -e"drop database mv_met_out;**

Relaunch METviewer
------------------

Next, let's take the METviewer application down. After making sure that we're in the directory that contains
the **docker-compose.yml** file, we'll run:

.. code::

  ls docker-compose.yml
  docker-compose down
  docker ps -a

The METviewer and MySQL containers are now gone. And checking the web browser, we see that the METviewer GUI
is no longer available. Now, from the terminal window, bring METviewer back up by running:

.. code::

  docker-compose up -d

And the GUI is now available again in the browser. Not only that, but the **mv_met_out** database still exists!
This is the reason why we write the MySQL output files to your local machine. Whenever you re-launch METviewer
it reads any existing database information from those files. So you can start and stop the METviewer container
whenver you'd like without losing any data.

Thank you for watching this video. I hope you find running METviewer through Docker to be a useful option.
