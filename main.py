#! /usr/bin/env python3

from module import Scrapper
import argparse
import sys

Bl='\033[30m' # VARIABLE COLOR 
Re='\033[1;31m'
Gr='\033[1;32m'
Ye='\033[1;33m'
Blu='\033[1;34m'
Mage='\033[1;35m'
Cy='\033[1;36m'
Wh='\033[1;37m'
Grey='\033[1;30;40m'

def arg_parse():
	parser = argparse.ArgumentParser(exit_on_error=False)
	parser.add_argument("-u", help="Profile Username", required=True, nargs=1)
	parser.add_argument("-d", help="Downloads the user profile picture", required=False, action='store_true')
	try:
		return parser.parse_args()
	except argparse.ArgumentError:
		is_u = 0
		is_d = 0
		for i in sys.argv:
			if "-u" in i:
				is_u == 1
			if "-d" in i:
				is_d == 1
		if (is_u == 0):
			user_input = input(f"\n{Wh}[{Blu}+{Wh}] Masukan username tiktok : {Cy}")
			args_list = ['-u',user_input]	
		if (is_d == 0):
			download_input = input(f"{Wh}[{Blu}+{Wh}] Download foto profile nya? (y/n) : {Cy}")
			if download_input in ("Y","y"):
				args_list.append('-d')	
		print(" ")
		return parser.parse_args(args_list)
	
def main():

	print(f" ") 
	print(f"{Blu}TikTok {Cy}OSINT")
	print(f" ") 
	print(f"{Grey}[+] Powered By HanX")
	print(f"{Grey}[+] Version : 1.0")
	print(f"{Grey}[+] Github : https://github.com/hanx-666")
	print(f" ")
	print(f"{Grey}Gunakan : python main.py -u <username>")

	args = arg_parse()
	
	try:
		tiktok = Scrapper(args.u[0])
		if args.d == True:
			tiktok.download_profile_picture()

		print(" ")
		print(f"{Ye}Done Sensei...{Wh}")

	except Exception as error:
		print(" ")
		print(f"{Re}An error occured : {Wh}", type(error).__name__, " – ", error)
		print(f"{Wh}Please try again later.")

if __name__ == "__main__":
	main()
