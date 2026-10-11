#String and it's functions
chnl_name="QA Solutions"
print(chnl_name)
start_idx=0
#print(chnl_name[start_idx])
end_idx=len(chnl_name)-1
#print(chnl_name[end_idx])

print(chnl_name[start_idx:end_idx+1:1])
print(f"String after replacement :  {chnl_name.replace("QA", "Testing")}")
print(chnl_name.upper())
print(chnl_name.lower())
print(chnl_name.capitalize())
'''print(chnl_name.title())
print(chnl_name.strip())
print(chnl_name.rstrip())
print(chnl_name.lstrip())'''
print(chnl_name.find("s"))
print(chnl_name.find("Testing"))
print(chnl_name.find("QA"))
print(chnl_name.split())
print(chnl_name.count(" "))
print(chnl_name.lower().count("s"))
print(chnl_name.count("s"))