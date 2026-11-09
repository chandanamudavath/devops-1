from flask import Flask, render_template, request
app=Flask(__name__)
@app.route('/')
def index():
    return render_template('Registration.html')
@app.route('/register', methods=['POST'])
def register():
    name = request.form['name']
    student_id = request.form['student_id']
    email = request.form['email']
    password = request.form['password']
    return render_template('Successful.html', name=name)
if __name__ == '__main__':
    app.run(debug=True)