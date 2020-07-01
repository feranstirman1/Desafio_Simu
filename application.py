from tkinter import *
import time

class App(Tk):
	def __init__(self, *args, **kwargs):
		Tk.__init__(self, *args, **kwargs)

		################### ALL THE IMAGES THAT THE APPLICATION WILL USE ############################################################
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

		''' IMAGES FOR PAGE FIVE '''
		self.tablaBgImg = PhotoImage(file="resources/tabla/tablaBG.png")
		self.tablaImg = PhotoImage(file="resources/tabla/tabla.png")
		self.tablaButtonImg = PhotoImage(file="resources/tabla/tablaButton.png")

		''' IMAGES FOR PAGE SIX '''
		self.pasosBgImg = PhotoImage(file="resources/pasos/pasosBG.png")
		self.pasos1ButtonImg = PhotoImage(file="resources/pasos/paso1Button.png")
		self.pasos2ButtonImg = PhotoImage(file="resources/pasos/paso2Button.png")
		self.pasos3ButtonImg = PhotoImage(file="resources/pasos/paso3Button.png")
		self.pasos4ButtonImg = PhotoImage(file="resources/pasos/paso4Button.png")
		self.pasos5ButtonImg = PhotoImage(file="resources/pasos/paso5Button.png")
		self.pasos6ButtonImg = PhotoImage(file="resources/pasos/paso6Button.png")
		self.paso1Img = PhotoImage(file="resources/pasos/paso1.png")
		self.paso2Img = PhotoImage(file="resources/pasos/paso2.png")
		self.paso3Img = PhotoImage(file="resources/pasos/paso3.png")
		self.paso4Img = PhotoImage(file="resources/pasos/paso4.png")
		self.paso5Img = PhotoImage(file="resources/pasos/paso5.png")
		self.paso6Img = PhotoImage(file="resources/pasos/paso6.png")

		''' IMAGES FOR PAGE SEVEN '''
		self.componentesBgImg = PhotoImage(file = "resources/componentes/componentesBG.png")
		self.parte1Img = PhotoImage(file = "resources/componentes/parte1.png")
		self.parte2Img = PhotoImage(file = "resources/componentes/parte2.png")
		self.parte3Img = PhotoImage(file = "resources/componentes/parte3.png")
		self.parte4Img = PhotoImage(file = "resources/componentes/parte4.png")
		self.parte5Img = PhotoImage(file = "resources/componentes/parte5.png")
		self.parte6Img = PhotoImage(file = "resources/componentes/parte6.png")
		self.parte1ButtonImg = PhotoImage(file = "resources/componentes/parte1Button.png")
		self.parte2ButtonImg = PhotoImage(file = "resources/componentes/parte2Button.png")
		self.parte3ButtonImg = PhotoImage(file = "resources/componentes/parte3Button.png")
		self.parte4ButtonImg = PhotoImage(file = "resources/componentes/parte4Button.png")
		self.parte5ButtonImg = PhotoImage(file = "resources/componentes/parte5Button.png")
		self.parte6ButtonImg = PhotoImage(file = "resources/componentes/parte6Button.png")

		##########################################################################################################################

		#Setup Frame
		container = Frame(self)
		container.pack(side="top", fill="both", expand=True)
		container.grid_rowconfigure(0, weight=1)
		container.grid_columnconfigure(0, weight=1)

		self.frames = {}

		for F in (StartPage, PageOne, PageTwo,PageThree,PageFour,PageFive,PageSix,PageSeven,PageEight):
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

		self.controller = controller

		#creating the canvas
		self.canvas = Canvas(self,width=1000,height=600)
		self.canvas.pack()

		''' placing the images onto the canvas '''
		tablaBG = self.canvas.create_image(500,300,image = controller.tablaBgImg)
		tablaButton = self.canvas.create_image(100,400,image = controller.tablaButtonImg)
		self.tabla = self.canvas.create_image(500,900,image = controller.tablaImg)

		casaIcon = self.canvas.create_image(159,75,image= controller.casaImg)
		flechaIcon = self.canvas.create_image(900,550,image = controller.flechaImg)

		''' Binding buttons '''
		self.canvas.tag_bind(tablaButton,"<Button-1>",self.mostrarTabla)
		self.canvas.tag_bind(casaIcon,"<Button-1>",self.changeToStartPage)
		self.canvas.tag_bind(flechaIcon,"<Button-1>",self.changeToPageSix)

	def changeToStartPage(self,event):
		self.controller.show_frame(StartPage)

	def changeToPageSix(self,event):
		self.controller.show_frame(PageSix)

	def mostrarTabla(self,event):
		self.moverArriba(self.tabla,375)

	def moverArriba(self,item,posicionFinal):
		yspeed=-1
		pos =  self.canvas.coords(item)
		while(pos[1] > posicionFinal):
			self.canvas.move(item,0,yspeed)
			pos = self.canvas.coords(item)
			self.controller.update()
			time.sleep(0.001)

