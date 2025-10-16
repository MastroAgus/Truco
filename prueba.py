import sys
import pygame

#############################
# Configuración básica
#############################
WIDTH, HEIGHT = 900, 600
TITLE = "Mi Videojuego - Menú"
FPS = 60

# Colores
BG = (18, 18, 22)
PANEL = (28, 28, 34)
PRIMARY = (99, 102, 241)   # violeta
ACCENT = (16, 185, 129)    # verde
TEXT = (240, 240, 245)
TEXT_MUTED = (180, 180, 190)
DANGER = (239, 68, 68)

#############################
# Utilidades
#############################
class Button:
    def __init__(self, text, pos, size=(260, 56), *, font=None, 
                 color_idle=PANEL, color_hover=PRIMARY, text_color=TEXT, 
                 shadow=True, on_click=None):
        self.text = text
        self.x, self.y = pos
        self.w, self.h = size
        self.font = font or pygame.font.Font(None, 36)
        self.color_idle = color_idle
        self.color_hover = color_hover
        self.text_color = text_color
        self.shadow = shadow
        self.on_click = on_click

        self.rect = pygame.Rect(self.x, self.y, self.w, self.h)
        self._hovered = False
        # Pre-render de textos para rendimiento
        self.text_surface_idle = self.font.render(self.text, True, self.text_color)
        self.text_surface_hover = self.font.render(self.text, True, (255, 255, 255))

    def draw(self, surf):
        self._hovered = self.rect.collidepoint(pygame.mouse.get_pos())
        color = self.color_hover if self._hovered else self.color_idle

        if self.shadow:
            shadow_rect = self.rect.copy()
            shadow_rect.topleft = (self.rect.x + 2, self.rect.y + 2)
            pygame.draw.rect(surf, (0, 0, 0), shadow_rect, border_radius=14)

        pygame.draw.rect(surf, color, self.rect, border_radius=16)
        # Borde sutil
        pygame.draw.rect(surf, (255, 255, 255, 30), self.rect, width=2, border_radius=16)

        text_surface = self.text_surface_hover if self._hovered else self.text_surface_idle
        text_rect = text_surface.get_rect(center=self.rect.center)
        surf.blit(text_surface, text_rect)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(event.pos) and self.on_click:
                self.on_click()


class Toggle:
    """Interruptor ON/OFF simple para opciones."""
    def __init__(self, label, pos, *, font=None, checked=False, on_change=None):
        self.label = label
        self.x, self.y = pos
        self.font = font or pygame.font.Font(None, 32)
        self.checked = checked
        self.on_change = on_change
        self.rect = pygame.Rect(self.x + 220, self.y - 8, 64, 32)

    def draw(self, surf):
        # Etiqueta
        label_surf = self.font.render(self.label, True, TEXT)
        surf.blit(label_surf, (self.x, self.y))
        # Switch
        track_color = ACCENT if self.checked else (80, 80, 90)
        pygame.draw.rect(surf, track_color, self.rect, border_radius=16)
        knob_x = self.rect.x + (self.rect.w - 28 - 4 if self.checked else 4)
        knob_rect = pygame.Rect(knob_x, self.rect.y + 4, 28, 24)
        pygame.draw.rect(surf, (255, 255, 255), knob_rect, border_radius=12)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(event.pos):
                self.checked = not self.checked
                if self.on_change:
                    self.on_change(self.checked)


