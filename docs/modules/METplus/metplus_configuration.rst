.. _metplus_configuration:

METplus Configuration
=====================

.. raw:: html

  <iframe width="560" height="315" src="https://www.youtube.com/embed/Nv0cX6ze_cc" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

Developed for **METplus Version 3.1**.

(*Setup: Go to https://github.com/dtcenter/METplus in a browser*)
(*Setup: Open Notepad and save an empty file called user.system.conf*)
(*Setup: Open images - title.png, setup_methods_1.png, setup_methods_2.png, setup_methods_3.png, met_ls.png*)

(*Setup: Create user.system.conf file so it can be run from Docker*)
(*Setup: Open terminal and start docker by running docker run --rm -it dtcenter/metplus:3.1 /bin/bash*)
(*Setup: run PS1='${debian_chroot:+($debian_chroot)}\w\$ ' to remove username/host.*)
(*Setup: Change color scheme to white background and black text*)

(*Setup: Pull up title.png*)


This video will cover how to configure the METplus wrappers in your environment. There are many METplus configuration
variables that can be used to customize your evaluation, but there are only a few that MUST be changed from the
default values. I am going to show you how to determine what values to plug into these variables so you can start
running use cases.

(*Pull up terminal, run master_metplus.py*)

master_metplus.py is the script that is used to run the METplus wrappers. If you call the script with no arguments,
you will see a usage statement explaining how to configure the tool. Using the -c argument, you can specify
configuration files to run.

(*Type or paste: master_metplus.py -c ./METplus/parm/use_cases/met_tool_wrapper/Example/Example.conf*)

However, attempting to run a use case without configuring your environment will result in an error.


Override Methods
----------------

There are a few ways to override the required configuration variables.

(*Pull up setup_methods_1.png*)

1. Create a METplus configuration file that is specific to you and your environment
This is the recommended approach. You will pass this configuration file into every call to the METplus wrappers.

(*Pull up setup_methods_2.png*)

2. Modify the variables under parm/metplus_config directly
This method works if you are the only person running the METplus code. If you are using a shared installation,
changes made to these files will affect all users can cause confusion. Also, if you upgrade to a
new version of the METplus wrappers, you will have to reset all of the variables that you changed.

(*Pull up setup_methods_3.png*)

3. Set the variable directly on the command line.
You can override a single METplus configuration variable on the command line using this syntax:

<section>.<variable_name>=<value>
dir.OUTPUT_BASE=/data/output

While this functionality can be useful, it would be tedious to type out each variable override for every call to the
METplus wrappers.

(*Pull up setup_methods_1.png*)

In this video, I will use the recommended first method.


User Configuration File
-----------------------

(*Pull up Notepad with user.system.conf*)

I created a new file and named it user dot system dot conf.
Now I need to determine which variables I need to set in this file.


(*Pull up GitHub page, click parm, click metplus_config*)
The default METplus configuration variables are found in the METplus code base in the parm/metplus_config directory.

Any variable that is set to forward slash path forward slash t-o will need to be set.

Let's start with the metplus underscore system dot conf file.

MET_INSTALL_DIR
^^^^^^^^^^^^^^^

(*click metplus_system.conf, scroll down to MET_INSTALL_DIR*)

The MET_INSTALL_DIR variable should be set to the directory where MET is installed. In most cases, there will be a
directory inside called 'bin' which contains all of the MET executables.

(*Pull up met_ls.png*)

ls /usr/local/met/bin
ascii2nc       grid_diag      mode           plot_data_plane    rmw_analysis      tc_pairs
ensemble_stat  grid_stat      mode_analysis  plot_mode_field    series_analysis   tc_rmw
gen_vx_mask    gsid2mpr       modis_regrid   plot_point_obs     shift_data_plane  tc_stat
gis_dump_dbf   gsidens2orank  mtd            point2grid         stat_analysis     wavelet_stat
gis_dump_shp   lidar2nc       pb2nc          point_stat         tc_dland          wwmca_plot
gis_dump_shx   madis2nc       pcp_combine    regrid_data_plane  tc_gen            wwmca_regrid

In this case, we would set MET_INSTALL_DIR = /usr/local/met

This variable is found under the [dir] section in metplus underscore system dot conf, so it must go under the [dir] section
in my user configuration file.

(*In user.system.conf, type [dir] MET_INSTALL_DIR = /usr/local/met*)

OUTPUT_BASE
^^^^^^^^^^^

The OUTPUT_BASE variable should be set to a directory that will contain the files created by the METplus wrappers.
This can be any valid path as long as you have permission to write in parent directory. Be aware of disk size limits.
Setting OUTPUT_BASE to a directory on a disk with limited space introduces the risk of filling up the disk.
This variable is also under the [dir] section.

(*In user.system.conf, type OUTPUT_BASE = /data/output*)

INPUT_BASE
^^^^^^^^^^

The INPUT_BASE variable should be set to the directory that contains your input data. The sample data to run the use cases
can be obtained by downloading tarballs from the GitHub Releases page or through a Docker data volume. The INPUT_BASE
directory will contain two subdirectories, met_test and model_applications.

Now save your new configuration file and call master_metplus.py again, passing in your user configuration file.

Now you can see METplus has run without any errors.


(*show https://dtcenter.github.io/METplus/Users_Guide/installation.html#running-metplus-wrappers*)

You can refer to the
`Running METplus Wrappers <https://dtcenter.github.io/METplus/Users_Guide/installation.html#running-metplus-wrappers>`_
section in Chapter 2 of the METplus User's Guide for more information on what was covered in this video.

Thanks for watching!
