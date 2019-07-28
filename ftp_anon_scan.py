import ftplib
import optparse

def returnDefault(ftp):
	try:
		dirList = ftp.nlst()
	except:
		dirList = []
		print('[-] Could not List any sites')
		return
	retList = []
	for filename in dirList:
		fn = filename.lower()
		if '.php' in fn or '.htm' in fn or '.asp' in fn:
			print("[+] Default page found: "+fn)
			retList.append(fn)
	return retList

def anonLogin(hostname):
	try:
		ftp = ftplib.FTP(hostname)
		ftp.login('anonymous','me@me.com')
		print('[+] Login scceeded')
		returnDefault(ftp)
	except Exception as e:
		print('\n[-] login '+hostname+' failed')
		return False


def main():
	parser = optparse.OptionParser('usage%prog'+' -H host')
	parser.add_option('-H', dest='hostname', type='string', help='Specify the target host')
	(options,args) = parser.parse_args()
	
	hostname = options.hostname

	if hostname == None:
		print(parser.usage)
		exit(0)
	anonLogin(hostname)
if __name__ == '__main__':
	main()