import hpe3parclient
from hpe3parclient import client, exceptions
import pprint, getpass, json

username = "dh034485"
#password = input("password: ")
password = getpass.getpass(prompt = "password: ")
array = "KC3T2G222"

# this creates the client object and sets the url to the
# 3PAR server with IP 10.10.10.10 on port 8008.
#cl = client.HPE3ParClient("http://10.10.10.10:8008/api/v1")

# SSL certification verification is defaulted to False. In order to
# override this, set secure=True. or secure='/path/to/cert.crt'
# cl = client.HPE3ParClient("https://10.10.10.10:8080/api/v1",
#                          secure=True)
# Or, to use ca certificates as documented by Python Requests,
# pass in the ca-certificates.crt file
# http://docs.python-requests.org/en/v1.0.4/user/advanced/
# cl = client.HPE3ParClient("https://10.10.10.10:8080/api/v1",
#                          secure='/etc/ssl/certs/ca-certificates.crt')

cl = client.HPE3ParClient("https://%s.cernerasp.com:8080/api/v1" % array, suppress_ssl_warnings=True)

# Set the SSH authentication options for the SSH based calls.
#cl.setSSHOptions("%s.cernerasp.com" % array, username, password)

try:
    cl.login(username, password)
    print("Login worked!")
except exceptions.HTTPUnauthorized as ex:
    print("Login failed.")

version = cl.getWsApiVersion()

pprint.pprint(version)

pvol = input("Do you want to print output? Y/N : ")
pvol = pvol[:1].lower()

if pvol == 'y':
    try:
        volumes = cl.getVolumes()
        #print(type(volumes))
        #pprint.pprint(volumes)
        #print(volumes)
        
        vols = volumes['members']   ## gets all volumes info using Dict --> class 'list'
        #get_vols = volumes.get('members')   ## gets all volumes info using get method --> class 'list'

        

        print("Volumes leng: ", len(volumes), "\tvolumes type: ", type(volumes))
        print("Vols leng: ", len(vols), "\tvols type: ", type(vols))
        #print("Get_vols leng: ", len(get_vols), "\tGet_vols type: ", type(get_vols))

        vol_member = volumes['members'][0]
        print("vol_member leng: ", len(vol_member), "\tvol_member type: ", type(vol_member))
        vol_member = volumes['members'][(len(vols) - 1)]
        print("vol_member leng: ", len(vol_member), "\tvol_member type: ", type(vol_member))   

        #pprint.pprint(vol_member)
        #print(vol_member['id'],"\t: ",vol_member['name'])
        
        for x in volumes['members']:
            print(x['id'],"\t: ",x['name'])

        ##with open('output.json', 'w') as file:
        ##    file.write(json.dumps(volumes))
        ##with open('output_vols.json', 'w') as file:
        ##    file.write(json.dumps(vols))

        #data = json.loads(json.dumps(vols))
        #print("data leng: ", len(data), "\tdata type: ", type(data))

        #for key,val in vols:
        #    print(key)

        #for key,vals in volumes.items():
        #    #print(key)
        #    if key == 'members':
        #        #print(vals[1])
        #        print(len(vals))
        #        #pprint.pprint(vals[369])
        #        #break

    except exceptions.HTTPUnauthorized as ex:
        print("You must login first")
    except Exception as ex:
        #something unexpected happened
        print(ex)

#spec_volume = cl.getVolume("UNIVTNAPP3.9")
#print(spec_volume)

quit = 'n'

while quit != 'y':
    quit = input("Would you like to quit? Y/N : ")
    quit = quit[:1].lower()
    cl.logout()

print("logout worked")