"""
@file name  : rag_lib.py
@author     : XiaoHeng
@date       : 2025-2-10
@brief      : implement the chatbot based on ollama
"""
import ollama
from ollama import chat
from ollama import ChatResponse, ResponseError

# ------------------------------------RAG-----------------------------------
def RAG(model, user_input):
  try:
    response: ChatResponse = chat(model=model, messages=[
      {
        'role': 'user',
        'content': user_input,  # example 'content': '你是谁？',
      },
    ])
  except ResponseError as e:
    print('Error:', e.error)
    if e.status_code == 404:
      ollama.pull(model)


  return response['message']['content'] # response to query

# Command window interaction
# while True:
#     user_input = input("You: ")
#     # If the user types "exit", exit the loop
#     if user_input == "exit":
#         break
#     response = RAG(user_input)
#     print(response)
# ------------------------------------RAG-----------------------------------