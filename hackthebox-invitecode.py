# coding: utf-8

import requests

import base64

print('''
    
     
    __  __ ___    ______ __ __ ______ __  __ ______ ____   ____  _  __
   / / / //   |  / ____// //_//_  __// / / // ____// __ ) / __ \| |/ /
  / /_/ // /| | / /    / ,<    / /  / /_/ // __/  / __  |/ / / /|   / 
 / __  // ___ |/ /___ / /| |  / /  / __  // /___ / /_/ // /_/ //   |  
/_/ /_//_/  |_|\____//_/ |_| /_/  /_/ /_//_____//_____/ \____//_/|_|  
                                                                                                                                   
[+] TOOL GENERATED BY MONISH KUMAR  [+]    
''')

API_LINK ="https://www.hackthebox.eu/api/invite/generate"

r=requests.post(url=API_LINK)

response_txt=r.text

print("<---------------------------------------------------------------------------->")


print("\n{+}YOUR RESPONSE GENERATED IS :  {+} \n \n"+response_txt)

print("\n<------------------------------------------------------------------------>")

base64txt=response_txt[29:69]

print("\n{+}YOUR INVITE CODE IN Base64 IS : "+base64txt+" {+}")

code=base64.b64decode(base64txt)

codef=str(code)

invite_code=codef[0:29]

print("\n<------------------------------------------------------------------------>")


print("\n{+}YOUR HACKTHEBOX INVITE-CODE IS : " + invite_code +" {+}")

print("\n<------------------------------------------------------------------------>")
