import os
from langchain_community.llms import Tongyi

from langchain_community.utilities import SQLDatabase
from langchain_experimental.sql import SQLDatabaseChain


def chain_tongyi(db_info):
    llm = Tongyi(model='qwen-turbo')

    db = SQLDatabase.from_uri(f"mysql+pymysql://{db_info['user']}:{db_info['password']}@{db_info['host']}/{db_info['name']}")
    db_chain = SQLDatabaseChain.from_llm(llm=llm, db=db, verbose=True, use_query_checker=False)

    #你的问题
    questions = ""
    response = db_chain.invoke(questions)
    print('>>问题：', questions)

    print('>>answer:', response)

if __name__ == "__main__":
    # 这里替换为你的api-key
    os.environ["DASHSCOPE_API_KEY"] = ""
    db_info = {
        # host：数据库地址，name：数据库名，user：用户名，password：密码
        'host': '',
        'name': '',
        'user': '',
        'password': ''
    }

    chain_tongyi(db_info)