class PageSix(Frame):
	def __init__(self, parent, controller):
		Frame.__init__(self, parent)		

		self.controller = controller

		#helper variables to help with the animations
		self.currentStep = 1

		#creating the canvas
		self.canvas = Canvas(self,width=1000,height=600)
		self.canvas.pack()

		''' placing the images onto the canvas '''
		pasosBG = self.canvas.create_image(500,300,image = controller.pasosBgImg)
		paso1Button = self.canvas.create_image(100,130,image = controller.pasos1ButtonImg)
		paso2Button = self.canvas.create_image(100,205,image = controller.pasos2ButtonImg)
		paso3Button = self.canvas.create_image(100,280,image = controller.pasos3ButtonImg)
		paso4Button = self.canvas.create_image(100,355,image = controller.pasos4ButtonImg)
		paso5Button = self.canvas.create_image(100,355+75,image = controller.pasos5ButtonImg)
		paso6Button = self.canvas.create_image(100,355+150,image = controller.pasos6ButtonImg)

		casaIcon = self.canvas.create_image(135,50,image= controller.casaImg)
		flechaIcon = self.canvas.create_image(900,60,image = controller.flechaImg)

		self.paso2 = self.canvas.create_image(1500,350,image = controller.paso2Img)
		self.paso1 = self.canvas.create_image(600,350,image = controller.paso1Img)
		self.paso3 = self.canvas.create_image(1500,350,image = controller.paso3Img)
		self.paso4 = self.canvas.create_image(1500,350,image = controller.paso4Img)
		self.paso5 = self.canvas.create_image(1500,350,image = controller.paso5Img)
		self.paso6 = self.canvas.create_image(1500,350,image = controller.paso6Img)

		''' Binding buttons '''
		self.canvas.tag_bind(paso1Button,"<Button-1>",self.mostrarPaso1)
		self.canvas.tag_bind(paso2Button,"<Button-1>",self.mostrarPaso2)
		self.canvas.tag_bind(paso3Button,"<Button-1>",self.mostrarPaso3)
		self.canvas.tag_bind(paso4Button,"<Button-1>",self.mostrarPaso4)
		self.canvas.tag_bind(paso5Button,"<Button-1>",self.mostrarPaso5)
		self.canvas.tag_bind(paso6Button,"<Button-1>",self.mostrarPaso6)

		self.canvas.tag_bind(casaIcon,"<Button-1>",self.changeToStartPage)
		self.canvas.tag_bind(flechaIcon,"<Button-1>",self.changeToPageSeven)

	def changeToStartPage(self,event):
		self.controller.show_frame(StartPage)

	def changeToPageSeven(self,event):
		self.controller.show_frame(PageSeven)
	
	def mostrarPaso1(self,event):
		if(self.currentStep == 1):
			pass
		elif(self.currentStep == 2):
			self.moverHorizontal(self.paso2,1500,"right")
		elif(self.currentStep == 3):
			self.moverHorizontal(self.paso3,1500,"right")
		elif(self.currentStep == 4):
			self.moverHorizontal(self.paso4,1500,"right")
		elif(self.currentStep == 5):
			self.moverHorizontal(self.paso5,1500,"right")
		elif(self.currentStep == 6):
			self.moverHorizontal(self.paso6,1500,"right")
		
		self.moverHorizontal(self.paso1,600,"left")
		self.currentStep = 1
	def mostrarPaso2(self,event):
		if(self.currentStep == 2):
			pass
		elif(self.currentStep == 1):
			self.moverHorizontal(self.paso1,1500,"right")
		elif(self.currentStep == 3):
			self.moverHorizontal(self.paso3,1500,"right")
		elif(self.currentStep == 4):
			self.moverHorizontal(self.paso4,1500,"right")
		elif(self.currentStep == 5):
			self.moverHorizontal(self.paso5,1500,"right")
		elif(self.currentStep == 6):
			self.moverHorizontal(self.paso6,1500,"right")	
		
		self.moverHorizontal(self.paso2,600,"left")
		self.currentStep = 2
	def mostrarPaso3(self,event):
		if(self.currentStep == 3):
			pass
		elif(self.currentStep == 2):
			self.moverHorizontal(self.paso2,1500,"right")
		elif(self.currentStep == 1):
			self.moverHorizontal(self.paso1,1500,"right")
		elif(self.currentStep == 4):
			self.moverHorizontal(self.paso4,1500,"right")
		elif(self.currentStep == 5):
			self.moverHorizontal(self.paso5,1500,"right")
		elif(self.currentStep == 6):
			self.moverHorizontal(self.paso6,1500,"right")	
		
		self.moverHorizontal(self.paso3,600,"left")
		self.currentStep = 3
	def mostrarPaso4(self,event):
		if(self.currentStep == 4):
			pass
		elif(self.currentStep == 2):
			self.moverHorizontal(self.paso2,1500,"right")
		elif(self.currentStep == 3):
			self.moverHorizontal(self.paso3,1500,"right")
		elif(self.currentStep == 1):
			self.moverHorizontal(self.paso1,1500,"right")
		elif(self.currentStep == 5):
			self.moverHorizontal(self.paso5,1500,"right")
		elif(self.currentStep == 6):
			self.moverHorizontal(self.paso6,1500,"right")	
		
		self.moverHorizontal(self.paso4,600,"left")
		self.currentStep = 4
	def mostrarPaso5(self,event):
		if(self.currentStep == 5):
			pass
		elif(self.currentStep == 2):
			self.moverHorizontal(self.paso2,1500,"right")
		elif(self.currentStep == 3):
			self.moverHorizontal(self.paso3,1500,"right")
		elif(self.currentStep == 4):
			self.moverHorizontal(self.paso4,1500,"right")
		elif(self.currentStep == 1):
			self.moverHorizontal(self.paso1,1500,"right")
		elif(self.currentStep == 6):
			self.moverHorizontal(self.paso6,1500,"right")
		
		self.moverHorizontal(self.paso5,600,"left")
		self.currentStep = 5
	def mostrarPaso6(self,event):
		if(self.currentStep == 6):
			pass
		elif(self.currentStep == 2):
			self.moverHorizontal(self.paso2,1500,"right")
		elif(self.currentStep == 3):
			self.moverHorizontal(self.paso3,1500,"right")
		elif(self.currentStep == 4):
			self.moverHorizontal(self.paso4,1500,"right")
		elif(self.currentStep == 1):
			self.moverHorizontal(self.paso1,1500,"right")
		elif(self.currentStep == 5):
			self.moverHorizontal(self.paso5,1500,"right")
		
		self.moverHorizontal(self.paso6,600,"left")
		self.currentStep = 6

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

