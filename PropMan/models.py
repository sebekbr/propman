from django.db import models

# Użytkownicy systemu
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


# Nieruchomości
class Property(models.Model):
    # Fields
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45, help_text='Property name')
    address = models.CharField(max_length=198, help_text='Property address')
    postalcode = models.CharField(max_length=6, help_text='Property postalcode')
    city = models.CharField(max_length=45, help_text='Property city')
    kw_number = models.CharField(max_length=15, help_text='Numer KW')
    # Dodać Foreign key housingAssociation

    # Metadata
    class Meta:
        ordering = ['id']

    # Methods
    #def get_absolute_url(self):
    #    """Returns the url to access a particular instance of MyModelName."""
    #    return reverse('model-detail-view', args=[str(self.id)])

    def __str__(self):
        """String for representing the MyModelName object (in Admin site etc.)."""
        return self.id, self.name, self.address, self.postalcode, self.city, self.kw_number


# Spółdzielnie/Wspólnoty mieszkaniowe
class HousingAssociation(models.Model):
    # Fields
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45, help_text='HA name')
    address = models.CharField(max_length=198, help_text='HA address')
    postalcode = models.CharField(max_length=6, help_text='HA postalcode')
    city = models.CharField(max_length=45, help_text='HA city')
    phone = models.CharField(max_length=12, help_text='HA phone number')
    email = models.EmailField(max_length=254)
    comments = models.TextField(max_length=1000, help_text='Comments')
    # Dodać Foreign key housingAssociation

    # Metadata
    class Meta:
        ordering = ['id']

    # Methods
    #def get_absolute_url(self):
    #    """Returns the url to access a particular instance of MyModelName."""
    #    return reverse('model-detail-view', args=[str(self.id)])

    def __str__(self):
        """String for representing the MyModelName object (in Admin site etc.)."""
        return self.id, self.name, self.address, self.postalcode, self.city, self.phone, self.email, self.comments