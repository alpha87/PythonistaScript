# --------------------------- #
#  FILE_NAME: "xvideosDL.py"  #
#  VERSION: "v1.0"            #
#  Desc: xvideos Downloader   #
# --------------------------- #

import re
import requests
from tqdm import tqdm


print("警告：未成年人请在成人陪同下使用!")
url = input("请输入 xvideos 视频链接：")
headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36"}
print("正在请求资源...")
html = requests.get(url, headers=headers).text
title = re.findall(r"html5player\.setVideoTitle\('(.*?)'\);", html)[0]
video_url = re.findall(r"html5player\.setVideoUrlHigh\('(.*?)'\);", html)[0]

print(f"标题：{title}\n")
r = requests.get(video_url, stream=True)
pbar = tqdm(total=int(r.headers["Content-Length"]))
chunk_size = 1024
with open(f"{title}.mp4", "wb") as v:
    for chunk in r.iter_content(chunk_size=chunk_size):
        if chunk:
            v.write(chunk)
            pbar.update(chunk_size)
pbar.close()
print("下载完成！")
