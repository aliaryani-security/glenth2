# GLENTH2
```
🎈 This project was originally <a href="https://github.com/theHannibalist/glenth>`glenth`</a> , but due to unclear and unimprovable coding that I made there , I decided to rewrite it entirely.
```
<br><br>
💎 `glenth2` comes with lots of improvements and new features :<br>
## Introducing `glenth2` and it's features 🧩
❓ Have you ever wondered "how long will it take to watch all these videos ?!"<br>
✅ The amazing `glenth2` is here to answer this question for you ! <br>
<br>
💎 New features that `glenth2` has brought to you : <br>
* using pure python code : the previous version was 80% shell script and 20% python code , but things are different now 😈
* using `subprocess` instead of `os` : old fashion ways are working no more 😄
* subdirectory search : not only you can scan one folder for videos , but also you can scan all subdirectories as well 📂
* verbose mode : by using this option , you can see the length of every single file as well 👁
* new theme : previous version had color problems with some shells , this new one has not. it uses simple colors that work everywhere 🎨
* custom file types : in this new version , you can choose any video types you want , and `glenth2` will scan for those only 🔍
<br>
## Usage 👨‍💻
By default , `glenth2` scans for all video files in the current directory. <br>
```sh
glenth2 [ options ]

-h    --help        shows the help message.
-V    --version     shows the version and exits. ( all other options will be ignored )
-v    --verbose     enables verbose mode. will show the length of every single video as well.
-s    --sub-directories   will scan subdirectories as well.
-d    --target-directory <directory>    choose a directory to scan
-t    --types        choose custom file types to scan for
```
<br>
## Installation and requirements ⚙
🎈 it's a python script , use can simply run it using `./main.py`<br>
💎 if you want to install it system-wide , use the following :
```sh
ln -s /path/to/glenth2/main.py /usr/bin/glenth2
```
<br><br>
🪐 before using this beauty, make sure you have `ffmpeg` installed 😉
## a few words ✍
I will be happy if you follow me on <a href="https://instagram.com/aliaryani.security"my instagram></a> ♥