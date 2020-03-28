# UPDATE:  
One day after publishing the<b> ALL_FIPS_datetime_cases.csv </b> file, New York Times released their more complete version of county data over time.  Please see the following link for their more robust data set:  https://github.com/nytimes/covid-19-data

##  Daily Updates no longer captured, see link above for data.
 
 
 # COVID19
Limited to United States counties afflicted by COVID.  Updated every day approximately 9:00am EST.


### Important Files
<b> ALL_FIPS_datetime_cases.csv </b> 
<ul> <li> nx3 data table with columns: FIPS, datetime, # of cases </li> </ul>
<b> Location_key.csv </b>
<ul> <li> 3232x7 data table with columns: FIPS, County, State, Country, Latitude, Longitude, Flag </li>
<li>  Flag indicates whether or not there has been a recorded data point.  1 indicates data present. 0 indicates no data.</li> </ul>

### Background
John's Hopkins University has case counts on a county level leading to March 9th, but not for following dates.
New York Times posts a live count of corona cases by county, but does not post previous data

By combining JHU data with the New York Times count that I scrape daily, I will log data on a county level over a time-series that is likely present somewhere but currently unaccessable.

### Methodology
<ul>
<li>  FIPS tags found online </li>
<li>  Latitude and Longitude calculated from averaging cencus tract coordinates within a county.  (converted to cartesian & averaged) </li>
<li>  Currently, NYT updates copy and pasted into CSV then analyzed in python </li>
<li>  Data points in NYT with unrecognizable locations dropped from dataset (ex: Unknown, Arkansas  -  Recorded in NYT update)  </li>
</ul> 


### Potential FAQs

<b>Question:  Why do we not have data for dates between March 9th and March 24th?</b>

Answer:  I began this project on March 24th and the only way to find county data (to my knowledge) is to ask county departments directly.  I believe that John's Hopkins University may have halted county data due to overwhelmed county health departments, but that is a personal conjecture.


## Sources:

John's Hopkins University Coronavirus database
https://github.com/CSSEGISandData/COVID-19/tree/master/csse_covid_19_data

The New York Times daily updates
https://www.nytimes.com/interactive/2020/us/coronavirus-us-cases.html

