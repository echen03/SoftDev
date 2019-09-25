from flask import Flask, render_template
import random

fn = 'occupations.csv'
fileR = open(fn, 'r')


dummy = fileR.readline() #get rid of the first line: "Job Class, Percentage"
jobs = fileR.readlines() #creates an list of every single line
occupations = dict()     #creates a dictionary

#adds keys into occupations
for job in jobs:
    words = job.split(',') #do not have to worry about multiple commas
    percentage = words.pop(len(words) - 1) #the value after the comma is the percentage
    occupations[','.join(words)] = float(percentage)

#takes a random occupation from the dictionary based on weights
def randomJob(dictOfJobs):
    perct = dictOfJobs['Total'] * 100
    randomperct = random.random() * perct
    keys = list(dictOfJobs.keys()) #gets a list of the keys in order to return to it
    x = 0; #index of the key that will be returned
    #will only stop iterating when the randomperct is in the range of the occupation weight
    while ((dictOfJobs[keys[x]] * 100) < randomperct):
        #subtracts the weight from the randomperct when it is not in range
        randomperct = randomperct - (dictOfJobs[keys[x]] * 100)
        x = x + 1
    return keys[x]


app = Flask(__name__) #create instance of class Flask

@app.route('/') #assign following fxn to run when run route requested
def hello_world():
    print(__name__) #where will this go?
    return "visit occupyflaskst"

@app.route("/occupyflaskst")
def getjobs():
    return render_template('model_templt.html',
                            collection=occupations,
                            randjob = randomJob(occupations)
                            )

if __name__ == "__main__":
    app.debug = True
    app.run()