#############################
# Juego con máquina de estados
#############################
class Game:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()  # por si luego usas sonidos

        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()

        # Estados: 'MENU', 'OPTIONS', 'CREDITS', 'PLAYING'
        self.state = 'MENU'
        self.running = True
        self.fullscreen = False

        # Fuentes
        self.font_h1 = pygame.font.Font(None, 72)
        self.font_h2 = pygame.font.Font(None, 44)
        self.font_p = pygame.font.Font(None, 28)

        # Construye pantallas
        self._build_menu()
        self._build_options()
        self._build_credits()

    #########################
    # Construcción de UI
    #########################
    def _build_menu(self):
        cx = WIDTH // 2 - 130
        start_y = HEIGHT // 2 - 40
        spacing = 72

        self.btn_play = Button("Jugar", (cx, start_y), on_click=self._go_playing)
        self.btn_options = Button("Opciones", (cx, start_y + spacing), on_click=self._go_options)
        self.btn_credits = Button("Créditos", (cx, start_y + 2*spacing), on_click=self._go_credits)
        self.btn_quit = Button("Salir", (cx, start_y + 3*spacing), color_idle=DANGER, on_click=self._quit)
        self.menu_buttons = [self.btn_play, self.btn_options, self.btn_credits, self.btn_quit]

    def _build_options(self):
        self.toggle_fullscreen = Toggle("Pantalla completa", (WIDTH//2 - 200, HEIGHT//2 - 20), checked=self.fullscreen, on_change=self._toggle_fullscreen)
        self.btn_back_opt = Button("Volver", (WIDTH//2 - 130, HEIGHT//2 + 80), on_click=self._go_menu)
        self.options_widgets = [self.toggle_fullscreen, self.btn_back_opt]

    def _build_credits(self):
        self.btn_back_cred = Button("Volver", (WIDTH//2 - 130, HEIGHT - 120), on_click=self._go_menu)

    #########################
    # Callbacks / navegación
    #########################
    def _go_menu(self):
        self.state = 'MENU'

    def _go_options(self):
        self.state = 'OPTIONS'

    def _go_credits(self):
        self.state = 'CREDITS'

    def _go_playing(self):
        self.state = 'PLAYING'

    def _quit(self):
        self.running = False

    def _toggle_fullscreen(self, checked):
        self.fullscreen = checked
        if self.fullscreen:
            pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        else:
            pygame.display.set_mode((WIDTH, HEIGHT))

    #########################
    # Bucle principal
    #########################
    def run(self):
        while self.running:
            dt = self.clock.tick(FPS) / 1000.0
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    # ESC: volver al menú si estás jugando; si ya estás en el menú, salir
                    if self.state == 'PLAYING':
                        self._go_menu()
                    elif self.state == 'MENU':
                        self._quit()

                # Pasar los eventos a los widgets según el estado
                if self.state == 'MENU':
                    for b in self.menu_buttons:
                        b.handle_event(event)
                elif self.state == 'OPTIONS':
                    self.toggle_fullscreen.handle_event(event)
                    self.btn_back_opt.handle_event(event)
                elif self.state == 'CREDITS':
                    self.btn_back_cred.handle_event(event)

            # Actualizar y dibujar
            self._draw()

        pygame.quit()
        sys.exit()

    #########################
    # Render por estado
    #########################
    def _draw(self):
        self.screen.fill(BG)

        if self.state == 'MENU':
            self._draw_title("Mi Videojuego")
            for b in self.menu_buttons:
                b.draw(self.screen)
            self._draw_footer("ESC para salir")

        elif self.state == 'OPTIONS':
            self._draw_subtitle("Opciones")
            self.toggle_fullscreen.draw(self.screen)
            self.btn_back_opt.draw(self.screen)
            self._draw_footer("Click para alternar opciones")

        elif self.state == 'CREDITS':
            self._draw_subtitle("Créditos")
            credit_lines = [
                "Hecho con Python + Pygame",
                "Autor: Tu Nombre",
                "Año: 2025",
            ]
            self._draw_paragraph(credit_lines, (WIDTH//2, HEIGHT//2 - 20))
            self.btn_back_cred.draw(self.screen)

        elif self.state == 'PLAYING':
            self._draw_subtitle("Jugando...")
            # --- Aquí iría tu lógica de juego ---
            # De momento, mostramos un placeholder:
            playing_text = self.font_p.render("(Coloca aquí tu loop del juego)", True, TEXT_MUTED)
            self.screen.blit(playing_text, (WIDTH//2 - playing_text.get_width()//2, HEIGHT//2))
            self._draw_footer("ESC para volver al menú")

        pygame.display.flip()

    def _draw_title(self, text):
        title_surf = self.font_h1.render(text, True, (255, 255, 255))
        title_rect = title_surf.get_rect(center=(WIDTH//2, HEIGHT//3 - 40))
        # banda decorativa
        band_rect = pygame.Rect(0, title_rect.centery - 50, WIDTH, 100)
        pygame.draw.rect(self.screen, (40, 40, 50), band_rect)
        self.screen.blit(title_surf, title_rect)

    def _draw_subtitle(self, text):
        subtitle = self.font_h2.render(text, True, (255, 255, 255))
        self.screen.blit(subtitle, (40, 30))
        # línea divisoria
        pygame.draw.line(self.screen, (70, 70, 80), (40, 80), (WIDTH-40, 80), 2)

    def _draw_paragraph(self, lines, center_pos):
        x, y = center_pos
        for i, line in enumerate(lines):
            surf = self.font_p.render(line, True, TEXT)
            rect = surf.get_rect(center=(x, y + i * 28))
            self.screen.blit(surf, rect)

    def _draw_footer(self, text):
        foot = self.font_p.render(text, True, TEXT_MUTED)
        rect = foot.get_rect(center=(WIDTH//2, HEIGHT - 28))
        self.screen.blit(foot, rect)


if __name__ == "__main__":
    Game().run()
