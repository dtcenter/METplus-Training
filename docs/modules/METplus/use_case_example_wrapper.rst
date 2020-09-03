.. _metplus_example_wrapper:

Example METplus Wrapper
=======================

.. raw:: html

  <iframe width="560" height="315" src="https://www.youtube.com/embed/KCISG0phmbw" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

Developed for **METplus Version 3.1**.

(*Introduction*)

If you would like to follow along with the exercises in this video, please select one of the options to set up your own
:ref:`Training Environment <training_environment>`.

In this tutorial video I will show you how to set up the METplus wrappers to run the Example wrapper. The Example
wrapper does not run any of the MET applications, but it does demonstrate how some of the commonly used METplus
configuration variables are used. It is a good starting point to understand how the wrappers are used.

Review user configuration file
------------------------------

The video assumes that you have already installed the MET tools and configured the METplus wrappers correctly.
If you are following the online
tutorial, you likely already set up your environment by sourcing the tutorial setup scripts. If not, and you haven’t
already created a user or tutorial configuration file, you will have to do so before running the example.
The video titled "METplus Configuration" (link) covers what variables need to be set to get started.

This is the user configuration file I am using on Docker to run this example::

(*Show user.system.conf*)

Review config file
----------------

Show how config values correspond to log output from wrapper

The Example wrapper was designed to demonstrate how the METplus
time looping variables work and how they interact with the filename templates to find the files to process.

For more detail on how the time looping variables can be configured, please refer to the
:ref:`Common Configuration Variables <metplus_common_config_vars>` video.

AUDIO FROM SWPC Tutorial:

(*Pull up parm/use_cases/met_tool_wrapper/Example/Example.conf*)

process list where you can put all the processes you want to run comma-separated. So in this use case, it's only running the example wrapper here Lou Pai valid. Can you can also set it to Loop by an it? If it's set to loop. I valid you'll need to set all of the valid corresponding valid configurations the time format just

ermine's the format of your valid begin invalid and values. So here is your month day hour. This has to be your month day hour as well. Same thing for the bout and time. The valid increment is the increment that it will deal change from starting from the begin time until you get to your end time. And then the the the lead sequence is the list least list of forecast leads that you'll process for each run time. So here you can see it starts on.

February 1st, 2017 0 z and ends on February 2nd 2017 at 0 Z and it will increment every 6 hours.

Below here one. Another thing to note that many mentioned earlier is a stir section has an input directory. So example corresponds to this example rapper. It's and this is the directory path that you'd put to specify where all your data lives. And then in the filename template section, you'll also have a corresponding example input template and this is where you can use this file name template syntax to Define. How your

Our files are named based on the current runtime. So here you can see we reference the init time here in a few places and then the forecast lead these keywords are are important to set these values and they're also mentioned in the documentation of all the valid values you can choose and custom is a new feature that we've added. So if you add another configuration called example custom Loop list and have a list of strings for each run time and

And Lead at least forecast lead it will Loop over these values and substitute it in wherever you need to so you can you know run on multiple different data sets. You can run on different configuration files so on. So let's take a look at what it looks like when you run met plus SO2 to run the tool. You'll have to call Master met plus that's the main power script and if you have it in your path, you don't need to specify the full path to

That the script so if you if you see when we run it here without any configuration that will just give you a sort of usage statement of how to pass in configs and a help which displays this. So if you forget how to pass in your variables, that's how you do it for our sorry configurations. So here we'll pass in the example comp file. So in use cases Farm use cases met tool rapper example, and this use case is called example.com

So we'll run this and you'll see that we'll get an error pretty quickly. That's because we didn't set this output base or it's set to path to rather. So you really need to make sure that that everything is set correctly and but it will give you some helpful warnings if you don't have that set correctly. So here what we'll do is pass in another configuration file, which is going to be my user config file. So here that's in the cave dot eyewall.com, but I run that you get a whole bunch of output to the

Train if everything worked correctly, you'll see they'll very last line should say info met plus it's successfully finished. If not, it will tell you that there were some errors and lists which rappers contain those errors. So some useful information. You can see here at the end. It lists its final Kampf. So this is in your output base directory and this shows you all of the configurations that were used for this run. So,

So if you pass in five configuration files, this is actually what's used. So if you're having trouble where you're not sure why something is not being set correctly. You can see what's actually used for this run. So a lot of useful information there for rerunning and then also in this output directory is a log directory. You can change the location of that but by default it goes under your output base and a directory called logs and the most important one you want to look at here to start it.

