#LIST
#task 1
my_list = [3, 5, 7, 9, 10.5]
print(my_list)
my_list.append("Python")
print('lenght = '+ str(len(my_list)))


#task 2
print('first element = ' + str(my_list[0]))
print('last element = ' + str(my_list[-1]))
print(my_list[1:5])
my_list.remove("Python")
print(my_list)


#DICT
#task 1
my_dict = {
	"city": "Москва", 
	"temperature": "20"
}

print(my_dict['city'])
my_dict['temperature'] = int(my_dict['temperature'])-5
print(my_dict)

#task2
print(my_dict.get('country'))
print(my_dict.get("country", "Россия"))
my_dict['date'] = "27.05.2019"

print(len(my_dict))