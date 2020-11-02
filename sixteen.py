print('Пошаговый конвертер из десятичной системы');
num = int(input("Введите число в десятиричной системе: "));
# setting
delimiter = 16; # основание системы исчисления 16
# 
firstNum = num; # Созраняем первичное значение для
pos1, pos2, answer = 0, 0, [];
# Запускаем цикл преобразования в 3-ю систему
while True:
	# Стандартные преобразования и операторы
	pos1 = num // delimiter; pos2 = num % delimiter;
	# Вывод каждого действия
	print(f"{num} // {delimiter} = {pos1} | {num} % {delimiter} = {pos2}");
	num = pos1; 
	if (pos2 == 10):
		answer.append("A");
	elif (pos2 == 11):
		answer.append("B");
	elif (pos2 == 12):
		answer.append("C");
	elif (pos2 == 13):
		answer.append("D");
	elif (pos2 == 14):
		answer.append("E");
	elif (pos2 == 15):
		answer.append("F");
	else:
		answer.append(str(pos2));
	# Если больше делить нечего - останавливаем
	if(pos1 == 0):
		break;
# Переворачиваем строку
answer = answer[::-1];
answer = ''.join(answer);
# Выводим ответ
print(f"{firstNum} = {answer}");