import sys
import json
from tweepy import Cursor
from twitter_client import get_twitter_client
from datetime import datetime

if __name__ == '__main__':
    users=["jairbolsonaro","lulaoficial","cirogomes","simonetebetbr","leopericlesup", "fdavilaoficial", "verapstu", "sofiamanzanopcb", "eymaeloficial", "sorayathronicke", "pablomarcal"]
    client = get_twitter_client()

    agora=datetime.now()
    hoje=format(agora.day)
    hoje+="-"+format(agora.month)

    for name in users:
        dirname= "timeline"
        filename = dirname + "/{}_timeline_".format(name)+ hoje + ".jsonl"
        consulta="from:"+name+" since:2022-08-01 until:2022-10-30"

        with open(filename, 'w') as f:
            for status in Cursor(client.search_tweets, q=consulta,include_entities=True).items(1000):
                f.write(json.dumps(status._json, indent=4)+"\n")
