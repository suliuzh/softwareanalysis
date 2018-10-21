#-*-coding:utf-8
import os
from git import Repo
import csv
def fromrelease(repo,tag):
	print(tag,"start get the commits!")
	git=repo.git
	filepath='/home/cyl/Downloads/course/csvfiles/'
	filename=filepath+tag+".csv"
	#with open(filename,'a',newline='') as f:
                #writer=csv.writer(f)
       		#writer.writerow(["sha and description","changed files"])
	commits=repo.iter_commits(tag)
	for cm in list(commits):
		desc=cm.message
		sha=cm.hexsha
		files=git.show(sha,"--oneline","--numstat")
		info=files.split("\n")
		info_list=[sha,desc]
		for temp in info[1:]:
			if temp:
				info_list.append(temp.split()[2])
		with open(filename,'a',newline='') as f:
			writer=csv.writer(f)
			writer.writerow(info_list)
	print(tag,"has got the commits!")
if __name__=="__main__":
	repo=Repo('numpy')
	tags=repo.tags
	for tag in tags:
		print(tag)
		fromrelease(repo,str(tag))

