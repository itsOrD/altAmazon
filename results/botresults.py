import sqlite3
# from datetime import datetime
import argparse

conn = sqlite3.connect('botresults')
print('RocketLeauge Bot Match Results DB opened successfully')

def init(botname, opponent, score):
    # TODO: add datetime field
    conn.execute('''
        CREATE TABLE IF NOT EXISTS botresults
        (
            ID              INT     NOT NULL    PRIMARY KEY,
            {botname}       TEXT    NOT NULL,
            {opponent}      TEXT    NOT NULL,
            {score}         INT     NOT NULL,
            GOODPNTS        INT,
            BADPNTS         INT
        );
    ''')

    print('RocketLeague "botresults" table created successfully!')
    conn.close()


if __name__ == "__main__":
    matchdata = { 'botname': botname, 'opponent': opponent, 'score': score }
    parser = argparse.ArgumentParser(description='Record match results in db for later processing')
    parser.add_argument('game', matchdata=matchdata, help='args required: botname, opponent, score')

args = parser.parse_args()
function = matchdata[args.game]
print(function(args))
