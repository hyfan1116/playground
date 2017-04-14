
if s is None:
	return 0
if len(s) == 1:
	return 1

for l in range(len(s)):
	if s.replace(s[:l],"") == "":
		return len(s)/l
return 1		