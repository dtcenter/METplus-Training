Session 1: Grid-to-Grid
=======================

**METplus Practical Session 1**


During the first METplus practical session, you will run the tools indicated below:

.. image:: ../figure/5.0_Practical_Session_1.avif

During this practical session, please work on the **Session 1** exercises. 
Proceed through the tutorial exercises by following the navigation links at the bottom of each page.

Tutorial Format
^^^^^^^^^^^^^^^

Throughout this tutorial, code blocks in have green text with a white background 
should be copied from your browser and pasted on the command line, e.g.:

.. code-block:: ini

  echo "Let's Get Started"

.. important::

  Text in **GREEN boxes** contains important information, expert hints or 
  helpful links. Please read carefully.

.. attention::

  Text in **ORANGE boxes** are instructions for the user to perform some action 
  or edit (add or modify) a specific file on your system.

.. note::

  Text in **BLUE boxes** are notes or instructions to be aware of while
  moving through the documentation.

.. admonition:: Sample Output
	   
  Text in **PURPLE boxes** are sample output from a command or contents of a file. 

.. admonition:: File Contents
	   
  Text in **PURPLE boxes** are sample output from a command or contents of a file.
 
  
Tutorial Tips
^^^^^^^^^^^^^

.. important::

  **Please read the instructions carefully!**
  In some cases there are two sets of instructions where only one 
  set of copyable instructions should be executed (i.e. bash vs. csh). 
  Ignoring the information and simply copy/pasting the command line 
  instructions may result in unintended consequences.

.. note::  

  Instructions in this tutorial use **vi** to open and edit files. 
  If you prefer to use a different file editor, feel free to substitute 
  it whenever you see **vi**.

.. note::
   
  Instructions in this tutorial use **okular** to view pdf, ps, and png files. 
  If you prefer to use a different file viewer, feel free to substitute it 
  whenever you see **okular**.

.. note::
   
  If you are running the tutorial inside Docker, you will not have access 
  to the visualization tools described in this tutorial (such as okular, ncview, etc.) 
  inside the Docker container. To run these commands, you will have to mount the 
  output directory inside Docker to your local computer file system and run these tools from there.

.. important::

  If you discover any typos, error in the run commands, incorrect output listed, 
  or any other issues while completing the tutorial, you are encouraged to submit
  your findings to the METplus team in a 
  `GitHub Discussions <https://github.com/dtcenter/METplus/discussions>`_. 
  Be sure to provide what session and specific page you encountered the issue on.

MET Tool: PCP-Combine
---------------------

.. important::

  If you are returning to the tutorial, you must source the tutorial setup script 
  before running the following instructions. If you are unsure if you have done this step, 
  please navigate to the :ref:`verify_env_correct` page.

We now shift to a discussion of the MET PCP-Combine tool and will practice running 
it directly on the command line.

PCP-Combine Functionality
^^^^^^^^^^^^^^^^^^^^^^^^^

The PCP-Combine tool is used (if needed) to **add, subtract, sum** or **derive** 
accumulated field values, most commonly precipitation, from several gridded data 
files into a single NetCDF file containing the desired accumulation period. 
Its NetCDF output may be used as input to the MET statistics tools. PCP-Combine 
may be configured to combine any gridded data field you'd like. However, all gridded 
data files being combined must have already been placed on a common grid. The copygb 
utility is recommended for re-gridding GRIB files. In addition, the PCP-Combine 
tool will only sum model files with the same initialization time unless it is 
configured to ignore the initialization time.

PCP-Combine Usage
^^^^^^^^^^^^^^^^^

View the usage statement for PCP-Combine by simply typing the following:

.. code-block:: ini

  pcp_combine

.. list-table:: Usage: pcp_combine
  :widths: auto
  :header-rows: 0


  * - **[[-sum] sum_args] | [-add input_files] | [-subtract input_files] | [-derive stat_list input_files]
      (Note: "|" means "or")**
    - 
  * - **[-sum] sum_args**
    - **Data from multiple files containing the same accumulation interval should be summed up using the arguments provided.**
  * - **-add input_files**
    - **Data from one or more files should be added together where the accumulation interval is specified separately for each input file.**
  * - **-subtract input_files**
    - **Data from exactly two files should be subtracted.**
  * - **-derive stat_list input_files**
    - **The comma-separated list of statistics in "stat_list" (sum, min, max, range, mean, stdev, vld_count) should be derived using data from one or more files.**
  * - out_file
    - Output NetCDF file to be written.
  * - [-field string]
    - Overrides the default use of accumulated precipitation (optional).
  * - [-name list]
    - Overrides the default NetCDF variable name(s) to be written (optional).
  * - [-vld_thresh n]
    - Overrides the default required ratio of valid data (1) (optional).
  * - [-log file]
    - Outputs log messages to the specified file
  * - [-v level]
    - Level of logging
  * - [-compress level]
    - NetCDF file compression

