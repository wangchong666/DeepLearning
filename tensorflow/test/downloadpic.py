import requests
import time
# 下载图片
def dowloadPic(imageUrl):
    r = requests.get(imageUrl,verify=False)
    with open("12306\\"+str(time.time())+".jpg", "wb") as code:
        code.write(r.content)
for _ in range(1000):
    dowloadPic("https://kyfw.12306.cn/passport/captcha/captcha-image?login_site=E&module=login&rand=sjrand&0.49646291468568404");