from flask import Flask, render_template
import random

fn = '190913f_data/occupations.csv'
fileR = open(fn, 'r')

jobs = fileR.readlines()
occupations = dict()
x=0

for job in jobs:
    words = job.split(',')
    percentage = words.pop(len(words) - 1)
    #delimiter = ','
    if x>0:
        occupations[','.join(words)] = float(percentage)
    else:
        occupations[','.join(words)] = percentage
    x=x+1

def randomJob(dictOfJobs):
    perct = dictOfJobs['Total'] * 100
    randomperct = random.random() * perct
    keys = dictOfJobs.keys()
    x = 0;
    while ((dictOfJobs[keys[x]] * 100) < randomperct):
        randomperct = randomperct - (dictOfJobs[keys[x]] * 100)
        x = x + 1
    return keys[x]

#print(randomJob(occupations))


app = Flask(__name__) #create instance of class Flask

@app.route('/') #assign following fxn to run when run route requested
def hello_word():
    print(__name__) #where will this go?
    return "Default"

@app.route("/occupyflaskst")
def protest():
    return render_template('model_templt.html',
                            titl="Occupation List",
                            collection=occupations,
                            head="Returns random occupation from the table below")
if __name__ == "__main__":
    app.debug = True
    app.run()
