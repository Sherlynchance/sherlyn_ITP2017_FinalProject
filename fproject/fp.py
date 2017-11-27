from pygame.sprite import *
from pygame import*
from pygame.locals import *
import random


def main():
    pygame.init()
    pygame.display.set_caption("Ludo")
    screen = pygame.display.set_mode((1100, 750))

    '''
    BoardWidth = 600
    BoardHeight = 600
    '''

    BoardBorder = 3
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    BLUE = (0, 0, 255)
    RED = (255, 0, 0)
    YELLOW = (255, 255, 0)
    GREEN = (0, 255, 0)
    '''
    Colors of the ludo buttons
    '''
    DARKRED = (152, 7, 7)
    DARKGREEN = (7, 152, 11)
    DARKYELLOW = (219, 213, 7)
    DARKBLUE = (10, 46, 152)

    main_box_width = 300    # the size of the biggest main box or the colured box
    main_box_height = 300   # the size of the biggest main box or the colured box
    sub_box_width = 250     # the size of the second box
    sub_box_height = 250    # the size of the second box
    route_box_width = 50    # the size of the small boxes which will be used as the track for the ludo buttons
    route_box_height = 50   # the size of the small boxes which will be used as the track for the ludo buttons

    def playerturn(p_turn):
        '''
        This function will draw a box to store the turn of the players
        The parameter p_turn will store the player turn and can be changed anytime
        '''
        pygame.draw.rect(screen, WHITE, (860, 500, 150, 40))
        render_text("Turn   :", BLACK, 870, 500, 30)
        render_text("P"+str(p_turn), BLACK, 970, 500, 30)

    def select_button():
        '''
        This function will draw a box to store the number 1-4 which indicates
        the number of butons each player has
        '''
        render_text("CHOOSE BUTTON", WHITE, 830, 550, 30)
        pygame.draw.rect(screen, WHITE, (835, 600, 200, 50))
        pygame.draw.line(screen, BLACK, (885, 600), (885, 650))
        pygame.draw.line(screen, BLACK, (935, 600), (935, 650))
        pygame.draw.line(screen, BLACK, (985, 600), (985, 650))
        pygame.draw.line(screen, BLACK, (1035, 600), (1035, 650))
        render_text("1", BLACK, 850, 600, 50)
        render_text("2", BLACK, 900, 600, 50)
        render_text("3", BLACK, 950, 600, 50)
        render_text("4", BLACK, 1000, 600, 50)

    def board():
        pygame.draw.line(screen, WHITE, (750, 0), (750, 750), BoardBorder)

        pygame.draw.rect(screen, GREEN, (0, 0, main_box_width, main_box_height))
        pygame.draw.rect(screen, YELLOW, (450, 450, main_box_width, main_box_height))
        pygame.draw.rect(screen, RED, (450, 0, main_box_width, main_box_height))
        pygame.draw.rect(screen, BLUE, (0, 450, main_box_width, main_box_height))

        pygame.draw.rect(screen, BLACK, (25, 25, sub_box_width, sub_box_height), 6)
        pygame.draw.rect(screen, BLACK, (475, 475, sub_box_width, sub_box_height), 6)
        pygame.draw.rect(screen, BLACK, (475, 25, sub_box_width, sub_box_height), 6)
        pygame.draw.rect(screen, BLACK, (25, 475, sub_box_width, sub_box_height), 6)

        circle = [[100, 100, GREEN], [200, 200, GREEN], [100, 200, GREEN], [200, 100, GREEN],
                  [550, 100, RED], [550, 200, RED], [650, 200, RED], [650, 100, RED],
                  [100, 550, BLUE], [200, 550, BLUE], [100, 650, BLUE], [200, 650, BLUE],
                  [650, 550, YELLOW], [550, 550, YELLOW], [550, 650, YELLOW], [650, 650, YELLOW]]

        for x in circle:
            if x[2] == GREEN:
                pygame.draw.circle(screen, BLACK, (x[0], x[1]), 50, 5)
            elif x[2] == RED:
                pygame.draw.circle(screen, BLACK, (x[0], x[1]), 50, 5)
            elif x[2] == BLUE:
                pygame.draw.circle(screen, BLACK, (x[0], x[1]), 50, 5)
            elif x[2] == YELLOW:
                pygame.draw.circle(screen, BLACK, (x[0], x[1]), 50, 5)

        left_route_list = [[0, 300, WHITE], [50, 300, GREEN], [100, 300, WHITE], [150, 300, WHITE], [200, 300, WHITE], [250, 300, WHITE],
                           [0, 350, WHITE], [50, 350, GREEN], [100, 350, GREEN], [150, 350, GREEN], [200, 350, GREEN], [250, 350, GREEN],
                           [0, 400, WHITE], [50, 400, WHITE], [100, 400, WHITE], [150, 400, WHITE], [200, 400, WHITE], [250, 400, WHITE]]
        for x in left_route_list:
            if x[2] == GREEN:
                pygame.draw.rect(screen, x[2], (x[0], x[1], route_box_width, route_box_height))
                pygame.draw.rect(screen, WHITE, (x[0], x[1], route_box_width, route_box_height), 1)
            else:
                pygame.draw.rect(screen, x[2], (x[0], x[1], route_box_width, route_box_height), 1)

        right_route_list = [[700, 300, WHITE], [650, 300, WHITE], [600, 300, WHITE], [550, 300, WHITE], [500, 300, WHITE], [450, 300, WHITE],
                            [700, 350, WHITE], [650, 350, YELLOW], [600, 350, YELLOW], [550, 350, YELLOW], [500, 350, YELLOW], [450, 350, YELLOW],
                            [700, 400, WHITE], [650, 400, YELLOW], [600, 400, WHITE], [550, 400, WHITE], [500, 400, WHITE], [450, 400, WHITE]]
        for x in right_route_list:
            if x[2] == YELLOW:
                pygame.draw.rect(screen, x[2], (x[0], x[1], route_box_width, route_box_height))
                pygame.draw.rect(screen, WHITE, (x[0], x[1], route_box_width, route_box_height), 1)
            else:
                pygame.draw.rect(screen, x[2], (x[0], x[1], route_box_width, route_box_height), 1)

        top_route_list = [[300, 0, WHITE], [300, 50, WHITE], [300, 100, WHITE], [300, 150, WHITE], [300, 200, WHITE], [300, 250, WHITE],
                          [350, 0, WHITE], [350, 50, RED], [350, 100, RED], [350, 150, RED], [350, 200, RED], [350, 250, RED],
                          [400, 0, WHITE], [400, 50, RED], [400, 100, WHITE], [400, 150, WHITE], [400, 200, WHITE], [400, 250, WHITE]]
        for x in top_route_list:
            if x[2] == RED:
                pygame.draw.rect(screen, x[2], (x[0], x[1], route_box_width, route_box_height))
                pygame.draw.rect(screen, WHITE, (x[0], x[1], route_box_width, route_box_height), 1)
            else:
                pygame.draw.rect(screen, x[2], (x[0], x[1], route_box_width, route_box_height), 1)

        bottom_route_list = [[300, 700, WHITE], [300, 650, BLUE], [300, 600, WHITE], [300, 550, WHITE], [300, 500, WHITE], [300, 450, WHITE],
                             [350, 700, WHITE], [350, 650, BLUE], [350, 600, BLUE], [350, 550, BLUE], [350, 500, BLUE], [350, 450, BLUE],
                             [400, 700, WHITE], [400, 650, WHITE], [400, 600, WHITE], [400, 550, WHITE], [400, 500, WHITE], [400, 450, WHITE]]
        for x in bottom_route_list:
            if x[2] == BLUE:
                pygame.draw.rect(screen, x[2], (x[0], x[1], route_box_width, route_box_height))
                pygame.draw.rect(screen, WHITE, (x[0], x[1], route_box_width, route_box_height), 1)
            else:
                pygame.draw.rect(screen, x[2], (x[0], x[1], route_box_width, route_box_height), 1)

        pygame.draw.polygon(screen, GREEN, ((300, 300), (300, 450), (375, 375)))  # draws the three sided polygon in the middle of the board
        pygame.draw.polygon(screen, RED, ((300, 300), (450, 300), (375, 375)))
        pygame.draw.polygon(screen, BLUE, ((300, 450), (450, 450), (375, 375)))
        pygame.draw.polygon(screen, YELLOW, ((450, 300), (450, 450), (375, 375)))

    def score_board():
        pygame.draw.rect(screen, WHITE, (890, 350, 200, 100))
        pygame.draw.line(screen, BLACK, (990, 350), (990, 450))
        pygame.draw.line(screen, BLACK, (1090, 350), (1090, 450))
        pygame.draw.line(screen, BLACK, (890, 400), (1090, 400))
        render_text("P1: " + str(Player1.score), BLACK, 925, 360, 20)
        render_text("P2: " + str(Player2.score), BLACK, 1025, 360, 20)
        render_text("P3: " + str(Player3.score), BLACK, 925, 415, 20)
        render_text("P4: " + str(Player4.score), BLACK, 1025, 415, 20)

    def render_text(string_text, color, x, y, fontsize):
        text = pygame.font.SysFont("Arial", fontsize)
        textsurface = text.render(string_text, True, color)
        screen.blit(textsurface, (x, y))

    class Dice(Sprite):
        def __init__(self):
            Sprite.__init__(self)
            self.image = pygame.image.load("dice1.jpg")
            self.image = pygame.transform.scale(self.image, (250, 250))
            self.rect = self.image.get_rect(topright=(1050, 25))

        def one(self):
            Sprite.__init__(self)
            self.image = pygame.image.load("one.png")
            self.image = pygame.transform.scale(self.image, (100, 100))
            self.rect = self.image.get_rect(topright=(875, 350))

        def two(self):
            Sprite.__init__(self)
            self.image = pygame.image.load("two.png")
            self.image = pygame.transform.scale(self.image, (100, 100))
            self.rect = self.image.get_rect(topright=(875, 350))

        def three(self):
            Sprite.__init__(self)
            self.image = pygame.image.load("three.png")
            self.image = pygame.transform.scale(self.image, (100, 100))
            self.rect = self.image.get_rect(topright=(875, 350))

        def four(self):
            Sprite.__init__(self)
            self.image = pygame.image.load("four.png")
            self.image = pygame.transform.scale(self.image,(100,100))
            self.rect = self.image.get_rect(topright=(875, 350))

        def five(self):
            Sprite.__init__(self)
            self.image = pygame.image.load("five.png")
            self.image = pygame.transform.scale(self.image, (100, 100))
            self.rect = self.image.get_rect(topright=(875, 350))

        def six(self):
            Sprite.__init__(self)
            self.image = pygame.image.load("six.png")
            self.image = pygame.transform.scale(self.image, (100,100))
            self.rect = self.image.get_rect(topright=(875, 350))

    class Ludobutton(Sprite):
        radius = 20
        center_x = 0
        center_y = 0

        def drawbutton(self, color, center_x, center_y):
            Sprite.__init__(self)
            self.center_x = 0
            self.center_y = 0
            pygame.draw.circle(screen, DARKGREEN, (self.center_x, self.center_y), self.radius)

    class Player(Ludobutton):
        def __init__(self, color, track):
            super().__init__()
            self.score = 0  # score 0 because no button reached home yet
            self.color = color
            self.track = track
            self.drawludobutton = [Ludobutton() for x in range(0, 5)]  # draw 4 buttons for each player
            self.finalstatus = [0, 0, 0, 0]  # if finalstatus == 1, means the buttons have reached home
            self.initialstatus = [0, 0, 0, 0]  # initialstatus == 0, means button is not yet initiated
            self.currentposition = [-1, -1, -1, -1]

        def placeludobutton(self, position, initiated):
            for x in range(4):
                if initiated[x] == position[x]:
                    kkk = 32  # doesnt have any effect, only indicator so that else can be used

                else:
                    pygame.draw.circle(screen, self.color, position[x-1], 18)
                    self.drawbutton(self.color, position[x-1], position[x-1])

        def move(self, current):
            #  move the button according to the dice roll

            pygame.draw.circle(screen, self.color, self.track[current + 1], self.radius)

        def initiatestart(self, btn_no):
            pygame.draw.circle(screen, self.color, self.track[0], self.radius)

        def isinhome(self):
            #  to check whether the button is in home or not
            for x in range(4):
                if self.currentposition[x] == 56 and self.finalstatus[x] != 1:
                    self.score += 1
                    self.finalstatus[x] = 1

        def displaytransitbuttons(self):
            for x in range(4):
                if self.currentposition[x] != -1:
                    pygame.draw.circle(screen, self.color, self.track[self.currentposition[x]], 20)
                    self.drawbutton(self.color, self.track[self.currentposition[x]], self.track[self.currentposition[x]])

    # Home button positions
    position_green = [[100, 100], [200, 100], [100, 200], [200, 200]]
    position_blue = [[100, 550], [100, 650], [200, 550], [200, 650]]
    position_red = [[550, 100], [650, 100], [550, 200], [650, 200]]
    position_yellow = [[550, 550], [550, 650], [650, 550], [650, 650]]

    # Status of the buttons
    initiated1 = [[0, 0], [0, 0], [0, 0], [0, 0]]
    initiated2 = [[0, 0], [0, 0], [0, 0], [0, 0]]
    initiated3 = [[0, 0], [0, 0], [0, 0], [0, 0]]
    initiated4 = [[0, 0], [0, 0], [0, 0], [0, 0]]

    # Player 1(Green)
    green_track = [[75, 325], [125, 325], [175, 325], [225, 325], [275, 325],
                   [325, 275], [325, 225], [325, 175], [325, 125], [325, 75], [325, 25], [375, 25],
                   [425, 25], [425, 75], [425, 125], [425, 175], [425, 225], [425, 275],
                   [475, 325], [525, 325], [575, 325], [625, 325], [675, 325], [725, 325], [725, 375],
                   [725, 425], [675, 425], [625, 425], [575, 425], [525, 425], [475, 425],
                   [425, 475], [425, 525], [425, 575], [425, 625], [425, 675], [425, 725], [375, 725],
                   [325, 725], [325, 675], [325, 625], [325, 575], [325, 525], [325, 475],
                   [275, 425], [225, 425], [175, 425], [125, 425], [75, 425], [25, 425],
                   [25, 375], [75, 375], [125, 375], [175, 375], [225, 375], [275, 375], [325, 375]]

    # Player 2(Red)
    red_track = [[425, 75], [425, 125], [425, 175], [425, 225], [425, 275],
                 [475, 325], [525, 325], [575, 325], [625, 325], [675, 325], [725, 325], [725, 375],
                 [725, 425], [675, 425], [625, 425], [575, 425], [525, 425], [475, 425],
                 [425, 475], [425, 525], [425, 575], [425, 625], [425, 675], [425, 725], [375, 725],
                 [325, 725], [325, 675], [325, 625], [325, 575], [325, 525], [325, 475],
                 [275, 425], [225, 425], [175, 425], [125, 425], [75, 425], [25, 425], [25, 375],
                 [25, 325], [75, 325], [125, 325], [175, 325], [225, 325], [275, 325],
                 [325, 275], [325, 225], [325, 175], [325, 125], [325, 75], [325, 25],
                 [375, 25], [375, 75], [375, 125], [375, 175], [375, 225], [375, 275], [375, 325]]

    # Player 3(Blue)
    blue_track = [[325, 675], [325, 625], [325, 575], [325, 525], [325, 475],
                  [275, 425], [225, 425], [175, 425], [125, 425], [75, 425], [25, 425], [25, 375],
                  [25, 325], [75, 325], [125, 325], [175, 325], [225, 325], [275, 325],
                  [325, 275], [325, 225], [325, 175], [325, 125], [325, 75], [325, 25], [375, 25],
                  [425, 25], [425, 75], [425, 125], [425, 175], [425, 225], [425, 275],
                  [475, 325], [525, 325], [575, 325], [625, 325], [675, 325], [725, 325], [725, 375],
                  [725, 425], [675, 425], [625, 425], [575, 425], [525, 425], [475, 425],
                  [425, 475], [425, 525], [425, 575], [425, 625], [425, 675], [425, 725],
                  [375, 725], [375, 675], [375, 625], [375, 575], [375, 525], [375, 475], [375, 425]]

    # Player 4(Yellow)
    yellow_track = [[675, 425], [625, 425], [575, 425], [525, 425], [475, 425],
                    [425, 475], [425, 525], [425, 575], [425, 625], [425, 675], [425, 725], [375, 725],
                    [325, 725], [325, 675], [325, 625], [325, 575], [325, 525], [325, 475],
                    [275, 425], [225, 425], [175, 425], [125, 425], [75, 425], [25, 425], [25, 375],
                    [25, 325], [75, 325], [125, 325], [175, 325], [225, 325], [275, 325],
                    [325, 275], [325, 225], [325, 175], [325, 125], [325, 75], [325, 25], [375, 25],
                    [425, 25], [425, 75], [425, 125], [425, 175], [425, 225], [425, 275],
                    [475, 325], [525, 325], [575, 325], [625, 325], [675, 325], [725, 325],
                    [725, 375], [675, 375], [625, 375], [575, 375], [525, 375], [475, 375], [425, 375]]

    # Players, their assigned colors and tracks
    Player1 = Player(DARKGREEN, green_track)
    Player2 = Player(DARKRED, red_track)
    Player3 = Player(DARKBLUE, blue_track)
    Player4 = Player(DARKYELLOW, yellow_track)

    dice = Dice()
    all_sprite = Group(dice)

    mouse_x = 0             # co-ordinate x of the mouse
    mouse_y = 0             # co-ordinate y of the mouse
    mouse_clicked = False
    p_turn = 1              # variable to hold the turn of the player
    n = 0                   # variable tells about number that turned up while rolling the dice

    while True:
        screen.fill(BLACK)  # Fill the background screen with black
        pos = pygame.mouse.get_pos()
        (pressed1, pressed2, pressed3) = pygame.mouse.get_pressed()

        if pressed1 and dice.rect.collidepoint(pos) == 1 and mouse_clicked == True:
            n = random.randint(1, 7)   # randomize dice number between 1-6
            if n == 1:
                dice.one()  # if number = 1, call the one method of class dice
            elif n == 2:
                dice.two()  # if number = 2, call the two method of class dice
            elif n == 3:
                dice.three()  # if number = 3, call the three method of class dice
            elif n == 4:
                dice.four()  # if number = 4, call the four method of class dice
            elif n == 5:
                dice.five()  # if number = 5, call the five method of class dice
            elif n == 6:
                dice.six()  # if number = 6, call the six method of class dice
            mouse_clicked = False

        board()             # Call the board
        playerturn(p_turn)  # Call the playerturn box
        select_button()     # Call the button box
        score_board()
        all_sprite.draw(screen)  # Draw all sprite on screen

        render_text('CLICK ON DICE TO ROLL', WHITE, 755, 300, 35)

        # Placing each button in their respective positions before initiated
        Player1.placeludobutton(position_green, initiated1)
        Player2.placeludobutton(position_red, initiated2)
        Player3.placeludobutton(position_blue, initiated3)
        Player4.placeludobutton(position_yellow, initiated4)

        Player1.displaytransitbuttons()
        Player2.displaytransitbuttons()
        Player3.displaytransitbuttons()
        Player4.displaytransitbuttons()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            elif event.type == MOUSEBUTTONUP:
                (mouse_x, mouse_y) = event.pos
                mouse_clicked = True

        if p_turn == 1:

            if Player1.finalstatus[0] == 1 and Player1.finalstatus[1] == 1 and Player1.finalstatus[2] == 1 and Player1.finalstatus[3] == 1:
                p_turn = 2

            elif mouse_clicked == True and mouse_x >= 835 and mouse_x <= 885 and mouse_y >= 600 and mouse_y <= 650:
                move_button = 1  # condition for the mouse cursor to be over the button, then if clicked, button 1 will move or get initiated
                mouse_clicked = False

                if move_button == 1:
                    diff = (56 - Player1.currentposition[0])

                    if Player1.initialstatus[0] == 0:
                        if n == 6:
                            Player1.initialstatus[0] = 1         # change the status of button 1 for player 1
                            initiated1[1] = position_green[1]    # set the button which has been initiated
                            Player1.initiatestart(1)             # Function call to initiate the start of button1
                            mouse_clicked = False                # Change the status of the event
                            Player1.currentposition[0] = 0
                            p_turn = 1

                        else:
                            p_turn = 2
                            mouse_clicked = False

                    else:

                        if Player1.finalstatus[0] != 1 and Player1.currentposition[0] != 56:

                            if Player1.currentposition[0] >= 50 and n <= diff:
                                if n == 1:
                                    Player1.move(Player1.currentposition[0])
                                    Player1.currentposition[0] += 1
                                elif n == 2:
                                    Player1.move(Player1.currentposition[0])
                                    Player1.currentposition[0] += 2
                                elif n == 3:
                                    Player1.move(Player1.currentposition[0])
                                    Player1.currentposition[0] += 3
                                elif n == 4:
                                    Player1.move(Player1.currentposition[0])
                                    Player1.currentposition[0] += 4
                                elif n == 5:
                                    Player1.move(Player1.currentposition[0])
                                    Player1.currentposition[0] += 5
                                elif n == 6:
                                    Player1.move(Player1.currentposition[0])
                                    Player1.currentposition[0] += 6
                                p_turn = 2

                            elif Player1.currentposition[0] < 50:
                                if n == 1:
                                    Player1.move(Player1.currentposition[0])
                                    Player1.currentposition[0] += 1
                                elif n == 2:
                                    Player1.move(Player1.currentposition[0])
                                    Player1.currentposition[0] += 2
                                elif n == 3:
                                    Player1.move(Player1.currentposition[0])
                                    Player1.currentposition[0] += 3
                                elif n == 4:
                                    Player1.move(Player1.currentposition[0])
                                    Player1.currentposition[0] += 4
                                elif n == 5:
                                    Player1.move(Player1.currentposition[0])
                                    Player1.currentposition[0] += 5
                                elif n == 6:
                                    Player1.move(Player1.currentposition[0])
                                    Player1.currentposition[0] += 6
                                p_turn = 2

                            else:
                                p_turn = 2
                                mouse_clicked = False

            elif mouse_clicked == True and mouse_x >= 885 and mouse_x <= 935 and mouse_y >= 600 and mouse_y <= 650:
                move_button = 2
                mouse_clicked = False

                if move_button == 2:
                    diff = (56 - Player1.currentposition[1])

                    if Player1.initialstatus[1] == 0:
                            if n == 6:
                                Player1.initialstatus[1] = 1    # change the status of button 2 for player 1
                                initiated1[2] = position_green[2]    # set the button which has been initiated
                                Player1.initiatestart(2)        # Function call to initiate the start of button 2
                                mouse_clicked = False            # Change the status of the event
                                Player1.currentposition[1] = 0

                            else:
                                p_turn = 2                        # change the p_turn if number is not 6
                                mouse_clicked = False

                    else:
                        if Player1.finalstatus[1] != 1:

                            if Player1.currentposition[1] >= 50 and n <= diff:
                                if n == 1:
                                    Player1.move(Player1.currentposition[1])
                                    Player1.currentposition[1] += 1
                                elif n == 2:
                                    Player1.move(Player1.currentposition[1])
                                    Player1.currentposition[1] += 2
                                elif n == 3:
                                    Player1.move(Player1.currentposition[1])
                                    Player1.currentposition[1] += 3
                                elif n == 4:
                                    Player1.move(Player1.currentposition[1])
                                    Player1.currentposition[1] += 4
                                elif n == 5:
                                    Player1.move(Player1.currentposition[1])
                                    Player1.currentposition[1] += 5
                                elif n == 6:
                                    Player1.move(Player1.currentposition[1])
                                    Player1.currentposition[1] += 6
                                p_turn = 2

                            elif Player1.currentposition[1] < 50:
                                if n == 1:
                                    Player1.move(Player1.currentposition[1])
                                    Player1.currentposition[1] += 1
                                elif n == 2:
                                    Player1.move(Player1.currentposition[1])
                                    Player1.currentposition[1] += 2
                                elif n == 3:
                                    Player1.move(Player1.currentposition[1])
                                    Player1.currentposition[1] += 3
                                elif n == 4:
                                    Player1.move(Player1.currentposition[1])
                                    Player1.currentposition[1] += 4
                                elif n == 5:
                                    Player1.move(Player1.currentposition[1])
                                    Player1.currentposition[1] += 5
                                elif n == 6:
                                    Player1.move(Player1.currentposition[1])
                                    Player1.currentposition[1] += 6
                                p_turn = 2

                            else:
                                p_turn = 2
                                mouse_clicked = False

            elif mouse_clicked == True and mouse_x >= 935 and mouse_x <= 985 and mouse_y >= 600 and mouse_y <= 650:
                move_button = 3
                mouse_clicked = False

                if move_button == 3:
                    diff = (56 - Player1.currentposition[2])

                    if Player1.initialstatus[2] == 0:
                            if n == 6:
                                Player1.initialstatus[2] = 1    # change the status of button 3 for player 1
                                initiated1[3] = position_green[3]    # set the button which has been initiated
                                Player1.initiatestart(3)        # Function call to initiate the start of button1
                                mouse_clicked = False            # Change the status of the event
                                Player1.currentposition[2] = 0

                            else:
                                p_turn = 2                        # change the p_turn if number is not 6
                                mouse_clicked = False

                    else:
                        if Player1.finalstatus[2] != 1:
                            if Player1.currentposition[2] >= 50 and n <= diff:
                                if n == 1:
                                    Player1.move(Player1.currentposition[2])
                                    Player1.currentposition[2] += 1
                                elif n == 2:
                                    Player1.move(Player1.currentposition[2])
                                    Player1.currentposition[2] += 2
                                elif n == 3:
                                    Player1.move(Player1.currentposition[2])
                                    Player1.currentposition[2] += 3
                                elif n == 4:
                                    Player1.move(Player1.currentposition[2])
                                    Player1.currentposition[2] += 4
                                elif n == 5:
                                    Player1.move(Player1.currentposition[2])
                                    Player1.currentposition[2] += 5
                                elif n == 6:
                                    Player1.move(Player1.currentposition[2])
                                    Player1.currentposition[2] += 6
                                p_turn = 2

                            elif Player1.currentposition[2] < 50:
                                if n == 1:
                                    Player1.move(Player1.currentposition[2])
                                    Player1.currentposition[2] += 1
                                elif n == 2:
                                    Player1.move(Player1.currentposition[2])
                                    Player1.currentposition[2] += 2
                                elif n == 3:
                                    Player1.move(Player1.currentposition[2])
                                    Player1.currentposition[2] += 3
                                elif n == 4:
                                    Player1.move(Player1.currentposition[2])
                                    Player1.currentposition[2] += 4
                                elif n == 5:
                                    Player1.move(Player1.currentposition[2])
                                    Player1.currentposition[2] += 5
                                elif n == 6:
                                    Player1.move(Player1.currentposition[2])
                                    Player1.currentposition[2] += 6
                                p_turn = 2

                            else:
                                p_turn = 2
                                mouse_clicked = False

            elif mouse_clicked == True and mouse_x >= 985 and mouse_x <= 1035 and mouse_y >= 600 and mouse_y <= 650:
                move_button = 4
                mouse_clicked = False

                if move_button == 4:
                    diff = (56 - Player1.currentposition[3])

                    if Player1.initialstatus[3] == 0:
                            if n == 6:
                                Player1.initialstatus[3] = 1    # change the status of button 4 for player 1
                                initiated1[0] = position_green[0]    # set the button which has been initiated
                                Player1.initiatestart(4)        # Function call to initiate the start of button1
                                mouse_clicked = False            # Change the status of the event
                                Player1.currentposition[3] = 0

                            else:
                                p_turn = 2                        # change the p_turn if number is not 6
                                mouse_clicked = False

                    else:
                        if Player1.finalstatus[3] != 1:

                            if Player1.currentposition[3] >= 50 and n <= diff:
                                if n == 1:
                                    Player1.move(Player1.currentposition[3])
                                    Player1.currentposition[3] += 1
                                elif n == 2:
                                    Player1.move(Player1.currentposition[3])
                                    Player1.currentposition[3] += 2
                                elif n == 3:
                                    Player1.move(Player1.currentposition[3])
                                    Player1.currentposition[3] += 3
                                elif n == 4:
                                    Player1.move(Player1.currentposition[3])
                                    Player1.currentposition[3] += 4
                                elif n == 5:
                                    Player1.move(Player1.currentposition[3])
                                    Player1.currentposition[3] += 5
                                elif n == 6:
                                    Player1.move(Player1.currentposition[3])
                                    Player1.currentposition[3] += 6
                                p_turn = 2

                            elif Player1.currentposition[3] < 50:
                                if n == 1:
                                    Player1.move(Player1.currentposition[3])
                                    Player1.currentposition[3] += 1
                                elif n == 2:
                                    Player1.move(Player1.currentposition[3])
                                    Player1.currentposition[3] += 2
                                elif n == 3:
                                    Player1.move(Player1.currentposition[3])
                                    Player1.currentposition[3] += 3
                                elif n == 4:
                                    Player1.move(Player1.currentposition[3])
                                    Player1.currentposition[3] += 4
                                elif n == 5:
                                    Player1.move(Player1.currentposition[3])
                                    Player1.currentposition[3] += 5
                                elif n == 6:
                                    Player1.move(Player1.currentposition[3])
                                    Player1.currentposition[3] += 6
                                p_turn = 2

                            else:
                                p_turn = 2
                                mouse_clicked = False

        if p_turn == 2:

                if Player2.finalstatus[0] == 1 and Player2.finalstatus[1] == 1 and Player2.finalstatus[2] == 1 and Player2.finalstatus[3] == 1:
                    p_turn = 3

                elif mouse_clicked == True and mouse_x >= 835 and mouse_x <= 885 and mouse_y >= 600 and mouse_y <= 650:
                    move_button = 1
                    mouse_clicked = False

                    if move_button == 1:
                        diff = (56 - Player2.currentposition[0])

                        if Player2.initialstatus[0] == 0:

                                if n == 6:
                                    Player2.initialstatus[0] = 1    # change the status of button 1 for player 2
                                    initiated2[1] = position_red[1]    # set the button which has been initiated
                                    Player2.initiatestart(1)        # Function call to initiate the start of button1
                                    mouse_clicked = False            # Change the status of the event
                                    Player2.currentposition[0] = 0

                                else:
                                    p_turn = 3                        # change the p_turn if number is not 6
                                    mouse_clicked = False

                        else:
                            if Player2.finalstatus[0] != 1:

                                if Player2.currentposition[0] >= 50 and n <= diff:
                                    if n == 1:
                                        Player2.move(Player2.currentposition[0])
                                        Player2.currentposition[0] += 1
                                    elif n == 2:
                                        Player2.move(Player2.currentposition[0])
                                        Player2.currentposition[0] += 2
                                    elif n == 3:
                                        Player2.move(Player2.currentposition[0])
                                        Player2.currentposition[0] += 3
                                    elif n == 4:
                                        Player2.move(Player2.currentposition[0])
                                        Player2.currentposition[0] += 4
                                    elif n == 5:
                                        Player2.move(Player2.currentposition[0])
                                        Player2.currentposition[0] += 5
                                    elif n == 6:
                                        Player2.move(Player2.currentposition[0])
                                        Player2.currentposition[0] += 6
                                    p_turn = 3

                                elif Player2.currentposition[0] < 50:
                                    if n == 1:
                                        Player2.move(Player2.currentposition[0])
                                        Player2.currentposition[0] += 1
                                    elif n == 2:
                                        Player2.move(Player2.currentposition[0])
                                        Player2.currentposition[0] += 2
                                    elif n == 3:
                                        Player2.move(Player2.currentposition[0])
                                        Player2.currentposition[0] += 3
                                    elif n == 4:
                                        Player2.move(Player2.currentposition[0])
                                        Player2.currentposition[0] += 4
                                    elif n == 5:
                                        Player2.move(Player2.currentposition[0])
                                        Player2.currentposition[0] += 5
                                    elif n == 6:
                                        Player2.move(Player2.currentposition[0])
                                        Player2.currentposition[0] += 6
                                    p_turn = 3

                                else:
                                    p_turn = 3
                                    mouse_clicked = False

                elif mouse_clicked == True and mouse_x >= 885 and mouse_x <= 935 and mouse_y >= 600 and mouse_y <= 650:
                    move_button = 2
                    mouse_clicked = False

                    if move_button == 2:
                        diff = (56 - Player2.currentposition[1])
                        # diff is a variable that holds the distance between the current pos of button and the home

                        if Player2.initialstatus[1] == 0:

                                if n == 6:
                                    Player2.initialstatus[1] = 1    # change the status of button 2 for player 2
                                    initiated2[2] = position_red[2]    # set the button which has been initiated
                                    Player2.initiatestart(2)        # Function call to initiate the start of button1
                                    mouse_clicked = False            # Change the status of the event
                                    Player2.currentposition[1] = 0

                                else:
                                    p_turn = 3                        # change the p_turn if number is not 6
                                    mouse_clicked = False

                        else:
                            if Player2.finalstatus[1] != 1:

                                if Player2.currentposition[1] >= 50 and n <= diff:
                                    if n == 1:
                                        Player2.move(Player2.currentposition[1])
                                        Player2.currentposition[1] += 1
                                    elif n == 2:
                                        Player2.move(Player2.currentposition[1])
                                        Player2.currentposition[1] += 2
                                    elif n == 3:
                                        Player2.move(Player2.currentposition[1])
                                        Player2.currentposition[1] += 3
                                    elif n == 4:
                                        Player2.move(Player2.currentposition[1])
                                        Player2.currentposition[1] += 4
                                    elif n == 5:
                                        Player2.move(Player2.currentposition[1])
                                        Player2.currentposition[1] += 5
                                    elif n == 6:
                                        Player2.move(Player2.currentposition[1])
                                        Player2.currentposition[1] += 6
                                    p_turn = 3

                                elif Player2.currentposition[1] < 50:
                                    if n == 1:
                                        Player2.move(Player2.currentposition[1])
                                        Player2.currentposition[1] += 1
                                    elif n == 2:
                                        Player2.move(Player2.currentposition[1])
                                        Player2.currentposition[1] += 2
                                    elif n == 3:
                                        Player2.move(Player2.currentposition[1])
                                        Player2.currentposition[1] += 3
                                    elif n == 4:
                                        Player2.move(Player2.currentposition[1])
                                        Player2.currentposition[1] += 4
                                    elif n == 5:
                                        Player2.move(Player2.currentposition[1])
                                        Player2.currentposition[1] += 5
                                    elif n == 6:
                                        Player2.move(Player2.currentposition[1])
                                        Player2.currentposition[1] += 6
                                    p_turn = 3


                                else:
                                    p_turn = 3
                                    mouse_clicked = False

                elif mouse_clicked == True and mouse_x >= 935 and mouse_x <= 985 and mouse_y >= 600 and mouse_y <= 650:
                    move_button = 3
                    mouse_clicked = False

                    if move_button == 3:
                        diff = (56 - Player2.currentposition[2])

                        if Player2.initialstatus[2] == 0:

                                if n == 6:
                                    Player2.initialstatus[2] = 1    # change the status of button 3 for player 2
                                    initiated2[3] = position_red[3]    # set the button which has been initiated
                                    Player2.initiatestart(3)        # Function call to initiate the start of button1
                                    mouse_clicked = False            # Change the status of the event
                                    Player2.currentposition[2] = 0

                                else:
                                    p_turn = 3                        # change the p_turn if number is not 6
                                    mouse_clicked = False

                        else:
                            if Player2.finalstatus[2] != 1:

                                if Player2.currentposition[2] >= 50 and n <= diff:
                                    if n == 1:
                                        Player2.move(Player2.currentposition[2])
                                        Player2.currentposition[2] += 1
                                    elif n == 2:
                                        Player2.move(Player2.currentposition[2])
                                        Player2.currentposition[2] += 2
                                    elif n == 3:
                                        Player2.move(Player2.currentposition[2])
                                        Player2.currentposition[2] += 3
                                    elif n == 4:
                                        Player2.move(Player2.currentposition[2])
                                        Player2.currentposition[2] += 4
                                    elif n == 5:
                                        Player2.move(Player2.currentposition[2])
                                        Player2.currentposition[2] += 5
                                    elif n == 6:
                                        Player2.move(Player2.currentposition[2])
                                        Player2.currentposition[2] += 6
                                    p_turn = 3

                                elif Player2.currentposition[2] < 50:
                                    if n == 1:
                                        Player2.move(Player2.currentposition[2])
                                        Player2.currentposition[2] += 1
                                    elif n == 2:
                                        Player2.move(Player2.currentposition[2])
                                        Player2.currentposition[2] += 2
                                    elif n == 3:
                                        Player2.move(Player2.currentposition[2])
                                        Player2.currentposition[2] += 3
                                    elif n == 4:
                                        Player2.move(Player2.currentposition[2])
                                        Player2.currentposition[2] += 4
                                    elif n == 5:
                                        Player2.move(Player2.currentposition[2])
                                        Player2.currentposition[2] += 5
                                    elif n == 6:
                                        Player2.move(Player2.currentposition[2])
                                        Player2.currentposition[2] += 6
                                    p_turn = 3

                                else:
                                    p_turn = 3
                                    mouse_clicked = False

                elif mouse_clicked == True and mouse_x >= 985 and mouse_x <= 1035 and mouse_y >= 600 and mouse_y <= 650:
                    move_button = 4
                    mouse_clicked = False

                    if move_button == 4:
                        diff = (56 - Player2.currentposition[3])

                        if Player2.initialstatus[3] == 0:

                                if n == 6:
                                    Player2.initialstatus[3] = 1    # change the status of button 4 for player 2
                                    initiated2[0] = position_red[0]    # set the button which has been initiated
                                    Player2.initiatestart(4)        # Function call to initiate the start of button1
                                    mouse_clicked = False            # Change the status of the event
                                    Player2.currentposition[3] = 0

                                else:
                                    p_turn = 3                        # change the p_turn if number is not 6
                                    mouse_clicked = False

                        else:
                            if Player2.finalstatus[3] != 1:

                                if Player2.currentposition[3] >= 50 and n <= diff:
                                    if n == 1:
                                        Player2.move(Player2.currentposition[3])
                                        Player2.currentposition[3] += 1
                                    elif n == 2:
                                        Player2.move(Player2.currentposition[3])
                                        Player2.currentposition[3] += 2
                                    elif n == 3:
                                        Player2.move(Player2.currentposition[3])
                                        Player2.currentposition[3] += 3
                                    elif n == 4:
                                        Player2.move(Player2.currentposition[3])
                                        Player2.currentposition[3] += 4
                                    elif n == 5:
                                        Player2.move(Player2.currentposition[3])
                                        Player2.currentposition[3] += 5
                                    elif n == 6:
                                        Player2.move(Player2.currentposition[3])
                                        Player2.currentposition[3] += 6
                                    p_turn = 3

                                elif Player2.currentposition[3] < 50:
                                    if n == 1:
                                        Player2.move(Player2.currentposition[3])
                                        Player2.currentposition[3] += 1
                                    elif n == 2:
                                        Player2.move(Player2.currentposition[3])
                                        Player2.currentposition[3] += 2
                                    elif n == 3:
                                        Player2.move(Player2.currentposition[3])
                                        Player2.currentposition[3] += 3
                                    elif n == 4:
                                        Player2.move(Player2.currentposition[3])
                                        Player2.currentposition[3] += 4
                                    elif n == 5:
                                        Player2.move(Player2.currentposition[3])
                                        Player2.currentposition[3] += 5
                                    elif n == 6:
                                        Player2.move(Player2.currentposition[3])
                                        Player2.currentposition[3] += 6
                                    p_turn = 3

                                else:
                                    p_turn = 3
                                    mouse_clicked = False

        if p_turn == 3:

                if Player3.finalstatus[0] == 1 and Player3.finalstatus[1] == 1 and Player3.finalstatus[2] == 1 and Player3.finalstatus[3] == 1:
                    p_turn = 4

                elif mouse_clicked == True and mouse_x >= 835 and mouse_x <= 885 and mouse_y >= 600 and mouse_y <= 650:
                    move_button = 1
                    mouse_clicked = False

                    if move_button == 1:
                        diff = (56 - Player3.currentposition[0])

                        if Player3.initialstatus[0] == 0:

                                if n == 6:
                                    Player3.initialstatus[0] = 1    # change the status of button 1 for player 3
                                    initiated3[1] = position_blue[1]    # set the button which has been initiated
                                    Player3.initiatestart(1)        # Function call to initiate the start of button1
                                    mouse_clicked = False            # Change the status of the event
                                    Player3.currentposition[0] = 0

                                else:
                                    p_turn = 4                        # change the p_turn if number is not 6
                                    mouse_clicked = False

                        else:
                            if Player3.finalstatus[0] != 1:

                                if Player3.currentposition[0] >= 50 and n <= diff:
                                    if n == 1:
                                        Player3.move(Player3.currentposition[0])
                                        Player3.currentposition[0] += 1
                                    elif n == 2:
                                        Player3.move(Player3.currentposition[0])
                                        Player3.currentposition[0] += 2
                                    elif n == 3:
                                        Player3.move(Player3.currentposition[0])
                                        Player3.currentposition[0] += 3
                                    elif n == 4:
                                        Player3.move(Player3.currentposition[0])
                                        Player3.currentposition[0] += 4
                                    elif n == 5:
                                        Player3.move(Player3.currentposition[0])
                                        Player3.currentposition[0] += 5
                                    elif n == 6:
                                        Player3.move(Player3.currentposition[0])
                                        Player3.currentposition[0] += 6
                                    p_turn = 4

                                elif Player3.currentposition[0] < 50:
                                    if n == 1:
                                        Player3.move(Player3.currentposition[0])
                                        Player3.currentposition[0] += 1
                                    elif n == 2:
                                        Player3.move(Player3.currentposition[0])
                                        Player3.currentposition[0] += 2
                                    elif n == 3:
                                        Player3.move(Player3.currentposition[0])
                                        Player3.currentposition[0] += 3
                                    elif n == 4:
                                        Player3.move(Player3.currentposition[0])
                                        Player3.currentposition[0] += 4
                                    elif n == 5:
                                        Player3.move(Player3.currentposition[0])
                                        Player3.currentposition[0] += 5
                                    elif n == 6:
                                        Player3.move(Player3.currentposition[0])
                                        Player3.currentposition[0] += 6
                                    p_turn = 4

                                else:
                                    p_turn = 4
                                    mouse_clicked = False

                elif mouse_clicked == True and mouse_x >= 885 and mouse_x <= 935 and mouse_y >= 600 and mouse_y <= 650:
                    move_button = 2
                    mouse_clicked = False

                    if move_button == 2:
                        diff = (56 - Player3.currentposition[1])

                        if Player3.initialstatus[1] == 0:

                                if n == 6:
                                    Player3.initialstatus[1] = 1    # change the status of button 2 for player 3
                                    initiated3[2] = position_blue[2]    # set the button which has been initiated
                                    Player3.initiatestart(2)        # Function call to initiate the start of button1
                                    mouse_clicked = False            # Change the status of the event
                                    Player3.currentposition[1] = 0

                                else:
                                    p_turn = 4                        # change the p_turn if number is not 6
                                    mouse_clicked = False

                        else:
                            if Player3.finalstatus[1] != 1:

                                if Player3.currentposition[1] >= 50 and n <= diff:
                                    if n == 1:
                                        Player3.move(Player3.currentposition[1])
                                        Player3.currentposition[1] += 1
                                    elif n == 2:
                                        Player3.move(Player3.currentposition[1])
                                        Player3.currentposition[1] += 2
                                    elif n == 3:
                                        Player3.move(Player3.currentposition[1])
                                        Player3.currentposition[1] += 3
                                    elif n == 4:
                                        Player3.move(Player3.currentposition[1])
                                        Player3.currentposition[1] += 4
                                    elif n == 5:
                                        Player3.move(Player3.currentposition[1])
                                        Player3.currentposition[1] += 5
                                    elif n == 6:
                                        Player3.move(Player3.currentposition[1])
                                        Player3.currentposition[1] += 6
                                    p_turn = 4

                                elif Player3.currentposition[1] < 50:
                                    if n == 1:
                                        Player3.move(Player3.currentposition[1])
                                        Player3.currentposition[1] += 1
                                    elif n == 2:
                                        Player3.move(Player3.currentposition[1])
                                        Player3.currentposition[1] += 2
                                    elif n == 3:
                                        Player3.move(Player3.currentposition[1])
                                        Player3.currentposition[1] += 3
                                    elif n == 4:
                                        Player3.move(Player3.currentposition[1])
                                        Player3.currentposition[1] += 4
                                    elif n == 5:
                                        Player3.move(Player3.currentposition[1])
                                        Player3.currentposition[1] += 5
                                    elif n == 6:
                                        Player3.move(Player3.currentposition[1])
                                        Player3.currentposition[1] += 6
                                    p_turn = 4

                                else:
                                    p_turn = 4
                                    mouse_clicked = False

                elif mouse_clicked == True and mouse_x >= 935 and mouse_x <= 985 and mouse_y >= 600 and mouse_y <= 650:
                    move_button = 3
                    mouse_clicked = False

                    if move_button == 3:
                        diff = (56 - Player3.currentposition[2])

                        if Player3.initialstatus[2] == 0:

                                if n == 6:
                                    Player3.initialstatus[2] = 1    # change the status of button 3 for player 3
                                    initiated3[3] = position_blue[3]    # set the button which has been initiated
                                    Player3.initiatestart(3)        # Function call to initiate the start of button1
                                    mouse_clicked = False            # Change the status of the event
                                    Player3.currentposition[2] = 0

                                else:
                                    p_turn = 4                        # change the p_turn if number is not 6
                                    mouse_clicked = False

                        else:
                            if Player3.finalstatus[2] != 1:

                                if Player3.currentposition[2] >= 50 and n <= diff:
                                    if n == 1:
                                        Player3.move(Player3.currentposition[2])
                                        Player3.currentposition[2] += 1
                                    elif n == 2:
                                        Player3.move(Player3.currentposition[2])
                                        Player3.currentposition[2] += 2
                                    elif n == 3:
                                        Player3.move(Player3.currentposition[2])
                                        Player3.currentposition[2] += 3
                                    elif n == 4:
                                        Player3.move(Player3.currentposition[2])
                                        Player3.currentposition[2] += 4
                                    elif n == 5:
                                        Player3.move(Player3.currentposition[2])
                                        Player3.currentposition[2] += 5
                                    elif n == 6:
                                        Player3.move(Player3.currentposition[2])
                                        Player3.currentposition[2] += 6
                                    p_turn = 4

                                elif Player3.currentposition[2] < 50:
                                    if n == 1:
                                        Player3.move(Player3.currentposition[2])
                                        Player3.currentposition[2] += 1
                                    elif n == 2:
                                        Player3.move(Player3.currentposition[2])
                                        Player3.currentposition[2] += 2
                                    elif n == 3:
                                        Player3.move(Player3.currentposition[2])
                                        Player3.currentposition[2] += 3
                                    elif n == 4:
                                        Player3.move(Player3.currentposition[2])
                                        Player3.currentposition[2] += 4
                                    elif n == 5:
                                        Player3.move(Player3.currentposition[2])
                                        Player3.currentposition[2] += 5
                                    elif n == 6:
                                        Player3.move(Player3.currentposition[2])
                                        Player3.currentposition[2] += 6
                                    p_turn = 4

                                else:
                                    p_turn = 4
                                    mouse_clicked = False

                elif mouse_clicked == True and mouse_x >= 985 and mouse_x <= 1035 and mouse_y >= 600 and mouse_y <= 650:
                    move_button = 4
                    mouse_clicked = False

                    if move_button == 4:
                        diff = (56 - Player3.currentposition[3])

                        if Player3.initialstatus[3] == 0:

                                if n == 6:
                                    Player3.initialstatus[3] = 1    # change the status of button 4 for player 3
                                    initiated3[0] = position_blue[0]    # set the button which has been initiated
                                    Player3.initiatestart(4)        # Function call to initiate the start of button1
                                    mouse_clicked = False            # Change the status of the event
                                    Player3.currentposition[3] = 0

                                else:
                                    p_turn = 4                        # change the p_turn if number is not 6
                                    mouse_clicked = False

                        else:
                            if Player3.finalstatus[3] != 1:

                                if Player3.currentposition[3] >= 50 and n <= diff:
                                    if n == 1:
                                        Player3.move(Player3.currentposition[3])
                                        Player3.currentposition[3] += 1
                                    elif n == 2:
                                        Player3.move(Player3.currentposition[3])
                                        Player3.currentposition[3] += 2
                                    elif n == 3:
                                        Player3.move(Player3.currentposition[3])
                                        Player3.currentposition[3] += 3
                                    elif n == 4:
                                        Player3.move(Player3.currentposition[3])
                                        Player3.currentposition[3] += 4
                                    elif n == 5:
                                        Player3.move(Player3.currentposition[3])
                                        Player3.currentposition[3] += 5
                                    elif n == 6:
                                        Player3.move(Player3.currentposition[3])
                                        Player3.currentposition[3] += 6
                                    p_turn = 4

                                elif Player3.currentposition[3] < 50:
                                    if n == 1:
                                        Player3.move(Player3.currentposition[3])
                                        Player3.currentposition[3] += 1
                                    elif n == 2:
                                        Player3.move(Player3.currentposition[3])
                                        Player3.currentposition[3] += 2
                                    elif n == 3:
                                        Player3.move(Player3.currentposition[3])
                                        Player3.currentposition[3] += 3
                                    elif n == 4:
                                        Player3.move(Player3.currentposition[3])
                                        Player3.currentposition[3] += 4
                                    elif n == 5:
                                        Player3.move(Player3.currentposition[3])
                                        Player3.currentposition[3] += 5
                                    elif n == 6:
                                        Player3.move(Player3.currentposition[3])
                                        Player3.currentposition[3] += 6
                                    p_turn = 4

                                else:
                                    p_turn = 4
                                    mouse_clicked = False

        if p_turn == 4:

            if Player4.finalstatus[0] == 1 and Player4.finalstatus[1] == 1 and Player4.finalstatus[2] == 1 and Player4.finalstatus[3] == 1:
                p_turn = 4

            elif mouse_clicked == True and mouse_x >= 835 and mouse_x <= 885 and mouse_y >= 600 and mouse_y <= 650:
                move_button = 1
                mouse_clicked = False

                if move_button == 1:
                    diff = (56 - Player4.currentposition[0])

                    if Player4.initialstatus[0] == 0:

                            if n == 6:
                                Player4.initialstatus[0] = 1    # change the status of button 1 for player 4
                                initiated4[1] = position_yellow[1]    # set the button which has been initiated
                                Player4.initiatestart(1)        # Function call to initiate the start of button1
                                mouse_clicked = False            # Change the status of the event
                                Player4.currentposition[0] = 0

                            else:
                                p_turn = 1                        # change the p_turn if number is not 6
                                mouse_clicked = False

                    else:
                        if Player4.finalstatus[0] != 1:

                            if Player4.currentposition[0] >= 50 and n <= diff:
                                if n == 1:
                                    Player4.move(Player4.currentposition[0])
                                    Player4.currentposition[0] += 1
                                elif n == 2:
                                    Player4.move(Player4.currentposition[0])
                                    Player4.currentposition[0] += 2
                                elif n == 3:
                                    Player4.move(Player4.currentposition[0])
                                    Player4.currentposition[0] += 3
                                elif n == 4:
                                    Player4.move(Player4.currentposition[0])
                                    Player4.currentposition[0] += 4
                                elif n == 5:
                                    Player4.move(Player4.currentposition[0])
                                    Player4.currentposition[0] += 5
                                elif n == 6:
                                    Player4.move(Player4.currentposition[0])
                                    Player4.currentposition[0] += 6
                                p_turn = 1

                            elif Player4.currentposition[0] < 50:
                                if n == 1:
                                    Player4.move(Player4.currentposition[0])
                                    Player4.currentposition[0] += 1
                                elif n == 2:
                                    Player4.move(Player4.currentposition[0])
                                    Player4.currentposition[0] += 2
                                elif n == 3:
                                    Player4.move(Player4.currentposition[0])
                                    Player4.currentposition[0] += 3
                                elif n == 4:
                                    Player4.move(Player4.currentposition[0])
                                    Player4.currentposition[0] += 4
                                elif n == 5:
                                    Player4.move(Player4.currentposition[0])
                                    Player4.currentposition[0] += 5
                                elif n == 6:
                                    Player4.move(Player4.currentposition[0])
                                    Player4.currentposition[0] += 6
                                p_turn = 1

                            else:
                                p_turn = 1
                                mouse_clicked = False

            elif mouse_clicked == True and mouse_x >= 885 and mouse_x <= 935 and mouse_y >= 600 and mouse_y <= 650:
                move_button = 2
                mouse_clicked = False

                if move_button == 2:
                    diff = (56 - Player4.currentposition[1])

                    if Player4.initialstatus[1] == 0:

                            if n == 6:
                                Player4.initialstatus[1] = 1    # change the status of button 2 for player 4
                                initiated4[2] = position_yellow[2]    # set the button which has been initiated
                                Player4.initiatestart(2)        # Function call to initiate the start of button1
                                mouse_clicked = False            # Change the status of the event
                                Player4.currentposition[1] = 0

                            else:
                                p_turn = 1                        # change the p_turn if number is not 6
                                mouse_clicked = False

                    else:
                        if Player4.finalstatus[1] != 1:

                            if Player4.currentposition[1] >= 50 and n <= diff:
                                if n == 1:
                                    Player4.move(Player4.currentposition[1])
                                    Player4.currentposition[1] += 1
                                elif n == 2:
                                    Player4.move(Player4.currentposition[1])
                                    Player4.currentposition[1] += 2
                                elif n == 3:
                                    Player4.move(Player4.currentposition[1])
                                    Player4.currentposition[1] += 3
                                elif n == 4:
                                    Player4.move(Player4.currentposition[1])
                                    Player4.currentposition[1] += 4
                                elif n == 5:
                                    Player4.move(Player4.currentposition[1])
                                    Player4.currentposition[1] += 5
                                elif n == 6:
                                    Player4.move(Player4.currentposition[1])
                                    Player4.currentposition[1] += 6
                                p_turn = 1

                            elif Player4.currentposition[1] < 50:
                                if n == 1:
                                    Player4.move(Player4.currentposition[1])
                                    Player4.currentposition[1] += 1
                                elif n == 2:
                                    Player4.move(Player4.currentposition[1])
                                    Player4.currentposition[1] += 2
                                elif n == 3:
                                    Player4.move(Player4.currentposition[1])
                                    Player4.currentposition[1] += 3
                                elif n == 4:
                                    Player4.move(Player4.currentposition[1])
                                    Player4.currentposition[1] += 4
                                elif n == 5:
                                    Player4.move(Player4.currentposition[1])
                                    Player4.currentposition[1] += 5
                                elif n == 6:
                                    Player4.move(Player4.currentposition[1])
                                    Player4.currentposition[1] += 6
                                p_turn = 1

                            else:
                                p_turn = 1
                                mouse_clicked = False

            elif mouse_clicked == True and mouse_x >= 935 and mouse_x <= 985 and mouse_y >= 600 and mouse_y <= 650:
                move_button = 3
                mouse_clicked = False

                if move_button == 3:
                    diff = (56 - Player4.currentposition[2])

                    if Player4.initialstatus[2] == 0:

                            if n == 6:
                                Player4.initialstatus[2] = 1    # change the status of button 3 for player 4
                                initiated4[3] = position_yellow[3]    # set the button which has been initiated
                                Player4.initiatestart(3)        # Function call to initiate the start of button1
                                mouse_clicked = False            # Change the status of the event
                                Player4.currentposition[2] = 0

                            else:
                                p_turn = 1                        # change the p_turn if number is not 6
                                mouse_clicked = False

                    else:
                        if Player4.finalstatus[2] != 1:

                            if Player4.currentposition[2] >= 50 and n <= diff:
                                if n == 1:
                                    Player4.move(Player4.currentposition[2])
                                    Player4.currentposition[2] += 1
                                elif n == 2:
                                    Player4.move(Player4.currentposition[2])
                                    Player4.currentposition[2] += 2
                                elif n == 3:
                                    Player4.move(Player4.currentposition[2])
                                    Player4.currentposition[2] += 3
                                elif n == 4:
                                    Player4.move(Player4.currentposition[2])
                                    Player4.currentposition[2] += 4
                                elif n == 5:
                                    Player4.move(Player4.currentposition[2])
                                    Player4.currentposition[2] += 5
                                elif n == 6:
                                    Player4.move(Player4.currentposition[2])
                                    Player4.currentposition[2] += 6
                                p_turn = 1

                            elif Player4.currentposition[2] < 50:
                                if n == 1:
                                    Player4.move(Player4.currentposition[2])
                                    Player4.currentposition[2] += 1
                                elif n == 2:
                                    Player4.move(Player4.currentposition[2])
                                    Player4.currentposition[2] += 2
                                elif n == 3:
                                    Player4.move(Player4.currentposition[2])
                                    Player4.currentposition[2] += 3
                                elif n == 4:
                                    Player4.move(Player4.currentposition[2])
                                    Player4.currentposition[2] += 4
                                elif n == 5:
                                    Player4.move(Player4.currentposition[2])
                                    Player4.currentposition[2] += 5
                                elif n == 6:
                                    Player4.move(Player4.currentposition[2])
                                    Player4.currentposition[2] += 6
                                p_turn = 1

                            else:
                                p_turn = 1
                                mouse_clicked = False

            elif mouse_clicked == True and mouse_x >= 985 and mouse_x <= 1035 and mouse_y >= 600 and mouse_y <= 650:
                move_button = 4
                mouse_clicked = False

                if move_button == 4:
                    diff = (56 - Player4.currentposition[3])

                    if Player4.initialstatus[3] == 0:
                            if n == 6:
                                Player4.initialstatus[3] = 1    # change the status of button 4 for player 4
                                initiated4[0] = position_yellow[0]    # set the button which has been initiated
                                Player4.initiatestart(4)        # Function call to initiate the start of button4
                                mouse_clicked = False            # Change the status of the event
                                Player4.currentposition[3] = 0

                            else:
                                p_turn = 1                        # change the p_turn if number is not 6
                                mouse_clicked = False

                    else:
                        if Player4.finalstatus[3] != 1:

                            if Player4.currentposition[3] >= 50 and n <= diff:
                                if n == 1:
                                    Player4.move(Player4.currentposition[3])
                                    Player4.currentposition[3] += 1
                                elif n == 2:
                                    Player4.move(Player4.currentposition[3])
                                    Player4.currentposition[3] += 2
                                elif n == 3:
                                    Player4.move(Player4.currentposition[3])
                                elif n == 4:
                                    Player4.move(Player4.currentposition[3])
                                    Player4.currentposition[3] += 4
                                elif n == 5:
                                    Player4.move(Player4.currentposition[3])
                                    Player4.currentposition[3] += 5
                                elif n == 6:
                                    Player4.move(Player4.currentposition[3])
                                    Player4.currentposition[3] += 6
                                p_turn = 1

                            elif Player4.currentposition[3] < 50:
                                if n == 1:
                                    Player4.move(Player4.currentposition[3])
                                    Player4.currentposition[3] += 1
                                elif n == 2:
                                    Player4.move(Player4.currentposition[3])
                                    Player4.currentposition[3] += 2
                                elif n == 3:
                                    Player4.move(Player4.currentposition[3])
                                    Player4.currentposition[3] += 3
                                elif n == 4:
                                    Player4.move(Player4.currentposition[3])
                                    Player4.currentposition[3] += 4
                                elif n == 5:
                                    Player4.move(Player4.currentposition[3])
                                    Player4.currentposition[3] += 5
                                elif n == 6:
                                    Player4.move(Player4.currentposition[3])
                                    Player4.currentposition[3] += 6
                                p_turn = 1

                            else:
                                p_turn = 1
                                mouse_clicked = False

        Player1.isinhome()
        Player2.isinhome()
        Player3.isinhome()
        Player4.isinhome()
        pygame.display.update()

main()

