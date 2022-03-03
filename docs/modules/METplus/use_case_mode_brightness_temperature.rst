.. _metplus_use_case_mode_brightness_temperature:

Use Case: MODE Brightness Temperature Verification
==================================================

.. raw:: html

  <iframe width="560" height="315" src="https://www.youtube.com/embed/IW3ZwcVRkL8" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

Developed for **METplus Version 4.0**.

(*Setup: Open 2 terminals*)

(*Setup: Open URL: https://metplus.readthedocs.io/en/main_v4.0/Users_Guide/index.html*)

(*Setup: Open URL: https://met.readthedocs.io/en/latest/*)


(*Introduction*)

If you would like to follow along with the exercises in this video, please select one of the options to set up your own
:ref:`Training Environment <training_environment>`.

(*Show Title Slide*)

My name is Christina Kalb and I'm a scientist working on the METplus team at NCAR.  This video will cover how to run the MODE Brightness Temperature use case.  
Specific information about this use case can be found in the METplus user's guide.

(*Open https://metplus.readthedocs.io/en/main_v4.0/Users_Guide/index.html, Click on User's Guide*)

Go to section five, METplus Use Cases, Model Applications, Convection Allowing Models, and click on MODE: Brightness Temperature Verification.

(*Click through METplus Use cases, Model Applications, Convection Allowing Models, MODE: Brightness Temperature Verification, scroll down to METplus workflow*)

Looking at the information, we see that this use case verifies FV3 ensemble members, compared to GOES satellite brightness temperature using MODE, 
the Method for Object based Diagnostic Evaluation.

(*Highlight FV3 Model member data and GOES Brightness Temperature, Scroll down*)

It is set up to run two ensemble members, one model initialization time, and two forecast lead times.

(*Highlight 2 ensemble members, Valid: 2019-05-21_01Z Forecast lead: 01 Valid: 2019-05-21_02Z*)

The METplus and MET configuration files are shown here in the documentation.

(*Scroll down through METplus and MET configuration files to Running METplus*)

If you want to learn more about MODE, go to the MET Tools users guide, and go to section seventeen, which is on the MODE Tool

(*Open https://met.readthedocs.io/en/latest/, Click on MODE Tool, Return to other browser tab*)

This video assumes that you have already installed MET tools and set up your environment for METplus.  Information on how to do this can be found in section 1 
and the installation and setup sections of the online tutorial topics.  Here we will be using the recommended setup, which is first passing in a use case specific 
configuration file followed by a second configuration file with settings that are specific to the system we are using.  

(*Highlight Passing in MODE_fcstFV3_obsGOES_BrightnessTemp.conf, user-specific system*)

So, let’s take a look at the use case and be sure that it is set up to be run.

(*Go to terminal*)

We will first go into the METplus repository.  

(*Type cd METplus, ls, Hightlight Tutorial_system.conf*)

Tutorial_system.conf is the system specific configuration file.  The use case specific configuration file is located
under parm, use_cases, model_applications, convection_allowing_models and it’s called MODE forecast FV3 obs GOES BrightnessTemp .conf.

(Type vim parm/use_cases/model_applications/convection_allowing_models, Highlight MODE_fcstFV3_obsGOES_BrightnessTemp.conf, paste 
MODE_fcstFV3_obsGOES_BrightnessTemp.conf, hit enter*)  

So, we will open this file and first check the directories for our input forecast and observation data.

(*Go to bottom of file, highlight FCST_MODE_INPUT_DIR = {INPUT_BASE}/model_applications/convection_allowing_models/brightness_temperature, # Directory of the 
GOES obs OBS_MODE_INPUT_DIR = {INPUT_BASE}/model_applications/convection_allowing_models/brightness_temperature*)

To do this, we will need to know the value of INPUT_BASE which is listed in the system specific configuration file.  So, we will pull up the system specific 
configuration file to check the value.

INPUT_BASE is set to the following path, listed here.  So, we can combine that with the rest of the FCST_MODE_INPUT_DIR to see if our data is available.  

Here we see that there are two date directories and a polygon for verification.  Looking at the MODE input template, we see the model date is give and year, month, 
day and hour.  So, that’s the first template seen here.  In this directory there are actually four ensemble members, but we’ll only be running two for the use case.  
So, lets check the first member and be sure there are files here.  In this directory, we see that there are two files, one for the one-hour lead time, and the second 
for the two-hour lead time.  This is as expected.  

So next, we’ll check the observation input files.  The OBS_MODE_INPUT_DIR is the same as the FCST_MODE_INPUT_DIR.  So, we can copy/paste here.  However, the date template 
in this case is given as year underscore, month underscore, day underscore, one-forty-one.  So, checking that directory, we see that there are two GOES files, one for 
the one-hour valid time and another for the two-hour valid time.  Next, we can go in and create an output directory for our output data as specified by the MODE_OUTPUT_DIR.  
We will first need to check Tutorial system .conf to get the value of output base.   Output base is located in this directory, and we will go ahead and make the directory as
specified in MODE_OUTPUT_DIR. So, our empty directory has now been created.

Now, lets check our input variables to be sure we have them correctly specified.  So first looking at the model data, we can open the first file or the one-hour lead time 
file.  If we look at our configuration file, our forecast variable name is set to SBTA1613 top of atmosphere, and the level is set as two asterisks in parenthesis which 
indicates two dimensions.  So looking for this variable in our input file, we can see that here it is, and it is in two dimensions, so that’s correct.

Now we can check on the observation files.  Going back to our configuration file, our obs variable name is channel 13 brightness temperature and again, it’s in two dimensions.  
And there is channel thirteen brightness temperature in two dimensions in our obs input file.

Finally, let’s take a look at some of the configuration settings that we have for MODE in this use case.  Here we are using a temperature threshold of less than or equal to 
235 Kelvin, defined by the MODE convolution threshold.  The CENSOR_VAL and CENSOR_THRESH variables contain information about missing data, and the variables below those two 
values give information on how MODE identifies objects. 

So now it’s time to start the use case.  We will start by calling the script run_metplus.py which is in the ush directory, followed by minus c, and then our use case specific 
configuration file, followed by another minus c and our system configuration file.  The run has started successfully.  This use case takes some time to run, because the model 
is high resolution.

(ush/run_metplus.py -c parm/use_cases/model_applications/convection_allowing_models/MODE_fcstFV3_obsGOES_BrightnessTemp.conf -c system.conf)

(video cut while use case runs)

The METplus run has now finished successfully.  Let’s check the output to make sure we have what is expected.  First, we’ll go back to the use case documentation
(Open https://metplus.readthedocs.io/en/main_v4.0/Users_Guide/index.html)
Scrolling down to the expected output section, we can see that the expected output is 16 files.  The first 8 are for the core_lsm1 member and the second 8 are for the 
core_mp1 member.   Each member contains 2 valid times, 01 UTC and 02 UTC valid on May 21, 2019.  There are four files for each ensemble member and valid time.  The first, 
with the cts.txt at the end of the file name contains contingency table statistics for the objects.  The second with obj.nc at the end contains gridded data of the defined 
objects.  The third with obj.txt at the end, contains the object attributes and matched pair statistics, and the final is a postscript file which contains images of the 
output and objects.

So let’s take a look at our output to be sure we have all 16 files.  We can first open the log file and scroll down to check our output directory.  The output directory is 
given here.  So if we do an ls on that directory, we see that we have all expected sixteen files.

Now let’s go in and check the first image.  Here we can see many objects identified and the output looks as expected.  So our METplus run has completed successfully.  This 
concludes the tutorial on the MODE brightness temperature use case.  Thank you for watching.
