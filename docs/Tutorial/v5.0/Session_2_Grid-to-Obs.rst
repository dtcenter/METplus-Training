
Session 2: Grid-to-Obs
======================

**METplus Practical Session 2**

During this practical session, you will run the tools indicated below:

??? Julie, this isn't a link.  It's missing the main image???

You may navigate through this tutorial by following the links at the bottom of each page or by using the menu navigation.
Since you already set up your runtime environment in Session 1, you should be ready to go! To be sure, run through the following instructions to check that your environment is set correctly.

**Prerequisites: Verify Environment is Set Correctly**

Before running the tutorial instructions, you will need to ensure that you have a few environment variables set up correctly. If they are not set correctly, the tutorial instructions will not work properly.

.. note::

**1:** Navigate to your tutorial directory and run the tutorial setup script.

.. important::

&lt;strong&gt;In the following instructions, change "/path/to" to the directory you chose.&lt;p&gt;&lt;/p&gt;
&lt;/strong&gt;&lt;p&gt;**EDIT AFTER COPYING and BEFORE HITTING RETURN!**&lt;/p&gt;

.. code-block::

cd /path/to/METplus-5.0.0_Tutorial&lt;br/&gt;
source METplus-5.0.0_TutorialSetup.sh

.. note::

**2:** Check that you have environment variables set correctly. If any of these variables are not set, navigate back to the METplus Setup section of the tutorial.

.. code-block::

echo ${METPLUS_TUTORIAL_DIR}&lt;br/&gt;
echo ${METPLUS_BUILD_BASE}&lt;br/&gt;
echo ${MET_BUILD_BASE}&lt;br/&gt;
echo ${METPLUS_DATA}&lt;br/&gt;
ls ${METPLUS_TUTORIAL_DIR}&lt;br/&gt;
ls ${METPLUS_BUILD_BASE}&lt;br/&gt;
ls ${MET_BUILD_BASE}&lt;br/&gt;
ls ${METPLUS_DATA}

.. important::

**METPLUS_TUTORIAL_DIR** is the location of all of your tutorial work, including configuration files, output data, and any other notes you'd like to keep.&lt;br/&gt;
**METPLUS_BUILD_BASE** is the full path to the METplus installation (/path/to/METplus-X.Y)&lt;br/&gt;
**MET_BUILD_BASE** is the full path to the MET installation (/path/to/met-X.Y)&lt;br/&gt;
**METPLUS_DATA** is the location of the sample test data directory

.. note::

**3:** Check that the MET applications are in the path:

.. code-block::

which point_stat

.. important::

You should see the usage statement for Point-Stat. The version number listed should correspond to the version listed in **MET_BUILD_BASE**. If it does not, you will need to either reload the met module, or add **${MET_BUILD_BASE}/bin** to your PATH.

.. note::

**4:** Check that the correct version of **run_metplus.py** is in your **PATH**:

.. code-block::

which run_metplus.py

.. important::

If you don't see the full path to script from the shared installation, please set it. It should look the same as the output from this command:

.. code-block::

echo ${METPLUS_BUILD_BASE}/ush/run_metplus.py&lt;br/&gt;
ls ${METPLUS_BUILD_BASE}/ush/run_metplus.py

See the instructions in Session 1 for more information.
You are now ready to move on to the next section.
.. important::

If you discover any typos, error in the run commands, incorrect output listed, or any other issues while completing the tutorial, you are encouraged to submit your findings to the METplus team in a `GitHub Discussions <https://github.com/dtcenter/METplus/discussions>`_. Be sure to provide what session and specific page you encountered the issue on.

MET Tool: PB2NC
---------------

.. important::

??? Julie, I removed the bolding to get the link to work???
IMPORTANT NOTE: If you are returning to the tutorial, you must source the tutorial setup script before running the following instructions. If you are unsure if you have done this step, please navigate to the :ref:`Verify Environment is Set Correctly <verif_env_set_correct>` page.

**PB2NC FUNCTIONALITY**

The PB2NC tool is used to stratify (i.e. subset) the contents of an input PrepBufr point observation file and reformat it into NetCDF format for use by the Point-Stat or Ensemble-Stat tool. In this session, we will run PB2NC on a PrepBufr point observation file prior to running Point-Stat. Observations may be stratified by variable type, PrepBufr message type, station identifier, a masking region, elevation, report type, vertical level category, quality mark threshold, and level of PrepBufr processing. Stratification is controlled by a configuration file and discussed on the next page.
The PB2NC tool may be run on both PrepBufr and Bufr observation files. As of met-6.1, support for Bufr is limited to files containing embedded tables. Support for Bufr files using external tables will be added in a future release.

???Julie, I put in th line breaks.  Do you want to actual web info shown???

| For more information about the PrepBufr format, visit:
| https://emc.ncep.noaa.gov/emc/pages/infrastructure/bufrlib.php
|
| For information on where to download PrepBufr files, visit:
| https://dtcenter.org/community-code/model-evaluation-tools-met/input-data

**PB2NC USAGE**

.. note::

 View the usage statement for PB2NC by simply typing the following:

.. code-block::
  pb2nc

.. code-block::

prepbufr_file
input prepbufr path/filename

netcdf_file
output netcdf path/filename

config_file
configuration path/filename

[-pbfile prepbufr_file]
additional input files

[-valid_beg time]
Beginning of valid time window [YYYYMMDD_[HH[MMSS]]]

[-valid_end time]
End of valid time window [YYYYMMDD_[HH[MMSS]]]

[-nmsg n]
Number of PrepBufr messages to process

[-index]
List available observation variables by message type (no output file)

[-dump path]
Dump entire contents of PrepBufr file to directory

[-obs_var var]
Sets the variable list to be saved from input BUFR files

[-log file]
Outputs log messages to the specified file

[-v level]
Level of logging

[-compression level]
NetCDF file compression

At a minimum, the input prepbufr_file, the output netcdf_file, and the configuration config_file must be passed in on the command line. Also, you may use the -pbfile command line argument to run PB2NC using multiple input PrepBufr files, likely adjacent in time.
When running PB2NC on a new dataset, users are advised to run with the -index option to list the observation variables that are present in that file.


Configure
^^^^^^^^^

.. note::

Start by making an output directory for PB2NC and changing directories:

.. code-block::

mkdir -p ${METPLUS_TUTORIAL_DIR}/output/met_output/pb2nc&lt;br/&gt;
cd ${METPLUS_TUTORIAL_DIR}/output/met_output/pb2nc

The behavior of PB2NC is controlled by the contents of the configuration file passed to it on the command line. The default PB2NC configuration may be found in the `data/config/PB2NCConfig_default <https://github.com/dtcenter/MET/blob/main_v11.0/data/config/PB2NCConfig_default>`_ file.

.. note::

Prior to modifying the configuration file, users are advised to make a copy of the default:

.. code-block::

cp ${MET_BUILD_BASE}/share/met/config/PB2NCConfig_default PB2NCConfig_tutorial_run1

.. note::

Open up the **PB2NCConfig_tutorial_run1** file for editing with your preferred text editor.

.. code-block::

vi PB2NCConfig_tutorial_run1

The configurable items for PB2NC are used to filter out the PrepBufr observations that should be retained or derived. You may find a complete description of the configurable items in the `pb2nc <https://metplus.readthedocs.io/projects/met/en/latest/Users_Guide/reformat_point.html#pb2nc-configuration-file>`_ configuration file section of the `MET User's Guide <https://metplus.readthedocs.io/projects/met/en/latest/Users_Guide/index.html>`_ or in the `Configuration File Overview <https://metplus.readthedocs.io/projects/met/en/latest/Users_Guide/config_options.html>`_.
For this tutorial, edit the PB2NCConfig_tutorial_run1 file as follows:

Set:

.. note::

message_type = [ "ADPUPA", "ADPSFC" ];

to retain only those 2 message types. Message types are described in:
??? Julie, do you want a visable link???
`<http://www.emc.ncep.noaa.gov/mmb/data_processing/prepbufr.doc/table_1.htm>`_

Set:

.. note::

obs_window = {&lt;br/&gt;
beg = -1800;&lt;br/&gt;
end =  1800;&lt;br/&gt;
}

so that only observations within 1800 second (30 minutes) of the file time will be retained.

Set:

.. note::

mask = {&lt;br/&gt;
grid = "G212";&lt;br/&gt;
poly = "";&lt;br/&gt;
}

to retain only those observations residing within NCEP Grid 212, on which the forecast data resides.

Set:

.. note::

obs_bufr_var = [ "QOB", "TOB", "UOB", "VOB", "D_WIND", "D_RH" ];

to retain observations for specific humidity, temperature, the u-component of wind, and the v-component of wind and to derive observation values for wind speed and relative humidity.
While we are request these observation variable names from the input file, the following corresponding strings will be written to the output file: SPFH, TMP, UGRD, VGRD, WIND, RH. This mapping of input PrepBufr variable names to output variable names is specified by the obs_prepbufr_map config file entry. This enables the new features in the current version of MET to be backward compatible with earlier versions.

.. note::

Next, save the **PB2NCConfig_tutorial_run1** file and exit the text editor.

Run
^^^

.. note::

Next, run PB2NC on the command line using the following command:

.. code-block::

pb2nc \&lt;br/&gt;
${METPLUS_DATA}/met_test/data/sample_obs/prepbufr/ndas.t00z.prepbufr.tm12.20070401.nr \&lt;br/&gt;
tutorial_pb_run1.nc \&lt;br/&gt;
PB2NCConfig_tutorial_run1 \&lt;br/&gt;
-v 2

.. important::

??? Julie, confirm this link is correct.  It downloaded to my computer.  I wasn't expecting that???
If this run fails due to runtime issues, please download a copy of the output file `here <https://dtcenter.org/sites/default/files/community-code/met/online-practical/tutorial_pb_run1.nc>`_ and manually save it as **tutorial_pb_run1.nc**.

