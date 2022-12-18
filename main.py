import PySimpleGUI as sg
import os
import PyPDF2
import pyttsx3


layout = [
    [sg.Text("Image File"),
        sg.Input(size=(40, 1)),
        sg.FileBrowse(key="-FILE-", file_types=("PDF Document", "*.pdf"), ),
        sg.Button("Load and read pdf file", key="-LOAD-")]
]
window = sg.Window('Window Title', layout)
speak = pyttsx3.init()
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel':
        break
    if event == "-LOAD-":
        if os.path.exists(values["-FILE-"]):
            pdf = open(values["-FILE-"], "rb")
            reader = PyPDF2.PdfReader(pdf)
            no_of_pages = len(reader.pages)
            for page in range(no_of_pages):
                current_page = reader.pages[page]
                text = current_page.extractText()
                speak.say(text)
                speak.runAndWait()





