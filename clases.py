
import pygame

class jugador:

    def __init__(self, tamaño, origen, imagen):

        self.superficie = pygame.image.load(imagen)
        self.superficie = pygame.transform.scale (self.superficie, tamaño)
        self.rec = self.superficie.get_rect()
        self.rec.center = origen  



    def mover (self, mano):

        if mano == 1: 

            self.rec.center = (206,220)
            
         
        elif mano == 2: 

            self.rec.center = (412,220)
        
        elif mano == 3:

            self.rec.center = (618,220)
        
        elif mano == 4:

            self.rec.center = (720,400)
        
        elif mano == 0:

            self.rec.center = (1000,300)
        
        



    def respuesta (self, mano):

        if mano == 1:
            self.rec.center = (256, 150)
           
        
        elif mano == 2: 

            self.rec.center = (462,150)
        
        elif mano == 3:

            self.rec.center = (668,150)



class boton:
    def __init__(self, origen, tamaño, colores, texto, color_letras):

        self.superficie = pygame.Surface(tamaño)
        self.color = colores[0]
        self.color_colision = colores[1]
        self.superficie.fill(self.color)
        self.rec = self.superficie.get_rect()
        self.rec.center = origen


        fuente = pygame.font.Font(None,32)
        self.texto = fuente.render (texto, True, color_letras)
    

 







        
        
    








 

        
        
        
        
                
