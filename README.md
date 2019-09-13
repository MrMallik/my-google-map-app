# my-google-map-app
Naive Google Map Searcher

# USAGE : map_app.py _query_

where, query is the place you'd like to search on Google Maps

# WHAT DOES IT DO?

1. Processes your query and encodes it as documented here(https://developers.google.com/maps/documentation/urls/guide).
2. For encoding the url, we make use of built-in in urllib as mentioned here(https://www.urlencoder.io/python/)
3. Finally, all queries made to the script are logged on to a log file in the following format - 

(now + " : \'"+query+"\'" + "\n\n)

where, now is the current timestamp
