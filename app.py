
from flask import Flask, render_template, request, redirect, url_for
from utils.data_handler import DataHandler

app = Flask(__name__)




data_handler = DataHandler()

# Route 1 : Home page

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')



# Route 2 : Feedback page

@app.route('/submit-feedback', methods=['POST'])
def submit_feedback():
    name = request.form.get('name')
    email = request.form.get('email')
    feedback = request.form.get('comments')
    satisfied = request.form.get('satisfied')
    data_handler.add_feedback(name, email,feedback,satisfied)
    return redirect(url_for('index'))



if __name__ == '__main__':
    app.run(debug=True)
