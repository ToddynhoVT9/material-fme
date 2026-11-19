# Verificação independente — Unidade 1 (exemplos e questões autorais) · w5
import itertools, math
from fractions import Fraction as Fr
from sympy import isprime, gcd, lcm, sqrt, Rational, pi, Integer
ok=lambda c,msg: print(('OK  ' if c else 'ERRO'), msg)
# Ex 1.2 — valores de p
ok((Integer(8)!=2**3)==False,'1.2a p F')
ok((-1>-2)==True,'1.2b p V')
ok(sqrt(2).is_rational==False,'1.2c √2∈Q F')
ok(18%4!=0,'1.2d 4|18 F')
ok(bool(pi<Rational(314,100))==False,'1.2e π<3,14 F')
# Ex 1.4 — A: "B é valete"; B: "nós dois somos valetes"
sol=[(A,B) for A,B in itertools.product([1,0],repeat=2) if A==(not B) and B==(not A and not B)]
ok(sol==[(1,0)],f'1.4 A cavaleiro, B valete {sol}')
# Q3 — 2^100+1 composto (proposição falsa)
ok((2**100+1)%17==0 and not isprime(2**100+1),'Q3f 2^100+1 composto (divisível por 17)')
# Q4
ok(12%5!=0,'Q4a ~p V'); ok(math.isqrt(49)==7,'Q4b ~p F'); ok(2**5>5**2,'Q4d p V → ~p F'); ok(42%6==0,'Q4e ~p F')
# Q5 (integradora) — era Q6 na v2
ok(gcd(12,18)==6,'Q5a p V'); ok(2**10>10**3,'Q5b p V'); ok(91%7==0,'Q5c p V')
ok(((-2)**4<(-2)**3)==False,'Q5d p F'); ok(lcm(4,6)==12,'Q5e p F (mmc=12)'); ok(sqrt(Rational(9,100))==Rational(3,10),'Q5f p V')
# Q7 — "n é negativo" não é negação de "n é positivo" (n=0 torna ambas falsas)
ok((0>0)==False and (0<0)==False,'Q7 n=0 torna as duas falsas → (c)')
# Q9 — OBMEP 2010 tamanduás (era Q5)
s=[v for v in itertools.product([1,0],repeat=4) if all(bool(st)==bool(t) for t,st in
   [(v[0],not v[1]),(v[1],v[2]),(v[2],v[3]!=v[0]),(v[3],not v[0])])]
ok(len(s)==1 and sum(s[0])==3,f'Q9 3 tamanduás {s}')
# Q6 — s(x): x^2 = 2x (era Q8)
ok(0**2==2*0 and 2**2==2*2 and 3**2!=2*3,'Q6 s(0) V, s(2) V, s(3) F')
# Q10 — A: "B é valete"; B: "C é valete"; C: "A e B são valetes"
s=[v for v in itertools.product([1,0],repeat=3) if v[0]==(not v[1]) and v[1]==(not v[2]) and v[2]==(not v[0] and not v[1])]
ok(s==[(0,1,0)],f'Q10 só B cavaleiro {s}')
# --- v3 ---
# Ex 1.6 — "eu sou valete": nenhum tipo pode dizer; "eu sou cavaleiro": ambos
ok([k for k in (0,1) if (k==1)==(k==0)]==[],'1.6a ninguém diz "sou valete"')
ok([k for k in (0,1) if (k==1)==(k==1)]==[0,1],'1.6b qualquer um diz "sou cavaleiro"')
# Q11 — pergunta encaixada revela o fato para os dois tipos
def q11(k,L):
    direta = L if k else (not L)
    return direta if k else (not direta)
ok(all(bool(q11(k,L))==bool(L) for k in (0,1) for L in (0,1)),'Q11 resposta = fato (dupla negação)')
# Q12 — contagem de palavras e cartão de duas frases
ok(len("Esta frase tem seis palavras".split())==5,'Q12a tem 5 palavras → F')
ok(len("Esta frase tem cinco palavras".split())==5,'Q12b tem 5 palavras → V')
ok([(f,v) for f,v in itertools.product([0,1],repeat=2) if f==v and v==(not f)]==[],'Q12c cartão: nenhuma atribuição consistente')
