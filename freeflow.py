import pygame
pygame.init()

pygame.mixer.music.load("Legend.mp3")
pygame.mixer.music.play(-1)
board1=[[1,0,0,0,0],[0,0,0,2,1],[2,3,0,0,3],[0,0,0,4,5],[4,5,0,0,0]]
board2=[[0,0,0,0,0,0,1],[0,0,0,0,0,2,6],[0,2,0,0,0,0,0],[0,0,0,3,4,0,0],[0,0,3,0,5,0,0],[0,0,0,0,6,5,0],[0,0,0,0,0,1,4]]


def front(surface):
    X=500
    Y=500
    exit_game=False
    darkgrey=(43,43,43)
    lightgrey=(56,56,56)
    white=(255,255,255)
    pygame.display.set_caption('Free Flow')
    bgimg = pygame.image.load("freeflow2.jpg")
    bgimg = pygame.transform.scale(bgimg,(X,Y)).convert_alpha()
    def text_objects(text,font):
        textsurface=font.render(text,True,white)
        return textsurface,textsurface.get_rect()
    while not exit_game:
        surface.fill(white)
        surface.blit(bgimg,(0,0))
        pygame.draw.rect(surface,darkgrey,(200,300,100,50))
        mouse = pygame.mouse.get_pos()
        if 200+300 > mouse[0] > 200 and 200+300 > mouse[1] > 300: 
            pygame.draw.rect(surface,lightgrey,(200,300,100,50))
        smallText = pygame.font.Font("freesansbold.ttf",20)
        textSurf, textRect = text_objects("Let's Play", smallText)
        textRect.center = (245+(5)),(300+(25))
        surface.blit(textSurf, textRect)
        for event in pygame.event.get():
            if 200+300 > mouse[0] > 200 and 200+300 > mouse[1] > 300:
                if event.type==pygame.MOUSEBUTTONDOWN:
                    m1,m2,m3=pygame.mouse.get_pressed()
                    if m1==1:
                        exit_game=True
            pygame.display.update()

def checkwin(board,surface):
    c=0
    exit_game=False
    for j in range(0,len(board)):
        for i in range(0,len(board[j])):
            if board[j][i]!=0:
                c+=1
                
                if c==49 or (c==25 and len(board)==5):
                    
                    gameover(surface)
                
                
def gameover(surface):
    X = 500
    Y = 500
    exit_game=False
    
    pygame.display.set_caption('Game over')
    

    bgimg = pygame.image.load("colourful.jpg")
    bgimg = pygame.transform.scale(bgimg,(X,Y)).convert_alpha()
    
    while not exit_game:
        surface.fill((255,255,255))
        surface.blit(bgimg,(0,0))

        
        for event in pygame.event.get() : 
      
            if event.type == pygame.QUIT :
                exit_game=True
        pygame.display.update()                                
                        
                                     
  
            
        

def colour(num):
    
    if(num==1):
        return (255,255,0)  
    if(num==2):
        return (255,0,0)
    if(num==3):
        return (0,0,255)
    if(num==4):
        return (255,51,153)
    if(num==5):
        return (0,255,0)
    if(num==6):
        return (0,255,255)
    return (0,0,0)
