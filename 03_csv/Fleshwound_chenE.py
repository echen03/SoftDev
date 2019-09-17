import random

fn = 'occupations.csv'
fileR = open(fn, 'r')

dummy = fileR.readline()
jobs = fileR.readlines()

occupations = dict()

for job in jobs:
    words = job.split(',')
    percentage = words.pop(len(words) - 1)
    delimiter = ','
    occupations[delimiter.join(words)] = float(percentage)

def randomJob(dictOfJobs):
    perct = dictOfJobs['Total'] * 100
    randomperct = random.random() * perct
    keys = dictOfJobs.keys()
    x = 0;
    while ((dictOfJobs[keys[x]] * 100) < randomperct):
        randomperct = randomperct - (dictOfJobs[keys[x]] * 100)
        print randomperct
        x = x + 1

randomJob(occupations)
