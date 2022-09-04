import sys
import json
import time
from datetime import datetime
from twitter_client import get_twitter_client

def usage():
    print("Usage:")
    print("python {} <username>".format(sys.argv[0]))

if __name__ == '__main__':
    users=["jairbolsonaro","lulaoficial","cirogomes","simonetebetbr","leopericlesup", "fdavilaoficial", "verapstu", "sofiamanzanopcb", "eymaeloficial", "sorayathronicke", "pablomarcal"]
    client = get_twitter_client()

    agora=datetime.now()
    hoje=format(agora.day)
    hoje+="-"+format(agora.month)

    for name in users:
        dirname="perfil"

        filename = dirname + "/{}_profile_".format(name)+ hoje + ".json"
        with open(filename, 'w') as f:
            profile = client.get_user(screen_name=name)
            f.write(json.dumps(profile._json, indent=4))
