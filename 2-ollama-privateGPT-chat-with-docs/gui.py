from tkinter import *
from tkinter import ttk
import requests
import json

def ollama():
    url = "http://localhost:11434/api/generate"
    #url = "https://ollamaproject.com/api/ask"
    headers = {"Content-Type": "application/json"}
    data = {"prompt": entry.get(), "model": "magiq-m0", "stream": False}
    response = requests.post(url, data=json.dumps(data), headers=headers)
    response_dict = json.loads(response.text)
    answer = response_dict["response"]
    text_area.insert(END, "Answer: {}\n".format(answer))
                     
#def raw_ollama():
#    url = "http://localhost:11434/api/generate"
#    #url = "https://ollamaproject.com/api/ask"
#    headers = {"Content-Type": "application/json"}
#    data = {"prompt": entry.get(), "model": "mistral", "raw": True, "stream": False}
#    response = requests.post(url, data=json.dumps(data), headers=headers)
#    response_dict = json.loads(response.text)
#    raw_answer = response_dict["raw_answer"]
#    text_area.insert(END, "Answer: {}\n".format(raw_answer))

# create the main window of the program with title and size
win = Tk()
win.title("Ollama Bot")
win.geometry('750x250')

#Create an Entry Widget
entry= ttk.Entry(win,font=('Century 12'),width=50)
entry.pack(pady= 30)

Label(text="Answer:").pack()

# create the text area to show response
text_area = Text(win, height=10, width=50)
text_area.pack()
# create a button to call Ollama API with raw=False
Button(text="Submit", command=ollama).pack()
#Button(text="Raw Mode", command=raw_ollama).pack()

# run the main loop of the program to show it on screen
win.mainloop()