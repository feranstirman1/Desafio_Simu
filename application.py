from tkinter import *
import time

class App(Tk):
	def __init__(self, *args, **kwargs):
		Tk.__init__(self, *args, **kwargs)

		###################ALL THE IMAGES THAT THE APPLICATION WILL USE############################################################
		''' IMAGES FOR THE START PAGE '''
		self.bgImg = PhotoImage(file="resources/startPage/homepage.png")
		self.bgnImg = PhotoImage(file="resources/startPage/beginButton.png")
		self.qtImg = PhotoImage(file="resources/startPage/quitButton.png")

		''' IMAGES FO PAGE ONE '''
		self.modelImg = PhotoImage(file = "resources/model/modeloBG.png")
		self.mostrarImg = PhotoImage(file = "resources/model/mostrarButton.png")
		self.casaImg = PhotoImage(file = "resources/model/casa.png")
		self.ecuacionesBgImg = PhotoImage(file = "resources/model/ecuacionesBG.png")
		self.ecuacion1Img = PhotoImage(file = "resources/model/ecuacion1.png")
		self.ecuacion2Img = PhotoImage(file = "resources/model/ecuacion2.png")
		self.flechaImg = PhotoImage(file="resources/model/flecha.png")
		##########################################################################################################################

		#Setup Frame
		container = Frame(self)
		container.pack(side="top", fill="both", expand=True)
		container.grid_rowconfigure(0, weight=1)
		container.grid_columnconfigure(0, weight=1)

		self.frames = {}

		for F in (StartPage, PageOne, PageTwo):
			frame = F(container, self)
			self.frames[F] = frame
			frame.grid(row=0, column=0, sticky="nsew")

		self.show_frame(StartPage)	
	def show_frame(self, context):
		frame = self.frames[context]
		frame.tkraise()


class StartPage(Frame):
	def __init__(self, parent, controller):
		Frame.__init__(self, parent)

		self.controller = controller

		#creating the canvas
		self.canvas = Canvas(self,width=1000,height=600)
		self.canvas.pack()
		''' placing the images onto the canvas '''
		bgImage = self.canvas.create_image(500,300,image = controller.bgImg)
		beginImage = self.canvas.create_image(500,370,image = controller.bgnImg)
		quitImage = self.canvas.create_image(500,450,image = controller.qtImg)

		self.canvas.tag_bind(beginImage,"<Button-1>", self.changeToPageOne)
		self.canvas.tag_bind(quitImage,"<Button-1>",self.quitApp)

	def changeToPageOne(self,event):
		self.controller.show_frame(PageOne)

	def quitApp(self,event):
		self.controller.destroy()

class PageOne(Frame):
	def __init__(self, parent, controller):
		Frame.__init__(self, parent)

		self.controller = controller

		#creating the canvas
		self.canvas = Canvas(self,width=1000,height=600)
		self.canvas.pack()

		''' placing the images onto the canvas '''
		modelBG = self.canvas.create_image(500,300,image = controller.modelImg)
		mostrarButton = self.canvas.create_image(500,550,image = controller.mostrarImg)
		casaIcon = self.canvas.create_image(70,75,image= controller.casaImg)
		flechaIcon = self.canvas.create_image(900,550,image = controller.flechaImg)
		self.ecuacionesBG = self.canvas.create_image(500,800,image = controller.ecuacionesBgImg)
		self.ecuacion1Image = self.canvas.create_image(-500,300,image = controller.ecuacion1Img)
		self.ecuacion2Image = self.canvas.create_image(1500,400,image = controller.ecuacion2Img)

		''' Binding the buttons on the canvas to perform their respective actions '''
		self.canvas.tag_bind(mostrarButton,"<Button-1>",self.mostrarEcuaciones)
		self.canvas.tag_bind(casaIcon,"<Button-1>",self.changeToStartPage)
		self.canvas.tag_bind(flechaIcon,"<Button-1>",self.changeToPageTwo)
	
	def changeToStartPage(self,event):
		self.controller.show_frame(StartPage)

	def changeToPageTwo(self,event):
		self.controller.show_frame(PageTwo)
	
	def moverArriba(self,item,posicionFinal):
		yspeed=-5
		pos =  self.canvas.coords(item)
		while(pos[1] > posicionFinal):
			self.canvas.move(item,0,yspeed)
			pos = self.canvas.coords(item)
			self.controller.update()
			time.sleep(0.003)
	
	def moverHorizontal(self,item,posicionFinal,direccion):
		if(direccion == "left"):
			xspeed = -10
			pos = self.canvas.coords(item)
			while(pos[0] > posicionFinal):
				self.canvas.move(item,xspeed,0)
				pos = self.canvas.coords(item)
				self.controller.update()
				time.sleep(0.001)
		else:
			xspeed = 7
			pos = self.canvas.coords(item)
			while(pos[0] < posicionFinal):
				self.canvas.move(item,xspeed,0)
				pos = self.canvas.coords(item)
				self.controller.update()
				time.sleep(0.001)

	def mostrarEcuaciones(self,event):
		self.moverArriba(self.ecuacionesBG,350)
		self.moverHorizontal(self.ecuacion1Image,500,"right")
		self.moverHorizontal(self.ecuacion2Image,500,"left")

class PageTwo(Frame):
	def __init__(self, parent, controller):
		Frame.__init__(self, parent)

		label = Label(self, text="Page Two")
		label.pack(padx=10, pady=10)
		start_page = Button(self, text="Start Page", command=lambda:controller.show_frame(StartPage))
		start_page.pack()
		page_one = Button(self, text="Page One", command=lambda:controller.show_frame(PageOne))
		page_one.pack()


app = App()
app.title("Desafio MEF en 3D")
app.geometry('1000x600+200+100')
app.resizable(False,False)
app.mainloop()