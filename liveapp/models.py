from django.db import models
from django.contrib.gis.db import models
import datetime
from phonenumber_field import formfields
from django.db.models import signals
from django.core.urlresolvers import reverse
from django.template.defaultfilters import date
from django.forms import TextInput
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import User, Group


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    activation_key = models.CharField(max_length=40, blank=True)
    key_expires = models.DateTimeField(default=datetime.date.today())

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name_plural = 'User profiles'


sub_county = (
    ('Kieni_East', 'Kieni_East'),
    ('Kieni_West', 'Kieni_West'),
    ('Mathira_East', 'Mathira_East'),
    ('Mathira_West', 'Mathira_West'),
    ('Nyeri_Central', 'Nyeri_Central'),
    ('Mukurweini', 'Mukurweini'),
    ('Tetu', 'Tetu'),
    ('Nyeri_South', 'Nyeri_South'),
)

Town = (
    ('Endarasha', 'Endarasha'),
    ('Gakawa', 'Gakawa'),
    ('Gatarakwa', 'Gatarakwa'),
    ('Mugunda', 'Mugunda'),
    ('Mweiga', 'Mweiga'),
    ('Naro_Moru', 'Naro_Moru'),
    ('Thegu_river', 'Thegu_river'),
    ('Commercial', 'Commercial'),
    ('Hospital', 'Hospital',),
    ('Iria-ini', 'Iria-ini'),
    ('Kirimukuyu', 'Kirimukuyu'),
    ('Konyu', 'Konyu'),
    ('Magutu', 'Magutu'),
    ('Market', 'Market'),
    ('Ngoranu', 'Ngoranu'),
    ('Railway', 'Railway'),
    ('Residential', 'Residential'),
    ('stadium', 'stadium'),
    ('Gakindu', 'Gakindu'),
    ('Giathungu', 'Giathungu'),
    ('Gikondi', 'Gikondi'),
    ('Githi', 'Githi',),
    ('Muhito', 'Muhito'),
    ('Rutune', 'Rutune'),
    ('Thanu', 'Thanu'),
    ('Chania', 'Chania'),
    ('Gatitu', 'Gatitu'),
    ('Kamakwa', 'Kamakwa'),
    ('Karia', 'Karia'),
    ('Kiganjo', 'Kiganjo'),
    ('Kirichu', 'Kirichu'),
    ('Mukaro', 'Mukaro'),
    ('Muruguru', 'Muruguru'),
    ('Nyaribu', 'Nyaribu'),
    ('Nyeri_Central', 'Nyeri_Central'),
    ('Kanyange', 'Kanyange'),
    ('Kianganda', 'Kianganda'),
    ('Nduye_River', 'Nduye_River'),
    ('Nyamari', 'Nyamari'),
    ('Thuti', 'Thuti'),
    ('Chinga', 'Chinga'),
    ('Karima', 'Karima'),
    ('Mahiga', 'Mahiga'),
    ('Mumwe', 'Mumwe'),
    ('Aguthi', 'Aguthi'),
    ('Karundu', 'Karundu'),
    ('Muhoya', 'Muhoya'),
    ('Tetu', 'Tetu'),
    ('Thingingi', 'Thingingi')
)


Disease = (
    ('East_cost_fever', 'East_cost_fever'),
    ('Anaplamosis', 'Anaplamosis'),
    ('Mastitis', 'Mastitis'),
    ('Milk_fever', 'Milk_fever'),
    ('Deworming', 'Deworming'),
    ('Dehorning', 'Dehorning'),
    ('metritis', 'metritis'),
    ('Foot_rot', 'Foot_rot'),
    ('Eye_infection', 'Eye_infection'),
    ('Pneumonia', 'Pneumonia'),
    ('Diarrhea', 'Diarrhea'),
    ('Retained_after_birth', 'Retained_after_birth'),
    ('Colibaccilosis', 'Colibaccilosis'),
    ('Costipation', 'Costipation'),
    ('Anthrax', 'Anthrax'),
    ('Broat', 'Broat'),
    ('Iron_infection', 'Iron_infection'),
    ('mange', 'mange'),
    ('Hydatit', 'Hydatit'),
    ('Echinococcus', 'Echinococcus'),
    ('Undetermined', 'Undetermined')
)

TREATED = (
    ('Yes', 'Yes'),
    ('No', 'No'),
)
Farming_METHODS = (
    ('zero_grazing', 'zero_grazing'),
    ('pastrolism', 'pastrolism'),
)

incidence_status = (
    ('Average', 'Average'),
    ('Bad', 'Bad'),
    ('Very Bad', 'Very Bad'),
    ('Unknown', 'Unknown'),
)

