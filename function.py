#task1
#Создайте функцию get_summ(one, two, delimiter='&'), 
#которая принимает два параметра, приводит их к строке 
#и отдает объединенными через разделитель delimiter
#Вызовите функцию, передав в нее два аргумента "Learn" и "python", 
#положите результат в переменную и выведите ее значение на экран
#Сделайте так, чтобы результирующая строка выводилась заглавными буквами


def get_summ(one, two, delimiter='&'):
	one = str(one)
	two = str(two)
	summ = one + delimiter + two
	return summ

p = get_summ('learn', 'python')
print(p.capitalize())


#video
def discounted(price, discount, max_discount=60):
    price = abs(float(price))
    discount = abs(float(discount))
    max_discount = abs(float(max_discount))
    if max_discount > 99:
        raise ValueError('Слишком большая максимальная скидка')
    if discount >= max_discount:
        return price
    else:
        return price - (price * discount / 100)


p = discounted(100,29, max_discount = 30)
print(p)