PB2NC is now filtering the observations from the PrepBufr file using the configuration settings we specified and writing the output to the NetCDF file name we chose. This should take a few minutes to run. As it runs, you should see several status messages printed to the screen to indicate progress. You may use the -v command line option to turn off (-v 0) or change the amount of log information printed to the screen.
.. note::

Inspect the PB2NC status messages.

If you'd like to filter down the observations further, you may want to narrow the time window or modify other filtering criteria. We will do that after inspecting the resultant NetCDF file.

Output
^^^^^^
When PB2NC is finished, you may view the output NetCDF file it wrote using the ncdump utility.

.. note::

Run the following command to view the header of the NetCDF output file:

.. code-block::

ncdump -h tutorial_pb_run1.nc

In the NetCDF header, you'll see that the file contains nine dimensions and nine variables. The obs_arr variable contains the actual observation values. The obs_qty variable contains the corresponding quality flags. The four header variables (hdr_typ, hdr_sid, hdr_vld, hdr_arr) contain information about the observing locations.
The obs_var, obs_unit, and obs_desc variables describe the observation variables contained in the output. The second entry of the obs_arr variable (i.e. var_id) lists the index into these array for each observation. For example, for observations of temperature, you'd see TMP in obs_var, KELVIN in obs_unit, and TEMPERATURE OBSERVATION in obs_desc. For observations of temperature in obs_arr, the second entry (var_id) would list the index of that temperature information.
.. note::

Inspect the output of **ncdump** before continuing.

**Plot-Point-Obs**

The plot_point_obs tool plots the location of these NetCDF point observations. Just like plot_data_plane is useful to visualize gridded data, run plot_point_obs to make sure you have point observations where you expect.
.. note::

Run the following command:

.. code-block::

plot_point_obs \&lt;br/&gt;
tutorial_pb_run1.nc \&lt;br/&gt;
tutorial_pb_run1.ps

.. note::

Display the output PostScript file by running the following command:

.. code-block::

gv tutorial_pb_run1.ps &amp;amp;

Each red dot in the plot represents the location of at least one observation value. The plot_point_obs tool has additional command line options for filtering which observations get plotted and the area to be plotted.
.. note::

View its usage statement by running the following command:

.. code-block::

plot_point_obs

By default, the points are plotted on the full globe.
.. note::

Next, try rerunning **plot_point_obs** using the **-data_file** option to specify the grid over which the points should be plotted:

.. code-block::

plot_point_obs \&lt;br/&gt;
tutorial_pb_run1.nc \&lt;br/&gt;
tutorial_pb_run1_zoom.ps \&lt;br/&gt;
-data_file ${METPLUS_DATA}/met_test/data/sample_fcst/2007033000/nam.t00z.awip1236.tm00.20070330.grb

MET extracts the grid information from the first record of that GRIB file and plots the points on that domain.
.. note::

Display the output PostScript file by running the following command:

.. code-block::

gv tutorial_pb_run1_zoom.ps &amp;amp;

The plot_data_plane tool can be run on the NetCDF output of any of the MET point observation pre-processing tools (pb2nc, ascii2nc, madis2nc, and lidar2nc).

Reconfigure and Rerun
^^^^^^^^^^^^^^^^^^^^^

Now we'll rerun PB2NC, but this time we'll tighten the observation acceptance criteria.
.. note::

Start by making a copy of the configuration file we just used:

.. code-block::

cp PB2NCConfig_tutorial_run1 PB2NCConfig_tutorial_run2

.. note::

Open up the **PB2NCConfig_tutorial_run2** file and edit it as follows:

.. code-block::

vi PB2NCConfig_tutorial_run2


Set:
.. note::

message_type = [];

to retain all message types.
Set:
.. note::

obs_window = {&lt;br/&gt;
beg = -25*30;&lt;br/&gt;
end =  25*30;&lt;br/&gt;
}

so that only observations 25 minutes before and 25 minutes after the top of the hour are retained.
Set:
.. note::

quality_mark_thresh = 1;

to retain only the observations marked "Good" by the NCEP quality control system.

.. note::

Next, run PB2NC again but change the output name using the following command:

.. code-block::

pb2nc \&lt;br/&gt;
${METPLUS_DATA}/met_test/data/sample_obs/prepbufr/ndas.t00z.prepbufr.tm12.20070401.nr \&lt;br/&gt;
tutorial_pb_run2.nc \&lt;br/&gt;
PB2NCConfig_tutorial_run2 \&lt;br/&gt;
-v 2

.. important::

If this run fails due to runtime issues, please download a copy of the output file &lt;a href="https://dtcenter.org/sites/default/files/community-code/met/online-practical/tutorial_pb_run2.nc"&gt;here&lt;/a&gt; and manually save it as **tutorial_pb_run2.nc**.

.. note::

Inspect the PB2NC status messages and note that fewer observations were retained than the previous example.

The majority of the observations were rejected because their valid time no longer fell inside the tighter obs_window setting.
When configuring PB2NC for your own projects, you should err on the side of keeping more data rather than less. As you'll see, the grid-to-point verification tools (Point-Stat and Ensemble-Stat) allow you to further refine which point observations are actually used in the verification. However, keeping a lot of point observations that you'll never actually use will make the data files larger and slightly slow down the verification. For example, if you're using a Global Data Assimilation (GDAS) PREPBUFR file to verify a model over Europe, it would make sense to only keep those point observations that fall within your model domain.

METplus Use Case: PB2NC
-----------------------

.. important::

??? Julie, I've removed the bolding so the links will work???
IMPORTANT NOTE: If you are returning to the tutorial, you must source the tutorial setup script before running the following instructions. If you are unsure if you have done this step, please navigate to the :ref:`Verify Environment is Set Correctly <verif_env_set_correct>` page.

This use case utilizes the MET PB2NC tool. 
Optional: Refer to the `MET Users Guide <https://metplus.readthedocs.io/projects/met/en/latest/Users_Guide/index.html>`_ for a description of the MET tools used in this use case.
Optional: Refer to the `METplus Config Glossary <https://metplus.readthedocs.io/en/latest/Users_Guide/glossary.html>`_ section of the METplus Users Guide for a reference to METplus variables used in this use case.

.. note::

**Review the settings in the PB2NC.conf file:**

.. code-block::

less ${METPLUS_BUILD_BASE}/parm/use_cases/met_tool_wrapper/PB2NC/PB2NC.conf

Note that the input directory PB2NC_INPUT_DIR is set to a path relative to {INPUT_BASE} and the output directory PB2NC_OUTPUT_DIR is set to a path relative to {OUTPUT_BASE}:
.. admonition:: Sample Output

[config]&lt;p&gt;&lt;/p&gt;
&lt;p&gt;...&lt;br/&gt;
PB2NC_INPUT_DIR = {INPUT_BASE}/met_test/data/sample_obs/prepbufr&lt;br/&gt;
...&lt;br/&gt;
PB2NC_OUTPUT_DIR = {OUTPUT_BASE}/pb2nc&lt;/p&gt;

{PARM_BASE} is set automatically by METplus. The wrapped MET config file for PB2NC is set relative to {PARM_BASE} in PB2NC_CONFIG_FILE:
.. admonition:: Sample Output

PB2NC_CONFIG_FILE = {PARM_BASE}/met_config/PB2NCConfig_wrapped

.. note::

Let's look at the PB2NC_CONFIG_FILE

Values for the MET tool PB2NC are passed in from METplus config files, including PB2NC.conf
.. code-block::

less ${METPLUS_BUILD_BASE}/parm/met_config/PB2NCConfig_wrapped

.. admonition:: Sample Output

////////////////////////////////////////////////////////////////////////////////&lt;br/&gt;
//&lt;br/&gt;
// PB2NC configuration file.&lt;br/&gt;
//&lt;br/&gt;
// For additional information, see the MET_BASE/config/README file.&lt;br/&gt;
// ////////////////////////////////////////////////////////////////////////////////&lt;p&gt;&lt;/p&gt;
&lt;p&gt;//&lt;br/&gt;
// PrepBufr message type&lt;br/&gt;
//&lt;br/&gt;
${PB2NC_MESSAGE_TYPE} ;&lt;/p&gt;
&lt;p&gt;//&lt;br/&gt;
// Mapping of message type group name to comma-separated list of values&lt;br/&gt;
// Derive PRMSL only for SURFACE message types&lt;br/&gt;
//&lt;br/&gt;
message_type_group_map = [&lt;br/&gt;
{ key = "SURFACE"; val = "ADPSFC,SFCSHP,MSONET"; },&lt;br/&gt;
{ key = "ANYAIR";  val = "AIRCAR,AIRCFT"; },&lt;br/&gt;
{ key = "ANYSFC";  val = "ADPSFC,SFCSHP,ADPUPA,PROFLR,MSONET"; },&lt;br/&gt;
{ key = "ONLYSF";  val = "ADPSFC,SFCSHP" }&lt;br/&gt;
];&lt;br/&gt;
&lt;/p&gt;

No modifications are needed to run the PB2NC METplus tool. 

.. note::

**Run the PB2NC use case:**

.. code-block::

run_metplus.py \&lt;br/&gt;
${METPLUS_BUILD_BASE}/parm/use_cases/met_tool_wrapper/PB2NC/PB2NC.conf \&lt;br/&gt;
${METPLUS_TUTORIAL_DIR}/tutorial.conf \&lt;br/&gt;
config.OUTPUT_BASE=${METPLUS_TUTORIAL_DIR}/output/PB2NC

.. note::

**Review the output file:**

.. code-block::

ls ${METPLUS_TUTORIAL_DIR}/output/PB2NC/pb2nc

The following is the statistical output and file generated from the command:

sample_pb.nc

MET Tool: ASCII2NC
------------------

.. important::
??? Julie, I've removed the bolding so the link will work.???
IMPORTANT NOTE: If you are returning to the tutorial, you must source the tutorial setup script before running the following instructions. If you are unsure if you have done this step, please navigate to the :ref:`Verify Environment is Set Correctly <verif_env_set_correct>` page.

**ASCII2NC FUNCTIONALITY**

