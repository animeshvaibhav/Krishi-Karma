from django.db import models

# Create your models here.

class Soil(models.Model):
    name = models.CharField(max_length=30,unique = True)
    
    def __str__(self):
        return f"{self.name}"

##############################################################

class State(models.Model):
    name = models.CharField(max_length=30)
    #districts = models.OneToManyField(District,related_name="state")
    def __str__(self):
        return f"{self.name}"

##############################################################

class Category(models.Model):
    name = models.CharField(max_length=30,unique = True)

    def __str__(self):
        return f"{self.name}"
    
##################################################################

class Crop(models.Model):
    name = models.CharField(max_length=30,unique = True)
    category = models.ForeignKey(Category, on_delete = models.SET_NULL, related_name="crops",null = True )
    #districts = models.ManyToManyField(District, related_name="crops")

    def __str__(self):
        return f"{self.name}"


###################################################################

class District(models.Model):
    name = models.CharField(max_length=30)
    state = models.ForeignKey(State, on_delete=models.CASCADE, related_name="districts",blank=True)
    crops = models.ManyToManyField(Crop,related_name="districts",blank=True) 

    class Meta:
        unique_together = ('name', 'state',) 

    def __str__(self):
        return f"{self.name}"  


###################################################################    
        
class Farmer(models.Model):
    name = models.CharField(max_length=30)
    state = models.ForeignKey(State, on_delete=models.CASCADE, related_name="farmers",blank=True, null = True)
    location = models.ForeignKey(District, on_delete=models.SET_NULL, related_name="farmers", null = True)
    plotno = models.IntegerField(blank=True)
    plotSize = models.IntegerField(blank=True)
    budget = models.IntegerField(blank=True)
    fundRaisedTillNow = models.IntegerField(blank=True)
    soil = models.ForeignKey(Soil, related_name = "farmers" , blank = True,on_delete = models.SET_NULL ,null = True)
    phValue = models.DecimalField(decimal_places = 3, max_digits = 5 ,blank=True)
    crop = models.ForeignKey(Crop, on_delete=models.SET_NULL, related_name = "farmers", null = True)
    loanRequired = models.IntegerField(blank=True)
    loanRaised = models.IntegerField(blank=True)
    Map = models.URLField(blank=True)

    def __str__(self):
        return f"{self.name} ({self.location.name} , {self.state.name})"

    