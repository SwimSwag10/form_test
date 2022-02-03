from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe' # set a secret key for security purposes

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/users', methods=['POST'])
def create_user():
    print("Got Post Info")
    # we create two sessions to store the name and email
    # these are also glonal sessions - they can be used on other methods!
    session['username'] = request.form['name']
    session['useremail'] = request.form['email']
    return redirect("/show")

@app.route('/show')
def show_user():
    return render_template('show.html')

# an example of how hidden routes can help users access different things within a single method.
# the method should have an IF ELSE statement here to identify if the user has pressed one hidden input or the other.
@app.route('/process', methods=['POST'])
def authenticate():
    if request.form['which_form'] == 'register':
        # register the user
        pass
    elif request.form['which_form'] == 'login':
        # login the user
        pass
    return render_template('show.html') # this should rerout to some page like /home or something

if __name__ == "__main__":
    app.run(debug=True)