The ASCII2NC tool reformats ASCII point observations into the intermediate NetCDF format that Point-Stat and Ensemble-Stat read. ASCII2NC simply reformats the data and does much less filtering of the observations than PB2NC does. ASCII2NC supports a simple 11-column format, described below, the Little-R format often used in data assimilation, SURFace RADiation (SURFRAD) data, Western Wind and Solar Integration Studay (WWSIS) data, and AErosol RObotic NEtwork (Aeronet) data versions 2 and 3 format. MET version 9.0 added support for passing observations to ASCII2NC using a Python script.  Future version of MET may be enhanced to support additional commonly used ASCII point observation formats based on community input.

**MET POINT OBSERVATION FORMAT**

The MET point observation format consists of one observation value per line. Each input observation line should consist of the following 11 columns of data:

Message_Type
Station_ID
Valid_Time in YYYYMMDD_HHMMSS format
Lat in degrees North
Lon in degrees East
Elevation in meters above sea level
Variable_Name for this observation (or GRIB_Code for backward compatibility)
Level as the pressure level in hPa or accumulation interval in hours
Height in meters above sea level or above ground level
QC_String quality control string
Observation_Value

It is the user's responsibility to get their ASCII point observations into this format.

**ASCII2NC USAGE**

.. note::

View the usage statement for ASCII2NC by simply typing the following:

.. code-block::

ascii2nc

Usage: ascii2nc

ascii_file1 [...]
One or more input ASCII path/filename

netcdf_file
Output NetCDF path/filename

[-format ASCII_format]
Set to met_point, little_r, surfrad, wwsis, aeronet, aeronetv2, aeronetv3, or python

[-config file]
Configuration file to specify how observation data should be summarized

[-mask_grid string]
Named grid or a gridded data file for filtering point observations spatially

[-mask_poly file]
Polyline masking file for filtering point observations spatially

[-mask_sid file|list]
Specific station ID's to be used in an ASCII file or comma-separted list

[-log file]
Outputs log messages to the specified file

[-v level]
Level of logging

[-compress level]
NetCDF compression level

At a minimum, the input ascii_file and the output netcdf_file must be passed on the command line. ASCII2NC interrogates the data to determine it's format, but the user may explicitly set it using the -format command line option. The -mask_grid, -mask_poly, and -mask_sid options can be used to filter observations spatially.

Run
^^^

.. note::

Start by making an output directory for ASCII2NC and changing directories:

.. code-block::

mkdir -p ${METPLUS_TUTORIAL_DIR}/output/met_output/ascii2nc&lt;br/&gt;
cd ${METPLUS_TUTORIAL_DIR}/output/met_output/ascii2nc

Since ASCII2NC performs a simple reformatting step, typically no configuration file is needed. However, when processing high-frequency (1 or 3-minute) SURFRAD data, a configuration file may be used to define a time window and summary metric for each station. For example, you might compute the average observation value +/- 15 minutes at the top of each hour for each station. In this example, we will not use a configuration file.
The sample ASCII observations in the MET tarball are still identified by GRIB code rather than the newer variable name option.
.. note::

Dump that file and notice that the GRIB codes in the seventh column could be replaced by corresponding variable names.

For example, 52 corresponds to RH:
.. code-block::

cat ${METPLUS_DATA}/met_test/data/sample_obs/ascii/sample_ascii_obs.txt

.. note::

Run ASCII2NC on the command line using the following command:

.. code-block::

ascii2nc \&lt;br/&gt;
${METPLUS_DATA}/met_test/data/sample_obs/ascii/sample_ascii_obs.txt \&lt;br/&gt;
tutorial_ascii.nc \&lt;br/&gt;
-v 2

ASCII2NC should perform this reformatting step very quickly since the sample file only contains data for 5 stations.

Output
^^^^^^

When ASCII2NC is finished, you may view the output NetCDF file it wrote using the ncdump utility.
.. note::

Run the following command to view the header of the NetCDF output file:

.. code-block::

ncdump -h tutorial_ascii.nc

The NetCDF header should look nearly identical to the output of the NetCDF output of PB2NC. You can see the list of stations for which we have data by inspecting the hdr_sid_table variable:
.. code-block::

ncdump -v hdr_sid_table tutorial_ascii.nc

.. note::

Feel free to inspect the contents of the other variables as well.

This ASCII data only contains observations at a few locations.
.. note::

Use the **plot_point_obs** to plot the locations, increasing the level of verbosity to 3 to see more detail:

.. code-block::

plot_point_obs \&lt;br/&gt;
tutorial_ascii.nc \&lt;br/&gt;
tutorial_ascii.ps \&lt;br/&gt;
-data_file ${METPLUS_DATA}/met_test/data/sample_fcst/2007033000/nam.t00z.awip1236.tm00.20070330.grb \&lt;br/&gt;
-v 3

.. code-block::

gv tutorial_ascii.ps &amp;amp;

Next, we'll use the NetCDF output of PB2NC and ASCII2NC to perform Grid-to-Point verification using the Point-Stat tool.

METplus Use Case: ASCII2NC with Python Embedding 
------------------------------------------------

.. important::

??? Julie, I've removed the bolding so the link will work???
IMPORTANT NOTE: If you are returning to the tutorial, you must source the tutorial setup script before running the following instructions. If you are unsure if you have done this step, please navigate to the :ref:`Verify Environment is Set Correctly <verif_env_set_correct>` page.

This use case utilizes the MET ASCII2NC tool to demonstrate Python Embedding. Python embedding is a novel capability within METplus that allows a user to place a Python script into a METplus workflow. For example, if a user has a data format that is unsupported by the MET tools then a user could write their own Python file reader, and hand off the data to the MET tools within a workflow.

??? Julie, I added line breaks???

| The data utilized in this use case are hypothetical accumulated precipitation data in ASCII format.
| Optional: Refer to the `MET Users Guide <https://metplus.readthedocs.io/projects/met/en/latest/Users_Guide/index.html>`_ for a description of the MET tools used in this use case.
| Optional: Refer to the `MET Users Guide Appendix F: Python Embedding <https://metplus.readthedocs.io/projects/met/en/latest/Users_Guide/appendixF.html>`_ for details on how Python embedding works for MET tools.
| Optional: Refer to the `METplus Config Glossary <https://metplus.readthedocs.io/en/latest/Users_Guide/glossary.html>`_ section of the METplus Users Guide for a reference to METplus variables used in this use case.

.. note::

**View the template Python Embedding scripts available with MET**

MET includes example scripts for reading point data and gridded data (all in ASCII format). These can be used by users as a jumping-off point for developing their own Python embedding scripts, and are also used by this use case and other METplus use cases that demonstrate Python Embedding
.. code-block::

ls -1 ${MET_BUILD_BASE}/share/met/python

.. admonition:: Sample Output

derive_WRF_semilatlon.py&lt;br/&gt;
met_point_obs.py&lt;br/&gt;
read_ascii_mpr.py&lt;br/&gt;
read_ascii_numpy_grid.py&lt;br/&gt;
read_ascii_numpy.py&lt;br/&gt;
read_ascii_point.py&lt;br/&gt;
read_ascii_xarray.py&lt;br/&gt;
read_met_point_obs.py

In this use case, read_ascii_point.py is used to read the sample accumulated precipitation data and serve them to ASCII2NC to format into the MET 11-column netCDF format.

.. note::

**Inspect a sample of the accumulated precipitation point data being read with Python.**

.. code-block::

head -3 ${METPLUS_DATA}/met_test/data/sample_obs/ascii/sample_ascii_obs.txt

These data are already in the 11-column format that MET requires, so using Python Embedding is fairly straightforward. If your data do not follow this format, some pre-processing of the data will be required to align your data to the required format. To learn more about what the 11 columns are and what MET expects each column to represent, please reference `this table <https://metplus.readthedocs.io/projects/met/en/latest/Users_Guide/reformat_point.html#table-reformat-point-ascii2nc-format>`_ from the MET users guide.

.. note::

**Inspect the Python Embedding script being used in this use case**

.. code-block::

less ${MET_BUILD_BASE}/share/met/python/read_ascii_point.py

Since the sample data are point data, the Python module Pandas is utilized to read the ASCII data, assign column names that match the MET 11-column format, and then pass the data to the MET ASCII2NC tool.

.. note::

**Run the ASCII2NC Python Embedding use case:**

.. code-block::

run_metplus.py \&lt;br/&gt;
${METPLUS_BUILD_BASE}/parm/use_cases/met_tool_wrapper/ASCII2NC/ASCII2NC_python_embedding.conf \&lt;br/&gt;
${METPLUS_TUTORIAL_DIR}/tutorial.conf \&lt;br/&gt;
config.OUTPUT_BASE=${METPLUS_TUTORIAL_DIR}/output/ASCII2NC_python_embedding

This command utilizes the METplus wrappers to execute a Python script to read in the ASCII data and pass them off to ASCII2NC to write to a netCDF file. While the Python script called here is simply for demonstration purposes, your Python script could serve to perform various data manipulation and formatting, or reading of proprietary or unsupported file formats to end up with a netCDF file compatible with the MET tools.

.. note::

**Review the Output Files**

.. code-block::

ls ${METPLUS_TUTORIAL_DIR}/output/ASCII2NC_python_embedding/met_tool_wrapper/ASCII2NC

You should see the output netCDF file (ascii2nc_python.nc), which conforms to the 11-column format required by the MET tools.

.. note::

**Let's Write Some Python!**

Copy the METplus use configuration file to your current working directory:
.. code-block::

cp ${METPLUS_BUILD_BASE}/parm/use_cases/met_tool_wrapper/ASCII2NC/ASCII2NC_python_embedding.conf ${METPLUS_TUTORIAL_DIR}

Copy the Python Embedding script to your current working directory and rename it to my_ascii_point.py:
.. code-block::

cp ${MET_BUILD_BASE}/share/met/python/read_ascii_point.py ${METPLUS_TUTORIAL_DIR}/my_ascii_point.py

Open the Python Embedding script in a text editor of your choice, and add the following on line 7 of the file (make sure the indentation matches the previous line):
.. code-block::

