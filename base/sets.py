abc = {'apple','orange'}
#print(abc)
#print(type(abc))
abc.update({'banana','biscuit'})
#print(abc)

abc.add("oreo")
abc.remove("apple")
abc.discard("abc")
aaa = sorted(abc)
print(aaa)