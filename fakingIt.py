###
#
# FAKINGIT - A TOOL TO JUST RANDOMLY CALL WEBSITES ON RANDOM SERVERS
#
# IF ENOUGH PPL WOULD USE SOMETHING LIKE THIS, THIS COULD SERIOUSLY MESS UP
# ANY PATTERN SURVILLANCE WITHOUT REAL CLUES WHERE THE REAL USE OF FINDING
# SERIOUS CRIMINALITY WOULD STAY THE SAME
#
# FREE SOFTWARE ! USE IT AT YOUR OWN RISK ETC.ETC.ETC.
#
###

import logging
import random
import requests
import time

logger = None

class fakingIt():

    def __init__(self):

        pass

    def makeRandomRequest(self,round):

        ip1 = random.randint(1, 255)
        ip2 = random.randint(1, 255)
        ip3 = random.randint(1, 255)
        ip4 = random.randint(1, 255)

        url = "http://"+str(ip1)+"."+str(ip2)+"."+str(ip3)+"."+str(ip4)

        logger.info(str(round)+" - "+url);

        try:
            r = requests.get(url)

        except Exception as ex:
            template = "An exception of type {0} occured. Arguments:\n{1!r}"
            message = template.format(type(ex).__name__, ex.args)
            print message


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

    time.sleep(1)

    round = round +1
