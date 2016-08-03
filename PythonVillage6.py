
s='When I find myself in times of trouble Mother Mary comes to me Speaking words of wisdom let it be And in my hour of darkness she is standing right in front of me Speaking words of wisdom let it be Let it be let it be let it be let it be Whisper words of wisdom let it be And when the broken hearted people living in the world agree There will be an answer let it be For though they may be parted there is still a chance that they will see There will be an answer let it be Let it be let it be let it be let it be There will be an answer let it be Let it be let it be let it be let it be Whisper words of wisdom let it be Let it be let it be let it be let it be Whisper words of wisdom let it be And when the night is cloudy there is still a light that shines on me Shine until tomorrow let it be I wake up to the sound of music Mother Mary comes to me Speaking words of wisdom let it be Let it be let it be let it be yeah let it be There will be an answer let it be Let it be let it be let it be yeah let it be Whisper words of wisdom let it be'

w=s.split()
l=len(w)
i=0
j=0
d={}
k=0
f={}
e={}
r={}
licz={}
while i<l:

    d[i]=w[i]
    
    i=i+1
    
l2=len(d)


for j in range(l):
    licznik=0
    for k in range(l2):
        if d[k]==w[j]:
            
            licznik=licznik+1
            s=str(licznik)
            r[d[k]]=d[k]+' '+s
            f[k]=d[k]+' '+s
for names in r:
    print r[names]
    
    




   


        
    

    
