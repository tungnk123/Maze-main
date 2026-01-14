"""
This file contains all the GLOBAL variables and imports all the required modules for the game loop to run smoothly.
(And also for easy modification as per requirements.)
"""
import pygame
import sys
import os
import Modules.MainMenu as MainMenu
import Modules.PlayGame as PlayGame
import Modules.Scores as Scores

# Suppress stderr
sys.stderr = open(os.devnull, 'w')

# Ensuring that the required files exist
os.makedirs('data', exist_ok=True)
with open('data/path.txt', 'a'):
    pass
if not os.path.isfile('data/LeastTimes.txt'):
    with open('data/LeastTimes.txt', 'w') as f:
        f.write("1000\n1000\n1000")

# Initializing Pygame
pygame.init()


# Defining a Quit function, which quits the pygame
def Quit():
    pygame.quit()
    sys.exit()


# For Loading a ScaledImage easily
def LoadScaledImage(image_path: str, scaling_factor: float = 1.0, scaling_dim: tuple = (0, 0)):
    image = pygame.image.load(image_path)
    if scaling_dim != (0, 0):
        resized_image = pygame.transform.scale(image, scaling_dim)
    elif scaling_factor != 1:
        new_width = int(image.get_width() * scaling_factor)
        new_height = int(image.get_height() * scaling_factor)
        resized_image = pygame.transform.scale(image, (new_width, new_height))
    else:
        resized_image = image
    return resized_image


# DIMENSIONS
WINDOW_DIM = (1440, 810)  # Three-Fourths of the most common screen resolution: 1920 * 1080
# Clock
clock = pygame.time.Clock()
# General Key delay
KeyDelay = 0.1
# General Button delay
ButtonDelay = 0.1
# Back Button - General
BackButtonBackground = LoadScaledImage("media/images/Buttons/MainMenuButton.png", scaling_dim=(300, 100))
BackButtonPos = ((WINDOW_DIM[0] / 2), (WINDOW_DIM[1] * 5 / 6))
BackButtonDelay = 0.5

# Intro
IntroTime = 3
PygameLogo = LoadScaledImage("media/images/Logos/pygame_powered.png", scaling_factor=(1 / 3))
PygameLogoPosition = ((WINDOW_DIM[0] / 2), (WINDOW_DIM[1] / 2) - 100)

IntroFontSize = 100
MazeHeadingFont = pygame.font.Font("media/fonts/Herona.ttf", IntroFontSize)
IntroMazeText = MazeHeadingFont.render("Maze", True, 'Yellow')

IntroLoadingBarBackground = LoadScaledImage("media/images/IntroLoadingBar/IntroLoadingBarBackground.png",
                                            scaling_dim=(500, 50))

# Main Menu

#    Background
MainMenuBackground = [LoadScaledImage(f"media/videos/MainMenuBackgroundDimmed/frame{i}.jpg", scaling_dim=WINDOW_DIM) for
                      i in range(600)]
MainMenuBackgroundFrameTime = 20

#    Header

#        PYGAME
MainMenuHeaderLogo = LoadScaledImage("media/images/Logos/pygame_logo_colorful.png", scaling_factor=(1 / 5))
MainMenuHeaderLogoPosition = ((WINDOW_DIM[0] / 2), (WINDOW_DIM[1] / 10))
MainMenuHeaderMaze = MazeHeadingFont.render("Maze", True, 'Yellow')

#        MAZE
MainMenuMazeFontSize = 75
MainMenuMazeFont = pygame.font.Font("media/fonts/Rubber-Duck.ttf", MainMenuMazeFontSize)
MainMenuMazeText = MainMenuMazeFont.render("MAZE", True, "White")

#    Buttons
MMButtonsImage = LoadScaledImage("media/images/Buttons/MainMenuButton.png", scaling_dim=(400, 100))
InactiveButtonFontSize = 25
ActiveButtonFontSize = 35
ButtonsFontInactive = pygame.font.Font("media/fonts/MightySouly.ttf", InactiveButtonFontSize)
ButtonsFontActive = pygame.font.Font("media/fonts/MightySouly.ttf", ActiveButtonFontSize)

PlayPos = (WINDOW_DIM[0] / 2, 350)
ScoresPos = (WINDOW_DIM[0] / 2, 450)
PreferencesPos = (WINDOW_DIM[0] / 2, 550)
QuitPos = (WINDOW_DIM[0] / 2, 650)

# Game!
PlayerName = "MrStark"  # Default Name

SolutionPathFileAddress = "data/path.txt"

TimeButtonImage = LoadScaledImage("media/images/Buttons/MainMenuButton.png",
                                  scaling_dim=(int(((WINDOW_DIM[0] - WINDOW_DIM[1]) / 2) * 1.5), int(75 * 1.5)))
StopWatchButtonPos = ((WINDOW_DIM[1] + WINDOW_DIM[0]) / 2 + WINDOW_DIM[0] / 20, 100)
GameStopwatchFont = pygame.font.Font("media/fonts/ArialRoundedMTBold.ttf", 35)

TimeTakenButtonPos = (WINDOW_DIM[0] / 2, WINDOW_DIM[1] / 2 - 25)

GameOverPNG_Address = "media/images/GameOver.png"

HighScoreButtonPos = (WINDOW_DIM[0] / 2, WINDOW_DIM[1] / 2 + 75)

