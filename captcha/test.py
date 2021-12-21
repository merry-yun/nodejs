
import base64
import requests
import time

if __name__ == "__main__":
    url = "http://localhost:8081/api/v1/captche"
    img_path = r"getVerify.jpg"
    with open(img_path, 'rb') as f:
        img_byte = base64.b64encode(f.read())
    data = {
        "img_byte": img_byte,
        "type": 1
    }
    start_time = time.time()
    print("start_data", start_time)
    for _ in range(5):
        response = requests.post(url, data=data)
        print(response.text)
        print("use_time", time.time() - start_time)