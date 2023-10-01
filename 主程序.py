import pygetwindow as gw
import pyautogui
import time
import io
import cv2
import numpy as np
from PIL import Image
from 易ocr import ocr_image
from 提取元素并查找模块 import process_search_ocr

# 获取所有打开的窗口
'''windows = gw.getWindowsWithTitle("QQ")  # 根据窗口标题匹配

if len(windows) > 0:
    # 遍历所有匹配的窗口
    for qq_window in windows:
        # 在这里可以添加条件来进一步判断是否是你需要的 QQ 窗口
        if "QQ" in qq_window.title:
            time.sleep(1)
            qq_window.activate()  # 激活QQ窗口
            time.sleep(1)

    # 获取QQ窗口的位置和大小
    left, top, width, height = qq_window.left, qq_window.top, qq_window.width, qq_window.height

    # 计算相对坐标的起点和终点
    relative_start_x = 310
    relative_start_y = 65
    relative_end_x = 815
    relative_end_y = 502

    # 计算绝对坐标的起点和终点
    absolute_start_x = left + relative_start_x
    absolute_start_y = top + relative_start_y
    absolute_end_x = left + relative_end_x
    absolute_end_y = top + relative_end_y

    # 截取相对坐标区域的截图
    screenshot = pyautogui.screenshot(region=(
    absolute_start_x, absolute_start_y, relative_end_x - relative_start_x, relative_end_y - relative_start_y))'''
# 获取当前激活的窗口
active_window = gw.getActiveWindow()

# 获取当前激活窗口的位置和大小
left, top, width, height = active_window.left, active_window.top, active_window.width, active_window.height

# 计算相对坐标的起点和终点
relative_start_x = 310
relative_start_y = 65
relative_end_x = 815
relative_end_y = 502

# 计算绝对坐标的起点和终点
absolute_start_x = left + relative_start_x
absolute_start_y = top + relative_start_y
absolute_end_x = left + relative_end_x
absolute_end_y = top + relative_end_y

# 使用 pyautogui 截取当前窗口的截图
screenshot = pyautogui.screenshot(region=(absolute_start_x, absolute_start_y, absolute_end_x - absolute_start_x, absolute_end_y - absolute_start_y))

# 转换为PIL Image
pil_image = Image.frombytes('RGB', screenshot.size, screenshot.tobytes())

# 将图像转为灰度图
gray_image = pil_image.convert('L')

    # 二值化处理
threshold = 128  # 设置阈值
binary_image = gray_image.point(lambda p: p > threshold and 255)

image_buffer = io.BytesIO()
screenshot.save(image_buffer, format='PNG')
image_buffer.seek(0)  # 将文件指针移至开头

    # 将内存中的图像数据传递给ocr_image模块
wenzi = ocr_image(image_buffer.getvalue())  # 使用 getvalue() 获取图像数据
#print(wenzi)

    # 保存截图
#screenshot.save('1qq_screenshot.png')

    #wenzi=ocr_image(screenshot)
    #print(wenzi)
#else:
#    print("未找到QQ窗口")
wenzi_culi = process_search_ocr(wenzi)
print(wenzi_culi)
