
x = int(input('clase 1 = '))

y = int(input('clase 2 = '))

z = int(input('clase 3 = '))

pupitres1 = x // 2 + x%2
pupitres2 = y // 2 + y%2
pupitres3 = z // 2 + z%2 

pupitres = pupitres1 + pupitres2 + pupitres3

print('necesitamos ' + str(pupitres)+ ' pupitres')