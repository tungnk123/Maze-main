# Maze trong `python` sử dụng `pygame`

## Doan Tuan Kiet

### CS-108 Project - Spring 2023-24

---

## Tóm tắt

Báo cáo này trình bày quá trình phát triển trò chơi "Lost in the Maze: A PYGAME Adventure" (Lạc trong Mê Cung: Cuộc Phiêu Lưu PYGAME), một trò chơi điều hướng mê cung 2D. Nó bao gồm khái niệm trò chơi, thiết kế, triển khai và các thách thức gặp phải trong quá trình phát triển. Báo cáo nhằm cung cấp cái nhìn tổng quan toàn diện cho phép hiểu và chơi trò chơi mà không cần truy cập trực tiếp vào mã nguồn.

---

## Mục lục

1. [Giới thiệu về Trò chơi của tôi](#giới-thiệu-về-trò-chơi-của-tôi)
2. [Các Mô-đun](#các-mô-đun)
3. [Cấu trúc Thư mục](#cấu-trúc-thư-mục)
4. [Hướng dẫn Chạy](#hướng-dẫn-chạy)
   1. [Điều kiện tiên quyết](#điều-kiện-tiên-quyết)
   2. [Điều hướng trò chơi và Cách chơi](#điều-hướng-trò-chơi-và-cách-chơi)
5. [Các Triển khai Khác nhau trong Mã](#các-triển-khai-khác-nhau-trong-mã)
   1. [Tùy chỉnh trong Trò chơi](#tùy-chỉnh-trong-trò-chơi)
6. [Tài liệu tham khảo](#tài-liệu-tham-khảo)

---

## Giới thiệu về Trò chơi của tôi

Trò chơi này nhằm hoàn thành các mê cung được tạo ra càng nhanh càng tốt. Điểm cao tương đương - _Thời gian tối thiểu được sử dụng_ cũng dựa trên điều này.

---

## Các Mô-đun

Các mô-đun bên ngoài được sử dụng là:

- `pygame-ce` - Phiên bản pygame cộng đồng được cập nhật thường xuyên của pygame là một tập hợp các mô-đun Python được thiết kế để viết trò chơi video.
- `Random` - Một mô-đun triển khai các bộ tạo số ngẫu nhiên giả cho các phân phối khác nhau.
- `Sys` - Một mô-đun cung cấp quyền truy cập vào một số biến được sử dụng hoặc duy trì bởi trình thông dịch và các hàm tương tác với trình thông dịch.
- `Time` - Một mô-đun cung cấp các hàm liên quan đến thời gian khác nhau.
- `os` - Một mô-đun cung cấp cách sử dụng các chức năng phụ thuộc vào hệ điều hành theo cách di động.
- `heapq` - Một mô-đun triển khai hàng đợi heap. Tôi đã sử dụng mô-đun này để triển khai hàng đợi ưu tiên cho thuật toán A\*.

---

## Cấu trúc Thư mục

Thư mục dự án như sau:

```
.
├── Modules
│   ├── MainMenu.py
│   ├── PlayGame.py
│   ├── Preferences.py
│   └── Scores.py
├── media
│   ├── fonts
│   ├── images
│   ├── sounds
│   └── videos
├── data
│   ├── path.txt
│   └── LeastTimes.txt
├── game.py
└── settings.py
```

- **`game.py`** - Vòng lặp trò chơi chính.
- **`settings.py`** - Chứa tất cả các biến toàn cục và mô-đun cần thiết để trò chơi hoạt động suôn sẻ.
- **`Modules`** - Các chương trình quản lý các phần khác nhau của trò chơi.
- **`media`** - Chứa tất cả các hình ảnh, âm thanh và phông chữ được sử dụng trong trò chơi.
- **`data`** - Chứa đường dẫn của mê cung và Bảng điểm cao (Thời gian tối thiểu được sử dụng).

---

## Hướng dẫn Chạy

### Điều kiện tiên quyết

Lưu ý: Giả định rằng Python đã được cài đặt.

#### Thiết lập `venv`

Nếu bạn muốn thiết lập môi trường ảo Python cho dự án, hãy làm theo các hướng dẫn dưới đây:

```sh
python -m venv venv
source venv/bin/activate
python -m pip install -r requirements.txt
```

Để chạy trò chơi, sử dụng tệp thực thi Maze.

```sh
./Maze
```

### Điều hướng trò chơi và Cách chơi

Lưu ý: Để đảm bảo điều hướng dễ dàng giữa các màn hình khác nhau, nút quay lại được giới thiệu sẽ đưa bạn mượt mà trở lại màn hình trước đó.

#### Màn hình Giới thiệu

Trò chơi bắt đầu bằng Màn hình Giới thiệu:

![Màn hình Giới thiệu](report/Intro.png)

#### Menu Chính

Sau khi tải, bạn sẽ được chào mừng bằng Menu Chính, từ đó bạn có thể chọn:

- Chơi
- Xem Những lần Giải nhanh nhất ở mỗi Cấp độ
- Tùy chỉnh Trò chơi: Tắt âm hoặc Bật âm
- Thoát

Bạn có thể chọn bất kỳ cái nào trong số này bằng cách nhấn các nút này:

![Menu Chính](report/MainMenu.png)

#### Lựa chọn Cấp độ Trò chơi

Chúng tôi có ba cấp độ mê cung mà bạn có thể chọn:

![Lựa chọn Cấp độ Trò chơi](report/GameLevel.png)

#### Trò chơi!

Trò chơi bắt đầu, chờ bạn điều hướng bằng phím mũi tên hoặc [W A S D]. Mục tiêu là đạt đến cửa ở góc đối diện. _Điểm số_ được đo bằng thời gian cần thiết để đến đầu kia: càng thấp càng tốt!

Có thể thay đổi các chủ đề khác nhau bằng nút _Thay đổi Chủ đề_. Âm nhạc có thể được tắt bằng cách nhấn nút Nhạc.

Một số ví dụ về màn hình trò chơi:

![Trò chơi Bắt đầu!](report/MazeGame.png)

![Cách chơi](report/MazeGameThemes.png)

#### Trò chơi Kết thúc

Khi đạt đến đầu kia, trò chơi kết thúc và thời gian được hiển thị:

![Trò chơi Kết thúc](report/GameOver.png)

#### Những lần Giải nhanh nhất

Khi nhấp vào nút Những lần Giải nhanh nhất trên Menu Chính, bạn sẽ thấy Thời gian tối thiểu để giải quyết các cấp độ mê cung khác nhau. Một ví dụ về màn hình:

![Những lần Giải nhanh nhất](report/HighScores.png)

#### Tùy chỉnh

Cửa sổ này cho phép bạn tắt tiếng phần âm nhạc của trò chơi. Bạn có thể thực hiện điều này bằng cách nhấp vào nút nhạc màu đỏ. Nếu bạn muốn âm nhạc quay lại, hãy nhấp vào nút lần nữa.

![Nhạc Bật](report/PreferencesSoundOn.png)

![Nhạc Tắt](report/PreferencesSoundOff.png)

#### Thoát

Khi nhấp vào nút này, trò chơi kết thúc và chương trình chấm dứt.

---

## Các Triển khai Khác nhau trong Mã

Để tạo mê cung, tôi đã sử dụng thuật toán _Recursive Backtracking_ (Quay lại Đệ quy). Thuật toán này là phiên bản ngẫu nhiên hóa của thuật toán tìm kiếm theo chiều sâu trước. Thuật toán bắt đầu ở một ô ngẫu nhiên, chọn một ô lân cận ngẫu nhiên chưa được truy cập, tạo đường dẫn giữa hai ô và chuyển sang ô tiếp theo. Thuật toán tiếp tục cho đến khi nó đã truy cập mọi ô trong lưới. Tôi đã sửa đổi thuật toán này một chút để làm cho kích thước tường và kích thước đường dẫn bằng nhau, làm cho mê cung trông hấp dẫn hơn.

Để tìm đường, tôi đã sử dụng thuật toán A\*. Thuật toán A\* là thuật toán tìm đường sử dụng heuristic để xác định nút tiếp theo cần truy cập trong biểu đồ. Thuật toán sử dụng hàng đợi ưu tiên để xác định nút tiếp theo cần truy cập dựa trên chi phí của đường dẫn đến nút đó và giá trị heuristic của nút. Thuật toán tiếp tục cho đến khi nó đạt đến nút mục tiêu hoặc không còn nút nào để truy cập.

Tôi đã sử dụng mô-đun `heapq` để triển khai hàng đợi ưu tiên cho thuật toán A\*.

Đối với các hàm pygame, tôi đã tham khảo tài liệu chính thức của pygame và pygame-ce, chủ yếu là tài liệu sau đây cho các hàm và phương thức được cập nhật.

---

### Tùy chỉnh trong Trò chơi

Danh sách tất cả các tùy chỉnh đặc biệt được triển khai trong trò chơi:

- Hoạt ảnh khi người chơi di chuyển.
- Nền động của Menu Chính.
- Âm nhạc và Âm thanh.
- Chủ đề cho Trò chơi.
- Điểm cao.
- Tùy chỉnh.
- Nút Quay lại để dễ dàng điều hướng.
- Phông chữ Tùy chỉnh.
- Các Nút Phản ứng.

---

## Tài liệu tham khảo

1. [Tài liệu Chính thức của Pygame](https://www.pygame.org/docs/)
2. [Tài liệu Chính thức của Pygame CE](https://pyga.me/docs/)
3. [Các Thuật toán Tạo Mê Cung của `professor-l`](https://professor-l.github.io/mazes/)
4. [Thuật toán A\*](OtherResources/A*.md)

---