Use the **-sum, -add, -subtract**, or **-derive** command line option to indicate 
the operation to be performed. Each operation has its own set of required arguments.

Rum Sum Command
^^^^^^^^^^^^^^^

Since PCP-Combine performs a simple operation and reformatting step, no configuration file is needed.

1. Start by making an output directory for PCP-Combine and changing directories:

.. code-block:: ini

  mkdir -p ${METPLUS_TUTORIAL_DIR}/output/met_output/pcp_combine
  cd ${METPLUS_TUTORIAL_DIR}/output/met_output/pcp_combine

2. Now let's run PCP-Combine twice using some sample data that's included with the MET tarball:

.. code-block:: ini

  pcp_combine \
  -sum 20050807_000000 3 20050807_120000 12 \
  sample_fcst_12L_2005080712V_12A.nc \
  -pcpdir ${METPLUS_DATA}/met_test/data/sample_fcst/2005080700

.. code-block:: ini

  pcp_combine \
  -sum 00000000_000000 1 20050807_120000 12 \
  sample_obs_12L_2005080712V_12A.nc \
  -pcpdir ${METPLUS_DATA}/met_test/data/sample_obs/ST2ml

.. note::

  The "**\\**" backslash symbols in the commands above are used for ease of reading. 
  They are line continuation markers enabling us to spread a long command 
  line across multiple lines. They should be followed immediately by "Enter". 
  You may copy and paste the command line OR type in the entire line with or 
  without the "\\".

Both commands run the **sum** command which searches the contents of the **-pcpdir** 
directory for the data required to create the requested accmululation interval.

In the first command, PCP-Combine summed up 4 3-hourly accumulation forecast files 
into a single 12-hour accumulation forecast. In the second command, PCP-Combine 
summed up 12 1-hourly accumulation observation files into a single 12-hour 
accumulation observation. PCP-Combine performs these tasks very quickly.

We'll use these PCP-Combine output files as input for Grid-Stat. 
So make sure that these commands have run successfully!

Output
^^^^^^

When PCP-Combine is finished, you may view the output NetCDF files it wrote using the 
**ncdump** and **ncview** utilities. 
Run the following commands to view contents of the NetCDF files:

.. code-block:: ini

  ncview sample_fcst_12L_2005080712V_12A.nc &
  ncview sample_obs_12L_2005080712V_12A.nc &
  ncdump -h sample_fcst_12L_2005080712V_12A.nc
  ncdump -h sample_obs_12L_2005080712V_12A.nc

The ncview windows display plots of the precipitation data in these files. 
The output of ncdump indicates that the gridded fields are named **APCP_12**,
the GRIB code abbreviation for accumulated precipitation. 
The accumulation interval is 12 hours for both the forecast 
(3-hourly * 4 files = 12 hours) and the observation (1-hourly * 12 files = 12 hours).

Note, if ncview is not found when you run it on your system, you may need to load it first.  
For example, on hera, you can use this command:

.. code-block:: ini

  module load ncview

Plot-Data-Plane Tool
^^^^^^^^^^^^^^^^^^^^

The Plot-Data-Plane tool can be run to visualize any gridded data that 
the MET tools can read. It is a very helpful utility for making sure that MET can 
read data from your file, orient it correctly, and plot it at the correct spot on 
the earth. When using new gridded data in MET, it's a great idea to run it 
through Plot-Data-Plane first:

.. code-block:: ini

  plot_data_plane \
  sample_fcst_12L_2005080712V_12A.nc \
  sample_fcst_12L_2005080712V_12A.ps \
  'name="APCP_12"; level="(*,*)";'

.. code-block:: ini

  gv sample_fcst_12L_2005080712V_12A.ps &

.. note::

  Ghostview (gv) can take a little while before it displays.  
  If you don't have gv on your computer, try using display, 
  or any tool that can visualize PostScript files, e.g.:

  .. code-block:: ini

    display sample_fcst_12L_2005080712V_12A.ps &

.. note::

  Another option is to create a PNG file from the PS file, 
  also rotating it to appear the right way:

  .. code-block:: ini

    convert -rotate 90 sample_fcst_12L_2005080712V_12A.ps \
    sample_fcst_12L_2005080712V_12A.png
    display sample_fcst_12L_2005080712V_12A.png

Next try re-running the command list above, but add the **convert(x)=x/25.4;**
function to the config string (*Hint: after the level setting and ; but before 
the last closing tick*) to change units from millimeters to inches. 
What happened to the values in the colorbar?

Now, try re-running again, but add the **censor_thresh=lt1.0; censor_val=0.0;**
options to the config string to reset any data values less 1.0 to a 
value of 0.0. How has your plot changed?

.. note::

  The **convert(x)** and **censor_thresh/censor_val** options can be used in config 
  strings and MET config files to transform your data in simple ways.

