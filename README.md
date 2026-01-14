# Maze Game - Python với Pygame

## Cấu trúc dự án

```
Maze-main/
│
├── game.py                 # FILE CHÍNH - Vòng lặp game
├── settings.py             # Cấu hình toàn cục, import modules
├── requirements.txt        # Dependencies: pygame
│
├── Modules/                # CÁC MODULE CHỨC NĂNG
│   ├── __init__.py         # Đánh dấu là Python package
│   ├── MainMenu.py         # Menu chính và nút bấm
│   ├── PlayGame.py         # Logic game, thuật toán mê cung
│   ├── Preferences.py      # Cài đặt âm thanh
│   └── Scores.py           # Quản lý điểm cao
│
├── data/                   # DỮ LIỆU GAME
│   ├── LeastTimes.txt      # Thời gian nhanh nhất (3 level)
│   └── path.txt            # Đường đi giải mê cung
│
└── media/                  # TÀI NGUYÊN
    ├── fonts/              # Font chữ (.ttf)
    ├── images/             # Hình ảnh (buttons, player, maze)
    ├── sounds/             # Âm thanh (.wav)
    └── videos/             # 600 frames background menu
```

---

## Cách chạy game

```bash
# Cài đặt pygame
pip3 install pygame

# Chạy game
python3 game.py
```

---

## Giải thích từng file

### 1. `game.py` - Vòng lặp chính

File này chứa **game loop** - vòng lặp chạy liên tục để:
- Xử lý sự kiện (nhấn phím, click chuột, thoát)
- Cập nhật trạng thái game
- Vẽ giao diện lên màn hình

```python
while True:
    # 1. Lấy sự kiện
    PygameEvents = pygame.event.get()
    keys = pygame.key.get_pressed()

    # 2. Xử lý thoát game
    for event in PygameEvents:
        if event.type == pygame.QUIT:
            Quit()

    # 3. Hiển thị màn hình phù hợp
    if main_menu.is_active:
        # Hiển thị menu chính
    if Game.is_active:
        # Chơi game
    if Scores.is_active:
        # Hiển thị điểm cao

    # 4. Cập nhật màn hình
    pygame.display.update()
```

**Các màn hình trong game:**
1. **Intro Screen** - Màn hình loading 3 giây
2. **Main Menu** - Menu chính (Play, Scores, Preferences, Quit)
3. **Level Selection** - Chọn độ khó (Easy, Medium, Hard)
4. **Game Screen** - Màn chơi mê cung
5. **Game Over** - Kết thúc, hiển thị thời gian

---

### 2. `settings.py` - Cấu hình toàn cục

File này:
- Import tất cả modules cần thiết
- Khởi tạo pygame
- Định nghĩa các biến toàn cục (kích thước cửa sổ, vị trí nút, ...)
- Tạo các đối tượng game (buttons, menu, player, ...)

```python
# Khởi tạo pygame
pygame.init()
pygame.mixer.init()

# Kích thước cửa sổ
WINDOW_DIM = (1440, 810)

# Tạo màn hình
screen = pygame.display.set_mode(WINDOW_DIM)

# Load hình ảnh
def LoadScaledImage(image_path, scaling_factor=1.0, scaling_dim=(0, 0)):
    image = pygame.image.load(image_path)
    # Scale hình ảnh theo tỷ lệ hoặc kích thước
    ...
    return resized_image

# Tạo các nút menu
MM_Play = MainMenu.MainMenuButton(screen, "PLAY", ...)
MM_Scores = MainMenu.MainMenuButton(screen, "FASTEST SOLVES", ...)
MM_Preferences = MainMenu.MainMenuButton(screen, "PREFERENCES", ...)
MM_Quit = MainMenu.MainMenuButton(screen, "QUIT", ...)

# Tạo đối tượng game
Game = PlayGame.GamePlay(screen, PlayerName, ...)
```

---

### 3. `Modules/MainMenu.py` - Menu và Nút bấm

**Class `MainMenuButton`** - Tạo nút bấm tương tác:

```python
class MainMenuButton:
    def __init__(self, screen, ButtonTitle, FontInactive, FontActive, Image, Pos, Sound):
        self.screen = screen
        self.ButtonRect = pygame.Rect(...)  # Vùng click được

    def display(self):
        # Vẽ nút lên màn hình
        # Đổi font khi hover (di chuột vào)
        if self.ButtonRect.collidepoint(pygame.mouse.get_pos()):
            # Hiển thị font Active (to hơn)
        else:
            # Hiển thị font Inactive

    def is_Clicked(self):
        # Kiểm tra nút được click chưa
        if self.ButtonRect.collidepoint(mouse_pos) and mouse_pressed:
            self.ButtonSound.play()
            return True
```

