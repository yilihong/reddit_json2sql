# __author__ = 'KevinHong@ASU'

import json
import mysql.connector as MS
import glob


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


mydb = MS.connect(host='localhost', user='root', passwd='1987Kevin', db='reddit')
cursor = mydb.cursor()

for file in glob.glob("data/*.json"):
    print "Loading file {}".format(file)
    with open(file) as data_file:
        for line in data_file:
            content = json.loads(line)
            insert = ("INSERT INTO comments_test "
                      "(body, score_hidden, archived, name, author, author_flair_text, downs, created_utc, subreddit_id, link_id, parent_id, score, retrieved_on, controversiality, gilded, id, subreddit, ups, distinguished, author_flair_css_class)"
                      "VALUES (%(body)s, %(score_hidden)s, %(archived)s, %(name)s, %(author)s, %(author_flair_text)s, %(downs)s, %(created_utc)s, %(subreddit_id)s, %(link_id)s, %(parent_id)s, %(score)s, %(retrieved_on)s, %(controversiality)s, %(gilded)s, %(id)s, %(subreddit)s, %(ups)s, %(distinguished)s, %(author_flair_css_class)s)")

            data = {
            "body": content.get("body", ""),
            "score_hidden": content.get("score_hidden", 0),
            "archived": content.get("archived", 0),
            "name": content.get("name", ""),
            "author": content.get("author", ""),
            "author_flair_text": content.get("author_flair_text", ""),
            "downs": content.get("downs", 0),
            "created_utc": content.get("created_utc", 0),
            "subreddit_id": content.get("subreddit_id", ""),
            "link_id": content.get("link_id", ""),
            "parent_id": content.get("parent_id", ""),
            "score": content.get("score", 0),
            "retrieved_on": content.get("retrieved_on", 0),
            "controversiality": content.get("controversiality", 0),
            "gilded": content.get("gilded", 0),
            "id": content.get("id", ""),
            "subreddit": content.get("subreddit", ""),
            "ups": content.get("ups", 0),
            "distinguished": content.get("distinguished", ""),
            "author_flair_css_class": content.get("author_flair_css_class", "")
            } # testing data

            try:
                cursor.execute(insert, data)
                mydb.commit()
                # print bcolors.OKGREEN + "success, inserted into database" + bcolors.ENDC
            except:
                print bcolors.FAIL + "error, not inserted" + bcolors.ENDC
        print "Done Insertion for file {}".format(file)
#close the connection to the database.
cursor.close()