vi ${METPLUS_TUTORIAL_DIR}/my_ascii_point.py

Add on line 7:
.. admonition:: Sample Output

print("HELLO! CREATING PANDAS DATAFRAME OF POINT OBS.")

Save the Python Embedding script.

.. note::

**Modify the METplus Use Case Configuration File to Use Your Python Script**

Open the METplus use case file in a text editor of your choice and modify line 43 to use your Python script:
.. code-block::

vi ${METPLUS_TUTORIAL_DIR}/ASCII2NC_python_embedding.conf

Change line 43 to:
.. admonition:: Sample Output

ASCII2NC_INPUT_TEMPLATE = "{ENV[METPLUS_TUTORIAL_DIR]}/my_ascii_point.py {INPUT_BASE}/met_test/data/sample_obs/ascii/sample_ascii_obs.txt"

The Python script contains an import of met_point_obs. This is found automatically by the read_ascii_point.py script because it is in the same share/met/python directory. Since you are calling my_ascii_point.py from your tutorial directory, you will have to set the PYTHONPATH to include the share/met/python directory so the import succeeds.
.. note::

**Set PYTHONPATH in the [user_env_vars] section of the METplus configuration file.**

Add the following to the very end of ${METPLUS_TUTORIAL_DIR}/ASCII2NC_python_embedding.conf:
.. admonition:: Sample Output

[user_env_vars]&lt;br/&gt;
PYTHONPATH={MET_INSTALL_DIR}/share/met/python:$PYTHONPATH

Save the METplus use case configuration file.


.. note::

**Re-run the Use Case, and See If Your Python Code Is Used**

.. code-block::

run_metplus.py \&lt;br/&gt;
${METPLUS_TUTORIAL_DIR}/ASCII2NC_python_embedding.conf \&lt;br/&gt;
${METPLUS_TUTORIAL_DIR}/tutorial.conf \&lt;br/&gt;
config.OUTPUT_BASE=${METPLUS_TUTORIAL_DIR}/output/ASCII2NC_python_embedding

.. note::

**Look for Your Python Print Statement In the METplus Log File**

The 2nd last log message printed to the screen will contain the full path to the log file that was created for this run. Copy this path and run less to view the log file. It will look something like this:
.. code-block::

less ${METPLUS_TUTORIAL_DIR}/output/ASCII2NC_python_embedding/logs/metplus.log.YYYYMMSSHHMMSS

(NOTE: Replace YYYYMMDDHHMMSS with the time and date appended to the log file from the run in step 8). You should see the print statement written to the log file, showing that your modifications were used by METplus and ASCII2NC!


MET Tool: Point-Stat
--------------------

.. important::

??? Julie, I've removed the bolding???
IMPORTANT NOTE: If you are returning to the tutorial, you must source the tutorial setup script before running the following instructions. If you are unsure if you have done this step, please navigate to the :ref:`Verify Environment is Set Correctly <verif_env_set_correct>` page.

**POINT-STAT FUNCTIONALITY**  

The Point-Stat tool provides verification statistics for comparing gridded forecasts to observation points, as opposed to gridded analyses like Grid-Stat. The Point-Stat tool matches gridded forecasts to point observation locations using one or more configurable interpolation methods. The tool then computes a configurable set of verification statistics for these matched pairs. Continuous statistics are computed over the raw matched pair values. Categorical statistics are generally calculated by applying a threshold to the forecast and observation values. Confidence intervals, which represent a measure of uncertainty, are computed for all of the verification statistics.

**POINT-STAT USAGE**

.. note::

View the usage statement for Point-Stat by simply typing the following:

.. code-block::

point_stat

Usage: point_stat

fcst_file
Input gridded file path/name

obs_file
Input NetCDF observation file path/name

config_file
Configuration file

[-point_obs file]
Additional NetCDF observation files to be used (optional)

[-obs_valid_beg time]
Sets the beginning of the matching time window in YYYYMMDD[_HH[MMSS]] format (optional)

[-obs_valid_end time]
Sets the end of the matching time window in YYYYMMDD[_HH[MMSS]] format (optional)

[-outdir path]
Overrides the default output directory (optional)

[-log file]
Outputs log messages to the specified file (optional)

[-v level]
Level of logging (optional)

At a minimum, the input gridded fcst_file, the input NetCDF obs_file (output of PB2NC, ASCII2NC, MADIS2NC, and LIDAR2NC, last two not covered in these exercises), and the configuration config_file must be passed in on the command line. You may use the -point_obs command line argument to specify additional NetCDF observation files to be used.

Configure
^^^^^^^^^

.. note::

Start by making an output directory for Point-Stat and changing directories:

.. code-block::

mkdir -p ${METPLUS_TUTORIAL_DIR}/output/met_output/point_stat&lt;br/&gt;
cd ${METPLUS_TUTORIAL_DIR}/output/met_output/point_stat

The behavior of Point-Stat is controlled by the contents of the configuration file passed to it on the command line. The default Point-Stat configuration file may be found in the 
`data/config/PointStatConfig_default <https://github.com/dtcenter/MET/blob/main_v11.0/data/config/PointStatConfig_default>`_ file.
The configurable items for Point-Stat are used to specify how the verification is to be performed. The configurable items include specifications for the following:

The forecast fields to be verified at the specified vertical levels.
The type of point observations to be matched to the forecasts.
The threshold values to be applied.
The areas over which to aggregate statistics - as predefined grids, lat/lon polylines, or individual stations.
The confidence interval methods to be used.
The interpolation methods to be used.
The types of verification methods to be used.

.. note::

Let's customize the configuration file. First, make a copy of the default:

.. code-block::

cp ${MET_BUILD_BASE}/share/met/config/PointStatConfig_default PointStatConfig_tutorial_run1

.. note::

Next, open up the **PointStatConfig_tutorial_run1** file for editing and modify it as follows:

.. code-block::

vi PointStatConfig_tutorial_run1

Set:
.. note::

fcst = {&lt;br/&gt;
message_type = [ "ADPUPA" ];&lt;br/&gt;
field = [&lt;br/&gt;
{&lt;br/&gt;
name     = "TMP";&lt;br/&gt;
level      = [ "P850-1050", "P500-850" ];&lt;br/&gt;
cat_thresh = [ &amp;lt;=273, &amp;gt;273 ];&lt;br/&gt;
}&lt;br/&gt;
];&lt;br/&gt;
}&lt;br/&gt;
obs = fcst;

to verify temperature over two different pressure ranges against ADPUPA observations using the thresholds specified.
Set:
.. note::

ci_alpha = [ 0.05, 0.10 ];

to compute confidence intervals using both a 5% and a 10% level of certainty.
Set:
.. note::

output_flag = {&lt;br/&gt;
fho    = BOTH;&lt;br/&gt;
ctc    = BOTH;&lt;br/&gt;
cts    = STAT;&lt;br/&gt;
mctc   = NONE;&lt;br/&gt;
mcts   = NONE;&lt;br/&gt;
cnt    = BOTH;&lt;br/&gt;
sl1l2  = STAT;&lt;br/&gt;
sal1l2 = NONE;&lt;br/&gt;
vl1l2  = NONE;&lt;br/&gt;
val1l2 = NONE;&lt;br/&gt;
pct    = NONE;&lt;br/&gt;
pstd   = NONE;&lt;br/&gt;
pjc    = NONE;&lt;br/&gt;
prc    = NONE;&lt;br/&gt;
ecnt   = NONE;&lt;br/&gt;
eclv   = BOTH;&lt;br/&gt;
mpr    = BOTH;&lt;br/&gt;
}

to indicate that the forecast-hit-observation (FHO) counts, contingency table counts (CTC), contingency table statistics (CTS), continuous statistics (CNT), partial sums (SL1L2), economic cost/loss value (ECLV), and the matched pair data (MPR) line types should be output. Setting SL1L2 and CTS to STAT causes those lines to only be written to the output .stat file, while setting others to BOTH causes them to be written to both the .stat file and the optional LINE_TYPE.txt file.
Set:
.. note::

output_prefix = "run1";

to customize the output file names for this run.

Note that in the mask dictionary, the grid entry is set to FULL. This instructs Point-Stat to compute statistics over the entire input model domain. Setting grid to FULL has this special meaning.
.. note::

Next, save the **PointStatConfig_tutorial_run1** file and exit the text editor.

Run
^^^
Next, run Point-Stat to compare a GRIB forecast to the NetCDF point observation output of the ASCII2NC tool.
.. note::

Run the following command line:

.. code-block::

point_stat \&lt;br/&gt;
${METPLUS_DATA}/met_test/data/sample_fcst/2007033000/nam.t00z.awip1236.tm00.20070330.grb \&lt;br/&gt;
../ascii2nc/tutorial_ascii.nc \&lt;br/&gt;
PointStatConfig_tutorial_run1 \&lt;br/&gt;
-outdir . \&lt;br/&gt;
-v 2

Point-Stat is now performing the verification tasks we requested in the configuration file. It should take less than a minute to run. You should see several status messages printed to the screen to indicate progress.
If you receive a syntax error such as the one listed below, review PointStatConfig_tutorial_run1 for an extra comma after the "}" on line number 59
.. admonition:: Sample Output

&lt;p&gt;        cat_thresh = [ &amp;gt;273.0 ];&lt;br/&gt;
}, &amp;lt;---Remove the comma&lt;/p&gt;

.. note::

&lt;p&gt;DEBUG 1: Default Config File: /usr/local/met-9.0/share/met/config/PointStatConfig_default&lt;br/&gt;
DEBUG 1: User Config File: PointStatConfig_tutorial_run1&lt;br/&gt;
ERROR  :&lt;br/&gt;
ERROR  : yyerror() -&amp;gt; syntax error in file "/tmp/met_config_26760_0"&lt;br/&gt;
ERROR  :&lt;br/&gt;
ERROR  :    line   = 59&lt;br/&gt;
ERROR  :&lt;br/&gt;
ERROR  :    column = 0&lt;br/&gt;
ERROR  :&lt;br/&gt;
ERROR  :    text   = "]"&lt;br/&gt;
ERROR  :&lt;br/&gt;
ERROR  :&lt;br/&gt;
ERROR  :    ];&lt;br/&gt;
ERROR  : _____&lt;br/&gt;
ERROR  :&lt;/p&gt;

