# Load the OS functions.
import os

# Disable new lines for print() by default
import sys
sys.stdout.write('')

# Hostlist to check
hostname_list = ['127.0.0.1']

# Define variables
count = 0
end = len(hostname_list)

# debug
# print ('Number of hosts: ', end)

# Do the loop
while (count < end):
    # ping the hostname_list
    response = os.system("ping -n 1 "+hostname_list[count])

    # check the response
    if response == 0:
        friendly_response = 'PING Reply!'
    else:
        friendly_response = 'FAILED!'

    # Display hostname_list, count 
    print ('Host: [',count, ']' ,hostname_list[count], friendly_response)

    # Increment the count
    count = count +1