This master met plus log and it has a timestamp of when you ran this. You can configure how much Precision you want to have in that file and that file name. So we'll go ahead and open this up you'll see it says met plus and the version was called with this command so you can see clearly what you brand for this run here. It's testing it ran met Plus at this valid time. And then all of this output is coming from the example rapper and it's really just looping over these time.

And then out putting some information to let you know what it's actually doing so you can see it's running for this salad time. It's using this input directory that was set by your example input there. It's using this template example input template and then it's looping over these custom strings to run. So for the first forecast lead three hours, it'll tell you the initialization and valid time that it was running and then it says it's looking into the input directory for this file. So you can see that corresponds to this input template of it's sold in this

You know We're looping over valid time. It fills in the initialization time for these values those in the forecast lead with a three digit precision and it add this custom string so you can have it run over EXT or netcdf and then it will Loop to the next forecast lead and do the exact same thing. They'll just the initialization time and look for the same files.

And then after it's done with all the the processing of this forecast leads, it will increment to the next valid time and do the same thing over and over again. So this is a really good place to start if you want to kind of see how the changes to your time configurations affect your output. What I'm going to do here is I'm going to take this example.

Config file, and I'm going to copy it into my tutorial area so that I don't mess anything up in the in the actual depository, but can make some changes for my next run. So I'm going to copy that here. I'm going to name it example underscore demo.

Whoa, and then I'm going to open up that file and it's the same as your previous run right now, but I can change some of the time so I'll change it to R actually run one run time. The increment needs to be at least a minute. But if you have the same values begin and end it will just run once then I'll change this. I only want to run one two, three hour forecast lead. This is often what I do when I'm trying to test a new use case out is I'll set it up to run for one time and make sure that everything is lined.

Crackly, and then once I'm confident that everything works correctly, then I can adjust my time and run it for many use cases.

So here we'll just run over the Sensi file. So call this again Master met Plus.

pass in my

example demo config file and then I'll also pass in my user config file will run that again and you can see that output is much smaller this time, but only ran for this one time for the 3:00 hour forecast lead. It's looking for just this file. So that's a good way to get started with understanding how the configs and in that place work.

Now I'll show you a example of running an actual tool called grid stat. So going here.

Here, this is the Met tool rapper grid stat use case and the documentation minute went over all these sections previously, but you can take a look at the config file. We're going to run. So this time we're press the process list contains good stat only and this time We're looping by an it. So then you'll notice that all of these instead of saying valid time format valid begin end. They're all starting with in it.

The lead sequence just has the 12 if you don't specify units here is it seems that it's ours, but you can also specify other time intervals like months minutes years. So on and one thing to note here is the scripts that config file. That's the configuration the Met configuration file that's used and a lot of these configurations will set values in the Met config file using environment variables.

Can kind of take a look at this and see what things can be set and at the bottom here will show you which met plus configuration variables correspond to these. So there's a lot of good resources here. You can also look at this python rapper section for that tool and that gives you a list of all the configuration file variables that are relevant to that tool and then if you click on any of those it takes you to the glossary entry.

To to get a little more information about that. So there's a lot of good information on that page. So very quickly. I know we're running at a time, but I will run just use case if that comps and then I'll pass in my tutorial config.

This is a lot more output.

And here it says that it is processing the 12-hour forecast lead. Here's the command that it built but you can see there's not a whole lot of information of what actually was done. So what I would like to do is at change the debugging levels,

so in this config even add under the config section log level by default is info you can set it to bug where I'm getting those that information from if you look in the repository under par met plus config. These default values have all the the possible things that you can change for these type of configurations. So in this met plus logging file, you can see all these things you can change and and a little

Scripture on what they would do. Another thing. I'll take here is this log met output to met plus and I'll set that to well. I'll set that and no or false you can use either one. So what this does is it'll take the output from grids that instead of dumping it to the same Master met plus log file. It'll put it in its own log file two separate things out so

we will run this use case again and you can see there's a lot more output that came out some of these debug messages say it's which files looking for for the forecast and up. So if you're if you have some errors, you're not sure why it's not working bump up the level to debug and you can see what it's actually trying to find and and you make adjustments from there and then here it also lists all the environment variables that are set automatically and passed into the Met config file and we list them all here nice readable.

Form and then here if you see this copy bull environment for the next command you can take that line and copy it and paste it into your terminal and then the next line is the actual commands. You can paste that in and recreate the command and kind of debug further from there.

