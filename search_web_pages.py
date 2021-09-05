import webbrowser
from ttkthemes import ThemedTk,THEMES
from tkinter import ttk


window = ThemedTk(theme = True)
window.set_theme('ubuntu')

def search():

    webbrowser.open_new('https://www.youtube.com/')


button = ttk.Button(window,text = 'Youtube',width = 20,command = search)
button.pack()


def click():

    webbrowser.open_new_tab('https://www.youtube.com/watch?v=yQSEXcf6s2I&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV')
    
    

button1 = ttk.Button(window,text = 'codemy.com',width = 20,command = click)
button1.pack()

def pypi():

    webbrowser.open('https://pypi.org/')

button3 = ttk.Button(window,text = 'pypi packages',width = 20,command = pypi)
button3.pack()

def matplotlib():

    webbrowser.open('https://matplotlib.org/stable/index.html')


button4 = ttk.Button(window,text = 'matplotlib',width = 20,command = matplotlib)
button4.pack()


def turtle():

    webbrowser.open('https://docs.python.org/3/library/turtle.html#:~:text=The%20turtle%20module%20is%20an,)%20100%25%20compatible%20with%20it.')

button5 = ttk.Button(window,text = 'turtle of python',width = 20,command = turtle)
button5.pack()


entry2 = ttk.Entry(window,width =30)
entry2.insert(0,'Enter location')
entry2.pack(pady = 10)

entry2.focus()

def location():

    webbrowser.open('https://www.google.lk/maps/@6.8263597,79.9528444,15z/search?q=' + entry2.get())


button6 = ttk.Button(window,text = 'Find your location',command = location)
button6.pack()


entry1 = ttk.Entry(window,width =30)
entry1.insert(0,'Google')
entry1.pack(pady = 10)


def ok():
    
    webbrowser.open('https://www.google.com/search?q='+entry1.get())

button2 = ttk.Button(window,text = 'Search',width = 20,command = ok)
button2.pack()



window.mainloop()
