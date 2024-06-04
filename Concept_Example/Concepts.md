# Project Concepts :


# Concept 1 : What is Flask ?

    Flask is a micro web framework written in Python. 
    flask is a lightweight/miminal/minimilistic web framework.
    it developed by Armin Ronacher in 2010.
    It is used to create web applications.
    It is based on the Werkzeug WSGI toolkit and Jinja2 template engine.
### Features of Flask :
1. Flask is a lightweight web framework.
2. Flask is a micro web framework.
3. Flask is a minimalistic web framework.
4. Flask is a WSGI(Web Server Gateway Interface) compliant web framework.
5. Flask is based on the Werkzeug WSGI toolkit and Jinja2 template engine.
6. Flask is easy to learn and easy to use.
7. Flask is easy to extend and easy to customize.
8. Flask is easy to deploy and easy to maintain.
9. Flask is easy to test and easy to debug.
10. Flask is easy to scale and easy to secure.

    - ### WSGI(Web Server Gateway Interface) :
.
  - it is a standard interface between web servers and web applications.
  
  - it is used to communicate between web servers and web applications using a simple and powerful API(Application Programming Interface).
  
  - it is used to communicate between web servers and web applications using a simple and flexible protocol(like HTTP, HTTPS, etc).
  
  - it is used to communicate between web servers and web applications using a simple and efficient mechanism like CGI(Common Gateway Interface), FastCGI(Fast Common Gateway Interface), etc.
  - it is used to handle web requests and web responses between web servers and web applications.

    - ### Werkzeug WSGI toolkit :
    - it is a WSGI(Web Server Gateway Interface) toolkit.
  
    - it is used to handle web requests and web responses between web servers and web applications
  
    - it is used to handle web requests and web responses between web servers and web applications using a simple and powerful API(Application Programming Interface).
  

    - ### Jinja2 template engine :
    - it is a template engine.
    - it is used to create dynamic web pages.
    - it is used to create dynamic web pages using a simple and powerful template language.
  
#
```--------------------------------------------------------------------
```
#



# Concept 2 : why flask is called micro web framework ?

    Minimal Core: Flask comes with only the basic tools necessary for web development, such as routing, request handling, and templating. It avoids including features that might not be needed in every project, keeping the core small and simple.

    Extensibility: Flask’s design allows developers to add extensions and libraries as needed. This modularity enables developers to build custom solutions tailored to their specific needs without being burdened by unnecessary components.

    No ORM or Admin Interface: Unlike some other frameworks, Flask does not include an Object-Relational Mapping (ORM) system or an administrative interface out of the box. These features can be added through extensions if required, allowing developers to choose the tools that best fit their project's requirements.

    Flexibility and Control: Flask provides more control to developers over the components and the architecture of the application. This flexibility is particularly appealing for small to medium-sized applications where simplicity and direct control over the codebase are important.

    Documentation and Community Support: Despite being minimal, Flask has extensive documentation and a strong community, which makes it easy to find resources, tutorials, and third-party extensions to enhance its functionality as needed

##  In Short Summry:
1. Minimal Core
2. Extensibility
3. No ORM or Admin Interface
4. Flexibility and Control
5. Documentation and Community Support



#

```-------------------------------------------------------------------
```
# Concept 3 :Flask – Application

    - Rules:
  1. Not create Flask name file(like flask.py)
  2. Not create Flask package(like flask folder)
  3. Not create Flask module(like flask module)
  4. Not create Flask class(like Flask class)

    - Steps:
    - Create a new Repository
    - clone of repository (like Flask_App_01)
    - Create a new File(like app.py)
    - Write a code in app.py
- Example:
```python
from flask import Flask  # import Flask class from flask module

app = Flask(__name__)  # create an object/instance of Flask class with __name__ variable as an argument 

@app.route('/')  # create a route('/') decorator with a function
def home():  # create a function
    return "Hello, World!"  # return a string

if __name__ == "__main__":  # if __name__ variable is equal to "__main__" string
    app.run(debug=True, port=8000)  # run the app with debug=True and port=8000

# Run the app.py file

# here is app.run() method is used to run the Flask application.
# parameters of app.run() method:
# 1. debug=True : it is used to run the Flask application in debug mode.
# 2. port=8000 : it is used to run the Flask application on port 8000.

# here is @app.route('/') decorator is used to create a route('/') with a function.
# its have two parameters:
# 1. route(rule) : it is used to define the URL rule.
# 2. methods : it is used to define the HTTP methods.   

```

















# Concept 3 : What is Flask Blueprint ?

# Concept 4 : What is Flask App Factory ?
# Concept 5 : What is Flask Config ?
# Concept 6 : What is Flask Extension ?

# Concept 7 : What is Flask Request ?
# Concept 8 : What is Flask Response ?
# Concept 9 : What is Flask Session ?

# Concept 10 : What is Flask Template ?
# Concept 11 : What is Flask Context ?
# Concept 12 : What is Flask Context Local ?

# Concept 13 : What is Flask CLI ?
# Concept 14 : What is Flask Command ?
# Concept 15 : What is Flask Shell ?

# Concept 16 : What is Flask URL ?
# Concept 17 : What is Flask URL Rule ?
# Concept 18 : What is Flask URL Converter ?


# Concept 19 : if __name__=="__main__" ?


