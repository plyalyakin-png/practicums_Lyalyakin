sentence = input().split()
for duplicat in sentence:
 if sentence.count(duplicat) == 2:
  print(duplicat)
  break