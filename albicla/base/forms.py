from django.forms import ModelForm
from .models import Room

class RoomForm(ModelForm):
    class Meta:
        # Create the form based on the meta data from Room model 
        model = Room
        fields = '__all__'
    
    