class PageSeven(Frame):
	def __init__(self, parent, controller):
		Frame.__init__(self, parent)

		self.controller = controller

		#helper variables to help with the animations
		self.currentStep = 1

		#creating the canvas
		self.canvas = Canvas(self,width=1000,height=600)
		self.canvas.pack()

		''' placing the images onto the canvas '''
		componentesBG = self.canvas.create_image(500,300,image = controller.componentesBgImg)

		parte1Button = self.canvas.create_image(120,75,image = controller.parte1ButtonImg)		
		parte2Button = self.canvas.create_image(120+150,75,image = controller.parte2ButtonImg)		
		parte3Button = self.canvas.create_image(120+150+150,75,image = controller.parte3ButtonImg)		
		parte4Button = self.canvas.create_image(120+150+150+150,75,image = controller.parte4ButtonImg)		
		parte5Button = self.canvas.create_image(120+150+150+150+150,75,image = controller.parte5ButtonImg)		
		parte6Button = self.canvas.create_image(120+150+150+150+150+150,75,image = controller.parte6ButtonImg)		

		self.parte1 = self.canvas.create_image(500,350,image = controller.parte1Img)
		self.parte2 = self.canvas.create_image(500,1000,image = controller.parte2Img)
		self.parte3 = self.canvas.create_image(500,1000,image = controller.parte3Img)
		self.parte4 = self.canvas.create_image(500,1000,image = controller.parte4Img)
		self.parte5 = self.canvas.create_image(500,1000,image = controller.parte5Img)
		self.parte6 = self.canvas.create_image(500,1000,image = controller.parte6Img)

		casaIcon = self.canvas.create_image(900,400,image= controller.casaImg)
		flechaIcon = self.canvas.create_image(900,500,image = controller.flechaImg)

		''' Binding buttons '''
		self.canvas.tag_bind(parte1Button,"<Button-1>",self.mostrarParte1)
		self.canvas.tag_bind(parte2Button,"<Button-1>",self.mostrarParte2)
		self.canvas.tag_bind(parte3Button,"<Button-1>",self.mostrarParte3)
		self.canvas.tag_bind(parte4Button,"<Button-1>",self.mostrarParte4)
		self.canvas.tag_bind(parte5Button,"<Button-1>",self.mostrarParte5)
		self.canvas.tag_bind(parte6Button,"<Button-1>",self.mostrarParte6)

		self.canvas.tag_bind(casaIcon,"<Button-1>",self.changeToStartPage)
		self.canvas.tag_bind(flechaIcon,"<Button-1>",self.changeToPageEight)
	
	def changeToStartPage(self,event):
		self.controller.show_frame(StartPage)

	def changeToPageEight(self,event):
		self.controller.show_frame(PageEight)

	def moverArriba(self,item,posicionFinal):
		yspeed=-10
		pos =  self.canvas.coords(item)
		while(pos[1] > posicionFinal):
			self.canvas.move(item,0,yspeed)
			pos = self.canvas.coords(item)
			self.controller.update()
			time.sleep(0.001)
	def moverAbajo(self,item,posicionFinal):
		yspeed=10
		pos =  self.canvas.coords(item)
		while(pos[1] < posicionFinal):
			self.canvas.move(item,0,yspeed)
			pos = self.canvas.coords(item)
			self.controller.update()
			time.sleep(0.001)

	def mostrarParte1(self,event):
		if(self.currentStep == 1):
			pass
		elif(self.currentStep == 2):
			self.moverAbajo(self.parte2,1000)
		elif(self.currentStep == 3):
			self.moverAbajo(self.parte3,1000)
		elif(self.currentStep == 4):
			self.moverAbajo(self.parte4,1000)
		elif(self.currentStep == 5):
			self.moverAbajo(self.parte5,1000)
		elif(self.currentStep == 6):
			self.moverAbajo(self.parte6,1000)
		
		self.moverArriba(self.parte1,350)
		self.currentStep = 1
	def mostrarParte2(self,event):
		if(self.currentStep == 2):
			pass
		elif(self.currentStep == 1):
			self.moverAbajo(self.parte1,1000)
		elif(self.currentStep == 3):
			self.moverAbajo(self.parte3,1000)
		elif(self.currentStep == 4):
			self.moverAbajo(self.parte4,1000)
		elif(self.currentStep == 5):
			self.moverAbajo(self.parte5,1000)
		elif(self.currentStep == 6):
			self.moverAbajo(self.parte6,1000)
		
		self.moverArriba(self.parte2,350)
		self.currentStep = 2
	def mostrarParte3(self,event):
		if(self.currentStep == 3):
			pass
		elif(self.currentStep == 2):
			self.moverAbajo(self.parte2,1000)
		elif(self.currentStep == 1):
			self.moverAbajo(self.parte1,1000)
		elif(self.currentStep == 4):
			self.moverAbajo(self.parte4,1000)
		elif(self.currentStep == 5):
			self.moverAbajo(self.parte5,1000)
		elif(self.currentStep == 6):
			self.moverAbajo(self.parte6,1000)
		
		self.moverArriba(self.parte3,350)
		self.currentStep = 3
	def mostrarParte4(self,event):
		if(self.currentStep == 4):
			pass
		elif(self.currentStep == 2):
			self.moverAbajo(self.parte2,1000)
		elif(self.currentStep == 3):
			self.moverAbajo(self.parte3,1000)
		elif(self.currentStep == 1):
			self.moverAbajo(self.parte1,1000)
		elif(self.currentStep == 5):
			self.moverAbajo(self.parte5,1000)
		elif(self.currentStep == 6):
			self.moverAbajo(self.parte6,1000)
		
		self.moverArriba(self.parte4,350)
		self.currentStep = 4
	def mostrarParte5(self,event):
		if(self.currentStep == 5):
			pass
		elif(self.currentStep == 2):
			self.moverAbajo(self.parte2,1000)
		elif(self.currentStep == 3):
			self.moverAbajo(self.parte3,1000)
		elif(self.currentStep == 4):
			self.moverAbajo(self.parte4,1000)
		elif(self.currentStep == 1):
			self.moverAbajo(self.parte1,1000)
		elif(self.currentStep == 6):
			self.moverAbajo(self.parte6,1000)
		
		self.moverArriba(self.parte5,350)
		self.currentStep = 5
	def mostrarParte6(self,event):
		if(self.currentStep == 6):
			pass
		elif(self.currentStep == 2):
			self.moverAbajo(self.parte2,1000)
		elif(self.currentStep == 3):
			self.moverAbajo(self.parte3,1000)
		elif(self.currentStep == 4):
			self.moverAbajo(self.parte4,1000)
		elif(self.currentStep == 5):
			self.moverAbajo(self.parte5,1000)
		elif(self.currentStep == 1):
			self.moverAbajo(self.parte1,1000)
		
		self.moverArriba(self.parte6,350)
		self.currentStep = 6

class PageEight(Frame):
	def __init__(self, parent, controller):
		Frame.__init__(self, parent)

		self.controller = controller

		#helper variables to help with the animations
		self.currentStep = 1

		#creating the canvas
		self.canvas = Canvas(self,width=1000,height=600)
		self.canvas.pack()

app = App()
app.title("Desafio MEF en 3D")
app.geometry('1000x600+200+100')
app.resizable(False,False)
app.mainloop()