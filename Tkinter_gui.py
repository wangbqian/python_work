from tkinter import *
import tkinter.messagebox as messagebox
class Applicaton(Frame):
    def __init__(self,master=None):
        Frame.__init__(self,master)
        self.pack()
        self.createWindgets()

    # def createWindgets(self):
    #     self.helloLabel = Label(self,text='Hello World!')
    #     self.helloLabel.pack()
    #     self.quitButton = Button(self,text='Quit',command=self.quit)
    #     self.quitButton.pack()
    def createWindgets(self):
        self.nameInput = Entry(self)
        self.nameInput.pack()
        self.alertButton = Button(self,text='Hello',command=self.hello)
        self.alertButton.pack()
        
    def hello(self):
        name = self.nameInput.get() or 'World'
        messagebox.showinfo('Message','Hello,%s' % name)




app = Applicaton()

app.master.title('Hello')
app.mainloop()