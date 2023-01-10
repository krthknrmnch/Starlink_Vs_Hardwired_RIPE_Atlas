#!/bin/bash
# Write csv header for new file
echo "URL,Provider,Continent,Country,City,Latitude,Longitude" >> step_1_output_Filtered_Live_Hosts.csv
while IFS= read -r line; do
	# Extract URL
    url=`echo "$line" | sed 's/,/\n/g' | head -n 1`
	echo $url
	# Ping URL to check if it is live
	ping -c 1 $url
	result=$?
	# If live, add to new file
	if [[ $result -eq 0 ]] ; then
		echo "Success"
		echo $line >> step_1_output_Filtered_Live_Hosts.csv
	fi
done < "$1"