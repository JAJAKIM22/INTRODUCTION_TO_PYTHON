file = open('test.txt', mode= 'r')

data = file.readline() ## read()/ read(10)/ readlne(10) / print(file.read())

print(data)

file.close()

with open('test.txt', mode= 'r') as file:
    data = file.readline()
    print(data)
    # print(file.read())
    # for x in file:
    #     print(x)
    # data = file.readlines()
    # for x in data:
    #     print(x)

with open('write.txt', mode= 'w') as file:
    file.write("I have written a line")

with open('writer.txt', mode= 'w') as file:
    file.writelines(["I have written a line" , "\n this is a new line", "\n I am happy"])

## APPEND
try:
  with open('sample/writers.txt',  'a') as file:
      file.writelines(["I have written a line" , "\n this is a new line", "\n I am happy"])
except FileNotFoundError as e:
  print("ERROR", e)