.. note::

Now try rerunning the command listed above, but increase the verbosity level to 3 (**-v 3**).

Notice the more detailed information about which observations were used for each verification task. If you run Point-Stat and get fewer matched pairs than you expected, try using the -v 3 option to see why the observations were rejected.
.. important::

&lt;span class="tip"&gt;Users often write MET-Help to ask why they got zero matched pairs from Point-Stat. The first step is always rerunning Point-Stat using verbosity level 3 or higher to list the counts of reasons for why observations were not used!&lt;/span&gt;

Output
^^^^^^

The output of Point-Stat is one or more ASCII files containing statistics summarizing the verification performed. Since we wrote output to the current directory, it should now contain 6 ASCII files that begin with the point_stat_ prefix, one each for the FHO, CTC, CNT, ECLV, and MPR types, and a sixth for the STAT file. The STAT file contains all of the output statistics while the other ASCII files contain the exact same data organized by line type.
.. important::

&lt;span class="tip"&gt;Since the lines of data in these ASCII files are so long, we strongly recommend configuring your text editor to **NOT** use dynamic word wrapping. The files will be much easier to read that way:&lt;/span&gt;&lt;p&gt;&lt;/p&gt;
&lt;ul&gt;
&lt;li&gt;In the **kwrite** editor, select **Settings-&amp;gt;Configure Editor**, de-select **Dynamic Word Wrap** and click **OK**.&lt;/li&gt;
&lt;li&gt;In the **vi** editor, type the command **:set nowrap**. To set this as the default behavior, run the following command:&lt;br/&gt;
&lt;div class="codeblock"&gt;echo "set nowrap" &amp;gt;&amp;gt; ~/.exrc&lt;/div&gt;
&lt;/li&gt;
&lt;/ul&gt;

.. note::

Open up the **point_stat_run1_360000L_20070331_120000V_ctc.txt** CTC file using the text editor of your choice and note the following:

.. code-block::

vi point_stat_run1_360000L_20070331_120000V_ctc.txt

This is a simple ASCII file consisting of several rows of data.
Each row contains data for a single verification task.
The FCST_LEAD, FCST_VALID_BEG, and FCST_VALID_END columns indicate the timing information of the forecast field.
The OBS_LEAD, OBS_VALID_BEG, and OBS_VALID_END columns indicate the timing information of the observation field.
The FCST_VAR, FCST_UNITS, FCST_LEV, OBS_VAR, OBS_UNITS, and OBS_LEV columns indicate the two parts of the forecast and observation fields set in the configure file.
The OBTYPE column indicates the PrepBufr message type used for this verification task.
The VX_MASK column indicates the masking region over which the statistics were accumulated.
The INTERP_MTHD and INTERP_PNTS columns indicate the method used to interpolate the forecast data to the observation location.
The FCST_THRESH and OBS_THRESH columns indicate the thresholds applied to FCST_VAR and OBS_VAR.
The COV_THRESH column is not applicable here and will always have NA when using point_stat.
The ALPHA column indicates the alpha used for confidence intervals.
The LINE_TYPE column indicates that these are CTC contingency table count lines.
The TOTAL column indicates the total number of matched pairs.
The remaining columns contain the counts for the contingency table computed by applying the threshold to the forecast/observation matched pairs. The FY_OY (forecast: yes, observation: yes), FY_ON (forecast: yes, observation: no), FN_OY (forecast: no, observation: yes), and FN_ON (forecast: no, observation: no) columns indicate those counts.

.. note::

Next, answer the following questions about this contingency table output:

What do you notice about the structure of the contingency table counts with respect to the two thresholds used? Does this make sense?
Does the model appear to resolve relatively cold surface temperatures?
Based on these observations, are temperatures &gt;273 relatively rare or common in the P850-500 range? How can this affect the ability to get a good score using contingency table statistics? What about temperatures &lt;=273 at the surface?

.. note::

Close that file, open up the **point_stat_run1_360000L_20070331_120000V_cnt.txt** CNT file, and note the following:

.. code-block::

vi point_stat_run1_360000L_20070331_120000V_cnt.txt


The columns prior to LINE_TYPE contain the same data as the previous file we viewed.
The LINE_TYPE column indicates that these are CNT continuous lines.
The remaining columns contain continuous statistics derived from the raw forecast/observation pairs. See the CNT OUTPUT FORMAT section in the Point-Stat section of the MET User's Guide for a thorough description of the output.
Again, confidence intervals are given for each of these statistics as described above.

.. note::

Next, answer the following questions about these continuous statistics:

What conclusions can you draw about the model's performance at each level using continuous statistics? Justify your answer. Did you use a single metric in your evaluation? Why or why not?
Comparing the first line with an alpha value of 0.05 to the second line with an alpha value of 0.10, how does the level of confidence change the upper and lower bounds of the confidence intervals (CIs)?
Similarly, comparing the first line with few numbers of matched pairs in the TOTAL column to the third line with more, how does the sample size affect how you interpret your results?

.. note::

Close that file, open up the **point_stat_run1_360000L_20070331_120000V_fho.txt** FHO file, and note the following:

.. code-block::

vi point_stat_run1_360000L_20070331_120000V_fho.txt

The columns prior to LINE_TYPE contain the same data as the previous file we viewed.
The LINE_TYPE column indicates that these are FHO forecast-hit-observation rate lines.
The remaining columns are similar to the contingency table output and contain the total number of matched pairs, the forecast rate, the hit rate, and observation rate.
The forecast, hit, and observation rates should back up your answer to the third question about the contingency table output.

.. note::

Close that file, open up the **point_stat_run1_360000L_20070331_120000V_mpr.txt** MPR file, and note the following:

.. code-block::

vi point_stat_run1_360000L_20070331_120000V_mpr.txt

The columns prior to LINE_TYPE contain the same data as the previous file we viewed.
The LINE_TYPE column indicates that these are MPR matched pair lines.
The remaining columns are similar to the contingency table output and contain the total number of matched pairs, the matched pair index, the latitude, longitude, and elevation of the observation, the forecasted value, the observed value, and the climatological value (if applicable).
There is a lot of data here and it is recommended that the MPR line_type is used only to verify the tool is working properly.

Reconfigure
^^^^^^^^^^^

Now we'll reconfigure and rerun Point-Stat.
.. note::

Start by making a copy of the configuration file we just used:

.. code-block::

cp PointStatConfig_tutorial_run1 PointStatConfig_tutorial_run2

This time, we'll use two dictionary entries to specify the forecast field in order to set different thresholds for each vertical level. Point-Stat may be configured to verify as many or as few model variables and vertical levels as you desire.
.. note::

Edit the **PointStatConfig_tutorial_run2** file as follows:

.. code-block::

vi PointStatConfig_tutorial_run2

Set:
.. note::

fcst = {&lt;br/&gt;
field = [&lt;br/&gt;
{&lt;br/&gt;
name       = "TMP";&lt;br/&gt;
level      = [ "Z2" ];&lt;br/&gt;
cat_thresh = [ &amp;gt;273, &amp;gt;278, &amp;gt;283, &amp;gt;288 ];&lt;br/&gt;
},&lt;br/&gt;
{&lt;br/&gt;
name       = "TMP";&lt;br/&gt;
level      = [ "P750-850" ];&lt;br/&gt;
cat_thresh = [ &amp;gt;278 ];&lt;br/&gt;
}&lt;br/&gt;
];&lt;br/&gt;
}&lt;br/&gt;
obs = fcst;

to verify 2-meter temperature and temperature fields between 750hPa and 850hPa, using the thresholds specified.
Set:
.. note::

message_type = ["ADPUPA","ADPSFC"];&lt;br/&gt;
sid_inc = [];&lt;br/&gt;
sid_exc = [];&lt;br/&gt;
obs_quality = [];&lt;br/&gt;
duplicate_flag = NONE;&lt;br/&gt;
obs_summary = NONE;&lt;br/&gt;
obs_perc_value = 50;

to include the Upper Air (UPA) and Surface (SFC) observations in the evaluation
Set:
.. note::

mask = {&lt;br/&gt;
grid  = [ "G212" ];&lt;br/&gt;
poly  = [ "MET_BASE/poly/EAST.poly",&lt;br/&gt;
"MET_BASE/poly/WEST.poly" ];&lt;br/&gt;
sid   = [];&lt;br/&gt;
llpnt = [];&lt;br/&gt;
}

to compute statistics over the NCEP Grid 212 region and over the Eastern and Western United States, as defined by the polylines specified.
Set:
.. note::

interp = {&lt;br/&gt;
vld_thresh = 1.0;&lt;br/&gt;
shape       = SQUARE;&lt;br/&gt;
type = [&lt;br/&gt;
{&lt;br/&gt;
method = NEAREST;&lt;br/&gt;
width  = 1;&lt;br/&gt;
},&lt;br/&gt;
{&lt;br/&gt;
method = DW_MEAN;&lt;br/&gt;
width  = 5;&lt;br/&gt;
}&lt;br/&gt;
];&lt;br/&gt;
}

to indicate that the forecast values should be interpolated to the observation locations using the nearest neighbor method and by computing a distance-weighted average of the forecast values over the 5 by 5 box surrounding the observation location.
Set:
.. note::

output_flag = {&lt;br/&gt;
fho    = BOTH;&lt;br/&gt;
ctc    = BOTH;&lt;br/&gt;
cts    = BOTH;&lt;br/&gt;
mctc   = NONE;&lt;br/&gt;
mcts   = NONE;&lt;br/&gt;
cnt    = BOTH;&lt;br/&gt;
sl1l2  = BOTH;&lt;br/&gt;
sal1l2 = NONE;&lt;br/&gt;
vl1l2  = NONE;&lt;br/&gt;
val1l2 = NONE;&lt;br/&gt;
pct    = NONE;&lt;br/&gt;
pstd   = NONE;&lt;br/&gt;
pjc    = NONE;&lt;br/&gt;
prc    = NONE;&lt;br/&gt;
ecnt   = NONE;&lt;br/&gt;
eclv   = BOTH;&lt;br/&gt;
mpr    = BOTH;&lt;br/&gt;
}

