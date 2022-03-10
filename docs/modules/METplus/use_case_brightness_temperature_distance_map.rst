.. _metplus_use_case_brightness_temperature_distance_map:

Use Case: Brightness Temperature Distance Map Verification
==========================================================

.. raw:: html

  <iframe width="560" height="315" src="https://www.youtube.com/embed/vKQwNBx7OmY" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

Developed for **METplus Version 4.0**.

(*Setup: Open 2 terminals*)

(*Setup: Open URL: https://metplus.readthedocs.io/en/main_v4.0/Users_Guide/index.html*)

(*Setup: Open URL: https://met.readthedocs.io/en/latest/*)


(*Introduction*)

If you would like to follow along with the exercises in this video, please select one of the options to set up your own
:ref:`Training Environment <training_environment>`.

(*Show Title Slide*)

My name is Christina Kalb, and I'm a scientist working on the METplus team at NCAR.  This video will cover how to run the Brightness Temperature Distance Map use case.  
Specific information about this use case can be found in the `METplus User's Guide <https://metplus.readthedocs.io/en/main_v4.0/Users_Guide>`_. 

(*Open https://metplus.readthedocs.io/en/main_v4.0/Users_Guide/index.html, Click on User's Guide*)

Go to section 5, METplus Use Cases, Model Applications, Convection Allowing Models and click on `Grid-Stat: Brightness Temperature Distance Maps <https://metplus.readthedocs.io/en/latest/generated/model_applications/convection_allowing_models/GridStat_fcstFV3_obsGOES_BrightnessTempDmap.html>_. 
Go to section five, METplus Use Cases, Model Applications, Convection Allowing Models, and click on MODE: Brightness Temperature Verification.  ??? This was already in the documentation, but it doesn't match what is said on the video.  Is this okay to remove???

(*Click through 
METplus Use cases, Model Applications, Convection Allowing Models, Grid-Stat: Brightness Temperature Distance Maps, scroll down to METplus Workflow*)

Looking at the information, we see that this use case runs Grid-Stat to create distance maps on the FV3 Model Ensemble members compared to GOES brightness temperature data. It is set up to run two Ensemble members: 
1. model initialization time and 
2. forecast lead times. 
The METplus and MET configuration files are shown here in the documentation. If you want to learn more about Grid-Stat and distance maps go to the ??? Met Users Guide under Section 10 which is on the Grid-Stat tool. This video assumes that you have already installed MET and set up your environment for METplus. Information on how to do this can be found in section one of the ??? Installation and Setup sections of the online tutorial. Topics here will be using the recommended setup. Which is first passing in a Use Case specific to the configuration file, followed by a second configuration file with settings that are specific to the system we are using. 

Let's go ahead and take a look at the parameter file in the settings for this Use Case. We’ll first go into the METplus Repository.   
(* Type cd METplus *)
(* Type vim Tutorial_system.conf *)
Tutorial_system.conf is the system specific configuration file.  The use case specific configuration file is located under: parm/use_cases/model_applications/convection_allowing_models 
and it's called: 
GridStat_fcstFV3_obsGOES_BrightnessTempDmap.conf 

Go ahead and open this file. 
(* Type ??? *)
If we first look at the process list inside this file, we will see that there are two instances of Grid_Stat. These two instances are for the two Ensemble members and the values in parenthesis are identifiers for the members. So if we scroll down to the bottom of the file and we look at:
GRID_STAT_OUTPUT_PREFIX = FV3_core {instance} 
prefix and
FCST_GRID_STAT_INPUT_TEMPLATE = {init?fmt=%y%m%d%h}/core_{instance}/core_{instance}_{init?fmt=%y%m%d}_{init?fmt=%h%m}_f{lead?fmt=%HH}.nc
We see the word {instance} in both of these variables. This value is set to the Ensemble Member in parenthesis in the process list when METplus is run and it's how it points to the different members.

 Next let's check our paths to the input data. To do this we need to know the value of INPUT_BASE as it is given in 
FCST_GRID_STAT_INPUT_DIR and
OBS_GRID_STAT_INPUT_DIR
So we'll go to another terminal and pull up Tutorial_system.conf 
(* Type Open new terminal window *)
(* Type cd METplus *)
(* Type vim Tutorial_system.conf *)

INPUT_BASE is set to the following path that's listed here. So we can combine that with the rest of the FCST_GRID_STAT_INPUT_DIR
to check for files. Here we see that there are two date directories and a polygon for verification. If we go back and then look at FCST_GRID_STAT_INPUT_TEMPLATE, we see that the model date is given as year, month, day, and hour. Which is the first template seen here. Inside this directory we will see that there are four Ensemble members. But only two will be run for the use case. 

So let's check the first Ensemble member and see if we’ve got files.
(* Type ls /d1/projects/METplus/METplus_Data/model_applications/convection_allowing_models/brightness_temperature/2019052100/core_lsm1 *)
 Here we see that there are two files. One for the 1 hour for the forecast lead time and another for the 2 hour forecast lead time, which is as we would expect. 

So next we will go ahead and check the observed input files. OBS_GRID_STAT_INPUT_DIR  is the same as FCST_GRID_STAT_INPUT_DIR.  So we will copy/paste.
(* Type /d1/projects/METplus/METplus_Data/model_applications/convection_allowing_models/brightness_temperature *)

However in this case, the observed input template is given as year_month_day_141. 
(* Type 2019_05_211_141 *)
So that's the second directory listed here. Inside this directory we see that there are two GOES files. 
one for the UTC valid time and another for the two UTC valid time. 

Next let's check our input variables to be sure that we have them correctly specified in the configuration file. First looking at the model data, we will open a model file.
(* Type ncdump /d1/projects/METplus/METplus_Data/model_applications/convection_allowing_models/brightness_temperature/2019052100/core_lsm1/core_lsm1_20190521_0000_f01.nc | more *)

The variable that we have specified in our configuration file is called SBTA1613_topofatmosphere and the level is set to 2 asterisks inside parentheses. “(*,*)” which indicates the variable is in two dimensions. We scroll through our input file. We see that the variable name, SBTA1613_topofatmosphere(lat, long), is listed here and it's in two dimensions. So our model variable is specified correctly. 

Next we will check the observed variable. I scroll up so that I can get the directory as we listed previously. 
(* Type ncdump /d1/projects/METplus/METplus_Data/model_applications/convection_allowing_models/brightness_temperature/2019_05_21_141/remap_GOES-16.20190521.010000.nc | more *)

Looking at the configuration file The observed variable is called channel_13_brightness_temperature(lat, lon) and it's also in two dimensions.  Scrolling down through the file here we see channel_13_brightness_temperature(lat, lon) and it's in two dimensions in our OBS_INPUT file ??? Additionally, in this case we’re using a threshold of 235 Kelvin to create the distance maps.
(le235) 

And, finally, to get distance map output from GRID_STAT we have to set the GRID_STAT_OUTPUT_FLAG_DMAP in our configuration file. It can be set to either STAT or BOTH. Here we have it sent to BOTH which will produce two output files.  A .stat file and a .txt file. 
(GRID_STAT_OUTPUT_FLAG_DMAP = BOTH)

So now we're ready to start the Use Case. We start by calling the script run_metplus.py which is in the ush/ directory. Followed by -c and then our Use Case specific configuration file, followed by a -c and then our tutorial or system configuration file.
(* Type ush/run_metplus.py -c param/use_cases/model_applications/convection_allowing_models/GirdStat_fcstFV3_obsGOES_BrightnessTempDmap.conf -c Tutorial_system.conf *)

So here the use case is running. It will go through four calls to GRID_STAT. One for each of the two forecast lead times and Ensemble members. And the METplus run has now finished successfully! So let's take a look at the output to be sure that we have what is expected. We will first go back to the Use Case documentation.
https://metplus.readthedocs.io/en/develop/generated/model_applications/convection_allowing_models/GridStat_fcstFV3_obsGOES_BrightnessTempDmap.html#expected-output

 Scrolling down to the expected output, we can see that the expected output is 12 files. The first six are for the core_lsm1 Ensemble member and the second six are for the core_mp1 Ensemble member. Each member contains two valid times, 01 UTC and 02 UTC valid on May 21st 2019. There are three files for each Ensemble member in valid time, the file ending in dmap.txt and .stat contain the distance map output line. We have two files here because we set the dmap flag to BOTH. The file with pairs.nc. at the end contains Gridded output including the distance map.

So if we go back to our METplus run, we can first take a look at the log output to find our output directory.
(* Type vim /d1/personal/CHANGE_TO_YOUR_DIRECTORY/METplus/logs/metplus_log_20220309104212 *)

 When we scroll down the output directory is listed here after the -outdir flag in our GRID_STAT call.
(* Type ls /d1/personal/CHANGE_TO_YOUR_DIRECTORY/METplus/convection_allowing_models/brightness_temperature/grid_stat *)

 Looking inside this directory we see that we have all 12 expected files. Finally, we can make a distance map image by using the plot data plane tool in MET. So first we need to take a look at the pairs.nc file so that we can get the name of the variable we want to apply for our distance map. 
(* Type ncdump /d1/personal/CHANGE_TO_YOUR_DIRECTORY/METplus/convection_allowing_models/brightness_temperature/grid_stat/grid_stat_FV3_core_lsm1_010000L_20190521_010000V.pairs.nc | more *)

 The OBS_DMAP_le235_channel_13_brightness_temperature_all_all_FULL(* Type lat, lon) variable is specified here and it's in two dimensions. Exiting out of this file
(* Type ???exit out *)

We can now call plot_data_plane, using plot_data_plane. And then we specify the input file name and then secondly the name of the output PostScript file we want which I'm going to call: distance_map.ps .  And then the variable we want to plot is specified using the following string, by calling it 
‘name=”OBS_DMAP_le235_channel_13_brightness_temperature_all_all_FULL; level=”(*,*)”;’

(* Type plot_data_plane /d1/personal/CHANGE_TO_YOUR_DIRECTORY/METplus/convection_allowing_models/brightness_temperature/grid_stat/grid_stat_FV3_core_lsm1_010000L_20190521_010000V.pairs.nc distance_map.ps ‘name=”OBS_DMAP_le235_channel_13_brightness_temperature_all_all_FULL; level=”(*,*)”;’  *)


So plot_data_plane has finished successfully. The output image looks as follows. 
??? Insert image

If we compare this to the distance map image in the use case documentation we will see that they match. So our METplus run has completed successfully! 

This concludes the tutorial on the Brightness Temperature Distance Map Use Case. Thank you for watching.

