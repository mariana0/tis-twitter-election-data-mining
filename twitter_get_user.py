import os
import sys
import json
import time
import math
import re
from datetime import datetime
from tweepy import Cursor
from twitter_client import get_twitter_client

def usage():
    print("Usage:")
    print("python {} <username>".format(sys.argv[0]))

if __name__ == '__main__':
    #screen_name = sys.argv[1]
    users=["jairbolsonaro","marinasilva","cirogomes","geraldoalckmin","haddad_fernando"]
    client = get_twitter_client()
    
    agora=datetime.now()
    hoje=format(agora.day)
    hoje+="-"+format(agora.month)

    for name in users:
        screen_name=name
        dirname="perfil"
        dirname += "/{}".format(screen_name)
        
        try:
            os.makedirs(dirname, mode=0o755, exist_ok=True)
        except OSError:
            print("Directory {} already exists".format(dirname))
        except Exception as e:
            print("Error while creating directory {}".format(dirname))
            print(e)
            sys.exit(1)

        # get user's profile
        fname1 = dirname
        fname1+="/user_profile_"
        fname1+=hoje
        fname1+=".json"
        with open(fname1, 'w') as f:
            profile = client.get_user(screen_name=screen_name)
            f.write(json.dumps(profile._json, indent=4))
    

    
    
