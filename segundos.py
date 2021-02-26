segundos = input("Por favor, entre com o número de segundos que deseja converter: ")
total_segundos = int(segundos)

dias = total_segundos // 86400
resto_seg1 = total_segundos % 86400

horas = resto_seg1 // 3600
resto_seg2 = resto_seg1 % 3600

minutos = resto_seg2 // 60
rest_seg_final = resto_seg2 % 60

print(dias, "dias,", horas, "horas,", minutos, "minutos e", rest_seg_final, "segundos.")