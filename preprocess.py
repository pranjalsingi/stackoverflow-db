import os

# Opening all the files
posts = open("posts.txt", "r")
ques = open("ques.txt", "w")
ans = open("ans.txt", "w")
acc = open("acc.txt", "w")
favs = open("favs.txt", "r")
favs1 = open("favs1.txt", "w")

# Spliting posts into questions and answers
for line in posts:
    temp =  line.strip('\n').split('\t')
    if temp[1] == '1':
        if temp[-1] != '\N':
            acc.write("\t".join(temp[:1] + [temp[-1]])+"\n")
            ques.write("\t".join(temp[:1] + temp[2:6] + ['1'])+"\n")
        else:
        	ques.write("\t".join(temp[:1] + temp[2:6] + ['0'])+"\n")
    else:
        ans.write("\t".join(temp[:1] + temp[2:4] + temp[5:7])+"\n")

# Deleting the thrid column of the favs.txt
for line in favs:
	temp = line.strip('\n').split('\t')
	favs1.write("\t".join(temp[:2] + [temp[-1]]) + "\n")

# Deleting favs file and rename favs1.txt to fav
for filename in os.listdir("."):
	if filename == "favs.txt":
		os.delete(filename)
	if filename == "favs1.txt":
		os.rename(filename, filename[:-1])
  
# Closing all the opened files  
posts.close()
ques.close()
ans.close()
acc.close()
favs.close()
favs1.close()