from ROOT import *

fname = 'tree.root'
f = TFile.Open(fname)
t = f.Get('Events')
t.GetEntry(1)

ConvertBack = lambda I : ''.join([chr(int(n, 16)) for n in [x+y for x,y in zip( [z for z in hex(I)[2:]][0::2], [z for z in hex(I)[2:]][1::2])]])

def ConvertBackList(L):
  ConvertBack = lambda I : ''.join([chr(int(n, 16)) for n in [x+y for x,y in zip( [z for z in hex(I)[2:]][0::2], [z for z in hex(I)[2:]][1::2])]])
  L = [ConvertBack(l) for l in L]
  for i in range(len(L))[::-1]: 
    if L[i].startswith('-'): L[i-1]+=L[i]
  return [x.replace('-', '') for x in list(filter(lambda x : not x.startswith('-'), L))]

n = []
for i in t.WCnames: n.append(i)
print('n = ', n)
print(ConvertBackList(n))
