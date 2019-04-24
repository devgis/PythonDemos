x = 1.09;
y = 1.03;
s1=1;
s2=1;

for  i in range(1,200):
    s1 = s1 * x;
    s2 = s2 * y;
    print ("第%s年 s1:%s,s2:%s\r"%(i, s1, s2))
    if (s1 > 3*s2):
        print ("第%s年超越了\r"%(i))
        break;     
        

