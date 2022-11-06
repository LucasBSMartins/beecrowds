n1, n2, n3, n4 = map(float, input().split())

m = (n1*2+n2*3+n3*4+n4)/10
print('Media: %.1f' %m)
if m >= 7.0:
  
    print('Aluno aprovado.')
    
elif m>=5.0:
    
    print('Aluno em exame.')
    e = float(input())
    print('Nota do exame: %.1f' %e)
    n = (e+m)/2
    if n >= 5.0 :
        print('Aluno aprovado.')
    else:
        print('Aluno reprovado.')
    print('Media final: %.1f' %n)
    
else:
    
    print('Aluno reprovado.')