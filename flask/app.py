from flask import Flask, request, render_template
from datetime import datetime


datetime.today().strftime('%A')

app = Flask(__name__)

@app.route('/')
def home():

    day_of_week = datetime.today().strftime('%A') 
    current_time = datetime.now().strftime('%H:%M:%S')
    # print(day_of_week)
        
    return render_template('index.html', day_of_week=day_of_week, current_time=current_time)

    # return 'Hello Guys!!!!! Welcome to my first flask app'


# @app.route('/second')
# def second():
#     return 'Welcome to the second page'

# @app.route('/second')
# def second():
#     return 'Welcome to the second page'


@app.route('/api')
def name():

    name = request.values.get('name')
    age = request.values.get('age')
    
    age = int(age)

    if age > 18:
        return "Welcome to the site. " + name + '!'
    else:
         return "Sorry you are too young to use this site. " + name + '!'
    # result = {
    #     'name': name,
    #     'age': age
    # }


    # return result


    # print(name)
    #  return 'Welcome to the second page'



    # length = len(name)
   
    # if length > 5:
    #     return 'Name is too long'
    # else:
    #     return 'Nice Name'
    
    # result = "Hello " + name + "!"
    # return result

if __name__=='__main__':
    app.run(debug=True)

