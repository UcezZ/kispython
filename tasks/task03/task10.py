import csv
import datetime
from matplotlib import pyplot
import numpy


def parse_time(text):
    return datetime.datetime.strptime(text, "%Y-%m-%d %H:%M:%S.%f")


with open('data/messages.csv', encoding='utf8') as f:
    messages = list(csv.reader(f, delimiter=','))
with open('data/results.csv', encoding='utf8') as f:
    results = list(csv.reader(f, delimiter=','))

print(messages[0])
print(results[0])

labels = []
for row in results:
    if not row[0] in labels:
        labels.append(row[0])
labels.sort()

counts = []
for row in labels:
    counts.append(0)
for row in results:
    counts[int(row[0])] += 1

counts2 = []
for row in labels:
    counts2.append(0)
for row in results:
    if ('ИКБО-10-20' in row[2]):
        counts2[int(row[0])] += 1

x = numpy.arange(len(labels))  # the label locations
width = 0.35  # the width of the bars

fig, ax = pyplot.subplots()
rects1 = ax.bar(x - width/2, counts, width, label='Кол-во выполнений')
rects2 = ax.bar(x + width/2, counts2, width, label='ИКБО-10-20')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Количество выполнений')
ax.set_title('Задачи')
ax.set_xticks(x, labels)
ax.legend()

ax.bar_label(rects1, padding=3)
ax.bar_label(rects2, padding=3)

fig.tight_layout()

pyplot.show()
