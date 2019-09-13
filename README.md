# my-google-map-app
Naive Google Map Searcher

# Description
Python script to directly search for a place on Google Maps from the commandline itself. This project has been developed as an learning exercise. It makes use of the concepts of *system arguments*, *url encoding*, *date & time processing* and *handling web browser*

# USAGE : map_app.py _query_

where, query is the place you'd like to search on Google Maps

# WHAT DOES IT DO?

1. Processes your query and encodes it as documented at [1].

2. For encoding the url, we make use of built-in in urllib as mentioned here[2]

3. We then generate the url as mentioned at [1]

4. All queries made to the script are logged on to a log file in the following format - 

        now + " : \'"+query+"\'" + "\n\n

where, *now* is the current timestamp

5. Finally, the *webbrowser* module is then used to open the url generated in the default web browser above as documented at [3]

# References

[1] : https://developers.google.com/maps/documentation/urls/guide
[2] : https://www.urlencoder.io/python/
[3] : https://automatetheboringstuff.com/chapter11/
