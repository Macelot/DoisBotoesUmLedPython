#############################################################
#  ########\                                                #
#  ##  _____|                                               #
#  ## |       ######\####\   #######\                       #
#  #####\     ##  _##  _##\ ##  _____|                      #
#  ##  __|    ## / ## / ## |## /                            #
#  ## |       ## | ## | ## |## |                            #
#  ########\  ## | ## | ## |\#######\                       #
#  \________| \__| \__| \__| \_______|                      #
#    Ércio       Marcelo       Cainã                        #
#                                                           #
#  Jogo de reflexos                                         #
#  Os pinos 8 e 10 são responsáveis por ligar o LED         #
#  O jogo inicia dentro de um intervalo de 5 e 10           #  
#  segundos.                                                #
#                                                           #
#  Autores: Marcelo Josué Telles,                           #
#           Ércio Luis Dorneles Berna,                      #
#           Cainã Silva da Costa                            #
#                                                           #
#  Data: 03/06/2017                                         #
#############################################################
#Definindo a utilização da biblioteca GPIO
from gpiozero import LED, Button
#Importação da biblioteca time para utilizar o método sleep
from time import sleep
#Importação da biblioteca random para utilizar o método uniform
from random import uniform
#Note que não será utilizada a GPIO.BOARD, desta forma o 
# setimo pino é a GPIO 4
led = LED(4) #7 pino real
left_button = Button(14)  #8 pino real
right_button = Button(15) #10 pino real

def pressed(button):
    print(str(button.pin.number) + ' Ganhou o jogo!')
try:
	while (True):
		print ('aguarde')
		led.on()
		sleep(uniform(5, 10))
		print ('vai')
		led.off()
		right_button.when_pressed = pressed
		left_button.when_pressed = pressed
		print('Reiniciando Jogo em 2 segundos')
		sleep(2)
		print('Se prepare')
except KeyboardInterrupt:
    print("Fim de programa. \n")
    pass
finally:
    GPIO.cleanup()	
#Fonte: Raspberry pi Fundation
#https://www.raspberrypi.org/learning/python-quick-reaction-game/worksheet/
