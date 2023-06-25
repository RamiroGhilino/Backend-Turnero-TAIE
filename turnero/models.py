from django.db import models
from django.core.validators import RegexValidator
from simple_history.models import HistoricalRecords

class User(models.Model):
    name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    ucc_key = models.PositiveIntegerField(unique=True)
    email = models.EmailField(unique=True,  validators=[
                    RegexValidator(
                        regex=r"^\d{7}@ucc.edu.ar$",
                        message="Only email addresses with '@ucc.edu.ar' domain are allowed."
                        )
                    ])
    academic_year = models.ForeignKey(
        "AcademicYear", on_delete = models.CASCADE
    ) 
    
    def __str__(self):
        return "Clave UCC: " + str(self.ucc_key) + "| Nombre " + self.name + " " + self.last_name
        
    class Meta:
        db_table = 'users'

class Role(models.Model):
    title = models.CharField(max_length = 50) #custom name to display
    type = models.CharField(max_length = 50) #actual role. eg Student, Tutor
    description = models.CharField(max_length = 255)
    users = models.ManyToManyField(
        "User", through="User_X_Role"
    )
    
    def __str__(self):
        return self.title
    
    class Meta:
        db_table = 'roles'
    
class Career(models.Model):
    name = models.CharField(max_length = 50)
    areas = models.ManyToManyField("Area", through="Career_X_Area")
    users = models.ManyToManyField("User", through="Career_X_User")
    academic_unit = models.ForeignKey(
        "AcademicUnit", on_delete=models.CASCADE
    )
    
    def __str__(self):
        return self.name
            
    class Meta:
        db_table = 'careers'

class Area(models.Model):
    name = models.CharField(max_length = 50)
    academic_year = models.ForeignKey(
        "AcademicYear", on_delete = models.CASCADE
    )
    postulations = models.ManyToManyField(
        "Postulation", through="Postulation_X_Area"
    )
    users = models.ManyToManyField(
        "User", through="User_X_Area"
    )
    
    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'areas'
    
class AcademicUnit(models.Model):
    name = models.CharField(max_length = 50)
    sede = models.CharField(max_length = 50)
    class Meta:
        db_table = 'academic_units'

class AcademicYear(models.Model):
    start = models.DateField()
    end = models.DateField()
    
    def __str__(self):
        return "Ciclo lectivo " + str(self.start.year) +" (" + str(self.start) + " - " + str(self.end) + ")"
    
    class Meta:
        db_table = 'academic_years'
    
class TutorUserReview(models.Model):
    comment = models.CharField(max_length = 500)
    occurred = models.BooleanField() #Bool to know if the tutorship was done
    absent = models.BooleanField() #If False, tutor was absent, if true, student was absent
    utility = models.PositiveSmallIntegerField()
    tutor_user = models.ForeignKey(
        "User", on_delete=models.CASCADE, related_name= "get_reviews_received"
    )
    student_user = models.ForeignKey(
        "User", on_delete=models.CASCADE, related_name="get_reviews_made"
    )
    tutorship_instance = models.ForeignKey(
        "TutorshipInstance", on_delete=models.CASCADE
    )
    class Meta:
        db_table = 'tutor_user_reviews'
    
class TutorshipInstance(models.Model):
    date = models.DateTimeField()
    status = models.CharField(max_length=25) # Status of the Tutorship. Scheduled, on going, canceled
    schedule = models.ForeignKey("TutorUserSchedule", on_delete=models.CASCADE)
    users = models.ManyToManyField(User, through='User_X_Tutorship_Instance_X_Role')
    area = models.ForeignKey("Area", on_delete=models.CASCADE)
    class Meta:
        db_table = 'tutorship_instances'

class Postulation(models.Model):
    date = models.DateTimeField()
    status = models.CharField(max_length=25) # Status of postulation. Revision, Pending, etc
    student_user = models.ForeignKey(
        "User", on_delete=models.CASCADE, related_name="get_postulation_made"
    )
    coordinator_user = models.ForeignKey(
        "User", on_delete=models.CASCADE, related_name="get_postulation_assigned"
    )
    
    def __str__(self):
        return "Postulación " + str(self.id) 
    
    class Meta:
        db_table = 'postulations'
    
class TutorshipReport(models.Model):
    comment = models.CharField(max_length=500)
    subject = models.CharField(max_length=50)
    tutorship_instance = models.ForeignKey(
        "TutorshipInstance", on_delete=models.CASCADE
    )
    tutor_user = models.ForeignKey(
        "User", on_delete=models.CASCADE
    )
    class Meta:
        db_table = 'tutorship_reports'

class TutorUserSchedule(models.Model):
    modality = models.CharField(max_length=20)
    day = models.CharField(max_length=10)
    begin = models.TimeField()
    end = models.TimeField()
    capacity = models.PositiveSmallIntegerField()
    tutor_user = models.ForeignKey(
        "User", on_delete=models.CASCADE, related_name="get_schedule"
    )
    class Meta:
        db_table = 'tutor_user_schedules'


# through tables starts
class User_X_Tutorship_Instance_X_Role(models.Model):
    user = models.ForeignKey(
        "User", on_delete=models.CASCADE
    )
    tutorship_instance = models.ForeignKey(
        "TutorshipInstance", on_delete=models.CASCADE
    )
    role = models.ForeignKey(
        "Role", on_delete=models.CASCADE
    )
    class Meta:
        db_table = 'users_x_tutorship_instances_x_roles'
        unique_together = [['user'],['tutorship_instance']]

class User_X_Area(models.Model): #done
    user = models.ForeignKey(
        "User", on_delete=models.CASCADE
    )
    area = models.ForeignKey(
        "Area", on_delete=models.CASCADE
    )
    class Meta:
        db_table = "users_x_areas"
    

class User_X_Role(models.Model): #done
    user = models.ForeignKey(
        "User", on_delete=models.CASCADE
    )
    role = models.ForeignKey(
        "Role", on_delete=models.CASCADE
    )
    active = models.BooleanField #Para saber que vista darle 
    class Meta:
        db_table = "users_x_roles"

class Career_X_Area(models.Model): #done
    career = models.ForeignKey(
        "Career", on_delete=models.CASCADE
    )
    area = models.ForeignKey(
        "Area", on_delete=models.CASCADE
    )
    class Meta:
        db_table = "careers_x_areas"

class Career_X_User(models.Model): #done
    career = models.ForeignKey(
        "Career", on_delete=models.CASCADE
    )
    user = models.ForeignKey(
        "User", on_delete=models.CASCADE
    )
    class Meta:
        db_table = "career_x_users"

class Postulation_X_Area(models.Model): #done
    postulation = models.ForeignKey(
        "Postulation", on_delete=models.CASCADE
    )
    area = models.ForeignKey(
        "Area", on_delete=models.CASCADE
    )
    class Meta:
        db_table = "postulations_x_areas"
    

