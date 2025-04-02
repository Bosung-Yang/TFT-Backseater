from langchain_openai import ChatOpenAI
from langchain_core.prompts.few_shot import FewShotPromptTemplate
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
from langchain_text_splitters import CharacterTextSplitter
from langchain_community.document_loaders import TextLoader
from langchain_core.prompts import PromptTemplate

import mykey
import os
os.environ['OPENAI_API_KEY'] = mykey.my_openai()

from langchain_openai import ChatOpenAI

model = ChatOpenAI(
    model="gpt-4o",
    max_tokens=2048,
    temperature=0.1,
)

from langchain_community.document_loaders import TextLoader

loader = TextLoader('data/patchnote.txt')
docs = loader.load()

from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
import os
import mykey
from langchain_text_splitters import CharacterTextSplitter

text_splitter = CharacterTextSplitter(chunk_size=10, chunk_overlap=0)
embeddings = OpenAIEmbeddings()
split_docs = text_splitter.split_documents(docs)
db = FAISS.from_documents(split_docs, embeddings)
retreieved = db.as_retriever()
prompt = PromptTemplate.from_template(
    """You are an assistant for a popular game called Teamfight Tactics. You are asked to provide information about the latest patch notes.

#Question: 
{question} 
#Context: 
{context} 

#Answer:"""
)

chain = (
    {"context" : retreieved, "question": RunnablePassthrough()} | prompt| model)

#chain = ( {"context" : retreieved, "question": RunnablePassthrough()} | prompt)

#print(chain)
answer = chain.invoke("context에 들어가있는 내용을 바탕으로 4코스트 쳄피언인 Elise 변경사항 알려주세요")
print(answer.content)
print(retreieved.invoke("Elise 변경사항")[0])
