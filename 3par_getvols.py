import hpe3parclient
from hpe3parclient import client, exceptions
import pprint, getpass, json, operator


def getKeysByValues(elements_dict, vals_list):
    key_list = list()
    items_list = elements_dict.items()
    for item  in items_list:
        if item[1] in vals_list:
            key_list.append(item[0])
    return  key_list 


def search(elements_dict, searchFor):
    key_list = list()
    items_list = elements_dict.items()
    for item  in items_list:
        if searchFor in item[1]:
            key_list.append(item[1])
    return  key_list 


def unique_elements(elements_dict):
    vol_list = list()
    items_list = elements_dict.items()
    for item  in items_list:
        vol_split = item[1].rsplit(".", 1)[0]
        vol_split = vol_split.rsplit("_", 1)[0]
        if vol_split not in vol_list:
            vol_list.append(vol_split)
    return  vol_list 



username = "dh034485"
#password = input("password: ")
password = getpass.getpass(prompt = "password: ")
array = "KC3T2G222"

# this creates the client object and sets the url to the
cl = client.HPE3ParClient("https://%s.cernerasp.com:8080/api/v1" % array, suppress_ssl_warnings=True)

# Set the SSH authentication options for the SSH based calls.
#cl.setSSHOptions("%s.cernerasp.com" % array, username, password)

try:
    cl.login(username, password)
    print("Login worked!")
except exceptions.HTTPUnauthorized as ex:
    print("Login failed.")

pvol = input("Do you want to print output? Y/N : ")
pvol = pvol[:1].lower()

if pvol == 'y':
    volumes = cl.getVolumes()
    volume_dict = {}
    iter = 0
    for x in volumes['members']:
        volume_dict[iter] = x['name']
        #volume_dict[iter] = [x['name'], x['id']]
        iter += 1

    #Get Keys for non-host volumes
    key_list = getKeysByValues(volume_dict, ['admin', '.srdata'] )
 
    #Iterate over the list of values, remove from dict
    for key in key_list:
        #print(key)
        #print("Before: ", len(volume_dict))
        del volume_dict[key]
        #print("After: ", len(volume_dict))

    sorted_all_volumes = sorted(volume_dict.items(), key=lambda kv: kv[1])
    #pprint.pprint(sorted_all_volumes)
    #for key,val in sorted_all_volumes:
    #    #pprint.pprint(val)
    #    print(val)

    #Get unique volume list
    unique_volumes = unique_elements(volume_dict)
    sorted_unique_volumes = sorted(unique_volumes)
    #pprint.pprint(unique_volumes)
    #pprint.pprint(sorted_unique_volumes)

    #Get volumes matching hostname pattern
    #print(type(volume_dict), type(sorted_all_volumes), type(hostname))
    #hostname = "CHLDWA724APP1"
    for host in sorted_unique_volumes:
        hostname = host
        matched_volumes = search(volume_dict, hostname)
        pprint.pprint(sorted(matched_volumes))
        print(len(matched_volumes))

        #spec_volume = cl.getVolume(matched_volumes[0])
        #print(spec_volume)

quit = 'n'

while quit != 'y':
    quit = input("Would you like to quit? Y/N : ")
    quit = quit[:1].lower()
    cl.logout()

print("logout worked")