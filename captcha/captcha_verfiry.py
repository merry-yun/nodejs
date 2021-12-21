import muggle_ocr
import requests
import json
import base64
import sys

def img2text(img_byte):
    byte = base64.b64decode(img_byte)
    sdk = muggle_ocr.SDK(model_type=muggle_ocr.ModelType.Captcha)
    text = sdk.predict(image_bytes=byte)
    return text

if __name__ == "__main__":
    img = sys.argv[1]
    # print(img)
    result_str = img2text(img)
    print(result_str)