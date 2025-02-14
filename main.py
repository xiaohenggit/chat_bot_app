"""
@file name  : main.py
@author     : XiaoHeng
@date       : 2025-2-10
@brief      : APP building with a GUI
"""
from rag_lib import RAG
from tkinter import *
import argparse

# model='deepseek-r1:latest'
def main():
  parser = argparse.ArgumentParser()
  parser.add_argument('--model', default='deepseek-r1:latest', type=str, required=False, help='Model')

  args = parser.parse_args()
  print('args:\n' + args.__repr__())

  opt = parser.parse_args()
  model = opt.model

  # ------------------------------------GUI-----------------------------------
  # GUI
  root = Tk()
  root.title("Chatbot")

  # style
  BG_GRAY = "#ABB2B9"
  BG_COLOR = "#17202A"
  TEXT_COLOR = "#EAECEE"

  FONT = "Helvetica 14"
  FONT_BOLD = "Helvetica 13 bold"

  # Send function
  def send():
    send = "You -> " + e.get()
    txt.insert(END, "\n" + send)

    input_ms = e.get().lower()

    if input_ms:
      # txt.insert(END, "\n" + "Bot -> Hi there, how can I help?")
      response = RAG(model, input_ms)
      txt.insert(END, "\n" + "Bot -> " + response)

    elif (input_ms == "exit"):
      txt.insert(END, "\n" + "Bot -> Have a nice day!")

    e.delete(0, END)

  lable1 = Label(root, bg=BG_COLOR, fg=TEXT_COLOR, text="Welcome", font=FONT_BOLD, pady=10, width=20, height=1).grid(
    row=0)

  txt = Text(root, bg=BG_COLOR, fg=TEXT_COLOR, font=FONT, width=60)
  txt.grid(row=1, column=0, columnspan=2)

  scrollbar = Scrollbar(txt)
  scrollbar.place(relheight=1, relx=0.974)

  e = Entry(root, bg="#2C3E50", fg=TEXT_COLOR, font=FONT, width=55)
  e.grid(row=2, column=0)

  send = Button(root, text="Send", font=FONT_BOLD, bg=BG_GRAY,
                command=send).grid(row=2, column=1)

  root.mainloop()
  # ------------------------------------GUI-----------------------------------


if __name__ == '__main__':
    main()