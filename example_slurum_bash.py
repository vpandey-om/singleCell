import glob
import os
import sys
import subprocess


def barseq_slurm(folder_with_path=None,project_id=None):
	# folder conatin the list of  fasta files
	# folder_with_path : location of the folder 
	# We want to compute barcodes for each fasta filess
	if folder_with_path==None:
		print("# folder_with_path (e.g.  /home/vikash/sampless)")
		return

	if project_id==None:
		print("We need to have project id for running slurm on cluster. For example \
			  snic2017-1-234")
		return


	# cd /proj/snic2019-8-97/barseq_sample/barSeq
	# python3 barseq.py -i data/sequence -b data/sample_small2.csv -r exp2
	os.chdir(folder_with_path)
	lfiles=glob.glob("*.fastq") # this is the list of fasta files

	for k,f in enumerate(lfiles):


		folder=f.replace('.fastq','')+"Folder"
		out=open("bash_"+folder+".sh","w")
		out.write("#!/bin/bash -l\n")
		out.write("#SBATCH -A %s\n"%project_id)
		out.write("#SBATCH -p core\n")
		out.write("#SBATCH -n 1\n")
		out.write("#SBATCH -t 05:00:00\n")
		out.write("#SBATCH -J job%d\n" %k)
		out.write("#SBATCH --output=%s.out\n" %f)
		out.write("cd /proj/snic2019-8-97/barseq_sample/barSeq\n")
		# split fasta files in seperate folder
		out.write("mkdir splitFolder\n")
		out.write("mkdir splitFolder/%s\n"%folder)
		out.write("mv data/sequence/%s splitFolder/%s\n"%(f,folder))
		out.write("python barseq.py -i splitFolder/%s -b data/sample.csv -r %sRES"%(f,folder))
		out.write("mv splitFolder/%s/%s, data/sequence/ \n"%(folder,f))
		out.close()

		# excecute bash script
		# subprocess.call(["sleep 1 && ./bash_"+f])


			#



if __name__=="__main__":
	folder_path=sys.argv[1]    # folder_with_path (e.g.  /home/vikash/sampless)
	project_id=sys.argv[2]
	barseq_slurm(folder_path,project_id)