def func(w,rows,surface,gw,board):
    
    x=0
    y=0
    
    for j in range(0,len(board)):
        
        for i in range(0,len(board[j])):
            x=i*gw
            y=j*gw
            pygame.draw.rect(surface,(0,0,0),[x,y,(gw-1),(gw-1)])
            if board[j][i]>0:
                pygame.draw.circle(surface,colour(board[j][i]),[int(x+gw/2),int(y+gw/2)],(gw-1)//2)
            
def func1(w,rows,surface,gw,board):
    #print(board)
    for j in range(0,len(board)):
        for i in range(0,len(board[j])):
            x=i*gw
            y=j*gw
            if board[j][i]<0:
                pygame.draw.rect(surface,colour(-board[j][i]),[x+gw/4,y+gw/4,gw/2,gw/2])
def callwindow(game_screen,gw,board):
    global rows
    global width
   
    
    game_screen.fill((255,255,255))
    func(width,rows,game_screen,gw,board)
    pygame.display.update()
def main():
    global width,rows
    width=500
    
    exit_game=False
    game_screen=pygame.display.set_mode((width,width))
    front(game_screen)
    exit_game=False
    black=(0,0,0)
    darkgrey=(43,43,43)
    lightgrey=(56,56,56)
    white = (255, 255, 255) 
    X = 500
    Y = 500
    exit_game=False
    

    pygame.display.set_caption('Menu')


    bgimg = pygame.image.load("freeflow2final.jpg")
    bgimg = pygame.transform.scale(bgimg,(X,Y)).convert_alpha()


    headimg=pygame.image.load("levels1.png")
    headimg= pygame.transform.scale(headimg,(200,60)).convert_alpha()

    def text_objects(text,font):
        textsurface=font.render(text,True,white)
        return textsurface,textsurface.get_rect()


    while not exit_game:
        game_screen.fill(white)
        game_screen.blit(bgimg,(0,0))

        pygame.draw.rect(game_screen,black,(200,200,100,50))
        pygame.draw.rect(game_screen,black,(200,300,100,50))

        smallText = pygame.font.Font("freesansbold.ttf",20)
        textSurf, textRect = text_objects("Easy", smallText)
        textRect.center = ( (200+(100/2)), (200+(50/2)) )
        game_screen.blit(textSurf, textRect)

        smallText = pygame.font.Font("freesansbold.ttf",20)
        textSurf, textRect = text_objects("Hard", smallText)
        textRect.center = ( (200+(100/2)), (300+(50/2)) )
        game_screen.blit(textSurf, textRect)


        game_screen.blit(headimg,(150,100))
        mouse = pygame.mouse.get_pos()
        

        for event in pygame.event.get() : 
            if 200+100 > mouse[0]>200 and 200+50 >mouse[1]>200:
                if event.type==pygame.MOUSEBUTTONDOWN:
                    m1,m2,m3=pygame.mouse.get_pressed()
                    if m1==1:
                        #easy
                        board=board1
                        exit_game=True
                    
                    
            
            if 200+100 > mouse[0]>200 and 300+50 >mouse[1]>300:
                if event.type==pygame.MOUSEBUTTONDOWN:
                    m1,m2,m3=pygame.mouse.get_pressed()
                    if m1==1:
                        #hard
                        board=board2
                        exit_game=True
                    
                  
                     
      
            pygame.display.update()

     
    rows=len(board)
   
    exit_game=False
    gw=width//rows
    
    callwindow(game_screen,gw,board)
    exit_game=False
    game_over=False
    pygame.display.update()
    selected=False
    while not exit_game:
        
        
        for event in pygame.event.get():
            
           
            pygame.display.update()
            if event.type==pygame.QUIT:
                checkwin(board,game_screen)   
                
                exit_game=True
            
            elif event.type==pygame.MOUSEBUTTONDOWN:
                m1,m2,m3=pygame.mouse.get_pressed()
                pygame.display.update()
                
                
                pos1,pos2=pygame.mouse.get_pos()
                if m1==1 and not selected==True:
                    
                    startx=pos1//gw
                    starty=pos2//gw
                    #1
                    curx=startx
                    cury=starty
                    if board[starty][startx]>0:
                        
                        selected=True
                    print(selected)
                

                elif( m1==1 and selected==True):
                    
                    x=int(pos1)//gw
                    y=int(pos2)//gw
                    
                    if(x>=0 and y>=0 and y<len(board) and x<len(board[0])):
                        
                        if board[y][x]==board[starty][startx]:
                            selected=False
                        if (x==curx+1 and y==cury) or (x==curx-1 and y==cury) or (x==curx and y==cury+1) or (x==curx and y==cury-1):
                            
                            board[y][x]=-board[starty][startx]
                            curx=x
                            cury=y
                            func1(width,rows,game_screen,gw,board)
                           
                
                    pygame.display.update()
                              
                
                
            
                        
                
        
    pygame.quit()
    quit()
main()
                
    