to switch the SL1L2 and CTS output to BOTH and generate the optional ASCII output files for them.
Set:
.. note::

output_prefix = "run2";

to customize the output file names for this run.

.. note::

Let's look at our configuration selections and figure out the number of verification tasks Point-Stat will perform:

2 fields: TMP/Z2 and TMP/P750-850
2 observing message types: ADPUPA and ADPSFC
3 masking regions: G212, EAST.poly, and WEST.poly
2 interpolations: UW_MEAN width 1 (nearest-neighbor) and DW_MEAN width 5

Multiplying 2 * 2 * 3 * 2 = 24. So in this example, Point-Stat will accumulate matched forecast/observation pairs into 24 groups. However, some of these groups will result in 0 matched pairs being found. To each non-zero group, the specified threshold(s) will be applied to compute contingency tables.
.. note::

Can you diagnose **why** some of these verification tasks resulted in zero matched pairs? (&lt;em&gt;Hint: Reread the tip two pages back!&lt;/em&gt;)

Rerun
^^^^^
Next, run Point-Stat to compare a GRIB forecast to the NetCDF point observation output of the PB2NC tool, as opposed to the much smaller ASCII2NC output we used in the first run.

.. note::

Run the following command line:

.. code-block::

point_stat \&lt;br/&gt;
${METPLUS_DATA}/met_test/data/sample_fcst/2007033000/nam.t00z.awip1236.tm00.20070330.grb \&lt;br/&gt;
../pb2nc/tutorial_pb_run1.nc \&lt;br/&gt;
PointStatConfig_tutorial_run2 \&lt;br/&gt;
-outdir . \&lt;br/&gt;
-v 2

Point-Stat is now performing the verification tasks we requested in the configuration file. It should take a minute or two to run. You should see several status messages printed to the screen to indicate progress. Note the number of matched pairs found for each verification task, some of which are 0.

Plot-Data-Plane Tool
^^^^^^^^^^^^^^^^^^^^^

In this step, we have verified 2-meter temperature. The Plot-Data-Plane tool within MET provides a way to visualize the gridded data fields that MET can read.
.. note::

Run this utility to plot the 2-meter temperature field:

.. code-block::

plot_data_plane \&lt;br/&gt;
${METPLUS_DATA}/met_test/data/sample_fcst/2007033000/nam.t00z.awip1236.tm00.20070330.grb \&lt;br/&gt;
nam.t00z.awip1236.tm00.20070330_TMPZ2.ps \&lt;br/&gt;
'name="TMP"; level="Z2";'

Plot-Data-Plane requires an input gridded data file, an output postscript image file name, and a configuration string defining which 2-D field is to be plotted.
.. note::

View the output by running:

.. code-block::

display nam.t00z.awip1236.tm00.20070330_TMPZ2.ps &amp;amp;

.. note::

View the usage for Plot-Data-Plane by running it with no arguments or using the --help option:

.. code-block::

plot_data_plane --help

.. note::

Now rerun this Plot-Data-Plane command but...

.. note::

Set the title to **2-m Temperature**.


.. note::

Set the plotting range as **250** to **305**.

.. note::

Use the color table named **${MET_BUILD_BASE}/share/met/colortables/NCL_colortables/wgne15.ctable**

Next, we'll take a look at the Point-Stat output we just generated.
.. note::

See the usage statement for all MET tools using the **--help** command line option or with no options at all.

Output
^^^^^^

The format for the CTC, CTS, and CNT line types are the same. However, the numbers will be different as we used a different set of observations for the verification.
.. note::

Open up the **point_stat_run2_360000L_20070331_120000V_cts.txt** CTS file, and note the following:

.. code-block::

vi point_stat_run2_360000L_20070331_120000V_cts.txt

The columns prior to LINE_TYPE contain header information.
The LINE_TYPE column indicates that these are CTS lines.
The remaining columns contain statistics derived from the threshold contingency table counts. See the point_stat output section of the MET User's Guide for a thorough description of the output.
Confidence intervals are given for each of these statistics, computed using either one or two methods. The columns ending in _NCL(normal confidence lower) and _NCU (normal confidence upper) give lower and upper confidence limits computed using assumptions of normality. The columns ending in _BCL (bootstrap confidence lower) and _BCU (bootstrap confidence upper) give lower and upper confidence limits computed using bootstrapping.

.. note::

Close that file, open up the **point_stat_run2_360000L_20070331_120000V_sl1l2.txt** SL1L2 partial sums file, and note the following:

.. code-block::

vi point_stat_run2_360000L_20070331_120000V_sl1l2.txt

The columns prior to LINE_TYPE contain header information.
The LINE_TYPE column indicates these are SL1L2 partial sums lines.

Lastly, the point_stat_run2_360000L_20070331_120000V.stat file contains all of the same data we just viewed but in a single file. The Stat-Analysis tool, which we'll use later in this tutorial, searches for the .stat output files by default but can also read the .txt output files.
.. code-block::

vi point_stat_run2_360000L_20070331_120000V.stat

METplus Use Case: PointStat
---------------------------

.. important::

**IMPORTANT NOTE: If you are returning to the tutorial, you must source the tutorial setup script before running the following instructions. If you are unsure if you have done this step, please navigate to the &lt;a href="https://dtcenter.org/metplus-practical-session-guide-version-5-0/session-1-metplus-setupgrid-grid/metplus-setup/verify-environment-set-correctly" target="_blank"&gt;Verify Environment is Set Correctly&lt;/a&gt; page.**

This use case utilizes the MET Point-Stat tool. 
Optional: Refer to the MET Users Guide for a description of the MET tools used in this use case.
Optional: Refer to the METplus Config Glossary section of the METplus Users Guide for a reference to METplus variables used in this use case.

.. note::

**View Configuration File**

.. note::

Change to the ${METPLUS_TUTORIAL_DIR} directory:

.. code-block::

cd ${METPLUS_TUTORIAL_DIR}

.. note::

Define a unique directory under output that you will use for this use case. In the example below, we'll  override **OUTPUT_BASE** to that directory on the command line.

.. code-block::

vi ${METPLUS_BUILD_BASE}/parm/use_cases/met_tool_wrapper/PointStat/PointStat.conf

The forecast and observations directories are specified in relation to INPUT_BASE (${METPLUS_DATA}), while the output directory is given in relation to {OUTPUT_BASE} (${METPLUS_TUTORIAL_DIR}/output).
.. note::

FCST_POINT_STAT_INPUT_DIR = {INPUT_BASE}/met_test/data/sample_fcst&lt;br/&gt;
OBS_POINT_STAT_INPUT_DIR = {INPUT_BASE}/met_test/out/pb2nc&lt;br/&gt;
...&lt;br/&gt;
POINT_STAT_OUTPUT_DIR = {OUTPUT_BASE}/point_stat

Using the PointStat configuration file, you should be able to run the use case using the sample input data set without any other changes.

.. note::

**Run the PointStat use case:**

.. code-block::

run_metplus.py \&lt;br/&gt;
${METPLUS_BUILD_BASE}/parm/use_cases/met_tool_wrapper/PointStat/PointStat.conf \&lt;br/&gt;
${METPLUS_TUTORIAL_DIR}/tutorial.conf \&lt;br/&gt;
config.OUTPUT_BASE=${METPLUS_TUTORIAL_DIR}/output/PointStat

.. note::

**Review the output file:**

.. code-block::

ls ${METPLUS_TUTORIAL_DIR}/output/PointStat/point_stat

The following is the statistical output and file are generated from the command:

point_stat_360000L_20070331_120000V.stat

.. note::

**Update configuration file and re-run**

.. note::

Copy the configuration file to the user_config directory and open for editing:

.. code-block::

cp ${METPLUS_BUILD_BASE}/parm/use_cases/met_tool_wrapper/PointStat/PointStat.conf ${METPLUS_TUTORIAL_DIR}/user_config/PointStat_tutorial.conf&lt;br/&gt;
vi ${METPLUS_TUTORIAL_DIR}/user_config/PointStat_tutorial.conf

.. note::

Update the POINT_STAT_OUTPUT_PREFIX and consolidate the FCST_VAR and OBS_VAR settings into BOTH_VAR being they are identical.

.. note::

POINT_STAT_OUTPUT_PREFIX = run2&lt;p&gt;&lt;/p&gt;
&lt;p&gt;BOTH_VAR1_NAME = TMP&lt;br/&gt;
BOTH_VAR1_LEVELS = P750-900&lt;br/&gt;
BOTH_VAR1_THRESH = &amp;lt;=273, &amp;gt;273&lt;br/&gt;
&lt;br/&gt;
BOTH_VAR2_NAME = UGRD&lt;br/&gt;
BOTH_VAR2_LEVELS = Z10&lt;br/&gt;
BOTH_VAR2_THRESH = &amp;gt;=5&lt;br/&gt;
&lt;br/&gt;
BOTH_VAR3_NAME = VGRD&lt;br/&gt;
BOTH_VAR3_LEVELS = Z10&lt;br/&gt;
BOTH_VAR3_THRESH = &amp;gt;=5&lt;/p&gt;

.. note::

**Rerun the use-case and compare the output**

.. code-block::

run_metplus.py \&lt;br/&gt;
${METPLUS_TUTORIAL_DIR}/user_config/PointStat_tutorial.conf \&lt;br/&gt;
${METPLUS_TUTORIAL_DIR}/tutorial.conf \&lt;br/&gt;
config.OUTPUT_BASE=${METPLUS_TUTORIAL_DIR}/output/PointStat

.. note::

Diff the original output file with run2. They should be identical.

.. code-block::

