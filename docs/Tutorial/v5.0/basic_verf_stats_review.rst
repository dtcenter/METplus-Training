Basic Verification Statistics Review
====================================

**Introduction**

This session is meant as a brief introduction (or review) of basic statistical verification 
methods applied for various classifications of meteorological variables, and to guide new users 
toward their usage within the METplus system. It is by no means a comprehensive review 
of all of the available statistical verification methods available in the atmospheric 
sciences, nor every single verification method available within the METplus system. 
More complete details on many of the techniques discussed here can be found in Wilks’ 
“Statistical Methods In The Atmospheric Sciences” (2019), Jolliffe and 
Stephenson’s “Forecast Verification; A Practitioner's Guide in Atmospheric Science” (2012) and the 
`forecast verification web page <https://www.cawcr.gov.au/projects/verification/>`_
hosted by Australia’s Bureau of Meteorology.  Upon completion of this session you will have 
a better understanding of five of the common classification groupings for 
meteorological verification and have access to generalized METplus examples of creating 
statistics from those categories.

Attributes of Forecast Quality
------------------------------

Forecast quality attributes are the basic characteristics of forecast quality that 
are of importance to a user and can be assessed through verification. Different 
forecast evaluation approaches will measure different attributes of the quality 
of the forecasts. Some verification statistics can be decomposed into several attributes, 
providing more nuance to the quality information. It can be commonplace in operational 
and research settings to find and settle on one or two of these complex statistics that 
can provide meaningful guidance for adjustments to the model being evaluated. For example, 
if a given verification statistic shows that a model has a high bias and low reliability, 
that can seem to provide a researcher with all they need to know to make the next 
iteration of the model perform better, having no need for any other statistical input. 
However, this is an example of the law of the instrument: 
“If the only tool you have is a hammer, you tend to see every problem as a nail”. 
More complete, meaningful verification requires examining forecast performance from 
multiple perspectives and applying a variety of statistical approaches that measure a 
variety of verification attributes.

In most cases, one or two forecast verification attributes will not provide enough 
information to understand the quality of a forecast. In the previous example where 
one verification statistic showed a model had high bias and low reliability, it could 
have been a situation where a second verification measure would have shown that the 
accuracy and resolution of the model were good, and making the adjustments to the next 
model iteration to correct bias and reliability would degrade accuracy and resolution. 
To fully grasp how well a particular forecast is performing, it is important to select 
the right combination of statistics that give you the “full picture” of the forecasts’ 
performance, which may consist of a more complete set of attributes, measuring the 
overall quality of your set of forecasts.

The following forecast attribute list is taken from Wilks (2019) and summarized for 
your convenience. Note how statistics showing one of these attributes on their own 
will not tell you exactly how “good” a forecast is, but combined with statistics 
showcasing other attributes you can have a better understanding of the utility of the forecast.

* Accuracy – The level of difference (or agreement) between the individual values of a 
  forecast dataset and the individual values of the observation dataset. This should 
  not be confused with the informal usage of “accurate”, which is often used by the 
  general population to describe a forecast that has high quality.
* Skill – The accuracy of a forecast relative to a reference forecast. The reference 
  forecast can be a single or group of forecasts that are compared against, with common 
  choices being climatological values, persistence forecasts 
  (forecasts that do not change over time), and older numerical model versions.
* Bias – The similarity between the mean forecast and mean observation. 
  Note that this differs slightly from the accuracy attribute, which measures the 
  individual value’s similarity.
* Reliability – The agreement between conditional forecast values and the distribution 
  of the observation values resulting from that condition. Another way to think of reliability 
  is as a measure of all of the observational value distributions that could happen given a forecast value. 
* Resolution – In a similar thought as reliability, resolution is the measure of the 
  forecast’s ability to resolve different observational distributions given a change in 
  the forecast value. Simply put, if value X is forecast, what level of difference is there 
  in the resulting observation distributions than a forecast of value Y.
* Discrimination – A simpler definition could be considered the inverse of resolution: 
  discrimination is the measure of a forecast’s distribution given a change in the observation 
  value. For example, if a forecast is just as likely to predict a tornado regardless of the 
  actual observation of a tornado occurring, that forecast would have a low discrimination ability for tornadoes.
* Sharpness – This property pertains only to the forecast with no consideration of its 
  observational pair. If the forecast does not deviate from a consistent  (e.g., climatological) 
  distribution, and instead sticks close to a “climatological value”, it exhibits low 
  sharpness. If the forecast has the ability to produce values different from climatology that change the distribution, then it 
  demonstrates sharpness.

Binary Categorical Forecasts
----------------------------

The first group of verification types to consider is one of the more basic, 
but most often used. Binary categorical forecast verification seeks to 
answer the question “did the event happen”. Some variables (e.g., rain/no rain) 
are by definition binary categorical, but every type of meteorological 
variable can be evaluated in the context of a binary forecast 
(e.g., by applying a threshold): Will the temperature exceed 86 degrees 
Fahrenheit? Will wind speeds exceed 15 knots? These are just some examples 
where the observations fall into one of only two categories, yes or no, 
which are created by the two categories of the forecast 
(e.g. the temperature will exceed 86 degrees Fahrenheit, 
or it will stay at or below 86 degrees Fahrenheit).

