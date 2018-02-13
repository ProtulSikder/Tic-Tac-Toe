import pygame,random,sys

class main_game:
    def __init__(self,user_input):
        self.user_input = user_input

        pygame.init()

        self.black = (0, 0, 0)
        self.white = (255, 255, 255)
        self.red = (255, 0, 0)
        self.green = (0, 255, 0)
        self.blue = (0, 0, 255)
        self.yellow = (255, 255, 0)

        self.windowSize = (300,150)
        self.screen = pygame.display.set_mode(self.windowSize)
        pygame.display.set_caption('3x3 Tic Tac Toe')

        pygame.draw.line(self.screen, self.blue, (0, 50), (300, 50), 4)
        pygame.draw.line(self.screen, self.blue, (0, 100), (300, 100), 4)
        pygame.draw.line(self.screen, self.blue, (100, 0), (100, 150), 4)
        pygame.draw.line(self.screen, self.blue, (200, 0), (200, 150), 4)

    def circle(self,cent_x,cent_y):
        pygame.draw.circle(self.screen, self.yellow, (cent_x, cent_y), 18, 3)

    def line_1(self, x1, y1, x2, y2):
        pygame.draw.line(self.screen, self.yellow, (x1, y1), (x2, y2), 3)

    def cross(self, a, b, c, d, e, f, g, h):
        self.line_1(a, b, c, d)
        self.line_1(e, f, g, h)

    def game_loop(self):
        if self.user_input == 'c':
            x_or_o = 1
        else:
            x_or_o = 0

        box = {
                'b_1_1': 0,
                'b_1_2': 0,
                'b_1_3': 0,
                'b_2_1': 0,
                'b_2_2': 0,
                'b_2_3': 0,
                'b_3_1': 0,
                'b_3_2': 0,
                'b_3_3': 0,
            }

        box_choice = [i for i in box.keys()]
        occupied_box = []
        winCondition = [{1, 2, 3}, {4, 5, 6}, {7, 8, 9}, {1, 4, 7}, {2, 5, 8}, {3, 6, 9}, {1, 5, 9}, {3, 5, 7}]

        wiloCross = set()
        wiloCircle = set()
        gameloop = 1
        while gameloop:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

                if x_or_o % 2 == 1:
                    while len(occupied_box) != 9:
                        choose = random.choice(box_choice)

                        if box[choose] == 0:
                            box[choose] = 1
                            occupied_box.append(choose)
                            break

                    if choose == 'b_1_1':
                        self.circle(50, 25)
                        x_or_o += 1
                        wiloCircle.add(1)

                    elif choose == 'b_1_2':
                        self.circle(150, 25)
                        x_or_o += 1
                        wiloCircle.add(2)

                    elif choose == 'b_1_3':
                        self.circle(250, 25)
                        x_or_o += 1
                        wiloCircle.add(3)

                    elif choose == 'b_2_1':
                        self.circle(50, 75)
                        x_or_o += 1
                        wiloCircle.add(4)

                    elif choose == 'b_2_2':
                        self.circle(150, 75)
                        x_or_o += 1
                        wiloCircle.add(5)

                    elif choose == 'b_2_3':
                        self.circle(250, 75)
                        x_or_o += 1
                        wiloCircle.add(6)

                    elif choose == 'b_3_1':
                        self.circle(50, 125)
                        x_or_o += 1
                        wiloCircle.add(7)

                    elif choose == 'b_3_2':
                        self.circle(150, 125)
                        x_or_o += 1
                        wiloCircle.add(8)

                    elif choose == 'b_3_3':
                        self.circle(250, 125)
                        x_or_o += 1
                        wiloCircle.add(9)

                elif x_or_o % 2 == 0:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        mouse_pos = pygame.mouse.get_pos()

                        if mouse_pos[0] < 100 and mouse_pos[1] < 50 and box['b_1_1'] != 1:
                            self.cross(25, 12, 75, 37, 75, 12, 25, 37)
                            x_or_o += 1
                            box['b_1_1'] = 1
                            occupied_box.append('b_1_1')
                            wiloCross.add(1)

                        elif mouse_pos[0] > 100 and mouse_pos[0] < 200 and mouse_pos[1] < 50 and box['b_1_2'] != 1:
                            self.cross(125, 12, 175, 37, 175, 12, 125, 37)
                            x_or_o += 1
                            box['b_1_2'] = 1
                            occupied_box.append('b_1_2')
                            wiloCross.add(2)

                        elif mouse_pos[0] > 200 and mouse_pos[0] < 300 and mouse_pos[1] < 50 and box['b_1_3'] != 1:
                            self.cross(225, 12, 275, 37, 275, 12, 225, 37)
                            x_or_o += 1
                            box['b_1_3'] = 1
                            occupied_box.append('b_1_3')
                            wiloCross.add(3)

                        elif mouse_pos[0] < 100 and mouse_pos[1] < 100 and box['b_2_1'] != 1:
                            self.cross(25, 63, 75, 87, 75, 63, 25, 87)
                            x_or_o += 1
                            box['b_2_1'] = 1
                            occupied_box.append('b_2_1')
                            wiloCross.add(4)

                        elif mouse_pos[0] > 100 and mouse_pos[0] < 200 and mouse_pos[1] < 100 and box['b_2_2'] != 1:
                            self.cross(125, 63, 175, 87, 175, 63, 125, 87)
                            x_or_o += 1
                            box['b_2_2'] = 1
                            occupied_box.append('b_2_2')
                            wiloCross.add(5)

                        elif mouse_pos[0] > 200 and mouse_pos[0] < 300 and mouse_pos[1] < 100 and box['b_2_3'] != 1:
                            self.cross(225, 63, 275, 87, 275, 63, 225, 87)
                            x_or_o += 1
                            box['b_2_3'] = 1
                            occupied_box.append('b_2_3')
                            wiloCross.add(6)

                        elif mouse_pos[0] < 100 and mouse_pos[1] > 100 and box['b_3_1'] != 1:
                            self.cross(25, 113, 75, 137, 75, 113, 25, 137)
                            x_or_o += 1
                            box['b_3_1'] = 1
                            occupied_box.append('b_3_1')
                            wiloCross.add(7)

                        elif mouse_pos[0] > 100 and mouse_pos[0] < 200 and mouse_pos[1] > 100 and box['b_3_2'] != 1:
                            self.cross(125, 113, 175, 137, 175, 113, 125, 137)
                            x_or_o += 1
                            box['b_3_2'] = 1
                            occupied_box.append('b_3_2')
                            wiloCross.add(8)

                        elif mouse_pos[0] > 200 and mouse_pos[0] < 300 and mouse_pos[1] > 100 and box['b_3_3'] != 1:
                            self.cross(225, 113, 275, 137, 275, 113, 225, 137)
                            x_or_o += 1
                            box['b_3_3'] = 1
                            occupied_box.append('b_3_3')
                            wiloCross.add(9)

                for wilo in winCondition:
                    if wilo.issubset(wiloCircle) or wilo.issubset(wiloCross):
                        if wilo == {1, 2, 3}:
                            self.line_1(20, 25, 275, 25)
                            gameloop = 0

                        elif wilo == {4, 5, 6}:
                            self.line_1(20, 75, 275, 75)
                            gameloop = 0

                        elif wilo == {7, 8, 9}:
                            self.line_1(20, 125, 275, 125)
                            gameloop = 0

                        elif wilo == {1, 4, 7}:
                            self.line_1(50, 10, 50, 140)
                            gameloop = 0

                        elif wilo == {2, 5, 8}:
                            self.line_1(150, 10, 150, 140)
                            gameloop = 0

                        elif wilo == {3, 6, 9}:
                            self.line_1(250, 10, 250, 140)
                            gameloop = 0

                        elif wilo == {1, 5, 9}:
                            self.line_1(10, 12, 289, 140)
                            gameloop = 0

                        elif wilo == {3, 5, 7}:
                            self.line_1(289, 12, 10, 140)
                            gameloop = 0


            pygame.display.update()



if __name__ == '__main__':
    print('Welcome to the 5x5 Tic Tac Toe.\n\nDo you want to play first?\n')

    while 1:
        print("If you want to play first press 'u' button.")
        print("If you want to let the computer to play first press 'c' button.")
        print("If you want to quit press 'q'.")
        inp = input('Enter here(c/u/q):')

        if inp == 'c' or inp == 'u':
            start = main_game(inp)
            start.game_loop()
        elif inp == 'q':
            break
        else:
            print("You pressed the long button.Try again.\n\n")