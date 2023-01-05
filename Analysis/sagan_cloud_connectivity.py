import array as arr
import json
import requests
from ripe.atlas.sagan import Result
from ripe.atlas.sagan import TracerouteResult

#total_probes_combined = 93

#1.CloudConnectivity-LatencyPerformance
starlink_probes_ids_na = arr.array('i', [28,10743,12426,19648,22802,23127,35042,50017,52422,53798,54330,55492,60234,61081,61365,61731,61780,61899,62365,62741,62868,1001040,1004232,1004482])
starlink_probes_ids_oc = arr.array('i', [19983,1004453])

hardwired_probes_ids_na = arr.array('i', [12108,55591,10540,34156,31492,55752,54251,32316,52422,55524,17423,15039,55209,61899,19172,52601,1003572,22802,11795,1004250,51636,52440,61565,13109,10969])
hardwired_probes_ids_oc = arr.array('i', [30236,52142,54484,62515])

#1.1 NA_US - us-central.azure.cloudharmony.net
total_starlink_na_rtt_average = float(0)
total_hardwired_na_rtt_average = float(0)

result_file = "./result_1_na_us_azure.txt"
with open(result_file) as results:
    for result in results.readlines():
        parsed_result = Result.get(result)
        if (int(parsed_result.probe_id or 0)) in starlink_probes_ids_na:
            total_starlink_na_rtt_average = total_starlink_na_rtt_average + float(parsed_result.rtt_average or 0)
        elif (int(parsed_result.probe_id or 0)) in hardwired_probes_ids_na:
            total_hardwired_na_rtt_average = total_hardwired_na_rtt_average + float(parsed_result.rtt_average or 0)

#Averaged NA Starlink RTT Avg
print("Average NA Starlink RTT Avg is:")
print(total_starlink_na_rtt_average/len(starlink_probes_ids_na))

#Averaged NA Hardwired RTT Avg
print("Average NA Hardwired RTT Avg is:")
print(total_hardwired_na_rtt_average/len(hardwired_probes_ids_na))

#Overall NA Starlink RTT Min was observed to be 42.084
print("Overall NA Starlink RTT Min is:")
print("42.084")

#Overall NA Hardwired RTT Min was observed to be 18.314
print("Overall NA Hardwired RTT Min is:")
print("18.314")

#1.2 OC_AU - australia-southeast1.gce.cloudharmony.net
total_starlink_oc_rtt_average = float(0)
total_hardwired_oc_rtt_average = float(0)

result_file = "./result_2_oc_au_gce.txt"
with open(result_file) as results:
    for result in results.readlines():
        parsed_result = Result.get(result)
        if (int(parsed_result.probe_id or 0)) in starlink_probes_ids_oc:
            total_starlink_oc_rtt_average = total_starlink_oc_rtt_average + float(parsed_result.rtt_average or 0)
        elif (int(parsed_result.probe_id or 0)) in hardwired_probes_ids_oc:
            total_hardwired_oc_rtt_average = total_hardwired_oc_rtt_average + float(parsed_result.rtt_average or 0)

#Averaged OC Starlink RTT Avg
print("Average OC Starlink RTT Avg is:")
print(total_starlink_oc_rtt_average/len(starlink_probes_ids_oc))

#Averaged OC Hardwired RTT Avg
print("Average OC Hardwired RTT Avg is:")
print(total_hardwired_oc_rtt_average/len(hardwired_probes_ids_oc))

#Overall OC Starlink RTT Min was observed to be 48.885
print("Overall OC Starlink RTT Min is:")
print("48.885")

#Overall OC Hardwired RTT Min was observed to be 4.973
print("Overall OC Hardwired RTT Min is:")
print("4.973")


#2.CloudConnectivity-PathlengthPerformance
starlink_probes_ids_de = arr.array('i', [50008,52676,60323,1002289,1002750])
starlink_probes_ids_au = arr.array('i', [19983,1004453])
                                   
hardwired_probes_ids_de = arr.array('i', [10678,24174,27280,50771])
hardwired_probes_ids_au = arr.array('i', [52142,54484,62515])
                                    
#2.1 EU_DE - eu-central-1.ec2.cloudharmony.net
total_starlink_de_hops = int(0)
total_hardwired_de_hops = int(0)

result_file = "./result_3_eu_de_ec2.txt"
with open(result_file) as results:
    for result in results.readlines():
        parsed_result = TracerouteResult.get(result)
        if (int(parsed_result.probe_id or 0)) in starlink_probes_ids_de:
            total_starlink_de_hops = total_starlink_de_hops + int(parsed_result.total_hops or 0)
        elif (int(parsed_result.probe_id or 0)) in hardwired_probes_ids_de:
            total_hardwired_de_hops = total_hardwired_de_hops + int(parsed_result.total_hops or 0)

#Averaged DE Starlink Total Hops
print("Average DE Starlink Total Hops is:")
print(total_starlink_de_hops/len(starlink_probes_ids_de))

#Averaged DE Hardwired Total Hops
print("Average DE Hardwired Total Hops:")
print(total_hardwired_de_hops/len(hardwired_probes_ids_de))

#2.2 OC_AU - australia-southeast1.gce.cloudharmony.net
total_starlink_au_hops = int(0)
total_hardwired_au_hops = int(0)

result_file = "./result_4_oc_au_gce.txt"
with open(result_file) as results:
    for result in results.readlines():
        parsed_result = TracerouteResult.get(result)
        if (int(parsed_result.probe_id or 0)) in starlink_probes_ids_au:
            total_starlink_au_hops = total_starlink_au_hops + int(parsed_result.total_hops or 0)
        elif (int(parsed_result.probe_id or 0)) in hardwired_probes_ids_au:
            total_hardwired_au_hops = total_hardwired_au_hops + int(parsed_result.total_hops or 0)

#Averaged AU Starlink Total Hops
print("Average AU Starlink Total Hops is:")
print(total_starlink_au_hops/len(starlink_probes_ids_au))

#Averaged AU Hardwired Total Hops
print("Average AU Hardwired Total Hops:")
print(total_hardwired_au_hops/len(hardwired_probes_ids_au))
