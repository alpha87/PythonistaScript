# ------------------------------- #
#  FILE_NAME: "installScript.py"  #
#  VERSION: "v1.0"                #
#  Desc: Python Script Installer  #
# ------------------------------- #

import re
import requests


file_url = input("请输入需要安装的脚本链接：")
response = requests.get(file_url).text
file_name = re.findall(r'FILE_NAME: "(.*?)"', response)[0]

with open(file_name, "w", encoding="utf-8") as f:
    f.write(response)
print("安装完成！")
