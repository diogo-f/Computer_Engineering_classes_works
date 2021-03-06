



# Redes semanticas
# -- Exemplo
#
# Introducao a Inteligencia Artificial
# DETI / UA
#
# (c) Luis Seabra Lopes, 2012-2016
# 2016/10/12
#


from semantic_network import *

a = Association('socrates','professor','filosofia')
s = Subtype('homem','mamifero')
m = Member('socrates','homem')

da = Declaration('descartes',a)
ds = Declaration('darwin',s)
dm = Declaration('descartes',m)

z = SemanticNetwork()
z.insert(da)
z.insert(ds)
z.insert(dm)
z.insert(Declaration('darwin',Association('mamifero','mamar','sim')))
z.insert(Declaration('darwin',Association('homem','gosta','carne')))

# novas declaracoes

z.insert(Declaration('darwin',Subtype('mamifero','vertebrado')))
z.insert(Declaration('descartes', Member('aristoteles','homem')))

b = Association('socrates','professor','matematica')
z.insert(Declaration('descartes',b))
z.insert(Declaration('simao',b))
z.insert(Declaration('simoes',b))

z.insert(Declaration('descartes', Member('platao','homem')))

e = Association('platao','professor','filosofia')
z.insert(Declaration('descartes',e))
z.insert(Declaration('simao',e))

z.insert(Declaration('descartes',Association('mamifero','altura',1.2)))
z.insert(Declaration('descartes',Association('homem','altura',1.75)))
z.insert(Declaration('simao',Association('homem','altura',1.85)))
z.insert(Declaration('darwin',Association('homem','altura',1.75)))

z.insert(Declaration('descartes', Association('socrates','peso',80)))
z.insert(Declaration('darwin', Association('socrates','peso',75)))
z.insert(Declaration('darwin', Association('platao','peso',75)))


z.insert(Declaration('damasio', Association('filosofo','gosta','filosofia')))
z.insert(Declaration('damasio', Member('socrates','filosofo')))


# Extra - descomentar as restantes declaracoes para o exercicio II.2.16

#z.insert(Declaration('descartes', AssocNum('socrates','pulsacao',51)))
#z.insert(Declaration('darwin', AssocNum('socrates','pulsacao',61)))
#z.insert(Declaration('darwin', AssocNum('platao','pulsacao',65)))

#z.insert(Declaration('descartes',AssocNum('homem','temperatura',36.8)))
#z.insert(Declaration('simao',AssocNum('homem','temperatura',37.0)))
#z.insert(Declaration('darwin',AssocNum('homem','temperatura',37.1)))
#z.insert(Declaration('descartes',AssocNum('mamifero','temperatura',39.0)))

#z.insert(Declaration('simao',Association('homem','gosta','carne')))
#z.insert(Declaration('darwin',Association('homem','gosta','peixe')))
#z.insert(Declaration('simao',Association('homem','gosta','peixe')))
#z.insert(Declaration('simao',Association('homem','gosta','couves')))

#z.insert(Declaration('damasio', AssocOne('socrates','pai','sofronisco')))
#z.insert(Declaration('darwin', AssocOne('socrates','pai','pericles')))
#z.insert(Declaration('descartes', AssocOne('socrates','pai','sofronisco')))
# x = z.declarations
# for c in x:
#     print(c)
#print(z)
print('2 - Exercicios\nex 1')
print(z.predecessor('vertebrado','socrates'))
print(z.predecessor('vertebrado','filosofo'))
print('ex 2')
print(z.predecessor_path('vertebrado','socrates'))
print('ex 3')
print(z.assocLst())
print('ex 4 ??')
print('ex5')
print(z.users())
print('ex6')
print(z.tipos())
print('ex7')
print('é para ignorar as member e subtype?')
print(z.assoc('socrates'))
print('ex8')
print(z.userRel('darwin'))
print('ex9')
print(z.userRelCount('darwin'))
print('ex10')
print(z.entUserAssoc('socrates'))
print('ex11a')
for x in z.query('socrates','altura'):
    print(x)
print('ex11a-\'socrates\'')
for x in z.query('socrates'):
    print(x)
print('ex11b------------??')
for x in z.query2('socrates'):
    print(x)
print('ex12')
for x in z.query_cancel('socrates','altura'):
    print(x)
