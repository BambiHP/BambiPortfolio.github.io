import os
import csv
import pandas

dirname = os.getcwd()

with open(dirname + '/data/accesslog_01.csv') as f:
    accesslog_data = list(csv.reader(f))
with open(dirname + '/data/botlist_01.csv') as f:
    botlist_data = list(csv.reader(f))
print(accesslog_data)

#answer_data = [["20200110",111],["20200111",222]]
#with open(dirname + '/data/accesslog_01.answer.csv', 'w') as f:
#    writer = csv.writer(f, lineterminator = '\n')
#    writer.writerows(answer_data)
