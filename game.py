from settings import *
import time

# Testcase selection state
TestcaseSelectMode = False
SelectedTestcaseIndex = 0

# PYGAME LOOP
start_ticks = pygame.time.get_ticks()
while True:
    PygameEvents = pygame.event.get()
    keys = pygame.key.get_pressed()
    # Mouse Position
    MousePosition = pygame.mouse.get_pos()

    # QUIT
    for event in PygameEvents:
        if event.type == pygame.QUIT:
            Quit()

    # Time
    MillisecondsPassed = pygame.time.get_ticks() - start_ticks

    # Intro Screen
    if MillisecondsPassed / 1000 < IntroTime - 0.5:
        PygameLogo_rect = PygameLogo.convert_alpha().get_rect()
        PygameLogo_rect.center = PygameLogoPosition
        screen.blit(PygameLogo.convert_alpha(), PygameLogo_rect)

        IntroMazeText_rect = IntroMazeText.get_rect()
        IntroMazeText_rect.midtop = (PygameLogo_rect.midbottom[0] - 20,
                                     PygameLogo_rect.midbottom[1])
        screen.blit(IntroMazeText, IntroMazeText_rect)

        IntroLoadingBarBackground_rect = IntroLoadingBarBackground.get_rect()
        IntroLoadingBarBackground_rect.midtop = (IntroMazeText_rect.midbottom[0], (IntroMazeText_rect.midbottom[1] + 50))
        screen.blit(IntroLoadingBarBackground, IntroLoadingBarBackground_rect)

        xLength = 480 * MillisecondsPassed / ((IntroTime - 0.5) * 1000)
        IntroLoadingBar = LoadScaledImage("media/images/IntroLoadingBar/IntroLoadingBar.png", scaling_dim=(xLength, 40))
        IntroLoadingBar_rect = IntroLoadingBar.get_rect()
        IntroLoadingBar_rect.midleft = (IntroLoadingBarBackground_rect.midleft[0] + 10, IntroLoadingBarBackground_rect.midleft[1])
        screen.blit(IntroLoadingBar, IntroLoadingBar_rect)
    elif int((MillisecondsPassed / 1000) * 4) / 4 == IntroTime - 0.25:
        screen.fill("Black")
    elif int((MillisecondsPassed / 1000) * 4) / 4 == IntroTime + 0.25:
        main_menu.is_active = True

    # Main Menu
    if main_menu.is_active:
        # Setting the frame rate
        main_menu.BackgroundFrameIndex = (MillisecondsPassed % (
                MainMenuBackgroundFrameTime * len(MainMenuBackground))) // MainMenuBackgroundFrameTime
        # Main Menu Background
        main_menu.BackgroundDisplay(MainMenuBackground[main_menu.BackgroundFrameIndex])
        # Header of the MainMenu
        MainMenuHeaderLogo_rect = MainMenuHeaderLogo.get_rect()
        MainMenuHeaderLogo_rect.center = MainMenuHeaderLogoPosition
        screen.blit(MainMenuHeaderLogo, MainMenuHeaderLogo_rect)
        MainMenuMazeText_rect = MainMenuMazeText.get_rect()
        MainMenuMazeText_rect.midtop = (MainMenuHeaderLogo_rect.midbottom[0] - 10, MainMenuHeaderLogo_rect.midbottom[1] + 20)
        screen.blit(MainMenuMazeText, MainMenuMazeText_rect)
        # Main Menu Buttons
        main_menu.Buttons()
        if MM_Quit.is_Clicked():
            Quit()
        elif MM_Play.is_Clicked():
            main_menu.is_active = False
            time.sleep(ButtonDelay)
            Game.is_active = True
        elif MM_Scores.is_Clicked():
            main_menu.is_active = False
            time.sleep(ButtonDelay)
            Scores.is_active = True

    # The Game!
    if Game.is_active:
        # Testcase Selection Mode
        if TestcaseSelectMode:
            main_menu.BackgroundDisplay(MainMenuBackground[0])

            # Lấy danh sách testcases
            testcases = Game.GetTestcaseList()

            if len(testcases) == 0:
                # Không có testcase
                no_tc_text = ButtonsFontActive.render("NO TESTCASES FOUND", True, 'WHITE')
                screen.blit(no_tc_text, no_tc_text.get_rect(center=(WINDOW_DIM[0] / 2, WINDOW_DIM[1] / 2)))
            else:
                # Hiển thị danh sách testcases
                title_text = ButtonsFontActive.render("SELECT TESTCASE:", True, 'YELLOW')
                screen.blit(title_text, title_text.get_rect(center=(WINDOW_DIM[0] / 2, 150)))

                for i, tc in enumerate(testcases):
                    color = 'YELLOW' if i == SelectedTestcaseIndex else 'WHITE'
                    tc_text = ButtonsFontInactive.render(f"> {tc}" if i == SelectedTestcaseIndex else f"  {tc}", True, color)
                    screen.blit(tc_text, tc_text.get_rect(center=(WINDOW_DIM[0] / 2, 250 + i * 50)))

                # Hướng dẫn
                help_text = ButtonsFontInactive.render("UP/DOWN: Select | ENTER: Load | ESC: Back", True, 'WHITE')
                screen.blit(help_text, help_text.get_rect(center=(WINDOW_DIM[0] / 2, WINDOW_DIM[1] - 100)))

                # Xử lý phím
                for event in PygameEvents:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_UP:
                            SelectedTestcaseIndex = (SelectedTestcaseIndex - 1) % len(testcases)
                        elif event.key == pygame.K_DOWN:
                            SelectedTestcaseIndex = (SelectedTestcaseIndex + 1) % len(testcases)
                        elif event.key == pygame.K_RETURN:
                            # Load testcase
                            tc_path = f"testcases/{testcases[SelectedTestcaseIndex]}"
                            if Game.ImportTestcase(tc_path):
                                Game.Level = 1
                                Game.LevelScreen = False
                                Game.GameScreen = True
                                TestcaseSelectMode = False
                        elif event.key == pygame.K_ESCAPE:
                            TestcaseSelectMode = False

            # Back button (ở trên cùng)
            Testcase_Back.display()
            if Testcase_Back.is_Clicked():
                TestcaseSelectMode = False
                time.sleep(BackButtonDelay)

        elif Game.LevelScreen:
            # Background Static
            main_menu.BackgroundDisplay(MainMenuBackground[0])
            # Buttons
            GLB_Easy.display()
            GLB_Medium.display()
            GLB_Difficult.display()

            GLB_Level_Back.display()

            # Import Testcase Button
            Game_Import.display()

            # Button Functionality Implementation
            if GLB_Easy.is_Clicked() or GLB_Medium.is_Clicked() or GLB_Difficult.is_Clicked():
                Game.LevelScreen = False
                if GLB_Easy.is_Clicked():
                    Game.Level = 1
                elif GLB_Medium.is_Clicked():
                    Game.Level = 2
                elif GLB_Difficult.is_Clicked():
                    Game.Level = 3
                Game.GameScreen = True
                Game.SetMazeLevel()
                time.sleep(ButtonDelay)
            elif GLB_Level_Back.is_Clicked():
                Game.is_active = False
                main_menu.is_active = True
                time.sleep(BackButtonDelay)
            elif Game_Import.is_Clicked():
                # Chuyển sang chế độ chọn testcase
                TestcaseSelectMode = True
                SelectedTestcaseIndex = 0
                time.sleep(ButtonDelay)

        elif Game.GameScreen:
            screen.fill("Black")

            Game.GamePlay(keys, MillisecondsPassed)

            # Right Background for Displaying Buttons
            screen.blit(GameRightBackground, (screen.get_height() + Game.XShift, 0))

            # StopWatch
            StopWatchButton = MainMenu.MainMenuButton(screen, f"Time Elapsed = {int(Game.StopwatchValue / 1000)}s",
                                                      GameStopwatchFont, GameStopwatchFont, TimeButtonImage,
                                                      StopWatchButtonPos)
            StopWatchButton.display()

            # Change Background Button
            Game_ChangeBackground.display()
            # Auto Solve Button
            Game_AutoSolve.display()
            # Export Testcase Button
            Game_Export.display()
            # Back Button
            Game_Back.display()

            if Game_ChangeBackground.is_Clicked():
                Game.ChangeBackground()
                time.sleep(ButtonDelay)
            elif Game_AutoSolve.is_Clicked():
                Game.StartAutoSolve()
                time.sleep(ButtonDelay)
            elif Game_Export.is_Clicked():
                exported_path = Game.ExportTestcase()
                if exported_path:
                    print(f"Testcase exported to: {exported_path}")
                time.sleep(ButtonDelay)

            # Thực hiện auto-solve step nếu đang auto-solve
            if Game.AutoSolving:
                Game.AutoSolveStep()

            # Back Button Functionality
            if Game_Back.is_Clicked():
                Game.MazeGame = None
                Game.GameScreen = False
                Game.LevelScreen = True
                time.sleep(ButtonDelay)

            if Game.GameOverScreen:
                pass

        elif Game.GameOverScreen:
            # Background Static
            main_menu.BackgroundDisplay(MainMenuBackground[0])
            Game.GameOverScreenDisplay()
            GameOver_Back.display()

            # StopWatch
            TimeTakenButton = MainMenu.MainMenuButton(screen, f"TIME TAKEN = {int(Game.StopwatchValue / 1000)} SEC",
                                                      ButtonsFontInactive, ButtonsFontInactive, TimeButtonImage,
                                                      TimeTakenButtonPos)
            TimeTakenButton.display()

            # High Score
            Scores.UpdateScore(Game.StopwatchValue / 1000, Game.Level)

            # High Score String
            HighScoreString = ("NEW HIGH SCORE : " + str(int(Game.StopwatchValue / 1000)) + " SEC") if Scores.isUpdated else ("HIGH SCORE: " + Scores.HighScore(Game.Level) + " SEC")

            HighScoreButton = MainMenu.MainMenuButton(screen, HighScoreString, ButtonsFontInactive, ButtonsFontInactive,
                                                      MMButtonsImage, HighScoreButtonPos)
            HighScoreButton.display()

            # Hiển thị Solution Path (Output)
            solution_path, path_length = Game.GetSolutionInfo()

            # Tiêu đề OUTPUT
            output_title = ButtonsFontActive.render("SOLUTION (DFS OUTPUT):", True, 'YELLOW')
            screen.blit(output_title, output_title.get_rect(center=(WINDOW_DIM[0] / 2, WINDOW_DIM[1] / 2 + 180)))

            # Hiển thị đường đi (cắt ngắn nếu quá dài)
            if solution_path and len(solution_path) > 50:
                display_path = solution_path[:50] + "..."
            else:
                display_path = solution_path if solution_path else "N/A"

            path_text = ButtonsFontInactive.render(f"Path: {display_path}", True, 'WHITE')
            screen.blit(path_text, path_text.get_rect(center=(WINDOW_DIM[0] / 2, WINDOW_DIM[1] / 2 + 230)))

            # Hiển thị độ dài đường đi
            length_text = ButtonsFontInactive.render(f"Path Length: {path_length} steps", True, 'WHITE')
            screen.blit(length_text, length_text.get_rect(center=(WINDOW_DIM[0] / 2, WINDOW_DIM[1] / 2 + 270)))

            # Back to Main Menu
            if GameOver_Back.is_Clicked():
                Game.MazeGame = None
                Scores.GameDone = False
                Game.is_active = False
                Game.GameOverScreen = False
                Game.LevelScreen = True
                main_menu.is_active = True
                time.sleep(BackButtonDelay)

    # Scores
    if Scores.is_active:
        # Background Static
        main_menu.BackgroundDisplay(MainMenuBackground[0])

        Scores.DisplayHighScores()

        Scores_Back.display()

        if Scores_Back.is_Clicked():
            Scores.is_active = False
            time.sleep(BackButtonDelay)
            main_menu.is_active = True

    pygame.display.update()
