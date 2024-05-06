from fastapi import FastAPI
from pydantic import BaseModel
import os
from langchain_community.llms import Tongyi
from langchain_community.utilities import SQLDatabase
from langchain_experimental.sql import SQLDatabaseChain

class Question(BaseModel):
    question: str

app = FastAPI()

def chain_tongyi(question):
    llm = Tongyi(model='qwen-turbo')

    # Database info
    db_info = {
        'host': '',
        'name': '',
        'user': '',
        'password': ''
    }

    db = SQLDatabase.from_uri(f"mysql+pymysql://{db_info['user']}:{db_info['password']}@{db_info['host']}/{db_info['name']}")
    db_chain = SQLDatabaseChain.from_llm(llm=llm, db=db, verbose=True, use_query_checker=False)

    response = db_chain.invoke(question)
    print('>> Question:', question)
    print('>> Answer:', response)
    return response

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/chain_tongyi")
def chain_tongyi_endpoint(question: Question):
    # Set the API key
    os.environ["DASHSCOPE_API_KEY"] = ""
    return chain_tongyi(question.question)