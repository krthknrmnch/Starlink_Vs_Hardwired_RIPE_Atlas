#!/bin/bash
# Write csv header for new file
echo "URL,Provider,Continent,Country,City,Latitude,Longitude,IP" >> step_3_output_List_of_IPs.csv
while IFS= read -r line; do
	# Extract URL
    url=`echo "$line" | sed 's/,/\n/g' | head -n 1`
	echo -n $line >> step_3_output_List_of_IPs.csv
	echo -n "," >> step_3_output_List_of_IPs.csv
	# Resolve IP and add to file
	nslookup "$url" | grep -Po 'Address:\s*[0-9.]+' | tail -1 | sed -e 's/Address:\s*//g' >> step_3_output_List_of_IPs.csv
done < "$1"