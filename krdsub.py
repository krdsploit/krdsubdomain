import requests
from colorama import init, Fore, Back, Style


art = '''





╭┳╮╱╱╭┳━╮╱╱╱╱╱╭┳╮╱╭━╮╱╭╮
┃╭╋┳┳╯┃━╋━┳╮╭━╋┫╰╮┃━╋┳┫╰╮
┃╰┫╭┫╋┣━┃╋┃╰┫╋┃┃╭┫┣━┃┃┃╋┃
╰┻┻╯╰━┻━┫╭┻━┻━┻┻━╯╰━┻━┻━╯
╱╱╱╱╱╱╱╱╰╯

Code by : krdsploit

github : krdsploit

                                                                                '''


print(art)


dom_target = input("[+] Enter The Web Url : ")

file = open("subdomain.txt")

content = file.read()

subdomains = content.splitlines()


discovered_subdomains = [] 

for subdomain in subdomains:
	url = f"http://{subdomain}.{dom_target}"

	try:
		requests.get(url)

	except requests.ConnectionError:
		pass
	else:
		print("[+] Disocovered Subdomain : ", url)


		discovered_subdomains.append(url)


with open("disc_sub.txt","w") as f:
	for subdomain in discovered_subdomains:
		print(subdomain, file=f)

pri

