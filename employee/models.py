from django.db import models


class AbstractPerson(models.Model):
    name = models.CharField(max_length=100)
    birth_date = models.DateField()

    class Meta:
        abstract = True

    def get_age(self):
        return 2022-self.birth_date.year


class Employee(AbstractPerson):
    position = models.CharField(max_length=50)
    salary = models.IntegerField()
    work_experience = models.CharField(max_length=50)

    def save(self, *args, **kwargs):
        self.position = self.position.upper()
        super().save(*args, **kwargs)
        print('В поле позиции большие буквы')

class Passport(models.Model):
    inn = models.BigIntegerField()
    id_card = models.CharField(max_length=18)
    employee = models.OneToOneField(Employee, on_delete=models.CASCADE)

    def get_inn(self):
        if str(self.inn)[0] == '2':
            result = 'Male'
        else:
            result = 'Female'
        return result

    def save(self, *args, **kwargs):
        self.id_card = self.id_card.upper()
        super().save(*args, **kwargs)
        print('В поле id card большие буквы')


class WorkProject(models.Model):
    project_name = models.CharField(max_length=50)
    members = models.ManyToManyField(Employee, through='Membership')

    def save(self, *args, **kwargs):
        self.project_name = self.project_name.upper()
        super().save(*args, **kwargs)
        print('В поле projectname большие буквы')


class Membership(models.Model):
    date_joined = models.DateField()
    work_project = models.ForeignKey(WorkProject, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)


class Client(AbstractPerson):
    address = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=50)

    def save(self, *args, **kwargs):
        self.address = self.address.upper()
        super().save(*args, **kwargs)
        print('В поле adress большие буквы')


class VIPClient(Client):
    vip_status_start = models.DateField()
    donation_amount = models.IntegerField()

    def save(self, *args, **kwargs):
        self.vip_status_start = self.vip_status_start.upper()
        super().save(*args, **kwargs)
        print('Выведен только год')
