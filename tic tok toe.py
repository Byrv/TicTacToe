import pygame ,sys
import numpy as np
pygame.init()
circle_radius=60
circle_width=15
board_rows=3
board_col=3
h=600
w=600
color = (165, 163, 148)
linecolor = (89, 141, 103)
linewidth = 15
coloro=(255, 173, 41)
space=55
crosswidth=25
screen = pygame.display.set_mode((h,w))
pygame.display.set_caption('Tic Tok Toe')
screen.fill(color)

board =np.zeros((board_rows , board_col))



def draw_lines():
    pygame.draw.line(screen, linecolor, (0,200),(600,200),linewidth)
    pygame.draw.line(screen, linecolor, (0,400),(600,400),linewidth)
    pygame.draw.line(screen, linecolor, (200,0),(200,600),linewidth)
    pygame.draw.line(screen, linecolor, (400,0),(400,600),linewidth)
draw_lines()


def draw_xo():
    for row in range(board_rows):
        for col in range(board_col):
            if board[row][col] == 1:
                pygame.draw.circle(screen ,coloro,(int(col * 200 +100),int(row * 200 + 100)),circle_radius,circle_width)
            elif board[row][col] ==2:
                pygame.draw.line(screen ,coloro,(col*200 +space,row*200+200-space), (col*200 +200-space,row*200+space),crosswidth) 
                pygame.draw.line(screen ,coloro,(col*200 +space,row*200+space), (col*200 +200-space,row*200+200-space),crosswidth) 
               
   

def mark_square(row,col,player):
    board[row][col] =player

def available_square(row,col):
    return board[row][col] == False

def is_board_full():
    for row in range(board_rows):
        for col in range(board_col):
            if board[row][col] == 0:
                return False
    return True


def checkwin(player):
    for col in range(board_col):
        if (board[0][col] == player and board[1][col] == player and board[2][col] == player):
            draw_verticalwin(col,player)
            return True
    for row in range(board_rows):
         if (board[row][0] == player and board[row][1] == player and board[row][2] == player):
             draw_horizontalwin(row,player)
             return True

    if board[2][0] == player and board[1][1] == player and board[0][2] == player:
            draw_asc_diagonal(player)
            return True
    
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
            draw_des_diagonal(player)
            return True
    return False

def draw_verticalwin(col,player):
    posX =col *200+100
    pygame.draw.line(screen, coloro,(posX,15),(posX,h -15),15)

def draw_horizontalwin(row,player):
    posY =row *200+100
    pygame.draw.line(screen, coloro,(15,posY),(w -15,posY),15)

def draw_asc_diagonal(player):
   pygame.draw.line(screen, coloro,(15,h - 15),(w-15,15),15)
def draw_des_diagonal(player):
    pygame.draw.line(screen, coloro,(15,15),(w-15,h-15),15)
def restart():
    screen.fill(color)
    draw_lines()
    player = 1
    for row in range(board_rows):
        for col in range(board_col):
            board[row][col]=0

player =1
gameover = False

while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        
        if event.type == pygame.MOUSEBUTTONDOWN and not gameover:
            
            mousex = event.pos[0]
            mousey = event.pos[1]
            
            click_row = int(mousey // 200)
            click_col = int(mousex // 200)
           
            if available_square(click_row,click_col):
                if player == 1:
                    mark_square(click_row,click_col,1)
                    if checkwin(player):
                        gameover=True
                    player =2
                
                elif player == 2:
                    mark_square(click_row,click_col,2)
                    if checkwin(player):
                        gameover=True
                    player =1
                
                draw_xo()                                
                print(board)
        if event.type == pygame.KEYDOWN:
            restart()
                           
    pygame.display.update()


