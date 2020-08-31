.. _metplus_configuration:
UNFINISHED!
METplus Configuration
=====================

.. raw:: html

  <iframe width="560" height="315" src="https://www.youtube.com/embed/KCISG0phmbw" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

Developed for **METplus Version 3.1**.

(*Setup: Go to https://github.com/dtcenter/METplus in a browser*)
(*Setup: Open Notepad and save an empty file called user.system.conf*)
(*Setup: Open images - title.png, setup_methods.png, met_ls.png*)
(*Setup: Pull up title.png*)

This video will cover how to configure the METplus wrappers in your environment. There are many METplus configuration
variables that can be used to customize your verification, but there are only a few that MUST be changed from the
default values. I am going to show you how to determine what values to plug into these variables so you can start
running use cases.

Override Methods
----------------

There are a few ways to override the required configuration variables.

1. Create a METplus configuration file that is specific to you and your environment
This is the recommended approach. You will pass this configuration file into every call to the METplus wrappers.

2. Modify the variables under parm/metplus_config directly
This method works if you are the only person running the METplus code. If you are using a shared installation,
changes made to these files will affect all users can cause confusion. Also, if you upgrade to a
new version of the METplus wrappers, you will have to reset all of the variables that you changed.

3. Pass in the variable overrides directly on the command line.
You can override a single METplus configuration variable on the command line using this syntax:

<section>.<variable_name>=<value>
dir.OUTPUT_BASE=/data/output

While this functionality can be useful, it would be tedious to type out each variable override for every call to the
METplus wrappers. In this video, I will use the recommended first method.


User Configuration File
-----------------------

(*Pull up Notepad with user.system.conf*)

I created a new file and named it user dot system dot conf.
Now I need to determine which variables I need to set in this file.
The default METplus configuration variables are found in the METplus code base in the parm/metplus_config directory.

(*Pull up GitHub page, click parm, click metplus_config*)

Any variable that is set to forward slash path forward slash t-o will need to be set.

Let's start with the metplus underscore system dot conf file.

MET_INSTALL_DIR
^^^^^^^^^^^^^^^

(*click metplus_system.conf, scroll down to MET_INSTALL_DIR*)

The MET_INSTALL_DIR variable should be set to the directory where MET is installed. In most cases, there will be a
directory inside this directory called 'bin' which contains all of the MET executables.

(*Show image of ls /usr/local/met/bin*)
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

The INPUT_BASE variable should be set to the directory that contains your input data.

(*show https://dtcenter.github.io/METplus/Users_Guide/installation.html#running-metplus-wrappers*)

You can refer to the
`Running METplus Wrappers <https://dtcenter.github.io/METplus/Users_Guide/installation.html#running-metplus-wrappers>`_
section in Chapter 2 of the METplus User's Guide for more information on what was covered in this video.

Thanks for watching!

Time Looping
------------

The METplus wrappers allow you to set a range of run times to process. For each run time, the wrappers will build commands to run the MET tools. The LOOP_BY variable determines if the run times should loop over initialization (INIT) times or valid (VALID) times. If LOOP_BY is set to INIT (or RETRO), then your configuration file must contain INIT_TIME_FMT, INIT_BEG, INIT_END, and INIT_INCREMENT. If LOOP_BY is set to VALID (or REALTIME), then your configuration file must contain VALID _TIME_FMT, VALID _BEG, VALID _END, and VALID _INCREMENT. Let’s focus on looping by valid time for now.

Looping by Valid Time
^^^^^^^^^^^^^^^^^^^^^

VALID_TIME_FMT defines the format of VALID_BEG and VALID_END. It uses Python’s strftime notation and accepts any strftime directives. A list of all possible directives can be found at strftime.org.

(*show https://strftime.org*)

The example configuration shown here will loop by valid time from February 1st, 2020 until February 3rd, 2020. The valid time format is set to contain year, month, and day, so the valid begin and end values match that format::

  LOOP_BY = VALID

  VALID_TIME_FMT = %Y%m%d

  VALID_BEG = 20200201
  VALID_END = 20200203

This next example contains the hour in the valid time format and the valid begin and end values. Execution will start at 12Z on February 1st, 2020 and will end at 18Z on February 1st, 2020::

  LOOP_BY = VALID

  VALID_TIME_FMT = %Y%m%d%H

  VALID_BEG = 2020020112
  VALID_END = 2020020318

The VALID_INCREMENT variable determines the interval between run times. The valid begin time will be processed, then the valid increment will be added to that time to determine the next run time. If the new run time is greater than the valid end time, then execution will stop. The value must be at least one minute::

  VALID_INCREMENT = 3600

The default units for valid increment are seconds if no unit identifier is present. Year, month, day, hour, minute, and second can be defined by adding the letter of the corresponding Python strftime directive to the end of the value. For example, a capital letter M corresponds to minute and a lowercase letter m corresponds to month::

  VALID_INCREMENT = 1M
