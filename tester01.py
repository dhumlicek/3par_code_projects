

host_to_get = input("Which host do you want to find? : ")
print(type(host_to_get))
##if host_to_get.isalnum():    
##    print("Host is an ALNUM")
##
##if host_to_get.isdigit():
##    print("Host is a DIGIT.")
##
##if host_to_get.isalpha():
##    print("Host is an ALPHA.")

print(host_to_get.isdigit())
print(host_to_get.isalpha())
print(host_to_get.isalnum())

if (host_to_get.isdigit() == False) and (host_to_get.isalpha() == False):
    if (host_to_get.isalnum()):
        print("Host is an ALNUM")
elif (host_to_get.isdigit() == True) and (host_to_get.isalpha() == False):
    print("Host is a DIGIT")
elif (host_to_get.isdigit() == False) and (host_to_get.isalpha() == True):
    print("Host is an ALPHA")

print(host_to_get)