import os
import sys
import requests
import json

def GetData() :
    if len(sys.argv) > 2:
        print('You have specified too many arguments')
        sys.exit()

    if len(sys.argv) < 2:
        print('You need to specify an IP')
        sys.exit()

    ip = sys.argv[1]

    request = json.loads(requests.get('http://ip-api.com/json/'+ip).text)

    print("Ip:"+ip)
    print("Status: "+request["status"])
    if(request["status"]=="success") :
        print("Country: "+request["countryCode"]+"/"+request["country"])

        print("Region: "+request["region"]+"/"+request["regionName"])

        print("City: "+request["city"])

        print("Zip: "+request["zip"])

        print("Lat/Lon: "+str(request["lat"])+"/"+str(request["lon"]))
    return request