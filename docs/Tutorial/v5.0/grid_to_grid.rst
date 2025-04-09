Session 1: Grid-to-Grid
=======================

METplus Practical Session 1
---------------------------

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

Add and Subtract Commands
^^^^^^^^^^^^^^^^^^^^^^^^^

Derive Command
^^^^^^^^^^^^^^

