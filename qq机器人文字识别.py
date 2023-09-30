from PIL import Image
import pytesseract
def ocr_image(image_path, lang='chi_sim'):
    try:
        # 打开要识别的图片
        image = Image.open(image_path)

        # 使用pytesseract进行文字识别
        text = pytesseract.image_to_string(image, lang=lang)

        return text
    except Exception as e:
        return "error"