Imagine a simplified scenario where the forecast calls for rain.

A *hit* occurs when a forecast predicts a rain event and the observation 
shows that the event occurred. In the scenario, a *hit* would be counted 
if rain was observed. A *false alarm* would be counted when the forecast 
predicted an event, but the event did not occur (i.e., in the scenario, 
this would mean no rain was observed). As you may have figured out, there 
are two other possible scenarios to cover for when the forecast says 
an event will not occur.

To describe these, imagine a second scenario where the forecast says 
there will be no rain.

*Misses* count the occasions when the forecast does not predict the event to 
occur, but it is observed. In this new scenario, a *miss* would be counted 
if rain was observed. Finally, *correct rejections* are those times that a 
forecast says the event will not occur, and observations show this to be true. 
Thus, in the rainfall scenario a correct rejection would be counted if no 
rain was forecasted *and* no rain was observed.

Because forecast verification is rarely performed on one event, a 
contingency table can be utilized to quickly convey the results of multiple 
events that all used the same binary event conditions. An example 
contingency table is shown here:

.. list-table:: Example Contingency Table
  :widths: auto

  * -  
    - **Observation "Yes"**
    - **Observation "No"**
  * - **Forecast "Yes"**
    - Hits
    - False Alarms
  * - **Forecast "No"**
    - Misses
    - Correct Rejections

Each of the paired categorical forecasts and observations can be assigned to 
one of the four categories of the contingency table. The statistics that are 
used to describe the categorical forecasts’ scalar attributes 
(accuracy, bias, reliability, etc.) are computed using the total 
counts in these categories.

It is important not to forget the total number of occurrences 
and non-occurrences, *n*, 
that are contained in all four categories. If *n* is too small, it can 
be easy to arrive at a misleading conclusion. For example, if a forecaster 
claims 100% accuracy in their rain forecast and produces a contingency table 
where the forecast values were all hits but *n* = 4, the conclusion is technically 
correct, but not very scientifically sound!

Verification Statistics for Binary Categorical Forecasts
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Most meteorological forecasts would be described as non-probabilistic, meaning 
the forecast value given is provided with no additional information of certainty 
in that value. Another term for this type of forecast is deterministic and will 
be the focus of the verification statistics in this section. For more information 
on probabilistic forecasts and their corresponding statistics please refer to 
the probabilistic section. When verifying binary categorical forecasts, the 
only important factor is whether or not the event occurred: The assumed certainty 
in the forecast is 100%.

Numerous computationally-easy (and very popular) scalar statistics are within 
reach without too much manipulation of a contingency table’s counts.

**ACCURACY (ACC)**
The scalar attribute of Accuracy is measured as a simple ratio between the 
forecasts that correctly predicted the event and the total number of occurrences 
and non-occurrences, n. In equation format,


.. math:: \text{Accuracy } = \frac{{Hits} + {Correct\ Rejections}}{n}

This measure (often called “Percent Correct”) is very easily computed and addresses 
how often a forecast is correctly predicting an event and non-event. As most 
verification resources will warn you, however, this measure should be used with 
caution, especially for an event that happens only rarely. The Finley tornado 
forecast study (1884) is an excellent example of the need for caution, with 
Finley reporting a 96.6% Accuracy for predicting a tornado due to the overwhelming 
count of correct negatives. Peers were quick to point out that a higher 
Accuracy (98.2%) could have been achieved with a persistence forecast of No Tornado! 
:ref:`See how to use this statistic in METplus <METplus-solutions_bin_cat_for_verif>`!

**PROBABILITY OF DETECTION (POD)**

Probability of Detection (POD), also referred to as the Hit Rate, measures the 
frequency that the forecasts were correct given that the forecast predicts an 
occurrence. Rather than computing the ratio of the correct forecasts to the entire 
occurrence and non-occurrence count (i.e., as in Accuracy), POD only focuses on the 
times the forecast predicted an event would occur. Thus, this measure is categorized 
as a discrimination statistic. POD is computed as

.. math:: \text{POD} = \frac{Hits} {{Hits} + {Misses}}

This measure is useful for rare events (tornadoes, 100-year floods, etc.) as it 
will penalize (i.e. go toward 0) the forecasts when there are too many missed 
forecasts. 
:ref:`See how to use this statistic in METplus <METplus-solutions_bin_cat_for_verif>`!

**PROBABILITY OF FALSE DETECTION (POFD)**

A countermeasure to POD is the probability of false detection (POFD). 
POFD (also called false alarm rate), measures the frequency of false alarm 
forecasts relative to the frequency that an event does not occur.

.. math:: \text{POFD} = \frac{False\ Alarms} {{Correct\ Rejections} + {False\ Alarms}}

Together, POD and POFD measure forecasts’ ability to discriminate between 
occurrences and non-occurrences of the event of interest. 
:ref:`See how to use this statistic in METplus <METplus-solutions_bin_cat_for_verif>`!

