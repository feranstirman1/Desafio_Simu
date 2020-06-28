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

		''' IMAGES FOR PAGE TWO '''
		self.dominioBgImg = PhotoImage(file = "resources/dominio/dominioBG.png")
		self.dominioImg = PhotoImage(file = "resources/dominio/dominio.png")
		self.dominioButtonImg = PhotoImage(file = "resources/dominio/dominioButton.png")

		''' IMAGES FOR PAGE THREEE '''
		self.mallaBgImg = PhotoImage(file = "resources/malla/mallaBG.png")
		self.mallaImg = PhotoImage(file = "resources/malla/malla.png")
		self.mallaButtonImg = PhotoImage(file = "resources/malla/mallaButton.png")

		''' IMAGES FOR PAGE FOUR '''
		self.condicionesBgImg = PhotoImage(file= "resources/condiciones/condicionesBG.png")
		self.condicion1Img = PhotoImage(file="resources/condiciones/condicion1.png")
		self.condicion2Img = PhotoImage(file="resources/condiciones/condicion2.png")
		self.condicionesButtonImg = PhotoImage(file="resources/condiciones/condicionesButton.png")

		##########################################################################################################################

		#Setup Frame
		container = Frame(self)
		container.pack(side="top", fill="both", expand=True)
		container.grid_rowconfigure(0, weight=1)
		container.grid_columnconfigure(0, weight=1)

		self.frames = {}

		for F in (StartPage, PageOne, PageTwo,PageThree,PageFour,PageFive,PageSix):
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

		self.controller = controller

		#creating the canvas
		self.canvas = Canvas(self,width=1000,height=600)
		self.canvas.pack()
		
		''' placing the images onto the canvas '''
		dominioBG = self.canvas.create_image(500,300,image = controller.dominioBgImg)
		casaIcon = self.canvas.create_image(159,75,image= controller.casaImg)
		flechaIcon = self.canvas.create_image(900,550,image = controller.flechaImg)
		dominioButton = self.canvas.create_image(350 , 75 + 100/2 , image = controller.dominioButtonImg)

		self.dominioImage = self.canvas.create_image(1300,300,image = controller.dominioImg)

		''' Binding the buttons on the canvas to perform their respective actions '''
		self.canvas.tag_bind(casaIcon,"<Button-1>",self.changeToStartPage)
		self.canvas.tag_bind(flechaIcon,"<Button-1>",self.changeToPageThree)
		self.canvas.tag_bind(dominioButton,"<Button-1>",self.mostrarDominio)

	def mostrarDominio(self,event):
		self.moverHorizontal(self.dominioImage,550,"left")


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
	
	def changeToStartPage(self,event):
		self.controller.show_frame(StartPage)

	def changeToPageThree(self,event):
		self.controller.show_frame(PageThree)

class PageThree(Frame):
	def __init__(self, parent, controller):
		Frame.__init__(self, parent)

		self.controller = controller

		#creating the canvas
		self.canvas = Canvas(self,width=1000,height=600)
		self.canvas.pack()
		
		''' placing the images onto the canvas '''
		mallaBG = self.canvas.create_image(500,300,image = controller.mallaBgImg)
		mallaButton = self.canvas.create_image(500,300,image = controller.mallaButtonImg)

		casaIcon = self.canvas.create_image(159,75,image= controller.casaImg)
		flechaIcon = self.canvas.create_image(900,550,image = controller.flechaImg)

		self.malla = self.canvas.create_image(500,900,image = controller.mallaImg)

		''' Binding buttons '''
		self.canvas.tag_bind(mallaButton,"<Button-1>",self.mostrarMalla)
		self.canvas.tag_bind(casaIcon,"<Button-1>",self.changeToStartPage)
		self.canvas.tag_bind(flechaIcon,"<Button-1>",self.changeToPageFour)
	
	def mostrarMalla(self,event):
		self.moverArriba(self.malla,400)

	def changeToStartPage(self,event):
		self.controller.show_frame(StartPage)

	def changeToPageFour(self,event):
		self.controller.show_frame(PageFour)

	def moverArriba(self,item,posicionFinal):
		yspeed=-1
		pos =  self.canvas.coords(item)
		while(pos[1] > posicionFinal):
			self.canvas.move(item,0,yspeed)
			pos = self.canvas.coords(item)
			self.controller.update()
			time.sleep(0.001)


class PageFour(Frame):
	def __init__(self, parent, controller):
		Frame.__init__(self, parent)

		self.controller = controller

		#creating the canvas
		self.canvas = Canvas(self,width=1000,height=600)
		self.canvas.pack()
		
		''' placing the images onto the canvas '''
		condicionesBG = self.canvas.create_image(500,300,image = controller.condicionesBgImg)
		mallaButton = self.canvas.create_image(100,400,image = controller.condicionesButtonImg)
		condicion1 = self.canvas.create_image(500,400,image = controller.condicion1Img)
		self.condicion2 = self.canvas.create_image(1500,400,image = controller.condicion2Img)

		casaIcon = self.canvas.create_image(159,75,image= controller.casaImg)
		flechaIcon = self.canvas.create_image(900,550,image = controller.flechaImg)

		''' Binding buttons '''
		self.canvas.tag_bind(mallaButton,"<Button-1>",self.cambiarCondicion)
		self.canvas.tag_bind(casaIcon,"<Button-1>",self.changeToStartPage)
		self.canvas.tag_bind(flechaIcon,"<Button-1>",self.changeToPageFive)

	def changeToStartPage(self,event):
		self.controller.show_frame(StartPage)

	def changeToPageFive(self,event):
		self.controller.show_frame(PageFive)

	def cambiarCondicion(self,event):
		pos = self.canvas.coords(self.condicion2)
		if(pos[0]<1500):
			self.moverHorizontal(self.condicion2,1500,"right")
		else:
			self.moverHorizontal(self.condicion2,500,"left")


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

class PageFive(Frame):
	def __init__(self, parent, controller):
		Frame.__init__(self, parent)

class PageSix(Frame):
	def __init__(self, parent, controller):
		Frame.__init__(self, parent)		



app = App()
app.title("Desafio MEF en 3D")
app.geometry('1000x600+200+100')
app.resizable(False,False)
app.mainloop()