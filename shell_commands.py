from datetime import date

from employee.models import *

ivan = Employee.objects.create(name='Ivan', birth_date=date(1968, 9, 4), position='Manager', salary=1000, work_experience = '1992' )
petr = Employee.objects.create(name='Petr', birth_date=date(1992, 8, 1), position='Developer', salary=2000, work_experience = '1998' )
rus = Employee.objects.create(name='Ruslan', birth_date=date(1984, 1, 2), position='Engineer', salary=3000, work_experience = '1992' )
uluk = Employee.objects.create(name='Uluk', birth_date=date(1992, 3, 20), position='Director', salary=5000, work_experience = '2014' )


vera = Employee.objects.create(name='Vera', birth_date=date(1991, 3, 20), position='Director', salary=5000, work_experience = '2014' )


p1=Passport.objects.create(inn=22004196801018, id_card='AN 411836', employee=ivan)
p2=Passport.objects.create(inn=22004199201018, id_card='AN 411836', employee=petr)
p3=Passport.objects.create(inn=22004198401018, id_card='AN 411836', employee=rus)
p4=Passport.objects.create(inn=22004145501018, id_card='AN 411836', employee=uluk)


p5=Passport.objects.create(inn=12004145501018, id_card='AN 411836', employee=vera)



workproject=WorkProject.objects.create(project_name='My_app')

workproject.members.set([ivan, petr, rus, uluk],through_defaults={'date_joined': '2022-08-20'})

to_delete_employee = Employee.objects.get(id=4)
to_delete_employee.delete()
# to_delete_passport = Passport.objects.get(id=4)
# to_delete_passport.delete()

workproject.members.set([vera],through_defaults={'date_joined': '2022-08-18'})


# Создание новых клиентов (3 чел)
c1 = Client.objects.create(name='Igor', birth_date=date(1968, 9, 4), address='Isanova 13', phone_number = '+996772001444')
c2 = Client.objects.create(name='Eva', birth_date=date(1999, 9, 4), address='Isanova 14', phone_number = '+996772001455')
c3 = Client.objects.create(name='Britney', birth_date=date(1981, 9, 4), address='Isanova 15', phone_number = '+996772001414')


# Создание нового VIP клиента (1 чел)
vip = VIPClient.objects.create(name='Igor', birth_date=date(1968, 9, 4), address='Isanova 13',
                               phone_number = '+996772001444', vip_status_start=2022, donation_amount=5000)

to_delete_client = Client.objects.get(id=3)
to_delete_client.delete()



employees = Employee.objects.raw("SELECT name FROM employee_employee")


employees_passport=Employee.oblects.raw("SELECT e.name, ep.*
FROM employee_employee as e
INNER JOIN employee_passport as ep
ON e.id = ep.id ")

# Вывести в окно терминала все проекты
projects = WorkProject.objects.raw("SELECT project_name FROM employee_workproject")

# Вывести в окно терминала проекты в которых трудитесь Вы, точнее Employee которого Вы создали используя свои личные данные

projects = WorkProject.objects.raw("SELECT project_name FROM employee_workproject")


# Вывести всех Клиентов
clients = Clients.objects.raw("SELECT name FROM employee_clients")

# Вывести Всех ВИП Клиентов

vipclients = VIPClient.objects.raw("SELECT name FROM employee_vipclient.")