**FREQUENCY BIAS (BIAS)**

Frequency bias (a measure of, you guessed it, bias!) compares the count of “yes” 
forecasts to the count of “yes” events observed.

.. math:: \text{Bias} = \frac{{Hits} + {False\ Alarms}} {{Hits} + {Misses}}

This ratio does not provide specific information about the performance of individual 
forecasts, but rather is a measure of over- or under-forecasting of the event. 
:ref:`See how to use this statistic in METplus <METplus-solutions_bin_cat_for_verif>`!


**FALSE ALARM RATIO (FAR)**

The False Alarm Ratio (FAR) provides information about both the reliability and 
resolution attributes of forecasts. It computes the ratio of “yes” forecasts 
that did not occur to the total number of times a “yes” forecast was made 
(i.e., the proportion of “yes” forecasts that were incorrect).

.. math:: \text{FAR} = \frac{{False\ Alarms} {{Hits} + {False\ Alarms}}

FAR also is the first statistic covered in this session that has a negative 
orientation: A FAR of 0 is desirable, while a FAR of 1 shows the worst possible 
ratio of “yes” forecasts that were not observed relative to total “yes” forecasts. 
:ref:`See how to use this statistic in METplus <METplus-solutions_bin_cat_for_verif>`!

**CRITICAL SUCCESS INDEX (CSI)**

The Critical Success Index (CSI), also commonly known as the Threat Score, i
s a second measure of the overall accuracy of forecasts 
(e.g., like the Accuracy measure mentioned earlier). Accuracy pertains to the 
agreement of individual forecast-observation pairs, and CSI can be calculated as

.. math:: \text{CSI} = \frac{{Hits} {{Hits} + {Misses} + {False\ Alarms}}

Note that by definition CSI can be described as the ratio between the times the 
forecast correctly called for an event and the total times the forecast called 
for an event or the event was observed. Thus, CSI ignores correct negatives, 
which differentiates it from percent correct. A CSI of 1 indicates a highly 
accurate forecast, while a value of 0 indicates no accuracy. 
:ref:`See how to use this statistic in METplus <METplus-solutions_bin_cat_for_verif>`!

Binary Categorical Skill Scores
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**HEIDKE SKILL SCORE (HSS)**

**HANSSEN-KUIPERS DISCRIMINANT (HK)**

**GILBERT SKILL SCORE (GSS)**

.. _METplus-solutions_bin_cat_for_verif:

METplus Solutions for Binary Categorical Forecast Verification
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**MET SOLUTIONS**

**METPLUS WRAPPER SOLUTIONS**


METplus Examples of Binary Categorical Forecast Verification
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**MET Example of Binary Categorical Forecast Verification**

**METplus Wrapper Example of Binary Categorical Forecast Verification**


Multicategorical Forecasts
--------------------------

Verification Statistics for Multicategorical Forecasts
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Multicategorical Skill Scores
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**HEIDKE SKILL SCORE (HSS)**

**HANSSEN-KUIPERS DISCRIMINANT (HK)**

**GERRITY SKILL SCORE**

METplus Solutions for Multicategorical Forecast Verification
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**MET SOLUTIONS**

**METPLUS WRAPPER SOLUTIONS**


METplus Examples for Multicategorical Forecast Verification
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**MET Example of Multicategorical Forecast Verification**

**METplus Wrapper Example of Multicategorical Forecast Verification**

Continuous Forecasts
--------------------

Verification Statistics for Continuous Forecasts
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**MEAN ERRORS**

**STANDARD DEVIATIONS**

**MULTIPLICATIVE BIAS**

**CORRELATION COEFFICIENTS (PEARSON, SPEARMAN RANK, AND KENDALL'S TAU)**

**ANOMALY CORRELATION**

METplus Solutions for Continuous Forecast Verification
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**MET SOLUTIONS**

**METPLUS WRAPPER SOLUTIONS**


METplus Examples for Continuous Forecast Verification
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**MET EXAMPLE OF CONTINUOUS FORECAST VERIFICATION**

**METPLUS WRAPPER EXAMPLE OF CONTINUOUS FORECAST VERIFICATION**

Probabilistic Forecasts
-----------------------

Verification Statistics for Probabilistic Forecasts
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**BRIER SCORE**

**RANKED PROBABILITY SCORE**

**CONTINUOS RANKED PROBABILITY SCORE**

Probabilistic Skill Scores
^^^^^^^^^^^^^^^^^^^^^^^^^^

**BRIER SCORE**

**RANKED PROBABILITY SKILL SCORE**


METplus Solutions for Probabilistic Forecast Verification
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**MET SOLUTIONS**

**METPLUS WRAPPER SOLUTIONS**


METplus Examples for Probabilistic Forecast Verification
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**MET EXAMPLE OF PROBABILISTIC FORECAST VERIFICATION**

**METPLUS WRAPPER EXAMPLE OF PROBABILISTIC FORECAST VERIFICATION**

