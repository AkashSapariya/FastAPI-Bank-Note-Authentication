#!/usr/bin/env python
# coding: utf-8

# In[3]:


# importing Required Libraries

import uvicorn #ASGI( Asynchronous Server Gateway Interface)
from fastapi import FastAPI
import pickle
import numpy as np
import pandas as pd
from BankNotes import BankNote


# In[4]:


# Create the app object

app = FastAPI()
pickle_in = open('classifier.pkl', 'rb')
classifier = pickle.load(pickle_in)


# In[6]:


# Index, Route, opens automatically on http://127.0.0.1:8000

@app.get('/')

def index():
    return {'message': 'Hello, World'}


# In[7]:


# Route with a single parameter, returns the parameter with a message 
# located at: http://127.0.0.1:8000/AnyNameHere

@app.get('/{name}')

def get_name(name: str):
    return {'Message': f'Hello, {name}'}


# In[8]:


# Expose the prediction functionality, make a prediction from the pass
# JSON data and return the predicted Bank Note with the confidence/probability

@app.post('/predict')

def predict_banknote(data: BankNote):
    data = data.dict()
    variance = data['variance']
    skewness = data['skewness']
    curtosis = data['curtosis']
    entropy = data['entropy']
    
    prediction = classifier.predict([[variance,skewness,curtosis,entropy]])
    if(prediction[0] > 0.5):
        prediction = "Fake Note"
    else:
        prediction = "Its a Bank Note"
    return {
        'Prediction': prediction
    }
    


# In[ ]:


# Run the API with uvicorn
# it will run on http://127.0.0.1:8000

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)

# uvicorn app:app --reload    

