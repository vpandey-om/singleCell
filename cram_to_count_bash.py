import glob
import os 
import subprocess
import sys

from paramiko import SSHClient
from scp import SCPClient




def main_script():
	''' This script is written to download cram files form obilab server and do analysis to get count matarix '''
	print ("start coppy")
	source=
	destination=
	apply_scp("source", "destination")
	


def apply_scp(source, destination):
	''' we can use scp to copy from the remote server to the working directory '''
	## source is the folder with path: we wnat to copy from
	## destination is the folder with path: where we want to send the files  
	ssh = SSHClient()
	ssh.load_system_host_keys()
	#import pdb;pdb.set_trace()
	ssh.connect("rackham.uppmax.uu.se",username="vpandey",password="helloSoni0507")

	# SCPCLient takes a paramiko transport as an argument
	scp = SCPClient(ssh.get_transport(),progress4=progress4)
	
	##
	# Uploading the 'test' directory with its content in the
	# '/home/user/dump' remote directory
	scp.put(source, recursive=True, remote_path=destination)

	scp.close()



def progress4(filename, size, sent, peername):
	sys.stdout.write("(%s:%s) %s\'s progress: %.2f%%   \r" % (peername[0], peername[1], filename, float(sent)/float(size)*100) )



if __name__=="__main__":
	main_script()
