from django.db import models


# # Użytkownicy systemu
# class Users(models.Model):
#     # Fields
#     id = models.AutoField(primary_key=True)
#     login = models.CharField(max_length=45, help_text='User login')
#     password = models.CharField(max_length=198, help_text='User password')
#     name = models.CharField(max_length=45, help_text='User first name')
#     surname = models.CharField(max_length=45, help_text='User last name')
#     type = models.CharField(max_length=1, help_text='Account type: 0 - user, 1 - admin')
#
#     # Metadata
#     class Meta:
#         ordering = ['id']
#
#     # Methods
#     # def get_absolute_url(self):
#     #    """Returns the url to access a particular instance of MyModelName."""
#     #    return reverse('model-detail-view', args=[str(self.id)])
#
#     def __str__(self):
#         """String for representing the MyModelName object (in Admin site etc.)."""
#         return self.id, self.login, self.password, self.name, self.surname, self.type
#

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

    # Metadata
    class Meta:
        ordering = ['id']

    # Methods
    # def get_absolute_url(self):
    #    """Returns the url to access a particular instance of MyModelName."""
    #    return reverse('model-detail-view', args=[str(self.id)])

    def __str__(self):
        """String for representing the MyModelName object (in Admin site etc.)."""
        return self.id, self.name, self.address, self.postalcode, self.city, self.phone, self.email, self.comments


# Najemcy
class Tenants(models.Model):
    # Fields
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45, help_text='Tenant first name')
    surname = models.CharField(max_length=45, help_text='Tenant last name')
    address = models.CharField(max_length=198, help_text='Tenant address')
    postalcode = models.CharField(max_length=6, help_text='Tenant postalcode')
    city = models.CharField(max_length=45, help_text='Tenant city')
    phone = models.CharField(max_length=12, help_text='Tenant phone number')
    email = models.EmailField(max_length=254, help_text='Tenant email address')
    comments = models.TextField(max_length=1000, help_text='Comments')

    # Metadata
    class Meta:
        ordering = ['id']

    # Methods
    # def get_absolute_url(self):
    #    """Returns the url to access a particular instance of MyModelName."""
    #    return reverse('model-detail-view', args=[str(self.id)])

    def __str__(self):
        """String for representing the MyModelName object (in Admin site etc.)."""
        return self.id, self.name, self.surname, self.address, self.postalcode, \
               self.city, self.phone, self.email, self.comments


# Właściciele
class Landlords(models.Model):
    # Fields
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45, help_text='Landlords first name')
    surname = models.CharField(max_length=45, help_text='Landlords last name')
    phone = models.CharField(max_length=12, help_text='Landlords phone number')
    email = models.EmailField(max_length=254, help_text='Landlords email address')

    # Metadata
    class Meta:
        ordering = ['id']

    # Methods
    # def get_absolute_url(self):
    #    """Returns the url to access a particular instance of MyModelName."""
    #    return reverse('model-detail-view', args=[str(self.id)])

    def __str__(self):
        """String for representing the MyModelName object (in Admin site etc.)."""
        return self.id, self.name, self.surname, self.phone, self.email


# Nieruchomości
class Property(models.Model):
    # Fields
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45, help_text='Property name')
    address = models.CharField(max_length=198, help_text='Property address')
    postalcode = models.CharField(max_length=6, help_text='Property postalcode')
    city = models.CharField(max_length=45, help_text='Property city')
    kw_number = models.CharField(max_length=15, help_text='Numer KW')
    # Foreign Keys
    house_association = models.ForeignKey(HousingAssociation, on_delete=models.CASCADE)

    # Metadata
    class Meta:
        ordering = ['id']

    # Methods
    # def get_absolute_url(self):
    #    """Returns the url to access a particular instance of MyModelName."""
    #    return reverse('model-detail-view', args=[str(self.id)])

    def __str__(self):
        """String for representing the MyModelName object (in Admin site etc.)."""
        return self.id, self.name, self.address, self.postalcode, self.city, self.kw_number


# Umowy najmu
class LeaseAgreement(models.Model):
    # Fields
    id = models.AutoField(primary_key=True)
    start = models.DateField(auto_now=False, auto_now_add=False, help_text='Lease agreement beginning date')
    end = models.DateField(auto_now=False, auto_now_add=False, help_text='Lease agreement ending date')
    value = models.DecimalField(max_digits=19, decimal_places=2, help_text='Lease agreement value')
    comments = models.TextField(max_length=1000, help_text='Comments')
    type = models.CharField(max_length=1, help_text='Lease agreement type: 0 - normal, 1 - notarial')
    # Foreign Keys
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    landlords = models.ForeignKey(Landlords, on_delete=models.CASCADE)
    tenants = models.ForeignKey(Tenants, on_delete=models.CASCADE)

    # Metadata
    class Meta:
        ordering = ['id']

    # Methods
    # def get_absolute_url(self):
    #    """Returns the url to access a particular instance of MyModelName."""
    #    return reverse('model-detail-view', args=[str(self.id)])

    def __str__(self):
        """String for representing the MyModelName object (in Admin site etc.)."""
        return self.id, self.start, self.end, self.value, self.comments, self.type


# Dostawcy rachunków
class BillVendors(models.Model):
    # Fields
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45, help_text='Vendors first name')
    address = models.CharField(max_length=45, help_text='Vendors address')
    postalcode = models.CharField(max_length=45, help_text="Vendors postalcode")
    city = models.CharField(max_length=45, help_text="Vendors city")
    phone = models.CharField(max_length=12, help_text='Vendors phone number')
    email = models.EmailField(max_length=254, help_text='Vendors email address')

    # Metadata
    class Meta:
        ordering = ['id']

    # Methods
    # def get_absolute_url(self):
    #    """Returns the url to access a particular instance of MyModelName."""
    #    return reverse('model-detail-view', args=[str(self.id)])

    def __str__(self):
        """String for representing the MyModelName object (in Admin site etc.)."""
        return self.id, self.name, self.address, self.postalcode, self.city, self.phone, self.email


# Rachunki i umowy
class Bills(models.Model):
    # Fields
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=198, help_text='Bills name')
    agreement_number = models.CharField(max_length=45, help_text='Agreement number')
    start = models.DateField(auto_now=False, auto_now_add=False, help_text='Agreement beginning date')
    duration = models.IntegerField(help_text="Duration in months")
    end = models.DateField(auto_now=False, auto_now_add=False, help_text='Agreement ending date')
    phone = models.CharField(max_length=12, help_text='Landlords phone number')
    email = models.EmailField(max_length=254, help_text='Landlords email address')
    # Foreign Keys
    bill_vendor = models.OneToOneField(BillVendors, on_delete=models.CASCADE)
    property = models.ForeignKey(Property, on_delete=models.CASCADE)

    # Metadata
    class Meta:
        ordering = ['id']

    # Methods
    # def get_absolute_url(self):
    #    """Returns the url to access a particular instance of MyModelName."""
    #    return reverse('model-detail-view', args=[str(self.id)])

    def __str__(self):
        """String for representing the MyModelName object (in Admin site etc.)."""
        return self.id, self.name, self.agreement_number, self.start, \
               self.duration, self.end, self.phone, self.email

