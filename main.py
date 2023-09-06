import time
import pyautogui

# Đường dẫn đến tệp văn bản chứa các nội dung bài đăng
file_path = "C:/Users/MSI GAMING/PycharmProjects/AutoTest1/Abc.txt"

# Đọc nội dung từ tệp văn bản và lưu vào danh sách
list_of_posts = []
with open(file_path, "r", encoding="utf-8") as file:
    for line in file:
        list_of_posts.append(line.strip())  # Xóa dấu xuống dòng và thêm vào danh sách

# Đợi một khoảng thời gian để chuyển sang trình duyệt và mở giao diện tạo bài đăng trên Facebook
time.sleep(5)
pyautogui.click(1235, 1045)
time.sleep(3)
pyautogui.write('facebook.com', interval=0.25)
pyautogui.press('enter')
time.sleep(7)
# Lặp qua danh sách và tạo bài đăng
for post_content in list_of_posts:
    # Tìm ô tạo bài đăng và nhấn chuột vào đó (cần điều chỉnh tọa độ cho phù hợp)
    pyautogui.click(833, 562)

    # Đợi một chút để đảm bảo giao diện đã mở
    time.sleep(5)

    # Gõ nội dung bài đăng
    pyautogui.write("mon tuong tac nguoi may: " + post_content)

    # Đợi một chút trước khi đăng bài (tùy chỉnh theo yêu cầu)
    time.sleep(2)
    pyautogui.click(1076, 694)
    time.sleep(3)
    pyautogui.write('Truong Dai hoc Quang Binh', interval=0.25)
    time.sleep(3)
    pyautogui.click(874, 432)
    # Ấn nút đăng bài (cần điều chỉnh tọa độ cho phù hợp)
    pyautogui.click(910, 832)

    # Đợi sau khi đăng bài để chuyển sang bài đăng tiếp theo (tùy chỉnh theo yêu cầu)
    time.sleep(5)

# Kết thúc chương trình
print("Hoàn thành tạo bài đăng trên Facebook từ tệp văn bản.")