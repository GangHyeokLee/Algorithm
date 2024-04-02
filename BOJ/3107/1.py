ip = input()

address = ip.split(":")

zeroIdx = []
for i in range(len(address)):
  if not address[i]:
    zeroIdx.append(i)
  elif len(address[i]) < 4:
    address[i] = "0" * (4-len(address[i])) + address[i]

if zeroIdx:
  i = zeroIdx[0]
  zeros = "0000:" * (8 - (len(address) - (len(zeroIdx) - 1)))
  zeros += "0000"
  address[i] = zeros

ans = []
for i in address:
  if i:
    ans.append(i)
    
print(":".join(ans))