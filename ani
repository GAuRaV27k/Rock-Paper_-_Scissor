import pygame
import random
import math
import sys

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 700
FPS = 60

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 100, 255)
PURPLE = (128, 0, 128)
ORANGE = (255, 165, 0)
YELLOW = (255, 255, 0)
GRAY = (128, 128, 128)
DARK_GRAY = (64, 64, 64)

class RockPaperScissors:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Animated Rock Paper Scissors")
        self.clock = pygame.time.Clock()
        
        # Game state
        self.state = "menu"  # menu, playing, countdown, reveal, result
        self.player_choice = None
        self.computer_choice = None
        self.player_score = 0
        self.computer_score = 0
        
        # Animation variables
        self.countdown_timer = 0
        self.countdown_number = 3
        self.reveal_timer = 0
        self.result_timer = 0
        self.shake_offset = 0
        self.pulse_scale = 1.0
        self.choice_animation_progress = 0
        
        # Font setup
        self.title_font = pygame.font.Font(None, 72)
        self.large_font = pygame.font.Font(None, 48)
        self.medium_font = pygame.font.Font(None, 36)
        self.small_font = pygame.font.Font(None, 24)
        
        # Button rectangles
        self.rock_btn = pygame.Rect(150, 500, 120, 80)
        self.paper_btn = pygame.Rect(320, 500, 120, 80)
        self.scissors_btn = pygame.Rect(490, 500, 120, 80)
        self.play_again_btn = pygame.Rect(400, 600, 200, 50)
        
        # Choice symbols
        self.choices = {
            'rock': '✊',
            'paper': '✋',
            'scissors': '✌️'
        }
        
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.state == "menu":
                    if self.rock_btn.collidepoint(event.pos):
                        self.start_game('rock')
                    elif self.paper_btn.collidepoint(event.pos):
                        self.start_game('paper')
                    elif self.scissors_btn.collidepoint(event.pos):
                        self.start_game('scissors')
                        
                elif self.state == "result":
                    if self.play_again_btn.collidepoint(event.pos):
                        self.reset_game()
            
            if event.type == pygame.KEYDOWN:
                if self.state == "menu":
                    if event.key == pygame.K_r:
                        self.start_game('rock')
                    elif event.key == pygame.K_p:
                        self.start_game('paper')
                    elif event.key == pygame.K_s:
                        self.start_game('scissors')
                elif self.state == "result":
                    if event.key == pygame.K_SPACE:
                        self.reset_game()
        
        return True
    
    def start_game(self, choice):
        self.player_choice = choice
        self.computer_choice = random.choice(['rock', 'paper', 'scissors'])
        self.state = "countdown"
        self.countdown_timer = 0
        self.countdown_number = 3
    
    def reset_game(self):
        self.state = "menu"
        self.player_choice = None
        self.computer_choice = None
        self.countdown_timer = 0
        self.reveal_timer = 0
        self.result_timer = 0
        self.choice_animation_progress = 0
    
    def update_animations(self, dt):
        # Pulse animation for buttons
        self.pulse_scale = 1.0 + 0.1 * math.sin(pygame.time.get_ticks() * 0.005)
        
        # Shake animation during countdown
        if self.state == "countdown":
            self.shake_offset = random.randint(-3, 3) if self.countdown_number <= 1 else 0
        
        # Update timers
        if self.state == "countdown":
            self.countdown_timer += dt
            if self.countdown_timer >= 1000:  # 1 second per number
                self.countdown_number -= 1
                self.countdown_timer = 0
                
                if self.countdown_number <= 0:
                    self.state = "reveal"
                    self.reveal_timer = 0
        
        elif self.state == "reveal":
            self.reveal_timer += dt
            self.choice_animation_progress = min(1.0, self.reveal_timer / 1000)
            
            if self.reveal_timer >= 1500:  # 1.5 seconds reveal
                self.state = "result"
                self.result_timer = 0
                self.update_score()
        
        elif self.state == "result":
            self.result_timer += dt
    
    def update_score(self):
        winner = self.get_winner()
        if winner == "player":
            self.player_score += 1
        elif winner == "computer":
            self.computer_score += 1
    
    def get_winner(self):
        if self.player_choice == self.computer_choice:
            return "tie"
        
        winning_combos = {
            ('rock', 'scissors'),
            ('paper', 'rock'),
            ('scissors', 'paper')
        }
        
        if (self.player_choice, self.computer_choice) in winning_combos:
            return "player"
        else:
            return "computer"
    
    def draw_button(self, rect, text, color, hover_color=None):
        mouse_pos = pygame.mouse.get_pos()
        is_hovered = rect.collidepoint(mouse_pos)
        
        # Button color with hover effect
        btn_color = hover_color if hover_color and is_hovered else color
        
        # Scale effect for hovered buttons
        if is_hovered and self.state == "menu":
            scale = self.pulse_scale
            scaled_rect = pygame.Rect(
                rect.centerx - rect.width * scale // 2,
                rect.centery - rect.height * scale // 2,
                rect.width * scale,
                rect.height * scale
            )
        else:
            scaled_rect = rect
        
        # Draw button
        pygame.draw.rect(self.screen, btn_color, scaled_rect, border_radius=10)
        pygame.draw.rect(self.screen, BLACK, scaled_rect, 3, border_radius=10)
        
        # Draw text
        text_surface = self.medium_font.render(text, True, BLACK)
        text_rect = text_surface.get_rect(center=rect.center)
        self.screen.blit(text_surface, text_rect)
    
    def draw_choice_symbol(self, choice, x, y, scale=1.0, alpha=255):
        """Draw animated choice symbols"""
        if choice in self.choices:
            # Create a temporary surface for alpha blending
            symbol_surface = self.large_font.render(self.choices[choice], True, BLACK)
            if alpha < 255:
                symbol_surface.set_alpha(alpha)
            
            # Scale the symbol
            if scale != 1.0:
                new_size = (int(symbol_surface.get_width() * scale), 
                           int(symbol_surface.get_height() * scale))
                symbol_surface = pygame.transform.scale(symbol_surface, new_size)
            
            # Center the symbol
            rect = symbol_surface.get_rect(center=(x, y))
            self.screen.blit(symbol_surface, rect)
    
    def draw_menu(self):
        self.screen.fill(WHITE)
        
        # Title
        title_text = self.title_font.render("Rock Paper Scissors", True, BLUE)
        title_rect = title_text.get_rect(center=(SCREEN_WIDTH//2, 100))
        self.screen.blit(title_text, title_rect)
        
        # Score display
        score_text = f"Player: {self.player_score}  |  Computer: {self.computer_score}"
        score_surface = self.medium_font.render(score_text, True, BLACK)
        score_rect = score_surface.get_rect(center=(SCREEN_WIDTH//2, 180))
        self.screen.blit(score_surface, score_rect)
        
        # Instructions
        instruction_text = "Choose your weapon!"
        instruction_surface = self.large_font.render(instruction_text, True, BLACK)
        instruction_rect = instruction_surface.get_rect(center=(SCREEN_WIDTH//2, 250))
        self.screen.blit(instruction_surface, instruction_rect)
        
        # Key instructions
        key_text = "Click buttons or press R/P/S keys"
        key_surface = self.small_font.render(key_text, True, GRAY)
        key_rect = key_surface.get_rect(center=(SCREEN_WIDTH//2, 300))
        self.screen.blit(key_surface, key_rect)
        
        # Choice buttons with symbols
        self.draw_button(self.rock_btn, "ROCK ✊", RED, ORANGE)
        self.draw_button(self.paper_btn, "PAPER ✋", GREEN, YELLOW)
        self.draw_button(self.scissors_btn, "SCISSORS ✌️", BLUE, PURPLE)
        
        # Button labels
        labels = ["(R)", "(P)", "(S)"]
        positions = [self.rock_btn.centerx, self.paper_btn.centerx, self.scissors_btn.centerx]
        for label, x in zip(labels, positions):
            label_surface = self.small_font.render(label, True, GRAY)
            label_rect = label_surface.get_rect(center=(x, 590))
            self.screen.blit(label_surface, label_rect)
    
    def draw_countdown(self):
        self.screen.fill(WHITE)
        
        # Shake effect
        offset_x = self.shake_offset
        offset_y = self.shake_offset
        
        # Player and Computer labels
        player_text = self.large_font.render("PLAYER", True, BLUE)
        player_rect = player_text.get_rect(center=(250 + offset_x, 150 + offset_y))
        self.screen.blit(player_text, player_rect)
        
        computer_text = self.large_font.render("COMPUTER", True, RED)
        computer_rect = computer_text.get_rect(center=(750 + offset_x, 150 + offset_y))
        self.screen.blit(computer_text, computer_rect)
        
        # Player choice (visible)
        self.draw_choice_symbol(self.player_choice, 250 + offset_x, 250 + offset_y, 3.0)
        
        # Computer choice (hidden with question mark)
        question_surface = self.large_font.render("❓", True, BLACK)
        question_rect = question_surface.get_rect(center=(750 + offset_x, 250 + offset_y))
        self.screen.blit(question_surface, question_rect)
        
        # Countdown number
        if self.countdown_number > 0:
            countdown_color = RED if self.countdown_number == 1 else BLACK
            countdown_text = self.title_font.render(str(self.countdown_number), True, countdown_color)
            countdown_rect = countdown_text.get_rect(center=(SCREEN_WIDTH//2 + offset_x, 400 + offset_y))
            self.screen.blit(countdown_text, countdown_rect)
        else:
            # "GO!" text
            go_text = self.title_font.render("GO!", True, GREEN)
            go_rect = go_text.get_rect(center=(SCREEN_WIDTH//2 + offset_x, 400 + offset_y))
            self.screen.blit(go_text, go_rect)
    
    def draw_reveal(self):
        self.screen.fill(WHITE)
        
        # Player and Computer labels
        player_text = self.large_font.render("PLAYER", True, BLUE)
        player_rect = player_text.get_rect(center=(250, 150))
        self.screen.blit(player_text, player_rect)
        
        computer_text = self.large_font.render("COMPUTER", True, RED)
        computer_rect = computer_text.get_rect(center=(750, 150))
        self.screen.blit(computer_text, computer_rect)
        
        # Animate choices appearing
        player_scale = 2.0 + self.choice_animation_progress
        computer_alpha = int(255 * self.choice_animation_progress)
        computer_scale = 1.0 + 2.0 * self.choice_animation_progress
        
        # Player choice (grows)
        self.draw_choice_symbol(self.player_choice, 250, 250, player_scale)
        
        # Computer choice (fades in and grows)
        self.draw_choice_symbol(self.computer_choice, 750, 250, computer_scale, computer_alpha)
        
        # VS text
        vs_text = self.large_font.render("VS", True, BLACK)
        vs_rect = vs_text.get_rect(center=(SCREEN_WIDTH//2, 250))
        self.screen.blit(vs_text, vs_rect)
    
    def draw_result(self):
        self.screen.fill(WHITE)
        
        # Player and Computer labels
        player_text = self.large_font.render("PLAYER", True, BLUE)
        player_rect = player_text.get_rect(center=(250, 150))
        self.screen.blit(player_text, player_rect)
        
        computer_text = self.large_font.render("COMPUTER", True, RED)
        computer_rect = computer_text.get_rect(center=(750, 150))
        self.screen.blit(computer_text, computer_rect)
        
        # Final choices
        self.draw_choice_symbol(self.player_choice, 250, 250, 3.0)
        self.draw_choice_symbol(self.computer_choice, 750, 250, 3.0)
        
        # Winner announcement
        winner = self.get_winner()
        if winner == "player":
            result_text = "🎉 YOU WIN! 🎉"
            result_color = GREEN
        elif winner == "computer":
            result_text = "💔 YOU LOSE! 💔"
            result_color = RED
        else:
            result_text = "🤝 IT'S A TIE! 🤝"
            result_color = ORANGE
        
        # Animated result text
        bounce_offset = int(10 * math.sin(self.result_timer * 0.01))
        result_surface = self.large_font.render(result_text, True, result_color)
        result_rect = result_surface.get_rect(center=(SCREEN_WIDTH//2, 400 + bounce_offset))
        self.screen.blit(result_surface, result_rect)
        
        # Updated score
        score_text = f"Score - Player: {self.player_score}  |  Computer: {self.computer_score}"
        score_surface = self.medium_font.render(score_text, True, BLACK)
        score_rect = score_surface.get_rect(center=(SCREEN_WIDTH//2, 500))
        self.screen.blit(score_surface, score_rect)
        
        # Play again button
        self.draw_button(self.play_again_btn, "PLAY AGAIN", BLUE, GREEN)
        
        # Instructions
        instruction_text = "Click 'PLAY AGAIN' or press SPACE"
        instruction_surface = self.small_font.render(instruction_text, True, GRAY)
        instruction_rect = instruction_surface.get_rect(center=(SCREEN_WIDTH//2, 670))
        self.screen.blit(instruction_surface, instruction_rect)
    
    def draw(self):
        if self.state == "menu":
            self.draw_menu()
        elif self.state == "countdown":
            self.draw_countdown()
        elif self.state == "reveal":
            self.draw_reveal()
        elif self.state == "result":
            self.draw_result()
        
        pygame.display.flip()
    
    def run(self):
        running = True
        
        while running:
            dt = self.clock.tick(FPS)
            
            running = self.handle_events()
            self.update_animations(dt)
            self.draw()
        
        pygame.quit()
        sys.exit()

# Run the game
if __name__ == "__main__":
    game = RockPaperScissors()
    game.run()