**Class `MainMenu`** - Quản lý menu chính:

```python
class MainMenu:
    def __init__(self, screen, Buttons):
        self.is_active = False           # Menu đang hiển thị?
        self.BackgroundFrameIndex = 0    # Frame background hiện tại

    def BackgroundDisplay(self, BackgroundFrame):
        # Vẽ background động (600 frames)
        self.screen.blit(BackgroundFrame, (0, 0))

    def Buttons(self):
        # Vẽ tất cả nút
        for Button in self.buttons:
            Button.display()
```

---

### 4. `Modules/PlayGame.py` - Logic game chính

#### Class `Maze` - Tạo và giải mê cung

**Thuật toán tạo mê cung: Recursive Backtracking (DFS)**

```python
class Maze:
    def __init__(self, Width, Height):
        # Tạo lưới toàn tường (1 = tường)
        self.maze = [[1 for _ in range(Width)] for _ in range(Height)]
        self.generate_maze()

    def carve_maze(self, x, y, maze):
        """Đào đường đi bằng DFS đệ quy"""
        # 4 hướng: lên, xuống, trái, phải
        ValidDirections = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        random.shuffle(ValidDirections)  # Xáo trộn để tạo ngẫu nhiên

        for dx, dy in ValidDirections:
            nx, ny = x + dx * 2, y + dy * 2  # Nhảy 2 ô
            if trong_phạm_vi and maze[ny][nx] == 1:  # Chưa đào
                maze[ny][nx] = 0      # Đào ô đích
                maze[ny-dy][nx-dx] = 0  # Đào ô giữa
                self.carve_maze(nx, ny, maze)  # Đệ quy tiếp
```

**Thuật toán tìm đường: A\* (A-Star)**

```python
def heuristic(x, y):
    """Khoảng cách Manhattan đến đích (1,1)"""
    return abs(x - 1) + abs(y - 1)

def solve_maze_a_star(self):
    """Tìm đường ngắn nhất bằng A*"""
    start = (width - 1, height - 1)  # Góc dưới phải
    goal = (1, 1)                     # Góc trên trái

    # Priority queue: (f_score, position)
    # f_score = g_score + heuristic
    frontier = [(heuristic(*start), start)]
    came_from = {start: None}
    cost_so_far = {start: 0}

    while frontier:
        current = heapq.heappop(frontier)[1]  # Lấy ô có f nhỏ nhất

        if current == goal:
            break

        for dx, dy in [(0,-1), (1,0), (0,1), (-1,0)]:
            next_pos = (current[0]+dx, current[1]+dy)

            if là_đường_đi_hợp_lệ:
                new_cost = cost_so_far[current] + 1

                if next_pos chưa_thăm or new_cost < cost_so_far[next_pos]:
                    cost_so_far[next_pos] = new_cost
                    priority = new_cost + heuristic(*next_pos)
                    heapq.heappush(frontier, (priority, next_pos))
                    came_from[next_pos] = current

    # Truy vết đường đi
    path = ""
    current = goal
    while current != start:
        prev = came_from[current]
        # Xác định hướng di chuyển (U/D/L/R)
        ...
        current = prev
    return path  # VD: "UULLDDRRUU..."
```

#### Class `Player` - Nhân vật

```python
class Player:
    def __init__(self, screen, image_path):
        # Load 16 frames animation (4 hướng x 4 frames)
        self.image = {
            'up': [load frame 13-16],
            'down': [load frame 1-4],
            'left': [load frame 5-8],
            'right': [load frame 9-12]
        }
        self.direction = 'down'

    def animate(self, keys, TimePassed, PlayerWidth, center):
        # Xác định hướng từ phím nhấn
        if keys[K_UP] or keys[K_w]:
            self.direction = 'up'
        # ...

        # Vẽ frame animation dựa trên thời gian
        frame_index = int((TimePassed % 400) / 100)  # 0-3
        self.screen.blit(self.image[direction][frame_index], ...)
```

#### Class `GamePlay` - Điều khiển game