#**************animals******************
Animal = (
    ('Cattle', 'Cattle'),
    ('Sheep', 'Sheep'),
    ('Goat', 'Goat'),
    ('Poultry', 'Poultry'),
    ('mixed', 'mixed')

)

#********** animal Breeds ***************

Breed = (
    ('Zebu', 'zebu'),
    ('Borana', 'Borana'),
    ('Sahiwal', 'Sahiwal'),
    ('red masai', 'red masai'),
    ('local breed', 'local breed'),
    ('mix red masai', 'mix red masai'),
    ('cross breed', 'cross breed'),
    ('galla', 'galla'),
    ('mix galla', 'mix galla'),
    ('local', 'local'),
    ('small east African', 'small east african'),
    ('local', 'local'),
    ('brown layers', 'brown_layers'),
    ('sussex', 'sussex'),
    ('rhode', 'rhode'),
    ('golden comet', 'golden comet')
)

conditions = (
    ('skinny', 'skinny'),
    ('medium', 'medium'),
    ('fat', 'fat')
)

Status = (
    ('active', 'active'),
    ('dormant', 'dormant'),
    ('other', 'other')
)
Owner = (
    ('public', 'public'),
    ('private', 'private'),
    ('community', 'community')
)
Reporter = (
    ('veterinary officer', 'veterinary officer'),
    ('farmer', 'farmer'),
    ('other', 'other')

)

Facility = (
    ('cattle dip', 'cattle dip'),
    ('milk collection centre', 'milk collection centre'),
    ('slaughter house', 'slaughter house'),
    ('Biogas digester', 'Biogas digester'),
    ('training center', 'training center'),
    ('Artificial insemination', 'Artificial insemination')

)

#************classes************************


