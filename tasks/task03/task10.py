import csv
import datetime
from matplotlib import pyplot
import numpy


def parse_time(text):
    return datetime.datetime.strptime(text, "%Y-%m-%d %H:%M:%S.%f")


def getStatsByWD(results, group=''):
    stats = []
    for i in range(7):
        stats.append(0)
    for row in results:
        if group in row[2]:
            stats[parse_time(row[3]).weekday()] += 1
    return stats


def getGroupsCount(results, group=''):
    g = []
    for row in results:
        if group in row[2] and not row[2] in g:
            g.append(row[2])
    return len(g)


def getStatsByTime(results, group='', avg=False):
    stats = []
    for i in range(24):
        stats.append(0)
    for row in results:
        if group in row[2]:
            stats[parse_time(row[3]).hour] += 1
    if avg:
        for i in range(24):
            stats[i] = stats[i]/getGroupsCount(results, group)
    return stats


with open('data/messages.csv', encoding='utf8') as f:
    messages = list(csv.reader(f, delimiter=','))
with open('data/results.csv', encoding='utf8') as f:
    results = list(csv.reader(f, delimiter=','))

print(messages[0])
print(results[0])

#labels = ['ПН', 'ВТ', 'СР', 'ЧТ', 'ПТ', 'СБ', 'ВС']
labels = []
for i in range(24):
    labels.append(str(i)+':00')

x = numpy.arange(len(labels))  # the label locations
width = 0.35  # the width of the bars

fig, ax = pyplot.subplots()
'''rects1 = ax.bar(x - width/2, getStatsByWD(results), width, label='Все группы')
rects2 = ax.bar(x + width/2, getStatsByWD(results,
                'ИКБО-10-20'), width, label='ИКБО-10-20')'''
rects1 = ax.bar(x - width/2, getStatsByTime(results, 'ИНБО', True),
                width, label='ИНБО')
rects2 = ax.bar(x + width/2, getStatsByTime(results,
                'ИКБО', True), width, label='ИКБО')
# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Количество выполнений')
ax.set_title('Задачи')
ax.set_xticks(x, labels)
ax.legend()

ax.bar_label(rects1, padding=3)
ax.bar_label(rects2, padding=3)

fig.tight_layout()

pyplot.show()
