###
#
# FAKINGIT - A TOOL TO JUST RANDOMLY CALL WEBSITES ON RANDOM SERVERS
#
# IF ENOUGH PPL WOULD USE SOMETHING LIKE THIS, THIS COULD SERIOUSLY MESS UP
# ANY PATTERN SURVILLANCE WITHOUT REAL CLUES
#
# FREE SOFTWARE USE IT AT YOUR OWN RISK ETC.ETC.ETC.
#
###

import logging
import random
import requests
import time

from netaddr import *
import pprint

logger = None

class fakingIt():

    def __init__(self):

        pass

    def makeRandomRequest(self,round):

        valid_address = False

        while valid_address == False:

            valid_address = True

            ip1 = random.randint(1, 255)
            ip2 = random.randint(1, 255)
            ip3 = random.randint(1, 255)
            ip4 = random.randint(1, 255)

            # SOURCE : 1) Wikipedia 2) http://www.heise.de/netze/Reservierte-IPv4-Adressen-475028.html

            network_list = []

            network_list.append(IPNetwork('10.0.0.0/24'))
            if(ip1 == 10):
                valid_address = False

            network_list.append(IPNetwork('192.0.0.0/24'))
            if(ip1 == 192):
                valid_address = False

            #network_list.append(IPNetwork('172.0.0.0/24'))
            if(ip1 == 172):
                if(ip2>15 and ip2<33):
                    valid_address = False

            network_list.append(IPNetwork('192.168.0.0/16'))
            if(ip1 == 192):
                if(ip2==168):
                    valid_address = False

            network_list.append(IPNetwork('127.0.0.0/8'))
            # 127.0.0.0/8
            if(ip1 == 127):
                if(ip2==0):
                    if(ip3==0):
                        valid_address = False

            network_list.append(IPNetwork('192.0.0.0/24'))
            # 192.0.0.0/24 (RFC 5736)
            if(ip1 == 192):
                if(ip2==0):
                    if(ip3==0):
                        valid_address = False

            network_list.append(IPNetwork('169.254.0.0/16'))
            # RFC 5735 als Link Local (RFC 3927 ?)
            if(ip1 == 169):
                if(ip2==254):
                    valid_address = False


            #172.16.0.0/12 (RFC 1918)
            network_list.append(IPNetwork('172.16.0.0/12'))
            if(ip1 == 172):
                if(ip2==16):
                    if(ip3>240):
                        valid_address = False


            # 192.0.2.0/24,  ,  (RFC 5737)
            network_list.append(IPNetwork('192.0.2.0/24'))
            if(ip1 == 192):
                if(ip2==0):
                    if(ip3==2):
                        valid_address = False

            #198.51.100.0/24 ,  (RFC 5737)
            network_list.append(IPNetwork('198.51.100.0/24'))
            if(ip1 == 198):
                if(ip2==51):
                    if(ip3==100):
                        valid_address = False

            #203.0.113.0/24 ,  (RFC 5737)
            network_list.append(IPNetwork('203.0.113.0/24'))
            if(ip1 == 203):
                if(ip2==0):
                    if(ip3==113):
                        valid_address = False

            # 192.88.99.0/24
            network_list.append(IPNetwork('192.88.99.0/24'))
            if(ip1 == 192):
                if(ip2==88):
                    if(ip3==99):
                        valid_address = False

            # 198.18.0.0/15 - RFC 2544
            network_list.append(IPNetwork('198.18.0.0/15'))
            if(ip1 == 198):
                if(ip2==18):
                    if(ip3>253):
                        valid_address = False


            ip  = str(ip1)+"."+str(ip2)+"."+str(ip3)+"."+str(ip4)

            ipobj = IPAddress(ip)

            if ipobj.is_multicast():
                valid_address = False

            if ipobj.is_reserved():
                valid_address = False

            if ipobj.is_private():
                valid_address = False

            if ipobj.is_unicast() and not ipobj.is_private():
                valid_address = True


            if valid_address == False:
                print("")
                msg = "Invalid IP : "+ip
                logger.error(msg)
                print(msg)


        url = "http://"+str(ip1)+"."+str(ip2)+"."+str(ip3)+"."+str(ip4)

        logger.info(str(round)+" - "+url);

        msg = "Trying to access web-port at IP : "+url

        #print(msg)

        #url = "http://www.google.com"

        try:
            r = requests.get(url, timeout=0.75)

        except Exception as ex:
            template = "An exception of type {0} occured. Arguments:\n{1!r}"
            message = template.format(type(ex).__name__, ex.args)
            r = None
            #print message

        if r != None:

            msg = "A connection worked to IP / URL : "+url
            print(msg)
            logger.info(msg);


# SETTING UP LOGGING
logger = logging.getLogger("fakingIt")
logger.setLevel(logging.DEBUG)
formater = logging.Formatter('%(asctime)s ( Module : %(module)s ) - %(message)s')

logfile_path ="";
logfile_filename = "logfile.log"

fh = logging.FileHandler(logfile_path + logfile_filename)
fh.setFormatter(formater)
logger.addHandler(fh)

# Class Stuff
fakeIt = fakingIt()

# MAIN LOOP
round = 1
running = True

while(running):

    fakeIt.makeRandomRequest(round)

    print(str(round)+','),

    time.sleep(1)

    round = round +1
