# OneP script to print interfaces with associated IPv4/IPv6 addresses
# 
# Usage:
#  python script_name.py [ip_address] [username] [password]


# This script uses the onep_connect.py module
from onep_connect import connect
from onep.interfaces import InterfaceFilter
import sys

if len(sys.argv) != 4:
	print 'Usage: python script_name.py [ip_address] [username] [password]'
	quit()

# Connect using passed in connection values
# (will raise a ValueError if bad IP address or credentials)
ne = connect(sys.argv[1], sys.argv[2], sys.argv[3])

try:  
	#Create Interface Filter and print interface list
	if_filter = InterfaceFilter(interface_type=1)
	for interface in ne.get_interface_list(if_filter):
		print '%s: %s' % (interface.name, interface.get_address_list())
		
		# Optionally, can print full interface switchport info
		# print interface.get_config()

finally:
	# Finally have the application disconnect from the Network Element  
	ne.disconnect() 



## Output:
# thePacketGeek$ python print_all_interface_IPs.py 10.211.55.200 admin admin
# Loopback0: ['1.1.1.1', '2001:100::1', 'FE80::AA:BB:CC:DD']
# GigabitEthernet1: ['10.211.55.200']
# GigabitEthernet2: ['192.168.56.1', '2001:56::1', 'FE80::111:222:333:444']
# GigabitEthernet3: []