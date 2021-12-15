from flask import Flask, render_template, request
import random

app = Flask(__name__)

'''
given a text file of three columns
 - generate three lists for three columns
 - return insult where:
    - insult is a string
    - insult is constructed in order (list1+list2+list3)

'''
def gen_insult():
    insult = ''
    insult_list_1 = []
    insult_list_2 = []
    insult_list_3 = []
    with open("insults.txt", "r") as f:
        for line in f:
            i = 0
            
            for word in line.split(' '):
                if word != '':
                    if i == 0:
                        insult_list_1.append(word)
                        i+=1
                    elif i == 1:
                        insult_list_2.append(word)
                        i+=1
                    elif i == 2:
                        insult_list_3.append(word)
                        i+=1
                    else:
                        i = 0
    
    insult= f'Thou {random.choice(insult_list_1)} {random.choice(insult_list_2)} {random.choice(insult_list_3)}!'
    return insult

@app.route('/', methods = ["GET", "POST"])
def home():
    insult = ''
    if request.method == "POST":
        if "Insult Me" in request.form:
            insult = gen_insult()
    return render_template('index.html',insult=insult)




if __name__ == '__main__':
    app.run(debug=True)