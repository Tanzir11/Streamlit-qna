from fastapi import APIRouter
from .dto import ChatBotParam
from .services import user_query

def Chat_bot(Question, session_ID):
    return user_query.chat_response(Question, session_ID)