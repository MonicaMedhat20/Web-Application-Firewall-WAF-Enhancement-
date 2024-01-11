from flask import Flask, request
from wtforms import Form, StringField, validators

app = Flask(__name__)

class MyForm(Form):
    username = StringField('Username', [validators.Length(min=4, max=25)])

@app.route('/submit', methods=['POST'])
def submit():
    form = MyForm(request.form)
    if form.validate():
        # Process the valid input
        return "Form validated successfully"
    else:
        # Handle validation errors
        return "Form validation failed"

#custom validation functions 
if __name__ == '__main__':
 app.run(debug=True)
# def is_valid_email(email):
#     # Implement your email validation logic
#     # Return True if valid, False otherwise
#     pass

# email = request.form.get('email')
# if is_valid_email(email):
#     # Process valid email
# else:
#     # Handle invalid email
   