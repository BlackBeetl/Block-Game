import pygame
import time
import random

pygame.init() 

display_width=1000
display_height=900
gameDisplay=pygame.display.set_mode((display_width,display_height))
clock=pygame.time.Clock()

ghost_width=50
ghostimg=pygame.image.load("1.png")

def ghost(x,y):
	gameDisplay.blit(ghostImg, (x,y))

darkBlue=(0,0,139)
white=(255,255,255)	
darkYellow=(204,204,0)
rectC=(204,204,0)
def text_object(text,font):
	textSurface=font.render(text,true,darkBlue)
	return textSurface, textSurface.get_rect()

def message_display(text):	
	largeText=pygame.font.Font("freesansbold.ttf",115)
	TextSurf,TextRect=text_object(text,largeText)
	TextRect.center=((display_width/2), (display_height/2))
	gameDisplay.blit(TextSurf, TextRect)


def button(txt, x,y,w,h,ic,ac,action=None):
		mouse=pygame.mouse.get_pos()
		click=pygame.mouse.get_pressed()


		if x+w > mouse[0] > x and y  + h > mouse[1] > y:
			pygame.draw.rect(gameDisplay,ac,(x,y,w,h))
			if click[0]==1 and action is not None:
				action()
		else:
			pygame.draw.rect(gameDisplay,ic,(x,y,w,h))

		smallText=pygame.font.Font("freesansbold.ttf",20)	
		textSurf, textRect=text_objects(msg,smallText)
		textRect.center=((x+(w/2)), (y+(h/2)))
		gameDisplay.bilt(textSurf, textRect)

def Lost():
	Lost=true
	largeText=pygame.font.Font('freesansbold.ttf',115)
	TextSurf,TextRect=text_objects("You lost",largeText)
	TextRect.center=((display_width/2), (display_height/2))
	gameDisplay.blit(TextSurf,TextRect)


	while Lost:
		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				pygame.quit()
				quit()

		button("Again",360,550,100,50,white,darkBlue,gaming)
		button("Exit",500,550,100,50,white,darkYellow,exitGame)	


		pygame.display.update()	
		clock.tick(15)

def beginGame():
	intro=True

	while intro:
		for event in pygame.event.get():
		    if event.type==pygame.QUIT:
		    	pygame.quit()
		    	quit()

		gameDisplay.fill(white)  
		largeText=pygame.font.Font('freesansbold.ttf',115)  	
		TextSurf, TextRect=text_objects("Let's Start", largeText)
		TextRect.center=((display_width/2), (display_height/2))
		gameDisplay.blit(TextSurf,TextRect)

		button("Play",250,600,100,50,white,darkYellow,gaming)
		button("Exit",650,600,100,50,white,darkYellow,quit)
		pygame.display.update()
		clock.tick(15)


def rectObst_scoreCount(count):	
	font=pygame.font.SysFont(None,50)
	text=font.render("Score"+ str(count),True,darkBlue)
	gameDisplay.blit(text,(50,100))


def rectObst(thingx,thingy,thingw,thingh,color):
	pygame.draw.rect(gameDisplay,color,[thingx,thingy,thingw,thingh])



def gaming():
	gameDisplay.fill(white)
	x=(display_width * 0.8) 
	y=(display_height * 0.8)
	moveX=0
	rectX=random.randrang(0,display_width)
	rectY=-900
	rectSpeed=4
	rectW=100
	rectH=100
	scoreCount=0
	gameExit=False
	while not gameExit:
		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				pygame.quit
				quit()

				if event.type==pygame.KEYDOWN:
					if event.key==pygame.K_LEFT:
					    moveX=-10
					if event.key==pygame.K_RIGHT:
					    moveX=10

					if   event.type==pygame.KEYUP:
						if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
							moveX=0

		x +=moveX	

		rectObst(rectX,rectY,rectW,rectC)	
		rectY +=rectSpeed
		ghost(x,y)	
		rectObst_scoreCount(scoreCount)   
		if x > display_width - ghost_width or x < 0:
			lost()

		if rectY > display_height:
			rectY = 0 - rectH
			rectX = random.randrang(0,display_width)
			scoreCount +=10
			rectSpeed +=0.6
			rectW += (scoreCount * 0.04)

		if y < rectY + rectH:
			if rectX < x < rectX + rectW or rectX < x + ghost_width < rectX + rectW:
				lost()


		pygame.display.update()	
		clock.tick(50)	
			
beginGame()




			










