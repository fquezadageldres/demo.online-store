from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, JsonResponse
from django.views.generic import View
import json


# Create your views here.
class P003(View):
    template_name = 'p003.html'

    def get(self, request, *args, **kwargs):
            return render(request, self.template_name)


    def p003Predict(request, *args, **kwargs):
        if request.method == 'POST' and request.FILES['file']:
            if request.is_ajax():
                myfile = request.FILES['file']
                fs = FileSystemStorage()
                filename = fs.save(myfile.name, myfile)
                uploaded_file_url = fs.url(filename)

                import numpy as np
                import os
                from tensorflow.keras.preprocessing import image
                from tensorflow.keras.models import load_model

                model = load_model('static/models/model_p003_3classes.h5')

                image_ = myfile.name

                image_ = image.load_img(image_, target_size=(128, 128))
                image_ = np.expand_dims(image_, axis=0)
                image_ = image_/255

                result = model.predict(image_)

                cat = float("%.1f" % (result[0][0]*100))
                dog = float("%.1f" % (result[0][1]*100))
                other = float("%.1f" % (result[0][2]*100))

                var = [cat,dog,other]

                if np.argmax(var) == 0:
                    msg = "Creo un " + str(cat) + "% que es un Gato!"
                elif np.argmax(var) == 1:
                    msg = "Creo un " + str(dog) + "% que es un Perro!"
                elif np.argmax(var) == 2:
                    msg = "Un momento... eso no es ni un gato ni un perro!"

                os.remove(filename)

                data = {'cat':cat, 'dog':dog, 'other':other, 'msg':msg}
                return JsonResponse(data)