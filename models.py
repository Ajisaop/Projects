from django.db import models



# Create your models here.max_length=100)
class login(models.Model):
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    type= models.CharField(max_length=100)

class student(models.Model):
    name=models.CharField(max_length=100)
    DOB = models.DateField()
    Gender= models.CharField(max_length=50)
    Email= models.EmailField(max_length=100)
    Mobileno=models.BigIntegerField()
    Parentname=models.CharField(max_length=100)
    Parentmobileno=models.BigIntegerField()
    Parentemail=models.EmailField(max_length=100)
    Class=models.CharField(max_length=100)
    Place=models.CharField(max_length=100)
    Post=models.CharField(max_length=50)
    Pin=models.BigIntegerField()
    District=models.CharField(max_length=100)
    Photo=models.CharField(max_length=100)

class tutor(models.Model):
    Name = models.CharField(max_length=100)
    DOB = models.DateField()
    Gender = models.CharField(max_length=50)
    Email = models.EmailField(max_length=100)
    Mobileno = models.BigIntegerField()
    SUBJECT=models.ForeignKey(subject,on_delete=models.CASCADE)
    Class=models.CharField(max_length=100)
    Place = models.CharField(max_length=100)
    Post = models.CharField(max_length=50)
    Pin = models.BigIntegerField()
    District = models.CharField(max_length=100)
    Photo=models.CharField(max_length=400)
    CV=models.CharField(max_length=400)


class subject(models.Model):
    Subject=models.CharField(max_length=400)

class timetable(models.Model):
    Date=models.DateField()
    Time=models.DateTimeField()
    SUBJECT = models.ForeignKey(subject, on_delete=models.CASCADE)
    Hour=models.CharField(max_length=50)

class bill(models.Model):
    Date = models.DateField()
    Amount=models.BigIntegerField()
    STUDENT = models.ForeignKey(student, on_delete=models.CASCADE)

class homework(models.Model):
    SUBJECT = models.ForeignKey(subject, on_delete=models.CASCADE)
    TUTOR = models.ForeignKey(tutor, on_delete=models.CASCADE)
    Homework = models.CharField(max_length=400)
    Date=models.DateField()
    Submitdate=models.DateField()

class payment_notification(models.Model):
    Notification = models.CharField(max_length=200)

class feedback(models.Model):
    Feedback= models.CharField(max_length=200)
    Date = models.DateField()
    STUDENT = models.ForeignKey(student, on_delete=models.CASCADE)

class notification(models.Model):
    Notification = models.CharField(max_length=200)
    Class_link= models.CharField(max_length=200)
    TUTOR = models.ForeignKey(tutor, on_delete=models.CASCADE)

class attendance(models.Model):
    Date = models.DateField()
    TUTOR = models.ForeignKey(tutor, on_delete=models.CASCADE)
    STUDENT = models.ForeignKey(student, on_delete=models.CASCADE)
    SUBJECT = models.ForeignKey(subject, on_delete=models.CASCADE)
    Attedance=models.CharField(max_length=50)

class homwork_answers(models.Model):
    HOMEWORK = models.ForeignKey(homework, on_delete=models.CASCADE)
    Answers=models.CharField(max_length=50)
    Date=models.DateField()
    STUDENT = models.ForeignKey(student, on_delete=models.CASCADE)

class complaint_replay(models.Model):
    Date = models.DateField()
    Complaint= models.CharField(max_length=200)
    Replay= models.CharField(max_length=200)
    STUDENT = models.ForeignKey(student, on_delete=models.CASCADE)






