.. _metplus_installation:

Installing METplus
==================

.. raw:: html

  <iframe width="560" height="315" src="https://www.youtube.com/embed/ap9-Fdlb7Fo" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

Developed for **METplus Version 3.1**.

**Follow Along!** with these exercises.

*Preparation:*

* *Have modules loaded if working on a machine where modules are used*
* *Terminal for sample data location*
* *Terminal for installation location*
* *Have user-specific configuration file ready*
* *METplus webpage pulled up*
* *METplus User's Guide pulled up*  
* *Have versions filled in below*
* *Have test command filled in below with proper locations*

(*Introduction*)

In this video, we will step through the process of installing the Model Evaluation Tools plus, or METplus, verification package.

(*Starting on https://dtcenter.org/community-code/metplus*)
This is the website for METplus. The information we need is on the "`Download <https://dtcenter.org/community-code/metplus/download>`_" page, so we will go to that page now by clicking on the "Download" link on the right side of this page.  Detailed information about the Software Installation can be found in `Chapter 2 <https://dtcenter.github.io/METplus/Users_Guide/installation.html>`_ of the METplus User's Guide.  Just as with the MET software, METplus also has a few dependencies.  So, let's take a look at the dependencies for METplus in the `Pre-requisites section <https://dtcenter.github.io/METplus/Users_Guide/installation.html#pre-requisites>`_ of Chapter 2 of the METplus User's Guide.

Python 3.6.3 or higher, the dateutil Python package, and the MET software, version 9.0 or above, are all required for running METplus Wrappers.  Some of the wrappers have additional dependencies to run. For example, the TCMPRPlotter wrapper requires R version 3.2.5, the SeriesByLead wrapper requires the NCO software package, the MakePlots wrapper requires the cartopy and pandas Python packages, and the CyclonePlotter wrapper requires the cartopy and matplotlib Python packages.

Now that we've gone over the dependencies, we can go back to the METplus Download page to get the link to the latest release. On the Download page, we can find the latest version of METplus under "Recommended".  We'll click on METplus-3.1 and that will take us to the `Releases <https://github.com/dtcenter/METplus/releases/tag/v3.1>`_ section of the METplus GitHub repository.  Now, we'll scroll down to the "Assets" section to get the source code.  We'll right click on "Source code (tar.gz)" and select "Copy Link Address". Going to the terminal window, I am currently in the location I chose to install METplus.  Please choose a location to install METplus, change directories to go into that installation directory, and then type "wget", space, and then paste in the link and hit enter.

Now we can unpack the file we downloaded by running the command:

.. code-block::

  tar zxf v3.1.tar.gz
  
  
And we users can remove the .tar.gz file to save some space:

.. code-block::

  rm v3.1.tar.gz
  
You'll also need to decide on a location to put some sample data so that you can run a test case to ensure everything is set up correctly.  If you're installing METplus for many users, you may want to download all of the sample data so that users can run a variety of cases.  We have a location picked out for this example, and we'll modify the configuration parameters to point to this sample data and to the installation of the MET tools.

Let's go into the parm/metplus_config subdirectory.  We'll modify two files here.  First, we'll open metplus_system.conf for editing.  We want to change the value of MET_INSTALL_DIR from "/path/to" to the location of the MET installation we want to use.  In this case, we'll use the MET version 9.1 installation and we'll list the full path to the top level installation directory.  Next, we'll open metplus_data.conf for editing.  We want to change the value of INPUT_BASE to point to the location of the sample data.  We'll use the full path to the sample data.

For this example, we will run a case using the data from the MET tool wrapper sample data set, so we'll grab the applicable data set.  In the Releases section of the METplus GitHub repository, also in the "Assets" section, we'll grab the "sample_data-met_tool_wrapper-3.1.tgz" file by right clicking on the the file and selecting "Copy Link Address".  Going back to the terminal window, we will go into the directory where we decided to put the sample data. We would type "wget", space, and then paste in the link that we copied and hit enter, but as you can see, I did this just before this video so that we wouldn't have to spend time waiting for the data to download.

Users can unpack the downloaded file by running the command:

.. code-block::

  tar zxf sample_data-met_tool_wrapper-3.1.tgz

And we users can remove the .tgz file to save some space:

.. code-block::

   rm sample_data-met_tool_wrapper-3.1.tgz

Now that we have installed METplus, have configured it for the location of the MET tools and for the sample data, and have gotten some sample data, we are ready to run a test case to ensure proper installation.

Going back to the METplus User's Guide, we'll go to `Chapter 5 <https://dtcenter.github.io/METplus/Users_Guide/usecases.html>`_ METplus Use Cases and will select "5.1 MET Tools", and then we'll select "5.1.8 Grid Stat".  We'll select "GridStat: Basic Use Case" and will scroll down to the "Running METplus" section.  This section notes that you can run this use case in two ways.  We'll run the first way by "Passing in GridStat.conf then a user-specific system configuration file". First, we need to create that user-specific system configuration file.  I did this ahead of time, but will go over its contents with you.  In this case, the file is called hera.jpresto.video.conf, where "hera" is the name of the machine I am using, "jpresto" is my username, "video" is because this file is specifically for this video, and ".conf" is because this is a configuration file.  

Looking in this file, we see "[dir]" which is a necessary section header to let METplus know what type of values we will be setting.  In this case, we are only modifying directories, so "[dir]" is the only section header we'll use.  We are going to modify the value of OUTBASE_BASE so that METplus knows where to write the output data. OUTPUT_BASE is set to "/path/to" in the metplus_system.conf file, but METplus won't run without a path specified, so we override that value here. You can override values set in other METplus configuration files by setting them in your user-specific system configuration file and passing your user-specific system configuration file last on the command line, as we are here.

Now we are ready to run our case.  We'll go back to the "Running METplus" section and will run the command listed there, fixing it up for our specific file location:

.. code-block::
   
  /contrib/METplus/METplus-3.1/ush/master_metplus.py -c /contrib/METplus/METplus-3.1/parm/use_cases/met_tool_wrapper/GridStat/GridStat.conf -c /scratch1/BMC/dtc/Julie.Prestopnik/METplus/hera.jpresto.video.conf

We can see "INFO: METplus has successfully finished running.", but we'll take a quick look at the screen output to ensure there were no errors.  

It looks like there was an issue, but not an error, in creating a font file, but that's ok because METplus generated a new fontManager.  If your run goes as well as this one, then congratulations on your successful installation of METplus.  If something goes wrong, please email met_help@ucar.edu with a description of the problem you experienced, and we will provide assistance.

Thank you for watching!

