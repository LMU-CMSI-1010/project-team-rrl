import pygame

# initial menu class with basic functions
class Menu():
    def __init__(self, game):
        self.game = game
        self.half_w = self.game.display_width / 2
        self.half_h = self.game.display_height / 2
        self.run_display = True
        self.cursor_rect = pygame.Rect(0, 0, 20, 20)
        self. offset = -100
        pygame.display.set_caption('shooter!')

    # indicates which line of the menu you're on
    def drawCursor(self):
        self.game.drawText("*", 25, self.cursor_rect.x, self.cursor_rect.y)
    
    # clears screen between frames
    def blitScreen(self):
        self.game.window.blit(self.game.display, (0, 0))
        pygame.display.update()
        self.game.resetInput()

# derived from menu, shows the main menu
class MainMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = "Start"
        self.startx, self.starty = self.half_w, self.half_h + 30
        self.helpx, self.helpy = self.half_w, self.half_h + 50
        self.creditsx, self.creditsy = self.half_w, self.half_h + 70
        self.quitx, self.quity = self.half_w, self.half_h + 90
        self.cursor_rect.midtop = (self.startx + self.offset, self.starty)
    
    # displays each line of the menu while the game is running but not playing
    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.checkEvents()
            self.checkInput()
            self.game.display.fill(self.game.black)
            self.game.drawText("shooter!", 50, self.half_w + 10, self.half_h - 100)
            self.game.drawText("Main Menu", 20, self.half_w, self.half_h - 20)
            self.game.drawText("Start Game", 20, self.startx, self.starty)
            self.game.drawText("Help", 20, self.helpx, self.helpy)
            self.game.drawText("Quit", 20, self.quitx, self.quity)
            self.game.drawText("Credits", 20, self.creditsx, self.creditsy)
            self.drawCursor()
            self.blitScreen()

    # allows the cursor to go between the three menu options
    def moveCursor(self):
        if self.game.down_key:
            if self.state == "Start":
                self.cursor_rect.midtop = (self.helpx + self.offset, self.helpy)
                self.state = "Help"
            elif self.state == "Help":
                self.cursor_rect.midtop = (self.quitx + self.offset, self.quity)
                self.state = "Quit"
            elif self.state == "Quit":
                self.cursor_rect.midtop = (self.creditsx + self.offset, self.creditsy)
                self.state = "Credits"
            elif self.state == "Credits":
                self.cursor_rect.midtop = (self.startx + self.offset, self.starty)
                self.state = "Start"
        if self.game.up_key:
            if self.state == "Start":
                self.cursor_rect.midtop = (self.creditsx + self.offset, self.creditsy)
                self.state = "Credits"
            elif self.state == "Credits":
                self.cursor_rect.midtop = (self.quitx + self.offset, self.quity)
                self.state = "Quit"
            elif self.state == "Help":
                self.cursor_rect.midtop = (self.startx + self.offset, self.starty)
                self.state = "Start"
            elif self.state == "Quit":
                self.cursor_rect.midtop = (self.helpx + self.offset, self.helpy)
                self.state = "Help"

    # uses pygame to check what the user has entered
    def checkInput(self):
        self.moveCursor()
        if self.game.start_key:
            if self.state == "Start":
                self.game.playing = True
            elif self.state == "Help":
                self.game.curr_menu = self.game.helpMenu
            elif self.state == "Quit":
                self.game.curr_menu = self.game.quitMenu
            elif self.state == "Credits":
                self.game.curr_menu = self.game.creditsMenu
            self.run_display = False

# doesn't actually work 100%, needs some TLC to get the cursor to do its thing , quit function doesnt work 
# # shows the quit menu and all the sub-menus under it  
class quitMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = "Yes!"
        self.yesx, self.yesy = self.half_w, self.half_h + 20
        self.nox, self.noy = self.half_w, self.half_h + 40
        self.cursor_rect.midtop = (self.yesx + self.offset, self.yesy)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.checkEvents()
            if self.game.back_key:
                self.game.curr_menu = self.game.mainMenu
                self.run_display = False
            elif self.game.up_key or self.game.down_key:
                if self.state == "Yes!":
                    self.cursor_rect.midtop = (self.nox + self.offset, self.noy)
                    self.state = "No!"
                elif self.state == "No!":
                    self.cursor_rect.midtop = (self.yesx + self.offset, self.yesy)
                    self.state == "Yes!"
            elif self.game.start_key:
                if self.state == "Yes!":
                    self.playing = False
                elif self.state == "No!":
                    self.game.curr_menu = self.game.mainMenu
                self.run_display = False
            self.game.display.fill((self.game.black))
            self.game.drawText("Are you sure you want to quit?", 20, self.half_w, self.half_h - 30)
            self.game.drawText("Yes!", 15, self.yesx, self.yesy)
            self.game.drawText("No!", 15, self.nox, self.noy)
            self.drawCursor()
            self.blitScreen()

    """
    # move between the different options (i hope)
    def moveCursor(self):
        if self.game.up_key or self.game.down_key:
            if self.state == "Yes!":
                self.cursor_rect.midtop = (self.nox + self.offset, self.noy)
                self.state = "No!"
            elif self.state == "No!":
                self.cursor_rect.midtop = (self.yesx + self.offset, self.yesy)
                self.state == "Yes!"
    """
    # check what user input is
    """
    def checkInput(self):
        self.moveCursor()
        if self.game.back_key:
            self.game.curr_menu = self.game.mainMenu
            self.run_display = False
        elif self.game.up_key or self.game.down_key:
            if self.state == "Yes!":
                self.cursor_rect.midtop = (self.nox + self.offset, self.noy)
                self.state = "No!"
            elif self.state == "No!":
                self.cursor_rect.midtop = (self.yesx + self.offset, self.yesy)
                self.state == "Yes!"
        elif self.game.start_key:
            if self.state == "Yes!":
                pygame.quit()
            elif self.state == "No!":
                self.game.curr_menu = self.game.mainMenu
            # self.run_display = False
    """
# shows the help menu (which is just a picture)
class helpMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
    
    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.checkEvents()
            if self.game.start_key or self.game.back_key:
                self.game.curr_menu = self.game.mainMenu
                self.run_display = False
            self.game.display.fill(self.game.black)
            helpscrn = pygame.image.load("assets/screens/help_screen.png").convert()
            pygame.display.flip()
            self.game.window.blit(helpscrn, (0,0))

# shows the credits screen based on the Menu class (another picture) 
class creditsMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
    
    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.checkEvents()
            if self.game.back_key:
                self.game.curr_menu = self.game.mainMenu
                self.run_display = False
            self.game.display.fill(self.game.black)
            creditscrn = pygame.image.load("gametest/credits_screen.png").convert()
            pygame.display.flip()
            self.game.window.blit(creditscrn, (0,0))