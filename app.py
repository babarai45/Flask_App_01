from flask import Flask, request , render_template,jsonify, redirect, url_for


app = Flask(__name__)    # Create a new instance of the Flask class

@app.route('/')          # Define the route for the root URL of the website
def hello_world(): 
    return 'Hello, World!'  # Return the string 'Hello, World!' as the response

#-----------------------------
@app.route('/about')          # Define the route for the root URL of the website
def about():
    return "<h1>This is my About Page </h1>"  # Return the string 'Hello, World!' as the response

#-----------------------------
# variable rules
# Define a new route that accepts a string as a parameter and returns the string reversed

# @app.route('/success/<score>')
# def success(score):
#     return "The success score is " + score

#------------

# @app.route('/success/<int:score>')
# def success(score):
#     return "The success score is " + str(score)

#------------ simple form


@app.route('/success/<int:score>')
def success(score):
    return "The success score is " + str(score)


@app.route('/fail/<int:score>')
def fail(score):
    return "The fail score is " + str(score)

#-----------------------------
# @app.route('/results/<int:score>')
# def results(score):
#     res = ""
#     if score > 50:
#         res = "success"
#     else:
#         res = "fail"
#     return "The result is " + res

#-----------------------------
@app.route('/form' , methods=['GET','POST'])
def form():
    if request.method == 'GET':
        return render_template('form.html')
    else:
        maths =float(request.form['math'])
        urdu = float(request.form['urdu'])
        english = float(request.form['english'])

        total = (maths + urdu + english)/3
        return render_template('form.html' , score= total)

        # res = ""
        # if total >=50:
        #     res = "success"
        # else:
        #     res = "fail"
        # return redirect(url_for(res , score=total))


#-----------------------------
# create a  simple  api
@app.route('/api', methods=['POST'])
def sum():
    request_data = request.get_json()
    val_a = float(request_data['a'])
    val_b = float(request_data['b'])
    return jsonify({'sum': val_a + val_b})  

if __name__ == '__main__':  # If this script is run from the command line
    app.run(debug=True)   # Start the Flask development server

