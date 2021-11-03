from django.shortcuts import render, redirect
from .forms import ImageForm
import dlib
from static.utils.alignment import align_face
import os


def run_alignment(image_path):
        # import dlib
        # from static.utils.alignment import align_face
        predictor = dlib.shape_predictor('static/shape_predictor_68_face_landmarks.dat')
        aligned_image = align_face(filepath=image_path, predictor=predictor) 
        return aligned_image


def image_upload(request):
  if request.method == 'POST':
    form = ImageForm(request.POST, request.FILES)
    if form.is_valid():
      form.save()
      image_name  = request.FILES['image']
      image_name2  = request.FILES['image2']
      image_url = 'media/documents/{}'.format(image_name)
      image_url2 = 'media/documents2/{}'.format(image_name2)
      
      align_image = run_alignment(image_url)
      align_image2 = run_alignment(image_url2)
      # align_image.resize((256,256))
      # align_image2.resize((256,256)
      align_image.save()

      align_url = 'media/align/{}'.format(align_image)
      align_url2 = 'media/align2/{}'.format(align_image2)

      return render(request, 'upload_img_app/image.html', {'align_url':align_url, 'align_url2':align_url2})
            

  else:
    form = ImageForm()
    return render(request, 'upload_img_app/index.html', {'form':form})