Add and Subtract Commands
^^^^^^^^^^^^^^^^^^^^^^^^^

We have run examples of the PCP-Combine **-sum** command, but the tool also 
supports the **-add, -subtract,** and **-derive** commands. While the **-sum** 
command defines a directory to be searched, for **-add, -subtract,** and 
**-derive** we tell PCP-Combine exactly which files to read and what data 
to process. The following command adds together 3-hourly precipitation from 
4 forecast files, just like we did in the previous step with the **-sum** command:

.. code-block:: ini

  pcp_combine -add \
  ${METPLUS_DATA}/met_test/data/sample_fcst/2005080700/wrfprs_ruc13_03.tm00_G212 03 \
  ${METPLUS_DATA}/met_test/data/sample_fcst/2005080700/wrfprs_ruc13_06.tm00_G212 03 \
  ${METPLUS_DATA}/met_test/data/sample_fcst/2005080700/wrfprs_ruc13_09.tm00_G212 03 \
  ${METPLUS_DATA}/met_test/data/sample_fcst/2005080700/wrfprs_ruc13_12.tm00_G212 03 \
  add_APCP_12.nc

By default, PCP-Combine looks for accumulated precipitation, and the **03** 
tells it to look for 3-hourly accumulations. However, that **03** string can be replaced 
with a configuration string describing the data to be processed, which doesn't have to 
be accumulated precipation. The configuration string should be enclosed in single quotes. 
Below, we add together the U and V components of 10-meter wind from the same input file. 
You would not typically want to do this, but this demonstrates the functionality. 
We also use the **-name** command line option to define a descriptive output NetCDF 
variable name:

.. code-block:: ini

  pcp_combine -add \
  ${METPLUS_DATA}/met_test/data/sample_fcst/2005080700/wrfprs_ruc13_03.tm00_G212 'name="UGRD"; level="Z10";' \
  ${METPLUS_DATA}/met_test/data/sample_fcst/2005080700/wrfprs_ruc13_03.tm00_G212 'name="VGRD"; level="Z10";' \
  add_WINDS.nc \
  -name UGRD_PLUS_VGRD

While the **-add** command can be run on one or more input files, the 
**-subtract** command requires *exactly two*. Let's rerun the wind example from 
above but do a subtraction instead:

.. code-block:: ini

  pcp_combine -subtract \
  ${METPLUS_DATA}/met_test/data/sample_fcst/2005080700/wrfprs_ruc13_03.tm00_G212 'name="UGRD"; level="Z10";' \
  ${METPLUS_DATA}/met_test/data/sample_fcst/2005080700/wrfprs_ruc13_03.tm00_G212 'name="VGRD"; level="Z10";' \
  subtract_WINDS.nc \
  -name UGRD_MINUS_VGRD

Now run Plot-Data-Plane to visualize this output. Use the **-plot_range** option 
to specify a the desired plotting range, the **-title** option to add a title, and the 
**-color_table** option to switch from the default color table to one that's good for positive 
and negative values:

.. code-block:: ini

  plot_data_plane \
  subtract_WINDS.nc \
  subtract_WINDS.ps \
  'name="UGRD_MINUS_VGRD"; level="(*,*)";' \
  -plot_range -15 15 \
  -title "10-meter UGRD minus VGRD" \
  -color_table ${MET_BUILD_BASE}/share/met/colortables/NCL_colortables/posneg_2.ctable

Now view the results:

.. code-block:: ini

  gv subtract_WINDS.ps &

Derive Command
^^^^^^^^^^^^^^

While the PCP-Combine **-add** and **-subtract** commands compute exactly one 
output field of data, the **-derive** command can compute multiple output fields 
in a single run. This command reads data from one or more input files and derives 
the output fields requested on the command line (sum, min, max, range, mean, stdev, vld_count).

Run the following command to derive several summary metrics for both the 10-meter U and V wind components:

.. code-block:: ini

  pcp_combine -derive min,max,mean,stdev \
  ${METPLUS_DATA}/met_test/data/sample_fcst/2005080700/wrfprs_ruc13_*.tm00_G212 \
  -field 'name="UGRD"; level="Z10";' \
  -field 'name="VGRD"; level="Z10";' \
  derive_min_max_mean_stdev_WINDS.nc

In the above example, we used a wildcard to list multiple input file names.  And we used 
the **-field** command line option twice to specify two input fields.  For each input field, 
PCP-Combine loops over the input files, derives the requested metrics, and writes them to 
the output NetCDF file.  Run ncview to visualize this output:

.. code-block:: ini

  ncview derive_min_max_mean_stdev_WINDS.nc &

This output file contains 8 variables: 2 input fields * 4 metrics. 
Note the output variable names the tool chose.  
You can still override those names using the **-name** command line argument, 
but you would have to specify a comma-separated list of 8 names, one for each output variable.
