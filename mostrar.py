import pygame
from registro import save_persona, load_persona
from variables import *

# Inicialización de pygame
pygame.init()

# Configuración de la pantalla
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Registro de Personas")

#fuente
FONT = pygame.font.Font(None, 36)

# Variables de entrada
input_boxes = {
    "nombre": {"rect": pygame.Rect(100, 100, 200, 40), "text": ""},
    "edad": {"rect": pygame.Rect(100, 160, 200, 40), "text": ""},
    "email": {"rect": pygame.Rect(100, 220, 200, 40), "text": ""},
}
active_box = None

# Lista de usuarios cargados
loaded_users = []

# Función para dibujar elementos
def draw_elements():
    screen.fill(blanco)
    for key, box in input_boxes.items():
        color = (0, 255, 0) if active_box == key else negro
        pygame.draw.rect(screen, color, box["rect"], 2)
        text_surface = FONT.render(box["text"], True, negro)
        screen.blit(text_surface, (box["rect"].x + 5, box["rect"].y + 5))
    
    # Botón Guardar
    guardado = FONT.render("Guardar", True, negro)
    pygame.draw.rect(screen, negro, (400, 100, 100, 40), 2)
    screen.blit(guardado, (405, 105))
    
    # Botón Mostrar Usuarios
    mostrar = FONT.render("Mostrar", True, negro)
    pygame.draw.rect(screen, negro, (400, 160, 100, 40), 2)
    screen.blit(mostrar, (405, 165))
    
    # Mostrar usuarios cargados
    y_offset = 300
    for user in loaded_users:
        user_text = FONT.render(f"{user[0]} | {user[1]} años | {user[2]}", True, negro)
        screen.blit(user_text, (50, y_offset))
        y_offset += 40
    
    pygame.display.flip()

# Bucle principal
run = True
while run == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = event.pos
            active_box = None
            for key, box in input_boxes.items():
                if box["rect"].collidepoint(pos):
                    active_box = key
            
            # Verificar si el botón "Guardar" fue clicado
            if pygame.Rect(400, 100, 100, 40).collidepoint(pos):
                save_persona(input_boxes["nombre"]["text"], input_boxes["edad"]["text"], input_boxes["email"]["text"])
                for key in input_boxes:
                    input_boxes[key]["text"] = ""
            
            # Verificar si el botón "Mostrar" fue clicado
            if pygame.Rect(400, 160, 100, 40).collidepoint(pos):
                loaded_users = load_persona()
        
        elif event.type == pygame.KEYDOWN:
            if active_box:
                if event.key == pygame.K_BACKSPACE:
                    input_boxes[active_box]["text"] = input_boxes[active_box]["text"][:-1]
                else:
                    input_boxes[active_box]["text"] += event.unicode

    draw_elements()

pygame.quit()