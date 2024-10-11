from langchain.chains import LLMChain, RetrievalQA

from .prompts import prompt_template, contextualize_q_system_prompt
from vendors.Openai import model, embeddings

from langchain_community.vectorstores.azure_cosmos_db import AzureCosmosDBVectorSearch
from vendors.Mongodb import collection
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain.chains import create_history_aware_retriever
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains import create_retrieval_chain
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_core.chat_history import BaseChatMessageHistory
from langchain.prompts import PromptTemplate
from configs import INDEX_NAME, NAMESPACE, CONNECTION_STRING

store = {}
def get_session_history(session_id: str) -> BaseChatMessageHistory:
    if session_id not in store:
        store[session_id] = ChatMessageHistory()
    return store[session_id]

def Qna_query(question,session_number):
    config = {"configurable": {"session_id": session_number}}
    contextualize_q_prompt = ChatPromptTemplate.from_messages(
        [
            ("system", contextualize_q_system_prompt),
            MessagesPlaceholder("chat_history"),
            ("human", "{input}"),
            ]
            )
    vectorstore = AzureCosmosDBVectorSearch.from_connection_string(CONNECTION_STRING, NAMESPACE, embeddings, index_name=INDEX_NAME)
    qa_retriever = vectorstore.as_retriever(
        search_type="similarity",
        search_kwargs={"k": 1})
    history_aware_retriever = create_history_aware_retriever(
        model, qa_retriever, contextualize_q_prompt
        )
    prompt = PromptTemplate(
        template=prompt_template,
        input_variables=["context"],
        MessagesPlaceholder=("history")
        )
    question_answer_chain = create_stuff_documents_chain(model, prompt)
    rag_chain = create_retrieval_chain(history_aware_retriever, question_answer_chain)
    conversational_rag_chain = RunnableWithMessageHistory(
        rag_chain,
        get_session_history,
        input_messages_key="input",
        history_messages_key="history",
        output_messages_key="answer",
        )
    llm_resp = conversational_rag_chain.invoke(
        {"input": question},
        config=config)
    data = llm_resp['answer']
    return data