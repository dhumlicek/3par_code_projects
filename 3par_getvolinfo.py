import hpe3parclient
from hpe3parclient import client, exceptions
import pprint, getpass, json


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
    hosts = cl.getHosts()
    hosts_dict = {}
    iter = 0
    # Dumps JSON data to file
    #with open('output_hosts.json', 'w') as file:
    #    file.write(json.dumps(hosts))

    #for x in hosts['members']:
    #    hosts_dict[iter] = x['name']
    #    iter += 1

    # Print Host and WWNs (FC only)
    while iter < len(hosts['members']):
        hn_path = hosts['members'][iter]['name']
        fc_path = hosts['members'][iter]['FCPaths']
        fc_cnt = len(fc_path)
        x = 0
        wwn_list = list()
        while x < fc_cnt:
            wwn_list.append(fc_path[x]['wwn'])
            x += 1

        iter += 1
        print(iter, ".\t", hn_path, end='\t')
        for item in wwn_list:
            print(item, sep='\t', end=' ')
        print("")

        

    host_to_get = input("Which host do you want to find? : ")
    host_info = cl.getHost(host_to_get)
    pprint.pprint(host_info)

    #with open('output_hostInfo.json', 'w') as file:
    #    file.write(json.dumps(host_info))

quit = 'n'

while quit != 'y':
    quit = input("Would you like to quit? Y/N : ")
    quit = quit[:1].lower()
    cl.logout()

print("logout worked")