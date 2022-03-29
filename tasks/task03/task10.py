import csv
import datetime


def parse_time(text):
    return datetime.datetime.strptime(text, "%Y-%m-%d %H:%M:%S.%f")


with open('data/messages.csv', encoding='utf8') as f:
    messages = list(csv.reader(f, delimiter=','))
with open('data/results.csv', encoding='utf8') as f:
    results = list(csv.reader(f, delimiter=','))

print(messages[0])
print(results[0])
