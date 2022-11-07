#!/usr/bin/env python
# coding: utf-8

# In[2]:


# pydantic is a data validation and settings management using python tyope annotation
# pydantic enforces type hints at runtime and provides user friendly errors when data is invalid


from pydantic import BaseModel   

# Class Which describes Bank Noes Measurements:

class BankNote(BaseModel):
    variance: float
    skewness: float
    curtosis: float
    entropy: float

