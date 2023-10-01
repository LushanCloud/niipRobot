import easyocr
from PIL import Image
#reader = easyocr.Reader(['ch_sim','en'],gpu=False) # this needs to run only once to load the model into memory
#result = reader.readtext('1qq_screenshot.png',detail = 0)
#print(result)

def ocr_image(image_data):
    try:
        # 初始化 OCR 阅读器，加载模型
        reader = easyocr.Reader(['ch_sim', 'en'], gpu=False)

        # 使用 OCR 阅读器识别图片中的文字
        text = reader.readtext(image_data, detail=0)

        return text
    except Exception as e:
        return str(e)

# 调用函数进行文字识别
#image_path = '1qq_screenshot.png'
#text = ocr_screenshot(image_path)
#print(text)