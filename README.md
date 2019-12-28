![pythonista3 Logo](https://i.loli.net/2019/12/28/miu2vzNfGRqxodM.png)

# [Pythonista](http://omz-software.com/pythonista/index.html)

> Pythonista is a complete development environment for writing Python™ scripts on your iPad or iPhone. Lots of examples are included — from games and animations to plotting, image manipulation, custom user interfaces, and automation scripts.
>
> In addition to the powerful standard library, Pythonista provides extensive support for interacting with native iOS features, like contacts, reminders, photos, location data, and more.

---

# Pythonista 使用

## 使用之前

我们首先会考虑 Pythonista 是否支持第三方库。如果不支持，那可玩性实在是太低了。还好，Pythonista 支持一些纯 Python 写成的第三方库，例如 requests，BeautifulSoup 等库还是支持的。所以有玩家首先会想到利用 you-get 来下载各种资源。

但是如何安装第三方库呢？需要我们在终端使用 pip 命令来安装。所以 [StaSh-Shell](https://github.com/ywangd/stash) 应运而生。

我们需要新建一个 py 文件，可以命名为 `install_stash.py`，内容如下：

```python
import requests as r; exec(r.get('https://raw.githubusercontent.com/ywangd/stash/master/getstash.py').text)
```

![安装 StaSh](https://i.loli.net/2019/12/28/7d5uO3CKgDxQyFb.png)

执行完成后，退出重新进入应用，会发现多了一个名为 `launch_stash.py` 的文件。运行此文件就可以调出 shell 界面，使用 pip 安装 Python 的第三方库了。

## 安装第三方库

我们可以安装 tqdm 来测试是否可以安装第三方库。

[tqdm](https://github.com/tqdm/tqdm) 是一个快速，可扩展的Python进度条。操作简单，功能全面。

![](https://raw.githubusercontent.com/tqdm/tqdm/master/images/tqdm.gif)

因为在之后的脚本中会使用到 tqdm 来显示下载进度，所以用此库测试。

运行 `launch_stash.py`，在终端输入 `pip install tqdm` 来安装。

执行结果如下表示安装成功：

![安装 tqdm](https://i.loli.net/2019/12/28/YLnsbOPdNcFZr9u.png)

# 脚本

**仓库内脚本仅限学习交流使用。如果不听我的我也拿你没什么办法～**
