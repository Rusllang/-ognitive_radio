import sys
import random as rnd

 
def Creation(a):
    with open("waves","w") as t:
    	a[0][1] = 'BPSK'
    	a[1][1] = 'BPSK'
    	a[2][1] = 'BPSK'
    	a[3][1] = 'BPSK'
    	for i in a:
    		t.write(str(i[0])+" "+'%s\n'%str(i[1]))
    
 
def writing(): 
    
    s = []
    for i in range(300):
        s.append(str(i)) 
    
    mod_psk = "PSK"
    mod_cum = "QAM"
    mod_num = ["B", "4-", "8-", "16-", "32-", "64-", "128-", "256-"]
    
    n = []
    for i in range(300):
        r1 = rnd.randint(0,2)
        if (r1 == 0):
            r2 = rnd.randint(0,len(mod_num)-1)
            q = [mod_num[r2],mod_psk]
            
            q = ''.join(list(q[0 : 2]))
            if (q == "4-PSK"):
                q = "QPSK"
            n.append(q)
        else:
            r3 = rnd.randint(1,len(mod_num)-1)
            #q1 = [mod_num[r3],mod_cum]
            q1 = [mod_num[r2],mod_psk]
            
            q1 = ''.join(list(q1[0 : 2]))
            if (q1 == "4-QAM"):
                q1 = "QPSK"
            n.append(q1)
    
    z = [s, n]
    

    
    x = [list(i) for i in zip(*z)]
    
    Creation(x)
 

    
 
def set(q):
    if int(q) == 1:
        print("select selection's size:")
        
        writing()
    
 
def main():  
    boolka = True
    while boolka == True:
        print ("select mode:")
        print("1 - create random file\n0 - exit")
        ans = int(input())
    
        if (ans == 0):
            print("fuck off")
            boolka = False
        set(ans)
 
writing()