class Incidence(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    phone = PhoneNumberField(null=True)
    email = models.EmailField(max_length=60, null=True, blank=True)
    sub_county = models.CharField(max_length=60, choices=sub_county)
    nearest_town = models.CharField(max_length=60, null=True, blank=True, choices=Town, help_text='name of my nearest town')
    date_reported = models.DateTimeField(auto_now_add=True)
    animal = models.CharField(max_length=50, null=True, blank=True, choices=Animal)
    number = models.IntegerField(blank=True, null=True, help_text='number of animals affected', default=0)
    disease = models.CharField(max_length=50, choices=Disease)
    description = models.CharField(max_length=200, null=False, blank=False, help_text="briefly describe the disease or the behaviour of animal")
    treated = models.CharField(max_length=20, null=True, blank=True, choices=TREATED)
    photo = models.FileField(upload_to='uploads', null=True, blank=True)
    reporter = models.CharField(max_length=30, choices=Reporter)
    geom = models.PointField(srid=4326)
    objects = models.GeoManager()

    def __unicode__(self):
        return self.first_name

    class Meta:
        verbose_name_plural = 'disease incidences'


class Corridor(models.Model):
    id = models.AutoField(primary_key=True)
    time = models.DateTimeField(auto_now_add=True)
    number = models.IntegerField(help_text='number of animals moved')
    name = models.CharField(max_length=50, help_text="name of the route")
    status = models.CharField(max_length=30, choices=Status)
    animal = models.CharField(max_length=30, choices=Animal)
    project = models.IntegerField(default=0)
    geom = models.MultiLineStringField(srid=4326)
    objects = models.GeoManager()

    def __unicode__(self):
        return str(self.name)

    class Meta:
        verbose_name_plural = 'Corridors'


class Manure(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    PhoneNumberField(null=True, blank=True)
    animal = models.CharField(max_length=50, choices=Animal)
    quantity = models.CharField(max_length=200, help_text='more details on manure eg quantity and age.')
    time = models.DateTimeField(auto_now_add=True)
    geom = models.PointField(srid=4326)
    objects = models.GeoManager()

    def __unicode__(self):
        return str(self.id)

    class Meta:
        verbose_name_plural = 'products'


class Facility(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    pupose = models.CharField(max_length=50, choices=Facility)
    size = models.IntegerField(help_text='estimated area in square meters')
    status = models.CharField(max_length=30, choices=Status)
    owner = models.CharField(max_length=30, choices=Owner)
    geom = models.PointField(srid=4326)
    objects = models.GeoManager()

    def __unicode__(self):
        return str(self.id)

    class Meta:
        verbose_name_plural = 'facilities'


class Market(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateTimeField()
    conditions = models.CharField(max_length=50, choices=conditions)
    animal = models.CharField(max_length=50, choices=Animal)
    breed = models.CharField(max_length=50, choices=Breed)
    Price = models.IntegerField()
    number = models.IntegerField(help_text='number of animals')
    market = models.CharField(max_length=50, help_text='market name')
    geom = models.PointField(srid=4326)
    objects = models.GeoManager()

    class Meta:
        verbose_name_plural = "Market"


#******************** events ***********************************************


event_type = (
    ('vaccination', 'vaccination'),
    ('Seminar', 'Seminar'),
    ('Road Show', 'Road Show'),
    ('Annual GM', 'Annual GM'),
    ('other', 'other'),

)


class Event(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, null=False)
    organizers = models.CharField(max_length=50, null=False)
    sponsors = models.CharField(max_length=50, null=False)
    date = models.DateField()
    location = models.CharField(max_length=50, null=False)
    agenda = models.CharField(max_length=50, null=False)
    purpose = models.CharField(max_length=50, choices=event_type)
    description = models.TextField(max_length=250, null=False)
    nearest_town = models.CharField(max_length=60, null=True, blank=True, choices=Town, help_text='name of my nearest town')
    contacts = PhoneNumberField(blank=True, null=True, help_text="for enquiries call.")
    geom = models.PointField(srid=4326)
    objects = models.GeoManager()

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Event"


Type_choices = (
    ("dairy", "dairy"),
    ("beef", "beef")
)

Farming_METHODS = (
    ('zero_grazing', 'zero_grazing'),
    ('pastrolism', 'pastrolism'),
)


class Cattle(models.Model):
    id = models.AutoField(primary_key=True)
    farmer_fname = models.CharField(max_length=50)
    farmer_lname = models.CharField(max_length=50)
    farmer_telephone = PhoneNumberField(null=True, blank=True)
    cow_type = models.CharField(max_length=50, choices=Type_choices)
    breed = models.CharField(max_length=50, choices=Breed)
    number_of_animals = models.IntegerField(help_text='number of animals')
    farming_method = models.CharField(max_length=50, choices=Farming_METHODS)
    geom = models.PointField(srid=4326)
    objects = models.GeoManager()

    def __unicode__(self):
        return self.farmer_fname


class Sheep(models.Model):
    id = models.AutoField(primary_key=True)
    farmer_fname = models.CharField(max_length=50)
    farmer_lname = models.CharField(max_length=50)
    farmer_telephone = PhoneNumberField(null=True, blank=True)
    sheep_type = models.CharField(max_length=50, choices=Type_choices)
    breed = models.CharField(max_length=50, choices=Breed)
    number_of_animals = models.IntegerField(help_text='number of animals')
    farming_method = models.CharField(max_length=50, choices=Farming_METHODS)
    geom = models.PointField(srid=4326)
    objects = models.GeoManager()

    def __unicode__(self):
        return self.farmer_fname


class Goat(models.Model):
    id = models.AutoField(primary_key=True)
    farmer_fname = models.CharField(max_length=50)
    farmer_lname = models.CharField(max_length=50)
    farmer_telephone = PhoneNumberField(null=True, blank=True)
    breed = models.CharField(max_length=50, choices=Breed)
    number_of_animals = models.IntegerField(help_text='number of animals')
    farming_method = models.CharField(max_length=50, choices=Farming_METHODS)
    geom = models.PointField(srid=4326)
    objects = models.GeoManager()

    def __unicode__(self):
        return self.farmer_fname


class Poultry(models.Model):
    id = models.AutoField(primary_key=True)
    farmer_fname = models.CharField(max_length=50)
    farmer_lname = models.CharField(max_length=50)
    farmer_telephone = PhoneNumberField(null=True, blank=True)
    breed = models.CharField(max_length=50, choices=Breed)
    number_of_birds = models.IntegerField(help_text='number of birds')
    geom = models.PointField(srid=4326)
    objects = models.GeoManager()

    class Meta:
        verbose_name_plural = "poultry"

    def __unicode__(self):
        return self.farmer_fname


class Subcounty(models.Model):
    shape_leng = models.FloatField()
    shape_area = models.FloatField()
    name = models.CharField(max_length=100)
    geom = models.MultiPolygonField(srid=4326)
    objects = models.GeoManager()

    class Meta:
        verbose_name_plural = 'counties'

    def __unicode__(self):
        return self.name


class Town(models.Model):
    id = models.AutoField(primary_key=True)
    town_name = models.CharField(max_length=50)
    town_type = models.CharField(max_length=50)
    geom = models.MultiPointField(srid=4326)
    objects = models.GeoManager()

    class Meta:
        verbose_name_plural = 'Towns'

    def __unicode__(self):
        return self.town_name
