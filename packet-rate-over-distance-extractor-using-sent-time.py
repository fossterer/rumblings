"""
We are working at millisecond precision
"""

import sys
import time
import math

time_log_name = sys.argv[1]
receiver_log_name = sys.argv[2]
gps_log_name = sys.argv[3]
nogps_log_name = sys.argv[4]

out_file_name = 'results/packet_rate_and_distance_'+sys.argv[5]+'_using_sent_time'+'.csv'

time_log = open(time_log_name, 'r')
receiver_log_for_gps_data = open(receiver_log_name, 'r')
receiver_log_for_non_gps_data = open(receiver_log_name, 'r')
gps_log = open(gps_log_name, 'r')
nogps_log = open(nogps_log_name, 'r')

out_file = open(out_file_name, 'w')

PACKET_FIELD_SEPERATOR = ','
PACKET_SENTENCE_SEPERATOR = '**'
GPS_PACKET_MAC_AND_ID_SEPERATOR = '/'
distance_increment = 15
no_of_points_marked = 61 #initial point '0' included

# Fetch consecutive epoch times "time-1" and "time-2" from time-logs
#     Traverse the receiver log till timestamp is greater than "time-1"
#     From here, count the total no. of packets till the timestamp is greater than "time-2"             --- (1)
#     Calculate the difference between "time-1" and "time-2"                (in seconds)                --- (2)
#           Dividing (1) by (2) gives packet rate for that part of motion  (Expected:4 non-GPS + 2 GPS packets) 
#     While moving, update the 'distance'
#	   1-166(ascending) -- multiply line no. minus 1 by 3 for distance in ft. 		 167-332(descending)-- multiply 332 minus line no. by 3 for distance in ft.
#         ***CRITICAL COMMENT*** -- The change of 'location' might occur long before the 'tick of second' or just 'at the tick' -- can differ for each instance;
#                                   We ignore its effect as the vehicle was moving very slow by virtue of which the change in distance would be negligible

# At the end of each second, output -
#     distance, packet rate

distance = 0
line_no = 0

received_gps_packet_count = 0
received_nogps_packet_count = 0
received_packet_count = 0
gps_packet_count = 0
nogps_packet_count = 0

while True:
    line_no = line_no + 1
    time_1 = time_log.readline()
    time_2 = time_log.readline()

    if not time_1:
	break
    time_1 = float(time_1)
    time_2 = float(time_2)
    print 'time1, time2:' + str(time_1) + ', ' + str(time_2)

#For reading gps data from receiver logs
    while True:
        line = receiver_log.readline()
        word_list = line.split(PACKET_SENTENCE_SEPERATOR)
	received_time = word_list[1]

	if GPS_PACKET_MAC_AND_ID_SEPERATOR in line:
	    if 'T' in received_time:	#Need to convert timestamp into epoch
		pattern = '%Y-%m-%dT%H:%M:%S'
		received_time = float(time.mktime(time.strptime(received_time[:-5], pattern))) - 14400.0			# UTC -04:00
	        print 'converted GPS packet time:' + str(received_time)
	    else:
                received_time = float(word_list[1])
	        print 'direct GPS packet time:' + str(received_time)
	    received_time = received_time * 1000 	#GPS packets contain time in seconds

	if received_time < time_1:
	    continue
	if received_time > time_2:
	    break
	print 'The received GPS packet is: ' + line + '\n'
	received_gps_packet_count = received_gps_packet_count + 1
    print 'received_gps_packet_count: ' + str(received_gps_packet_count)

#For reading non-gps data from receiver logs
    while True:
        line = receiver_log_for_non_gps_data.readline()
        word_list = line.split(PACKET_SENTENCE_SEPERATOR)
	received_time = word_list[1]

	if GPS_PACKET_MAC_AND_ID_SEPERATOR not in line:
            received_time = float(word_list[1])
	    print 'direct non-GPS packet time:' + str(received_time)

	if received_time < time_1:
	    continue
	if received_time > time_2:
	    break
	print 'The received non-GPS packet is: ' + line + '\n'
	received_nogps_packet_count = received_nogps_packet_count + 1
    print 'received_nogps_packet_count: ' + str(received_nogps_packet_count)

    received_packet_count = received_gps_packet_count + received_nogps_packet_count
    print 'received_packet_count: ' + str(received_packet_count)

##Sender logs ==> gps logs + nogps logs
#For reading from gpslog logs
    while True:
	gps_log.readline()		#To skip odd-numbered lines
        line = gps_log.readline()
        word_list = line.split(PACKET_SENTENCE_SEPERATOR)
	received_time = word_list[2]

        if 'T' in received_time:	#Need to convert timestamp into epoch
	    pattern = '%Y-%m-%dT%H:%M:%S'
	    received_time = float(time.mktime(time.strptime(received_time[:-5], pattern))) - 14400.0			# UTC -04:00
	    #print 'converted:' + str(received_time)
	else:			#Already is in seconds; don't convert
            received_time = float(word_list[2])
	    #print 'direct:' + str(received_time)
	received_time = received_time * 1000 	#GPS packets contain time in seconds
	
	if received_time < time_1:
	    continue
	if received_time > time_2:
	    break
	print 'The sent GPS packet is: ' + line + '\n'
	gps_packet_count = gps_packet_count + 1
    print 'gps_packet_count: ' + str(gps_packet_count)

#For reading from nogpslog logs
    while True:
	nogps_log.readline()		#To skip odd-numbered lines
        line = nogps_log.readline()
        word_list = line.split(PACKET_SENTENCE_SEPERATOR)
	received_time = word_list[2]

        received_time = float(word_list[2])
	#print 'direct:' + str(received_time)

	if received_time < time_1:
	    continue
	if received_time > time_2:
	    break
	print 'The sent non-GPS packet is: ' + line + '\n'
	nogps_packet_count = nogps_packet_count + 1
    print 'nogps_packet_count: ' + str(nogps_packet_count)

    packet_rate = float(received_packet_count)/float(gps_packet_count + nogps_packet_count) * 100

    if line_no > 1 and line_no <= no_of_points_marked:
        distance = distance + distance_increment #ft.

    line_to_write = ','.join([str(distance), str(packet_rate)])
    print line_to_write + '\n'
    out_file.write(line_to_write+'\n')

    # Reset 'packet_counts'; we haven't already seen any first packets of next term! -- because specifically for this experiment, there is a considerable amount of gap between two consecutive collections
    received_gps_packet_count = 0
    received_nogps_packet_count = 0
    received_packet_count = 0
    gps_packet_count = 0
    nogps_packet_count = 0



time_log.close()
gps_log.close()
nogps_log.close()
receiver_log.close()
out_file.close()
