print('Пошаговый конвертер из десятичной системы');
num = int(input("Введите число в десятиричной системе: "));
# setting
delimiter = 3; # основание системы исчисления 1 - 9
# 
firstNum = num; # Созраняем первичное значение для
pos1, pos2, answer = 0, 0, '';
# Запускаем цикл преобразования в 3-ю систему
while True:
	# Стандартные преобразования и операторы
	pos1 = num // delimiter; pos2 = num % delimiter;
	# Вывод каждого действия
	print(f"{num} // {delimiter} = {pos1} | {num} % {delimiter} = {pos2}");
	num = pos1; answer += str(pos2);
	# Если больше делить нечего - останавливаем
	if(pos1 == 0):
		break;
# Переворачиваем строку
answer = answer[::-1];
# Выводим ответ
print(f"{firstNum} = {answer}");