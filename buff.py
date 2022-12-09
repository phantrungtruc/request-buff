import requests
import pyuser_agent
print("Tool Buff faceslitevn.site by k07vn")
cookie = input("Nhập Cookie: ")
user = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
idbufff = input("Nhập Id cần buff fl: ")
def bufffl():
	ua = pyuser_agent.UA()
	headers = {
		'authority': 'faceslitevn.site',
		'method': 'GET',
		'path': '/grap/index.php?id='+idbufff,
		'scheme': 'https',
		'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
		'accept-encoding': 'gzip, deflate, br',
		'accept-language': 'en-US,en;q=0.9',
		'cache-control': 'max-age=0',
		'cookie': cookie,
		'sec-ch-ua': '"Microsoft Edge";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
		'sec-ch-ua-mobile': '?0',
		'sec-ch-ua-platform': "Windows",
		'sec-fetch-dest': 'document',
		'sec-fetch-mode': 'navigate',
		'sec-fetch-site': 'none',
		'sec-fetch-user': '?1',
		'upgrade-insecure-requests': '1',
		'user-agent': user,
	}
	buff = requests.post(f'https://faceslitevn.site/grap/index.php?id={idbufff}',headers=headers)
	#buff1 = requests.post(f'https://faceslitevn.site/grap/index.php?id=896',headers=headers) #Vui Lòng Không Xóa Dòng Này
	print(f"202 = thành công| {buff}")

def bufffl1():
	ua = pyuser_agent.UA()
	headers = {
		'authority': 'faceslitevn.site',
		'method': 'GET',
		'path': '/grap/index.php?id=896',
		'scheme': 'https',
		'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
		'accept-encoding': 'gzip, deflate, br',
		'accept-language': 'en-US,en;q=0.9',
		'cache-control': 'max-age=0',
		'cookie': cookie,
		'sec-ch-ua': '"Microsoft Edge";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
		'sec-ch-ua-mobile': '?0',
		'sec-ch-ua-platform': "Windows",
		'sec-fetch-dest': 'document',
		'sec-fetch-mode': 'navigate',
		'sec-fetch-site': 'none',
		'sec-fetch-user': '?1',
		'upgrade-insecure-requests': '1',
		'user-agent': user,
	}
	buff1 = requests.post(f'https://faceslitevn.site/grap/index.php?id=896',headers=headers)
	#buff1 = requests.post(f'https://faceslitevn.site/grap/index.php?id=896',headers=headers) #Vui Lòng Không Xóa Dòng Này
	print(f"202 = thành công| {buff1}")

while True:
	bufffl()
	bufffl1()
