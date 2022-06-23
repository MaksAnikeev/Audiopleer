from tkinter import *
from tkinter import filedialog as fd

from pygame import mixer

mixer.init()

root = Tk()
frame = Frame(root,  bg = 'black')
frame.pack()

info_frame = Frame(frame,  bg = 'black')
controls_frame = Frame(frame,  bg = 'black')
file_frame = Frame(frame,  bg = 'black')

info_frame.grid(row = 0, column = 0)
controls_frame.grid(row = 1, column = 0)
file_frame.grid(row = 0, column = 5)

label = Label(info_frame, width = 51, text = 'Остановлено',  bg = 'white')
label.pack()
list = Listbox(info_frame, width = 60, height = 10, selectbackground="blue", selectmode = SINGLE,  bg = 'grey')
list.pack()

def play():
    chose1 = list.curselection()
    song = list_name[chose1[0]]
    mixer.music.load(song)
    mixer.music.play()
    label['text'] = 'Воспроизведение'

def stop():
    mixer.music.stop()
    label['text'] = 'Остановлено'
    list.selection_clear(ACTIVE)

def pause():
    if label['text'] == 'Воспроизведение':
        mixer.music.pause()
        label['text'] = 'Пауза'
    elif label['text'] == 'Пауза':
        mixer.music.unpause()
        label['text'] = 'Воспроизведение'

def next():
    chose = list.curselection()
    chose = chose[0] + 1
    song = list_name[chose]
    mixer.music.load(song)
    mixer.music.play()
    list.selection_clear(0, END)
    list.activate(chose)
    list.select_set(chose, last = None)

def back():
    chose = list.curselection()
    chose = chose[0] - 1
    song = list_name[chose]
    mixer.music.load(song)
    mixer.music.play()
    list.selection_clear(0, END)
    list.activate(chose)
    list.select_set(chose, last = None)

but1 = Button(controls_frame, text = '<-', width = 5, command = back, bg = 'white')
but2 = Button(controls_frame, text = '->', width = 5, command = next, bg = 'white')
but3 = Button(controls_frame, text = '|>', width = 5, command = play, bg = 'white')
but4 = Button(controls_frame, text = '||', width = 5, command = pause, bg = 'white')
but5 = Button(controls_frame, text = '[]', width = 5, command = stop, bg = 'white')

but1.pack(side=LEFT)
but2.pack(side=LEFT)
but3.pack(side=LEFT)
but4.pack(side=LEFT)
but5.pack(side=LEFT)

list_name = []
def open():
    file = fd.askopenfilename(initialdir='tracks/', title="Выберите песню!", filetypes=(("mp3 Files", "*.mp3"),))
    list_name.append(file)
    file_name = str(file)
    file_name = file_name.split('/')
    file_name = file_name[-1]
    file_name = file_name.partition('.')[0]
    list.insert(END, file_name)

def opens():
    files = fd.askopenfilenames(initialdir='tracks/', title="Выберите песню!", filetypes=(("mp3 Files", "*.mp3"),))
    for i in files:
        list_name.append(i)
        file_name = str(i)
        file_name = file_name.split('/')
        file_name = file_name[-1]
        file_name = file_name.partition('.')[0]
        list.insert(END, file_name)

button = Button(file_frame, text = 'Открыть файл', command = open)
button1 = Button(file_frame, text = 'Несколько файлов', command = opens)

button.pack(side=TOP)
button1.pack(side=TOP)

root.mainloop()
