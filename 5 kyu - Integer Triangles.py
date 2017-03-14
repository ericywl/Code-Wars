def give_triang(per):
    cnt = 0
    for a in range(3, per):
        if (2*a > per): 
        	break
        for b in range(a,per):
            if (a + 2*b > per): 
            	break
            c = (a*a + a*b + b*b)**0.5
            if (c == int(c) and a+b+c <= per):
                cnt += 1
    return cnt
