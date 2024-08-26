print('hello'.upper())  #ადიდებს სტრინგს
print('HELLO'.lower())  #აპატარავებს სტრინგს
print('hello'.capitalize()) #პირველ ასოს ადიდებს სტრინგში
print("HeLlo".swapcase())   #რომელი ასოც დიდია აპატარავებს და რომელიც პატარა ადიდებს
print("hello".find("e"))    #პოულობს მერამდენე ინდექსზე დგას ფრჩხილებში გადაცემული სტრინგ
print(len("hello"))    #გვიბრუნებს სტრინგის სიგრძეს
listn = [1,2,3]
listn.append(5)
print(listn)            #სიის ბოლოში ამატებს ელემენტს
listn.insert(1,"hello")
print(listn)          #ამატებს სიაში მითითებულ ინდექსზე
listn.pop(4)
print(listn)        #შლის სიაში მითითებულ ინდექსზე მყოფ ელემენტს