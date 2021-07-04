import json
import os
from urllib.request import Request, urlopen
import threading
import colorama
from colorama import Fore
from queueclass import Queue


colorama.init()


def pad_to_center(l: list, w: int) -> str:
    return '\n'.join([' ' * (w // 2 - (len(max(l, key=len)) // 2)) + x for x in l])


def print_discord():
    text = f'''{Fore.CYAN}
          .///////.           ////////
       ///////////////////////////////////
      //////////////////////////////////////*
    /////////////////////////////////////////
   ///////////////////////////////////////////
  /////////////////////////////////////////////
 ////////////      //////////,     ,///////////,
 ///////////        .///////         ///////////
////////////        ,///////         ///////////.
/////////////*     ///////////     //////////////
/////////////////////////////////////////////////
/////////////////////////////////////////////////
 ,///////////    ///////////////    ///////////
   .////////.                       /////////{Fore.WHITE}'''

    width = os.get_terminal_size().columns
    print(pad_to_center(text.splitlines(), width))


def print_title():
    text = f'''{Fore.CYAN}
░█████╗░██████╗░░█████╗░███╗░░░███╗██╗░██████╗  ████████╗░█████╗░██╗░░██╗███████╗███╗░░██╗
██╔══██╗██╔══██╗██╔══██╗████╗░████║╚█║██╔════╝  ╚══██╔══╝██╔══██╗██║░██╔╝██╔════╝████╗░██║
███████║██║░░██║███████║██╔████╔██║░╚╝╚█████╗░  ░░░██║░░░██║░░██║█████═╝░█████╗░░██╔██╗██║
██╔══██║██║░░██║██╔══██║██║╚██╔╝██║░░░░╚═══██╗  ░░░██║░░░██║░░██║██╔═██╗░██╔══╝░░██║╚████║
██║░░██║██████╔╝██║░░██║██║░╚═╝░██║░░░██████╔╝  ░░░██║░░░╚█████╔╝██║░╚██╗███████╗██║░╚███║
╚═╝░░╚═╝╚═════╝░╚═╝░░╚═╝╚═╝░░░░░╚═╝░░░╚═════╝░  ░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝╚══════╝╚═╝░░╚══╝

░█████╗░██╗░░██╗███████╗░█████╗░██╗░░██╗███████╗██████╗░
██╔══██╗██║░░██║██╔════╝██╔══██╗██║░██╔╝██╔════╝██╔══██╗
██║░░╚═╝███████║█████╗░░██║░░╚═╝█████═╝░█████╗░░██████╔╝
██║░░██╗██╔══██║██╔══╝░░██║░░██╗██╔═██╗░██╔══╝░░██╔══██╗
╚█████╔╝██║░░██║███████╗╚█████╔╝██║░╚██╗███████╗██║░░██║
░╚════╝░╚═╝░░╚═╝╚══════╝░╚════╝░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝
{Fore.WHITE}'''.replace('░', ' ')

    width = os.get_terminal_size().columns
    print(pad_to_center(text.splitlines(), width))


print_discord()
print_title()


def get_headers(token):
    headers = {
        'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36 OPR/75.0.3969.285',
        'Authorization': token
    }
    return headers


def getuserdata(token):
    try:
        return json.loads(
            urlopen(Request("https://discordapp.com/api/v8/users/@me", headers=get_headers(token))).read().decode())
    except:
        pass


def check_token():
    global working_tokens

    while not queue.empty():
        token = queue.get()
        if len(token) > 10:
            response = getuserdata(token)
            if response is not None:
                print(f'[{Fore.GREEN}Found Valid Token{Fore.WHITE}] - [{Fore.GREEN}{token}{Fore.WHITE}] - [{Fore.GREEN}{response["username"]}#{response["discriminator"]}{Fore.WHITE}]')
                working_tokens.append(token)
            else:
                print(f'[{Fore.RED}Found Invalid Token{Fore.WHITE}] - [{Fore.RED}{token}{Fore.WHITE}]')


lines = []
print(f'{Fore.CYAN}┍━━ Please enter your tokens.')
while True:
    line = input('┃  ')
    if line:
        lines.append(line)
    else:
        break
text = '\n'.join(lines)
print(Fore.WHITE)

working_tokens = []
threading_list = []
queue = Queue(queue=text.split('\n'))

for i in range(500):
    checkThread = threading.Thread(target=check_token)
    threading_list.append(checkThread)

for thread in threading_list:
    thread.start()

for thread in threading_list:
    thread.join()

print(f'\n{Fore.CYAN}Done Checking Tokens.{Fore.WHITE}\n')
for token in working_tokens:
    with open('tokens.txt', 'a') as f:
        f.write(token + '\n')

    print(f'[{Fore.GREEN}{token}{Fore.WHITE}] - [{Fore.GREEN}{getuserdata(token)}{Fore.WHITE}]')

input()