# Scores
#    High Scores CSV File Address
HighScoresCSV_Address = "data/LeastTimes.txt"


''' PyGame Variables '''

# Pygame Screen
screen = pygame.display.set_mode(WINDOW_DIM)
pygame.display.set_caption("Maze!")

# MAIN MENU
#    Main Menu Buttons
MM_Play = MainMenu.MainMenuButton(screen, "PLAY", ButtonsFontInactive, ButtonsFontActive, MMButtonsImage, PlayPos)
MM_Scores = MainMenu.MainMenuButton(screen, "FASTEST SOLVES", ButtonsFontInactive, ButtonsFontActive, MMButtonsImage,
                                    ScoresPos)
MM_Quit = MainMenu.MainMenuButton(screen, "QUIT", ButtonsFontInactive, ButtonsFontActive, MMButtonsImage, PreferencesPos)
#    Main Menu Screen
main_menu = MainMenu.MainMenu(screen, (MM_Play, MM_Scores, MM_Quit))

# The GAME!!!
PlayerImagesPath = "media/images/Player"
MazeImagesPath = "media/images/MazeBackground"
Game = PlayGame.GamePlay(screen, PlayerName, PlayerImagesPath, MazeImagesPath, SolutionPathFileAddress, GameOverPNG_Address)
#    Game Level Buttons
EasyPos = (WINDOW_DIM[0] / 2, 200)
MediumPos = (WINDOW_DIM[0] / 2, 350)
DifficultPos = (WINDOW_DIM[0] / 2, 500)
GLB_Easy = MainMenu.MainMenuButton(screen, "EASY (20 X 20)", ButtonsFontInactive, ButtonsFontActive, MMButtonsImage, EasyPos)
GLB_Medium = MainMenu.MainMenuButton(screen, "MEDIUM (40 X 40)", ButtonsFontInactive, ButtonsFontActive, MMButtonsImage,
                                     MediumPos)
GLB_Difficult = MainMenu.MainMenuButton(screen, "DIFFICULT (60 X 60)", ButtonsFontInactive, ButtonsFontActive, MMButtonsImage,
                                        DifficultPos)

# Level Selection Back Button (ở trên cùng)
LevelBackButtonPos = (WINDOW_DIM[0] / 2, 50)
GLB_Level_Back = MainMenu.MainMenuButton(screen, "BACK", ButtonsFontInactive, ButtonsFontActive, BackButtonBackground,
                                         LevelBackButtonPos)

#    Game
GameRightBackground = MainMenuBackground[0].subsurface(pygame.Rect(screen.get_height() + Game.XShift, 0, screen.get_width() - (screen.get_height() + Game.XShift), screen.get_height()))

# Game Over
GameOver_Back = MainMenu.MainMenuButton(screen, "MAIN MENU", ButtonsFontInactive, ButtonsFontActive, BackButtonBackground, BackButtonPos)

#        GameButtons
GameBackButtonPos = ((screen.get_height() + screen.get_width()) / 2 + Game.XShift / 2, BackButtonPos[1])
Game_Back = MainMenu.MainMenuButton(screen, "BACK", ButtonsFontInactive, ButtonsFontActive, BackButtonBackground,
                                    GameBackButtonPos)


GameButtonImage = LoadScaledImage("media/images/Buttons/MainMenuButton.png", scaling_dim=(300, 100))

ChangeThemeButtonPos = ((screen.get_height() + screen.get_width()) / 2 + Game.XShift / 2, 300)
Game_ChangeBackground = MainMenu.MainMenuButton(screen, "CHANGE THEME", ButtonsFontInactive, ButtonsFontActive, GameButtonImage, ChangeThemeButtonPos)

# Auto Solve Button (DFS)
AutoSolveButtonPos = ((screen.get_height() + screen.get_width()) / 2 + Game.XShift / 2, 400)
Game_AutoSolve = MainMenu.MainMenuButton(screen, "AUTO SOLVE (DFS)", ButtonsFontInactive, ButtonsFontActive, GameButtonImage, AutoSolveButtonPos)

# Export Testcase Button
ExportButtonPos = ((screen.get_height() + screen.get_width()) / 2 + Game.XShift / 2, 500)
Game_Export = MainMenu.MainMenuButton(screen, "EXPORT TESTCASE", ButtonsFontInactive, ButtonsFontActive, GameButtonImage, ExportButtonPos)

# Import Testcase Button (sẽ hiển thị ở Level Selection)
ImportButtonPos = (WINDOW_DIM[0] / 2, 650)
Game_Import = MainMenu.MainMenuButton(screen, "IMPORT TESTCASE", ButtonsFontInactive, ButtonsFontActive, MMButtonsImage, ImportButtonPos)

# Testcase Selection Back Button (ở trên cùng)
TestcaseBackButtonPos = (WINDOW_DIM[0] / 2, 50)
Testcase_Back = MainMenu.MainMenuButton(screen, "BACK", ButtonsFontInactive, ButtonsFontActive, BackButtonBackground, TestcaseBackButtonPos)


# Scores
Scores = Scores.HighScores(screen, HighScoresCSV_Address, ButtonsFontActive)
Scores_Back = MainMenu.MainMenuButton(screen, "BACK", ButtonsFontInactive, ButtonsFontActive, BackButtonBackground, BackButtonPos)
