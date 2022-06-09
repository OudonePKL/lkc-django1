from django.shortcuts import render
from .models import *

# Create your views here.
def home(request):
    bgImage = BackGImage.objects.all() # For background's images
    teachers1 = Teachers1.objects.all() # For teacher's images first line
    teachers2 = Teachers2.objects.all() # For teacher's images second line
    lkcDatas = LKCDatas.objects.all() # For LKC's informations
    aboutUs = AboutUs.objects.all() # For about us's informations
    lkcActivity = LKCActivity.objects.all() # For LKC's Activities
    
    return render(request, 'index.html', {
        'bgImage': bgImage,
        'teachers1': teachers1,
        'teachers2': teachers2,
        'lkcDatas': lkcDatas,
        'aboutUs': aboutUs,
        'lkcActivity': lkcActivity
    })