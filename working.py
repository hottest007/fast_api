#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"Data": "Test"}


