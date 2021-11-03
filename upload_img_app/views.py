from django.shortcuts import render, redirect
from .forms import ImageForm
import dlib
from static.utils.alignment import align_face
import cv2

# 顔の切り出しの関数
def run_alignment(image_path, output_path):
        predictor = dlib.shape_predictor('static/shape_predictor_68_face_landmarks.dat')
        aligned_image = align_face(filepath=image_path, predictor=predictor) 
        return aligned_image.save(output_path)

def image_upload(request):
  if request.method == 'POST':
    form = ImageForm(request.POST, request.FILES)
    if form.is_valid():
      form.save()
    
      image_name  = request.FILES['image']
      image_name2  = request.FILES['image2']
      image_url = 'media/documents/{}'.format(image_name) 
      image_url2 = 'media/documents2/{}'.format(image_name2)

      #切り出した画像の保存場所
      align_url = 'media/align/align.jpg'
      align_url2 = 'media/align2/agign2.jpg'

      # 切り出しの実行
      align_image = run_alignment(image_url, align_url)
      align_image2 = run_alignment(image_url2, align_url2)

      return render(request, 'upload_img_app/image.html', {'align_url':align_url, 'align_url2':align_url2})
            

  else:
    form = ImageForm()
    return render(request, 'upload_img_app/index.html', {'form':form})


