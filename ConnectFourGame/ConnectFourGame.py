import pygame
import sys

# Constants
ROW_COUNT = 6
COLUMN_COUNT = 7
SQUARE_SIZE = 100
RADIUS = SQUARE_SIZE // 2 - 5
WIDTH = COLUMN_COUNT * SQUARE_SIZE
HEIGHT = (ROW_COUNT + 1) * SQUARE_SIZE
WINDOW_SIZE = (WIDTH, HEIGHT)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

class ConnectFourGame:
    def __init__(self):
        self.board = [[0 for _ in range(COLUMN_COUNT)] for _ in range(ROW_COUNT)]
        self.turn = 1  # 1 for player 1, 2 for player 2
        self.game_over = False

    def drop_piece(self, col):
        for r in range(ROW_COUNT - 1, -1, -1):
            if self.board[r][col] == 0:
                self.board[r][col] = self.turn
                return True
        return False

    def check_winner(self):
        # Check horizontal
        for r in range(ROW_COUNT):
            for c in range(COLUMN_COUNT - 3):
                if self.board[r][c] == self.board[r][c + 1] == self.board[r][c + 2] == self.board[r][c + 3] != 0:
                    return True

        # Check vertical
        for c in range(COLUMN_COUNT):
            for r in range(ROW_COUNT - 3):
                if self.board[r][c] == self.board[r + 1][c] == self.board[r + 2][c] == self.board[r + 3][c] != 0:
                    return True

        # Check diagonals
        for r in range(ROW_COUNT - 3):
            for c in range(COLUMN_COUNT - 3):
                if self.board[r][c] == self.board[r + 1][c + 1] == self.board[r + 2][c + 2] == self.board[r + 3][c + 3] != 0:
                    return True

                if self.board[r][c + 3] == self.board[r + 1][c + 2] == self.board[r + 2][c + 1] == self.board[r + 3][c] != 0:
                    return True

        return False

    def switch_turn(self):
        self.turn = 3 - self.turn

    def is_full(self):
        return all(self.board[0])

# Initialize the game
def reset_game():
    return ConnectFourGame()

game = reset_game()

pygame.init()
screen = pygame.display.set_mode(WINDOW_SIZE)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEMOTION:
            pygame.draw.rect(screen, BLACK, (0, 0, WIDTH, SQUARE_SIZE))
            col = event.pos[0] // SQUARE_SIZE
            if game.turn == 1:
                pygame.draw.circle(screen, RED, (col * SQUARE_SIZE + SQUARE_SIZE // 2, SQUARE_SIZE // 2), RADIUS)
            else:
                pygame.draw.circle(screen, YELLOW, (col * SQUARE_SIZE + SQUARE_SIZE // 2, SQUARE_SIZE // 2), RADIUS)
            pygame.display.update()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pygame.draw.rect(screen, BLACK, (0, 0, WIDTH, SQUARE_SIZE))
            col = event.pos[0] // SQUARE_SIZE
            if game.drop_piece(col):
                if game.check_winner():
                    game.game_over = True
                else:
                    game.switch_turn()

    for r in range(ROW_COUNT):
        for c in range(COLUMN_COUNT):
            pygame.draw.rect(screen, BLUE, (c * SQUARE_SIZE, (r + 1) * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
            if game.board[r][c] == 1:
                pygame.draw.circle(screen, RED, (c * SQUARE_SIZE + SQUARE_SIZE // 2, (r + 1) * SQUARE_SIZE + SQUARE_SIZE // 2), RADIUS)
            elif game.board[r][c] == 2:
                pygame.draw.circle(screen, YELLOW, (c * SQUARE_SIZE + SQUARE_SIZE // 2, (r + 1) * SQUARE_SIZE + SQUARE_SIZE // 2), RADIUS)

    pygame.display.update()

    # Check for a winner
    if game.game_over:
        winning_player = game.turn
        font = pygame.font.Font(None, 74)
        text = font.render(f"Player {winning_player} wins!", True, BLACK)
        screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height() // 2))
        pygame.display.update()
        pygame.time.wait(2000)  # Wait for 2 seconds before restarting
        game = reset_game()  # Reset the game state