```python
class GamePlay:
    def __init__(self, screen, ...):
        self.Player = Player(screen, PlayerImagesPath)
        self.MazeGame = None
        self.PlayerCellCoordinates = (1, 1)  # Vị trí player
        self.BackgroundType = 0              # Theme hiện tại (0-4)

    def SetMazeLevel(self):
        """Tạo mê cung theo level"""
        if self.Level == 1:
            self.MazeGame = Maze(20, 20)   # Easy
        elif self.Level == 2:
            self.MazeGame = Maze(30, 30)   # Medium
        elif self.Level == 3:
            self.MazeGame = Maze(40, 40)   # Hard

        # Lưu đường đi giải vào file
        with open(self.pathAddress, 'w') as file:
            file.write(self.MazeGame.solve_maze_a_star())

    def GamePlay(self, keys, TimePassed):
        """Vòng lặp chính khi chơi"""
        self.DisplayMazeBackground()  # Vẽ mê cung
        self.Player.animate(...)       # Vẽ player
        self.PlayerCellCoordinatesMover(keys)  # Di chuyển
        self.GameOver()                # Kiểm tra thắng

    def PlayerCellCoordinatesMover(self, keys):
        """Di chuyển player theo phím"""
        if keys[K_UP]:
            new_pos = (x, y - 1)
        # ...

        # Chỉ di chuyển nếu ô mới là đường đi (0)
        if self.MazeGame.maze[new_y][new_x] == 0:
            self.PlayerCellCoordinates = new_pos

    def GameOver(self):
        """Kiểm tra đã đến đích chưa"""
        if self.PlayerCellCoordinates == (1, 1):
            self.GameOverScreen = True
```

---

### 5. `Modules/Scores.py` - Quản lý điểm cao

```python
class HighScores:
    def __init__(self, screen, FileAddress, Font):
        self.File = FileAddress  # data/LeastTimes.txt

    def HighScoreUpdate(self, NewScore, Level):
        """Cập nhật điểm cao nếu tốt hơn"""
        with open(self.File, 'r') as f:
            scores = f.readlines()  # ["100\n", "200\n", "300\n"]

        current_score = int(scores[Level - 1])
        if NewScore < current_score:
            scores[Level - 1] = str(int(NewScore)) + '\n'
            with open(self.File, 'w') as f:
                f.writelines(scores)
            return True
        return False

    def DisplayHighScores(self):
        """Hiển thị bảng điểm cao"""
        LEVEL = ["EASY : ", "MEDIUM : ", "HARD : "]
        for i, score in enumerate(scores):
            text = self.Font.render(LEVEL[i] + score + " SEC", ...)
            self.screen.blit(text, ...)
```

---

### 6. `Modules/Preferences.py` - Cài đặt

```python
class Preferences:
    def __init__(self, screen):
        self.is_active = False
        self.MusicState = True  # Bật/tắt nhạc
```

---

## Sơ đồ luồng hoạt động

```
                    ┌─────────────┐
                    │   game.py   │
                    │ (Game Loop) │
                    └──────┬──────┘
                           │
                    ┌──────▼──────┐
                    │ settings.py │
                    │ (Import &   │
                    │  Initialize)│
                    └──────┬──────┘
                           │
        ┌──────────────────┼──────────────────┐
        │                  │                  │
┌───────▼───────┐  ┌───────▼───────┐  ┌───────▼───────┐
│ MainMenu.py   │  │ PlayGame.py   │  │  Scores.py    │
│ - Buttons     │  │ - Maze class  │  │ - HighScores  │
│ - Menu        │  │ - Player      │  │ - Read/Write  │
└───────────────┘  │ - GamePlay    │  └───────────────┘
                   └───────────────┘
```

---

## Điều khiển

| Phím | Chức năng |
|------|-----------|
| `W` / `↑` | Di chuyển lên |
| `S` / `↓` | Di chuyển xuống |
| `A` / `←` | Di chuyển trái |
| `D` / `→` | Di chuyển phải |

---

## Thuật toán chính

### 1. Recursive Backtracking (Tạo mê cung)
- Dựa trên DFS (Depth-First Search)
- Bắt đầu từ ô (1,1), đào ngẫu nhiên theo 4 hướng
- Backtrack khi không còn đường đi

### 2. A* (Tìm đường)
- Thuật toán tìm đường ngắn nhất
- Sử dụng heuristic: khoảng cách Manhattan
- Priority queue (heapq) để chọn ô tốt nhất
- f(n) = g(n) + h(n)
  - g(n): chi phí từ start đến n
  - h(n): ước lượng từ n đến goal
