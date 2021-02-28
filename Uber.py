a=[1,2,3,4]
sign=['+','-','*','/']
b=[1,1,2,4]
c=[2,2,6,2]
result=[]
for i in range(len(sign)):
    if(sign[i]=='+'):
        if a[i]+b[i]==c[i]:
            result.append('true')
        else:
            result.append('false')
    if(sign[i]=='-'):
        if a[i]-b[i]==c[i]:
            result.append('true')
        else:
            result.append('false')
    if(sign[i]=='*'):
        if a[i]*b[i]==c[i]:
            result.append('true')
        else:
            result.append('false')
    if(sign[i]=='/'):
        if a[i]/b[i]==c[i]:
            result.append('true')
        else:
            result.append('false')
print('[%s]' % ', '.join(map(str, result)))
