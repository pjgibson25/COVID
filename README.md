# COVID19_timeseries_bycounty
Limited to United States counties afflicted by COVID.  Updated every day approximately 9:00am EST.


### The Purpose
Many sources have done extrodinarily well to track the spread of coronavirus amidst this pandemic.
One data gap that I have noticed is a database that tracks the spread of coronavirus through American counties over time.  

### The Background
John's Hopkins was able to capture this information but as far as I can tell, after March 9th, they switched to tracking data on a state-scale instead of on a county-scale.    Recently, the New York Times has published a daily update that indicates new statistics on COVID cases by county.  As far as I can tell, New York Times has yet to publish a cohesive dataset.  They only update the counts.

My goal is to use:
<ul>
<li>John's Hopkins Dataset for timestamps leading to March 9th.</li>
<li>New York Times Daily Updates for timestamps of March 24th moving forward.</li>
</ul>

### The Methodology
My methods are fairly straightforward.
<ol>
  <li>I will copy the John's Hopkins Dataset for dates leading up to March 9th.</li>
  <li>I will create a CSV file for data from each date starting from March 24th moving forward.  This will be captured from the New York Times: "Coronavirus in the U.S.: Latest Map and Case Count"</li>
  <ul>
    <li>Initially this will be copy/paste.
      I hope to change to using a python scraping method</li>
    <li>Beginning on March 25th, I will record a screenshot of the timestamp used when copying this daily update. </li>
  </ul>
</ol>

### Potential FAQs

<b>Question:  Why do we not have data for dates between March 9th and March 24th?</b>

Answer:  I began this project on March 24th and the only way to find county data (to my knowledge) is to ask county departments directly.  I believe that John's Hopkins University may have halted county data due to overwhelmed county health departments, but that is a personal conjecture.


<b>Question:  Why did you not begin with a webscraping method of capturing new data?</b>

Answer:  At first, I was only familiar with webscraping using Python's Selenium package.  Due to New York Time's solid security system, I was unable to use this due to the company's bot-protection security measures.  Smart.


<b>Question:  What happends when a county all of a sudden sprouts a new case?</b>

Answer:  I create a new data row and assume that all previous dates has a 0 case count.



<b>Question:  Is pjgibson25 single?</b>

Answer:  No, he's in a committed relationship.



## Sources:

John's Hopkins University Coronavirus database
https://github.com/CSSEGISandData/COVID-19/tree/master/csse_covid_19_data

The New York Times daily updates
https://www.nytimes.com/interactive/2020/us/coronavirus-us-cases.html

