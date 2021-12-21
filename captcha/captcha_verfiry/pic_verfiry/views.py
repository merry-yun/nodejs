from django.shortcuts import render

# Create your views here.

import muggle_ocr
import base64
import json
from django.http import JsonResponse, HttpResponse, HttpRequest
from django.views.decorators.http import require_http_methods

def img2text(img_byte):
    byte = base64.b64decode(img_byte)
    sdk = muggle_ocr.SDK(model_type=muggle_ocr.ModelType.Captcha)
    text = sdk.predict(image_bytes=byte)
    data = {
        "img_str": text,
        "msg": "succeed"
    }
    return data

@require_http_methods(['POST'])
def pic_verfiry(request: HttpRequest):
    img_type = int(request.POST.get('type'))
    if img_type == 1:
        img_byte = request.POST.get('img_byte')
        data = img2text(img_byte)
    elif img_type == 2:
        data = {
            "msg": "padding run"
        }
    else:
        data = {
            "msg": "the type is error"
        }
    result = {
        "code": HttpResponse.status_code,
        "data": data
    }
    return HttpResponse(json.dumps(result))

def index(request: HttpRequest):
    return '<h1> Wellconme To Django </h1> '