diff \&lt;br/&gt;
${METPLUS_TUTORIAL_DIR}/output/PointStat/point_stat/point_stat_360000L_20070331_120000V.stat \&lt;br/&gt;
${METPLUS_TUTORIAL_DIR}/output/PointStat/point_stat/point_stat_run2_360000L_20070331_120000V.stat

METplus Use Case: PointStat - Standard Verification of Global Upper Air
-----------------------------------------------------------------------

.. important::

**IMPORTANT NOTE: If you are returning to the tutorial, you must source the tutorial setup script before running the following instructions. If you are unsure if you have done this step, please navigate to the &lt;a href="https://dtcenter.org/metplus-practical-session-guide-version-5-0/session-1-metplus-setupgrid-grid/metplus-setup/verify-environment-set-correctly" target="_blank"&gt;Verify Environment is Set Correctly&lt;/a&gt; page.**

This use case utilizes the MET Point-Stat tool. 
Optional: Refer to the MET Users Guide for a description of the MET tools used in this use case.
Optional: Refer to the METplus Config Glossary section of the METplus Users Guide for a reference to METplus variables used in this use case.

.. note::

**View Configuration File**

.. note::

Change to the ${METPLUS_TUTORIAL_DIR} directory:

.. code-block::

cd ${METPLUS_TUTORIAL_DIR}

.. note::

View the &lt;a href="https://metplus.readthedocs.io/en/latest/generated/model_applications/medium_range/PointStat_fcstGFS_obsGDAS_UpperAir_MultiField_PrepBufr.html#sphx-glr-generated-model-applications-medium-range-pointstat-fcstgfs-obsgdas-upperair-multifield-prepbufr-py" target="_blank"&gt;Medium Range Weather application use-case for upper air&lt;/a&gt; using GDAS PrepBUFR observations, GFS global forecast, and evaluating multiple fields.

.. note::

NOTE: the naming convention for the use-cases is:&lt;br/&gt;
&lt;em&gt;**[statistics tool(s)]_fcst[Model]_obs[Point Data or Analysis]_[other decriptors including file format].conf**&lt;/em&gt;

.. code-block::

less ${METPLUS_BUILD_BASE}/parm/use_cases/model_applications/medium_range/PointStat_fcstGFS_obsGDAS_UpperAir_MultiField_PrepBufr.conf

This use-case includes running two tools, PB2NC to extract the observations and then Point-Stat to compute statistics. Note the specification of wrappers to run is given in the PROCESS_LIST at the top of the file.
.. admonition:: Sample Output

[config]&lt;br/&gt;
PROCESS_LIST = PB2NC, PointStat

.. admonition:: Sample Output

BOTH_VAR1_NAME = TMP&lt;br/&gt;
BOTH_VAR1_LEVELS = P1000, P925, P850, P700, P500, P400, P300, P250, P200, P150, P100, P50, P20, P10&lt;p&gt;&lt;/p&gt;
&lt;p&gt;BOTH_VAR2_NAME = RH&lt;br/&gt;
BOTH_VAR2_LEVELS = P1000, P925, P850, P700, P500, P400, P300&lt;br/&gt;
...&lt;br/&gt;
BOTH_VAR5_NAME = HGT&lt;br/&gt;
BOTH_VAR5_LEVELS = P1000, P950, P925, P850, P700, P500, P400, P300, P250, P200, P150, P100, P50, P20, P10&lt;/p&gt;

.. admonition:: Sample Output

POINT_STAT_MESSAGE_TYPE = ADPUPA

Using the PointStat configuration file, you should be able to run the use case using the sample input data set without any other changes.

.. note::

**Run the PointStat use case:**

.. code-block::

run_metplus.py \&lt;br/&gt;
${METPLUS_BUILD_BASE}/parm/use_cases/model_applications/medium_range/PointStat_fcstGFS_obsGDAS_UpperAir_MultiField_PrepBufr.conf \&lt;br/&gt;
${METPLUS_TUTORIAL_DIR}/tutorial.conf \&lt;br/&gt;
config.OUTPUT_BASE=${METPLUS_TUTORIAL_DIR}/output/PointStat_UpperAir

This may take a few minutes to run.

.. note::

**Review the output files:**

.. code-block::

ls ${METPLUS_TUTORIAL_DIR}/output/PointStat_UpperAir/gdas

.. code-block::

less ${METPLUS_TUTORIAL_DIR}/output/PointStat_UpperAir/gdas/point_stat_000000L_20170601_000000V.stat

If you scroll down to the middle of the file, you will notice the statistics line-type starts alternating from SL1L2 (partial_sums for continuous statistics) to VL1L2 (partial_sums for vector continuous statistics). If you scroll over, you will see that the lines are different lengths. The MET Users' Guide explains what statistics are reported in each line. See point-stat output in the MET User's Guide.
.. admonition:: Sample Output

V11.0.0 gfs NA 000000 20170601_000000 20170601_000000 000000 20170531_231500 20170601_004500 VGRD m/s P1000 VGRD NA P1000 ADPUPA FULL BILIN 4 NA NA NA NA **SL1L2** 274 0.58128 0.71095 12.1183 14.53877 14.52693 1.57316&lt;br/&gt;
V11.0.0 gfs NA 000000 20170601_000000 20170601_000000 000000 20170531_231500 20170601_004500 UGRD_VGRD m/s P1000 UGRD_VGRD NA P1000 ADPUPA FULL BILIN 4 NA NA NA NA **VL1L2** 274 -0.94226 0.58128 -0.73759 0.71095 28.62333 34.35785 32.59062 4.94574 4.67908&lt;br/&gt;
V11.0.0 gfs NA 000000 20170601_000000 20170601_000000 000000 20170531_231500 20170601_004500 VGRD m/s P925 VGRD NA P925 ADPUPA FULL BILIN 4 NA NA NA NA **SL1L2** 523 0.45376 0.44876 29.18591 29.53347 32.41237 1.34806&lt;br/&gt;
V11.0.0 gfs NA 000000 20170601_000000 20170601_000000 000000 20170531_231500 20170601_004500 UGRD_VGRD m/s P925 UGRD_VGRD NA P925 ADPUPA FULL BILIN 4 NA NA NA NA **VL1L2** 523 0.67347 0.45376 0.81969 0.44876 67.86401 67.37296 74.9574 6.98307 7.34872

.. note::

**Update configuration file and re-run**

.. note::

Copy the configuration file to the user_config directory and open for editing:

.. code-block::

cp ${METPLUS_BUILD_BASE}/parm/use_cases/model_applications/medium_range/PointStat_fcstGFS_obsGDAS_UpperAir_MultiField_PrepBufr.conf ${METPLUS_TUTORIAL_DIR}/user_config/PointStat_UpperAir_example2.conf

Let's look at the two line-types separately in a more human-readable format.
.. note::

Update the **POINT_STAT_OUTPUT_FLAG_SL1L2** and **POINT_STAT_OUTPUT_FLAG_VL1L2** to print out both .stat and .txt output files:

.. code-block::

vi ${METPLUS_TUTORIAL_DIR}/user_config/PointStat_UpperAir_example2.conf

.. admonition:: Sample Output

POINT_STAT_OUTPUT_FLAG_SL1L2 = BOTH&lt;br/&gt;
POINT_STAT_OUTPUT_FLAG_VL1L2 = BOTH

.. note::

Also, PB2NC has already been run, so it doesn't need to be run again.

.. admonition:: Sample Output

PROCESS_LIST = PointStat

.. note::

Update the **OBS_POINT_STAT_INPUT_DIR** to point to the output from the previous run. To do so, we need to reference the METPLUS_TUTORIAL_DIR environment variable.

.. code-block::

vi ${METPLUS_TUTORIAL_DIR}/user_config/PointStat_UpperAir_example2.conf

.. admonition:: Sample Output

OBS_POINT_STAT_INPUT_DIR = {ENV[METPLUS_TUTORIAL_DIR]}/output/PointStat_UpperAir/gdas/upper_air

.. note::

**Rerun the use-case and compare the output**

.. code-block::

run_metplus.py \&lt;br/&gt;
${METPLUS_TUTORIAL_DIR}/user_config/PointStat_UpperAir_example2.conf \&lt;br/&gt;
${METPLUS_TUTORIAL_DIR}/tutorial.conf \&lt;br/&gt;
config.OUTPUT_BASE=${METPLUS_TUTORIAL_DIR}/output/PointStat_UpperAir_example2

.. code-block::

ls ${METPLUS_TUTORIAL_DIR}/output/PointStat_UpperAir_example2/gdas -1

.. admonition:: Sample Output

point_stat_000000L_20170601_000000V_sl1l2.txt&lt;br/&gt;
point_stat_000000L_20170601_000000V.stat&lt;br/&gt;
point_stat_000000L_20170601_000000V_vl1l2.txt&lt;br/&gt;
point_stat_000000L_20170602_000000V_sl1l2.txt&lt;br/&gt;
point_stat_000000L_20170602_000000V.stat&lt;br/&gt;
point_stat_000000L_20170602_000000V_vl1l2.txt&lt;br/&gt;
point_stat_000000L_20170603_000000V_sl1l2.txt&lt;br/&gt;
point_stat_000000L_20170603_000000V.stat&lt;br/&gt;
point_stat_000000L_20170603_000000V_vl1l2.txt

Inspect the .txt files, they should have the same data as in the .stat file, just separated by line type. You will notice the header includes the name of statistics in the .txt files because they are specific to each line type.

METplus Use Case: PointStat - Standard Verification for CONUS Surface
---------------------------------------------------------------------

.. important::

**IMPORTANT NOTE: If you are returning to the tutorial, you must source the tutorial setup script before running the following instructions. If you are unsure if you have done this step, please navigate to the &lt;a href="https://dtcenter.org/metplus-practical-session-guide-version-5-0/session-1-metplus-setupgrid-grid/metplus-setup/verify-environment-set-correctly" target="_blank"&gt;Verify Environment is Set Correctly&lt;/a&gt; page.**

