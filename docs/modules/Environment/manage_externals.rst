.. _environment_manage_externals:

Manage Externals
================

.. raw:: html

  <iframe width="560" height="315" src="https://www.youtube.com/embed/OSTRdIrEDZs" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

Developed for **METplus version 3.1**.

**Follow Along!** with these exercises.

This is the manage externals piece of the METplus tutorial.

We have a couple directories in the newest release of METplus that relate to building components. If you clone METplus, you will see them in the top level. The one I'm going to talk about right now is build components. We are calling all of the things that go along with METplus, such as METviewer, METcalcpy, and METplotpy, components. Manage externals is a tool to help you download and build all of these components along with METplus.

If you don't have access to one of the HPC computers where everything is installed for you, and you need to either install this yourself on a common machine or you want to install it on your own machine, this is a way to do it. Manage externals is a set of scripts that the CESM group at NCAR has created and that allows you, using this **externals.config** file, to specify other GitHub repositories that you want to automatically clone and put in a directory either on the same level as your METplus or somewhere else of your choosing.

Right now we have it set up to clone the latest build of MET and clone the latest build of METviewer, which will then put it in a directory one level up from METplus, which I will show you later after I go through this example of how it'll grab those two repositories. They'll be some future components that we're going to add as well.

To start with, we are going to clone the METplus repository from GitHub:

.. code-block::

  git clone https://github.com/dtcenter/METplus

Change directories into build_components and show the external.config file:

.. code-block::

  cd METplus/build_components
  cat Externals.cfg

The first file we want to look at is Externals.cfg.
If you create your own Externals.cfg file, you can clone other things as well. If you have your scripts in another GitHub repository, or other code repositories like SVN, you can modify the config file to point wherever you need,  it should be fairly easy to understand.

Lets go on to the build_MET.sh script:

.. code-block::

  less build_MET.sh

We have created this build MET script file. This script runs manage_externals to clone the repositories set up in your Externals.cfg file and then does some preparation to build MET. First it grabs a tar file from the dtcenter.org web site that contain the external libraries that MET needs to run, then it grabs a MET compile script that Julie Prestopnik has created that will build the external libraries and then build MET.

(*Show the section with the MET build script.*)
 
We have this tested for a couple different machines, but the list is not comprehensive and many machines can be a little tricky to build on. The key things to modify if you're going to try and do this is this env_vars.bash and changing your test base, changing your CC Flags, changing your LD flags are all important for installing on your own system.
 
This capability is in its early development stage and has not been widely tested, it will probably get you 90% of the way towards compiling MET. All the external libraries should be built and a lot of the beginning stages of MET will get built. It probably won't get you the whole way but there shouldn't be too many additional things you have to change to get there. If you have a local machine you want to install on or a share machine that doesn't have MET already installed in a common area, this is where you want to start for building your own MET and METplus and eventually the other METplus components once METplus v4.0 is released next spring.

This is the actual GitHub repository that I'm showing.

Here is the section of the `METplus Users Guide <https://dtcenter.github.io/METplus/Users_Guide/installation.html#build-components-and-using-manage-externals>`_ which describes using manage externals and building your own METplus.

