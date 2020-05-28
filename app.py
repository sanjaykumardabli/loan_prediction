from flask import Flask,render_template, request, redirect
import pickle

app = Flask(__name__)
@app.route('/')
def dude():
    return render_template('HOME.html')


@app.route('/login', methods=['GET', 'POST'])
def login_form():
    return render_template('login.html')


@app.route('/input_form', methods=['GET', 'POST'])
def input_form():
    if request.method == 'POST':
        admin = request.form['user']
        password = int(request.form['password'])
        if admin=='admin' and password==1234:
                return render_template('Input Form.html')
        
      # elif admin!='admin' and password!=1234:
        return render_template('login.html')



@app.route('/about_author', methods=['GET', 'POST'])
def abouts():
    
        return render_template('about_san.html')


@app.route('/predict', methods=['GET', 'POST'])
def predict():
    values=[]
    if request.method == 'POST':
        values.append(int(request.form['gender']))
        values.append(int(request.form['married']))
        values.append(int(request.form['dependents']))
        values.append(int(request.form['educated']))
        values.append(int(request.form['self_employment']))
        values.append(int(request.form['Applicant_Income']))
        values.append(int(request.form['Coapplicant_Income']))
        values.append(int(request.form['Loan_amount']))
        values.append(int(request.form['Loan_amount_term']))
        values.append(int(request.form['Credit_history']))
        values.append(int(request.form['Property_area']))
        value = []
        value.append(values)
        model=pickle.load(open('models/log_model.pickle', 'rb'))
        output=model.predict(value)
        if output == 1:
            return render_template('congrats.html')
        
        return render_template('sad.html')
    

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    
        return render_template('contact.html')

@app.route('/home', methods=['GET', 'POST'])
def home():
    
        return render_template('HOME.html')
    
@app.route('/thank_you', methods=['GET', 'POST'])
def thanks():
    
        return render_template('thank_you.html')

@app.route('/resume', methods=['GET', 'POST'])
def resume():
    
        return render_template('resume.html')
    
if __name__ == "__main__":
    app.run(debug=False)
  #  app.run(debug=True)
