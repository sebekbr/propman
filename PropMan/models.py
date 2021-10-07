from django.db import models


class Users(models.Model):
    # Fields
    id = models.AutoField(primary_key=True)
    login = models.CharField(max_length=45, help_text='User login')
    password = models.CharField(max_length=198, help_text='User password')
    name = models.CharField(max_length=45, help_text='User first name')
    surname = models.CharField(max_length=45, help_text='User last name')
    type = models.CharField(max_length=1, help_text='Account type: 0 - user, 1 - admin')

    # Metadata
    class Meta:
        ordering = ['id']

    # Methods
    #def get_absolute_url(self):
    #    """Returns the url to access a particular instance of MyModelName."""
    #    return reverse('model-detail-view', args=[str(self.id)])

    def __str__(self):
        """String for representing the MyModelName object (in Admin site etc.)."""
        return self.id, self.login, self.password, self.name, self.surname, self.type