This use case utilizes the MET Point-Stat tool. 
Optional: Refer to the MET Users Guide for a description of the MET tools used in this use case.
Optional: Refer to the METplus Config Glossary section of the METplus Users Guide for a reference to METplus variables used in this use case.

.. note::

**View Configuration File**

.. note::

Change to the ${METPLUS_TUTORIAL_DIR} directory:

.. code-block::

cd ${METPLUS_TUTORIAL_DIR}

.. note::

Review the use case configuration file

.. code-block::

less ${METPLUS_BUILD_BASE}/parm/use_cases/model_applications/medium_range/PointStat_fcstGFS_obsNAM_Sfc_MultiField_PrepBufr.conf

Many of the options are similar, except the fields typically at the surface (BOTH_VARn_LEVELS = Z2 and Z10 or integrated BOTH_VARn_LEVELS = L0). Also, the Point-Stat MESSAGE_TYPE is set to a specific keyword ONLYSF for only surface fields. Finally, the PB2NC_INPUT_TEMPLATE includes a da_init specification in the input template to help determine the valid time of the data.
.. note::

POINT_STAT_MESSAGE_TYPE = ONLYSF&lt;br/&gt;
...&lt;br/&gt;
PB2NC_INPUT_TEMPLATE = nam.{da_init?fmt=%Y%m%d}/nam.t{da_init?fmt=%2H}z.prepbufr.tm{offset?fmt=%2H}

Using this configuration file, you should be able to run the use case using the sample input data set without any other changes.

.. note::

**Run the PointStat use case**

.. code-block::

run_metplus.py \&lt;br/&gt;
${METPLUS_BUILD_BASE}/parm/use_cases/model_applications/medium_range/PointStat_fcstGFS_obsNAM_Sfc_MultiField_PrepBufr.conf \&lt;br/&gt;
${METPLUS_TUTORIAL_DIR}/tutorial.conf \&lt;br/&gt;
config.OUTPUT_BASE=${METPLUS_TUTORIAL_DIR}/output/PointStat_Sfc

This may take a few minutes to run.

.. note::

**Review the output files**


.. code-block::

ls ${METPLUS_TUTORIAL_DIR}/output/PointStat_Sfc/nam

.. code-block::

less ${METPLUS_TUTORIAL_DIR}/output/PointStat_Sfc/nam/point_stat_000000L_20170601_000000V.stat

Inspection of the file shows that statistics for TMP, RH, UGRD, VGRD, UGRD_VGRD are available. Also, based on the number listed after the line type (SL1L2 and VL1L2), there are between 8263 - 9300 points included in the computation of the statistics. The big question is why are there no statistics for TCDC and PRMSL? Let's look at the log files.
.. code-block::

ls ${METPLUS_TUTORIAL_DIR}/output/PointStat_Sfc/logs

Open the log file and search on TCDC, you will see that there is an error message stating "no fields matching TCDC/L0 found" in the GFS file. That is why TCDC does not appear in the output.
Look for PRMSL/Z0 in the log file.  We can see the following:
.. admonition:: Sample Output

DEBUG 2: Processing PRMSL/Z0 versus PRMSL/Z0, for observation type ONLYSF, over region FULL, for interpolation method BILIN(4), using 0 matched pairs.&lt;br/&gt;
DEBUG 2: Number of matched pairs = 0&lt;br/&gt;
DEBUG 2: Observations processed = 441178&lt;br/&gt;
DEBUG 2: Rejected: station id = 0&lt;br/&gt;
DEBUG 2: Rejected: obs var name = 441178

You will note, the number of observations processed is the same as the number rejected due to a mismatch with the obs var name. That suggests we need to look at how the OBS variable for PRMSL is defined.

.. note::

**Inspect configuration file and plot fields**

.. code-block::

less ${METPLUS_BUILD_BASE}/parm/use_cases/model_applications/medium_range/PointStat_fcstGFS_obsNAM_Sfc_MultiField_PrepBufr.conf

Note that PB2NC_OBS_BUFR_VAR_LIST = PMO, TOB, TDO, UOB, VOB, PWO, TOCC, D_RH, where PMO is the identifier for MEAN SEA-LEVEL PRESSURE OBSERVATION according to https://www.nco.ncep.noaa.gov/sib/decoders/BUFRLIB/toc/prepbufr/prepbufr_bftab/. Let's use Plot-Data-Plane to confirm this identifier will provide valid observations for Point-Stat to use.
.. code-block::

plot_point_obs \&lt;br/&gt;
${METPLUS_TUTORIAL_DIR}/output/PointStat_Sfc/nam/conus_sfc/20170601/nam.2017060100.nc \&lt;br/&gt;
${METPLUS_TUTORIAL_DIR}/output/PointStat_Sfc/nam/conus_sfc/20170601/nam.2017060100.ps \&lt;br/&gt;
-obs_var PMO

.. note::

Convert to PNG and display

.. code-block::

convert -rotate 90 \&lt;br/&gt;
${METPLUS_TUTORIAL_DIR}/output/PointStat_Sfc/nam/conus_sfc/20170601/nam.2017060100.ps \&lt;br/&gt;
${METPLUS_TUTORIAL_DIR}/output/PointStat_Sfc/nam/conus_sfc/20170601/nam.2017060100.png&lt;p&gt;&lt;/p&gt;
&lt;p&gt;display ${METPLUS_TUTORIAL_DIR}/output/PointStat_Sfc/nam/conus_sfc/20170601/nam.2017060100.png&lt;/p&gt;

.. note::

**Update configuration file and re-run**

.. note::

Open up the PointStat2 conf file and examine the definition of variables. Note that we might want to try changing the BOTH_VAR7_NAME to FCST_VAR7_NAME and OBS_VAR7_NAME:

.. note::

Copy the configuration file to the user_config directory and open for editing:

.. code-block::

cp ${METPLUS_BUILD_BASE}/parm/use_cases/model_applications/medium_range/PointStat_fcstGFS_obsNAM_Sfc_MultiField_PrepBufr.conf ${METPLUS_TUTORIAL_DIR}/user_config/PointStat_Sfc2.conf

.. code-block::

vi ${METPLUS_TUTORIAL_DIR}/user_config/PointStat_Sfc2.conf

.. note::

FCST_VAR7_NAME = PRMSL&lt;br/&gt;
FCST_VAR7_LEVELS = Z0&lt;p&gt;&lt;/p&gt;
&lt;p&gt;OBS_VAR7_NAME = PMO&lt;br/&gt;
OBS_VAR7_LEVELS = Z0&lt;/p&gt;

.. code-block::

run_metplus.py \&lt;br/&gt;
${METPLUS_TUTORIAL_DIR}/user_config/PointStat_Sfc2.conf \&lt;br/&gt;
${METPLUS_TUTORIAL_DIR}/tutorial.conf \&lt;br/&gt;
config.OUTPUT_BASE=${METPLUS_TUTORIAL_DIR}/output/PointStat_Sfc2

.. code-block::

less ${METPLUS_TUTORIAL_DIR}/output/PointStat_Sfc2/nam/point_stat_000000L_20170601_000000V.stat

There is now a line with PRMSL listed and statistics reported.

End of Session 2 and Additional Exercises
-----------------------------------------

Congratulations! You have completed Session 2!
If you have extra time, you may want to try this additional METplus exercise.
The default statistics created by this exercise only dump the partial sums, so we will be also modifying the MET configuration file to add the continuous statistics to the output. There is a little more setup in this use case, which will be instructive and demonstrate the basic structure, flexibility and setup of METplus configuration.

EXERCISE 2.1: Rerun Point-Stat to produce additional continuous statistics file types.

.. note::

**Instructions:** Copy and modify the METplus configuration file for Upper Air to write Continuous statistics (cnt) and the Vector Continuous Statistics (vcnt) line types to both the stat file and its own file.

.. note::

Copy the PointStat.conf file to the user_config directory.

.. code-block::

cp ${METPLUS_BUILD_BASE}/parm/use_cases/met_tool_wrapper/PointStat/PointStat.conf \&lt;br/&gt;
${METPLUS_TUTORIAL_DIR}/user_config/PointStat_add_linetype.conf

.. note::

Edit the file to remove the # character from the beginning of the variables (this uncomments the line) and set the values to BOTH.

.. note::

Change this line (around line 68):

.. admonition:: Sample Output

#POINT_STAT_OUTPUT_FLAG_CNT =

to
.. admonition:: Sample Output

POINT_STAT_OUTPUT_FLAG_CNT = BOTH

.. note::

and change this line (around line 73):

.. admonition:: Sample Output

#POINT_STAT_OUTPUT_FLAG_VCNT =

to
.. admonition:: Sample Output

POINT_STAT_OUTPUT_FLAG_VCNT = BOTH

.. code-block::

vi ${METPLUS_TUTORIAL_DIR}/user_config/PointStat_add_linetype.conf

.. note::

Rerun METplus and use config.OUTPUT_BASE to change the output directory from the command line:

.. code-block::

run_metplus.py \&lt;br/&gt;
${METPLUS_TUTORIAL_DIR}/user_config/PointStat_add_linetype.conf \&lt;br/&gt;
${METPLUS_TUTORIAL_DIR}/tutorial.conf \&lt;br/&gt;
config.OUTPUT_BASE=${METPLUS_TUTORIAL_DIR}/output/PointStat_AddLinetype

.. note::

Review the additional output files generated under ${METPLUS_TUTORIAL_DIR}/output/PointStat_AddLinetype/point_stat

.. code-block::

ls -1 ${METPLUS_TUTORIAL_DIR}/output/PointStat_AddLinetype/point_stat

.. admonition:: Sample Output

point_stat_360000L_20070331_120000V_cnt.txt&lt;br/&gt;
point_stat_360000L_20070331_120000V.stat&lt;br/&gt;
point_stat_360000L_20070331_120000V_vcnt.txt

.. note::

Open the stat file and notice there are two more linetypes, cnt and vcnt.

.. code-block::

less ${METPLUS_TUTORIAL_DIR}/output/PointStat_AddLinetype/point_stat/point_stat_360000L_20070331_120000V.stat
