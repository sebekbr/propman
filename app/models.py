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
    name = models.CharField(max_length=45, blank=False) # HA name
    address = models.CharField(max_length=198, blank=False) # HA address
    postalcode = models.CharField(max_length=6, blank=False) # HA postalcode
    city = models.CharField(max_length=45, blank=False) # HA city
    phone = models.CharField(max_length=12, blank=True) # HA phone number
    email = models.EmailField(max_length=254, blank=True)
    comments = models.TextField(max_length=1000, blank=True) # Comments

    # Metadata
    class Meta:
        ordering = ['id']

    # Methods
    def add(self):
        self.save()

    def __str__(self):
        """String for representing the MyModelName object (in Admin site etc.)."""
        # return self.name, self.address, self.postalcode, self.city, self.phone, self.email, self.comments
        return self.name


# Najemcy
class Tenants(models.Model):
    # Fields
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45, blank=False) # Tenant first name
    surname = models.CharField(max_length=45, blank=False) # Tenant last name
    address = models.CharField(max_length=198, blank=False) # Tenant address
    postalcode = models.CharField(max_length=6, blank=False) # Tenant postalcode
    city = models.CharField(max_length=45, blank=False) # Tenant city
    phone = models.CharField(max_length=12, blank=True) # Tenant phone number
    email = models.EmailField(max_length=254, blank=True) # Tenant email address
    comments = models.TextField(max_length=1000, blank=True) # Comments

    # Metadata
    class Meta:
        ordering = ['id']

    # Methods
    def add(self):
        self.save()

    def __str__(self):
        """String for representing the MyModelName object (in Admin site etc.)."""
        # return self.id, self.name, self.surname, self.address, self.postalcode, \
        #        self.city, self.phone, self.email, self.comments
        return " ".join((self.name, self.surname))


# Właściciele
class Landlords(models.Model):
    # Fields
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45, blank=False) # Landlords first name
    surname = models.CharField(max_length=45, blank=False) # Landlords last name
    phone = models.CharField(max_length=12, blank=True) # Landlords phone number
    email = models.EmailField(max_length=254, blank=True) # Landlords email address

    # Metadata
    class Meta:
        ordering = ['id']

    # Methods
    def add(self):
        self.save()

    def __str__(self):
        """String for representing the MyModelName object (in Admin site etc.)."""
        # return self.id, self.name, self.surname, self.phone, self.email
        return " ".join((self.name, self.surname))


# Nieruchomości
class Property(models.Model):
    # Fields
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45, blank=False) # Property name
    address = models.CharField(max_length=198, blank=False) # Property address
    postalcode = models.CharField(max_length=6, blank=False) # Property postalcode
    city = models.CharField(max_length=45, blank=False) # Property city
    kw_number = models.CharField(max_length=15, blank=True) # Numer KW
    # Foreign Keys

    house_association = models.ForeignKey(HousingAssociation, on_delete=models.CASCADE)

    # Metadata
    class Meta:
        ordering = ['id']

    # Methods
    def add(self):
        self.save()

    def __str__(self):
        """String for representing the MyModelName object (in Admin site etc.)."""
        # return self.id, self.name, self.address, self.postalcode, self.city, self.kw_number
        return self.name


# Umowy najmu
class LeaseAgreement(models.Model):
    LA_TYPE_CHOICES = [
        (0, 'Zwykła'),
        (1, 'Notarialna'),
    ]

    # Fields
    id = models.AutoField(primary_key=True)
    agreement_number = models.CharField(max_length=45, blank=True)
    start = models.DateField(auto_now=False, auto_now_add=False, blank=False)  # Lease agreement beginning date
    end = models.DateField(auto_now=False, auto_now_add=False, blank=False)  # Lease agreement ending date
    value = models.DecimalField(max_digits=19, decimal_places=2, blank=False)  # Lease agreement value
    comments = models.TextField(max_length=1000, blank=True)  # Comments
    type = models.IntegerField(choices=LA_TYPE_CHOICES, blank=False, default=0)  # LA type: 0 - normal, 1 - notarial
    # Foreign Keys
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    landlords = models.ForeignKey(Landlords, on_delete=models.CASCADE)
    tenants = models.ForeignKey(Tenants, on_delete=models.CASCADE)

    # Metadata
    class Meta:
        ordering = ['id']

    # Methods
    def add(self):
        self.save()

    def __str__(self):
        """String for representing the MyModelName object (in Admin site etc.)."""
        return self.agreement_number #, self.start, self.end, self.value, self.comments, self.type


# Dostawcy rachunków
class BillVendors(models.Model):
    # Fields
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45, blank=False) # Vendors first name
    address = models.CharField(max_length=45, blank=False) # Vendors address
    postalcode = models.CharField(max_length=45, blank=False) # Vendors postalcode
    city = models.CharField(max_length=45, blank=False) # Vendors city
    phone = models.CharField(max_length=12, blank=True) # Vendors phone number
    email = models.EmailField(max_length=254, blank=True) # Vendors email address

    # Metadata
    class Meta:
        ordering = ['id']

    # Methods
    def add(self):
        self.save()

    def __str__(self):
        """String for representing the MyModelName object (in Admin site etc.)."""
        return self.name


# Rachunki i umowy
class Bills(models.Model):
    # Fields
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=198, blank=False) # Bills name
    agreement_number = models.CharField(max_length=45, blank=False) # Agreement number
    start = models.DateField(auto_now=False, auto_now_add=False, blank=False) # Agreement beginning date
    duration = models.IntegerField(blank=False) # Duration in months
    end = models.DateField(auto_now=False, auto_now_add=False, blank=False) # Agreement ending date
    # Foreign Keys
    bill_vendor = models.OneToOneField(BillVendors, on_delete=models.CASCADE)
    property = models.ForeignKey(Property, on_delete=models.CASCADE)

    # Metadata
    class Meta:
        ordering = ['id']

    # Methods
    def add(self):
        self.save()

    def __str__(self):
        """String for representing the MyModelName object (in Admin site etc.)."""
        # return self.id, self.name, self.agreement_number, self.start, \
               # self.duration, self.end
        return self.name
