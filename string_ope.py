# coding: utf-8
s = "abcdefghi"
print len(s)
print s.find("e")
print s.find("z")
print s[4] #e
# endを指定する場合はindex-1までが返ってくる
print s[4:7] #efg
print s[:7] #abcdefg
print s[7:] #hi
print s[4:-2] #efg
