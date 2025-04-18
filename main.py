from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')




@app.route('/skills')
def skills():
    return render_template('skills.html')



@app.route('/projects')
def projects():
    return render_template('projects.html')


@app.route('/contacts')
def contacts():

    
    return render_template('contacts.html')



if __name__ == "__main__":

    app.run(debug=True)