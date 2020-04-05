from django.db import models

"""
user model
"""

    role_id = models.ForeignKey("Role", on_delete=models.CASCADE)
    login = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=60)
    firstname = models.CharField(max_length=60)    
    lastname = models.CharField(max_length=60)
    email = models.EmailField(max_length=255, unique=True)
    langue = models.CharField(max_length=2)

    class Meta:
        db_table = "users"
        verbose_name_plural = "Users"        
        verbose_name = "User"

    def __str__(self):
        return 'Role ID : ' + self.role_id \
        '\nLogin : ' + self.login \
        '\nFirstname : ' + self.firstname \
        '\nLastname : ' + self.lastname \
        '\nEmail : ' + self.email \ 
        '\nLangue : ' + self.langue \