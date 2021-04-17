from flask import Flask, render_template, url_for, request, redirect
app = Flask(__name__)
print(__name__)


# @app.route('/<username>')
# def hello_world(username=None):
#     return render_template('index.html', name=username)

@app.route('/')
def my_home():
    return render_template('index.html')


@app.route('/<string:page_name>')
def page_name(page_name):
    return render_template(page_name)


def write_to_file(data):
    with open('database.txt', mode='a') as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        file = database.write(f'\n{email},{subject},{message}')


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_file(data)
            return redirect('/thanks.html')
        except:
            return 'did not save to database'
    else:
        return 'something went wrong'

# @app.route('/index.html')
# def index():
#     return render_template('index.html')


# @app.route('/works.html')
# def works():
#     return render_template('works.html')


# @app.route('/work.html')
# def work():
#     return render_template('work.html')


# @app.route('/contact.html')
# def contact():
#     return render_template('contact.html')


# @app.route('/blog')
# def blog():
#     return 'This is my blog'


# @app.route('/blog/2020')
# def blog2():
#     return 'This is my dog blog'


# @app.route('/about.html')
# def about():
#     return render_template('about.html')
