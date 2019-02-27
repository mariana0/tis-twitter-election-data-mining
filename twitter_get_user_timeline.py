import sys
import json
from tweepy import Cursor
from twitter_client import get_twitter_client
from datetime import datetime

if __name__ == '__main__':
    #user = sys.argv[1]
    users=["jairbolsonaro","marinasilva","cirogomes","geraldoalckmin","haddad_fernando"]
    client = get_twitter_client()
    
    for name in users:
        dirname= "timeline/{}".format(name)
        fname2=dirname
        fname2+= "/user_timeline_29-10.jsonl"
        consulta="from:"+name+" since:2018-10-29 until:2018-10-30"

        with open(fname2, 'w') as f:
            for status in Cursor(client.search, q=consulta,result_type='recent',include_entities=True, monitor_rate_limit=False, wait_on_rate_limit=False).items(300):
                f.write(json.dumps(status._json)+"\n")


            

