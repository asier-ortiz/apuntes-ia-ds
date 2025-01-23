import datetime

# year = int(input("Introduce el year:"))
# month = int(input("Introduce el month:"))
# day = int(input("Introduce el day:"))
#
# fecha = datetime.date(year, month, day)
# print(fecha)

fecha = input("Introduce una fecha (Ejemplo: Jun 1 2021  1:33PM)")
# fecha
datetime_object = datetime.datetime.strptime(fecha, '%b %d %Y %I:%M%p')
print(datetime_object)


