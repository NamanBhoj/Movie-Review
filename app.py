import numpy as np
from flask import Flask , render_template , url_for , request, jsonify

import pickle # serialisation



app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))




app.config['SECRET_KEY'] = 'mysecretkey'



@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict' , methods= ['POST'])
def predict():
    features = request.form.values()
    predictions = model.predict(features)
    output = predictions[0]
    if( output == 'neg'):
        output = output +'ative'
        return render_template('index.html', prediction_text =f"The review you gave is {output}!. This was bound to happend , afterall nothing beats an Iron Man Movie" )
    elif(output == 'pos'):
        output = output + "itive"
        return render_template('index.html', prediction_text =f"The review you gave is {output}!" )
    


if __name__ == '__main__':
    app.run(debug=True) 