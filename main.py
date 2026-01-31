def name(input_name):   
  print(f"your name is: {input_name}")
  return input_name.lower()


n = input("enter your name: ")
x = name(n)

file_w = open("save.txt", "w")
file_w.write(x)
file_w.close()

file_r = open("hello.txt", "r")
print(file_r.read())
file_r.close()