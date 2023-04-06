import numpy as np
import pickle
import pandas as pd
#from flasgger import Swagger
import streamlit as st 

from PIL import Image

#app = Flask(__name__)
model = pickle.load(open('RigeModel.pkl', 'rb'))

#@app.route('/')
def welcome():
    return "Welcome All"

def predict_autmobile_price(horsepower,curb-weight,engine-size,highway-mpg):
    
    """Let's Authenticate the Banks Note 
    This is using docstrings for specifications.
    ---
    parameters:  
      - name: variance
        in: query
        type: number
        required: true
      - name: skewness
        in: query
        type: number
        required: true
      - name: curtosis
        in: query
        type: number
        required: true
      - name: entropy
        in: query
        type: number
        required: true
    responses:
        200:
            description: The output values
        
    """
   
    prediction=classifier.predict([[variance,skewness,curtosis,entropy]])
    print(prediction)
    return prediction

#@app.route('/predict',methods=['POST'])
def main():
    st.title('Automobile price prediction')
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Streamlit Bank Authenticator ML App </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    horsepower = st.text_input("horsepower","Type Here")
    curb-weight = st.text_input("curb-weight","Type Here")
    engine-size = st.text_input("engine-size","Type Here")
    highway-mpg = st.text_input("highway-mpg","Type Here")
    result=""
    if st.button("Predict"):
        result=predict_autmobile_price(horsepower,curb-weight,engine-size,highway-mpg)
    st.success('The output is {}'.format(result))
    if st.button("About"):
        st.text("Lets LEarn")
        st.text("Built with Streamlit")
  
    #int_features = [int(x) for x in request.form.values()]
    #final_features = [np.array(int_features)]
    #prediction = model.predict(final_features)

    #output = round(prediction[0], 2)

    #return render_template('index.html', prediction_text='automobile price should be $ {}'.format(output))


if __name__=='__main__':
    main()
