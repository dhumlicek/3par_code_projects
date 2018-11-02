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
#array = "KC3T2G222"
array = "KC1T0G234"

# this creates the client object and sets the url to the
cl = client.HPE3ParClient("https://%s.cernerasp.com:8080/api/v1" % array, suppress_ssl_warnings=True)

# Set the SSH authentication options for the SSH based calls.
#cl.setSSHOptions("%s.cernerasp.com" % array, username, password)

try:
    cl.login(username, password)
    print("Login worked!")
except exceptions.HTTPUnauthorized as ex:
    print("Login failed.")


quit = 'n'

while quit != 'y':
    hosts = cl.getHosts()
    hosts_dict = {}
    iter = 0

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

        
    # Select host by ID or Displayed name
    while True:
        host_to_get = input("Which host do you want to find? : ")
        if (host_to_get.isdigit() == False) and (host_to_get.isalpha() == False):
            if (host_to_get.isalnum()):
                try: 
                    host_info = cl.getHost(host_to_get.upper())
                except exceptions.HTTPNotFound:
                    host_info = "Find Host by NAME does not exist."
                break
            else:
                print("Valid input not received. Try again")
                continue
        elif (host_to_get.isdigit() == True) and (host_to_get.isalpha() == False):
            try: 
                host_info = cl.getHost(hosts['members'][int(host_to_get) - 1]['name'])
            except exceptions.HTTPNotFound:
                host_info = "Find Host by ID does not exist."
            break
        elif (host_to_get.isdigit() == False) and (host_to_get.isalpha() == True):
            try: 
                host_info = cl.getHost(host_to_get.upper())
            except exceptions.HTTPNotFound:
                host_info = "Find Host by ALPHA NAME does not exist."
            break
        else:
            print("Valid input not received. Try again")
            continue

    pprint.pprint(host_info)

    print('-' * 10)
    host_vlun = cl.getHostVLUNs(host_info['name'])
    print(len(host_vlun))
    host_vlun_cnt = int((len(host_vlun)) / 3)
    print(host_vlun_cnt)
    pprint.pprint(host_vlun)
    #pprint.pprint(host_vlun[-host_vlun_cnt:])

    host_volname = list()
    for list in (host_vlun[-host_vlun_cnt:]):
        host_volname.append(list['volumeName'])

    pprint.pprint(host_volname)

    #pprint.pprint(cl.getVolume("MCVHVADB11_SHARED.8"))
    #pprint.pprint(cl.getVLUN("MCVHVADB11_SHARED.8"))
    #pprint.pprint(cl.getVLUN("MCVHVADB11.5"))

    #pprint.pprint(cl.http.get('/vluns?query=MCVHVADB11_SHARED.8'))
    
    #pprint.pprint(cl.getVolume(host_volname[9]))
    #pprint.pprint(cl.getVLUN(host_volname[9]))

    #with open('output_hostInfo.json', 'w') as file:
    #    file.write(json.dumps(host_info))
    with open('output_vluns.json', 'w') as file:
        file.write(json.dumps(cl.getVLUNs()))

    quit = input("Would you like to quit? Y/N : ")
    quit = quit[:1].lower()
        

cl.logout()
print("logout worked")