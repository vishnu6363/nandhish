
import pickle
import streamlit as st
import numpy as np
import pandas as pd
# from flask import jsonify
import json

# loding the saved model
house_price = pickle.load(open('banglore_house_price_model.pkl', 'rb'))

# silde bar for navigation




__locations = None
__data_columns = None
__model = None
with open("columns.json") as f:
    __data_columns = json.load(f)['data_columns']
    __location = __data_columns[3:]

data = pd.read_csv('Bengaluru_House_Data.csv')
loc = data['location'].unique()


def house_prices(location, sqt, bhk, bath):
    try:
        loc_index = __data_columns.index(location.lower())
    except:
        loc_index = -1

    # loc_index = np.where(X.columns==location)[0][0]
    x = np.zeros(243)
    x[0] = sqt
    x[1] = bath
    x[2] = bhk

    if loc_index >= 0:
        x[loc_index] = 1

    return round(house_price.predict([x])[0], 3)


'''-------------------------------------------------------------------'''


def main():
    st.title('Hi Welcome to Bangalore')

    location = st.selectbox('Enter the location', loc)
    sqt = st.text_input("Enter the squrefeet")
    bath = st.text_input("Enter the number of Bathroom")
    bhk = st.text_input("Enter the number of BHK")
    result = ''

    if st.button('House Price in laks'):
        result = house_prices(location, sqt, bhk, bath)
    st.success("The Final Price in INR {} \-".format(result))


if __name__ == '__main__':
    main()