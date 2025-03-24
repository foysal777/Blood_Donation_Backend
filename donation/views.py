from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
import cloudinary.uploader
from .models import Donor
from .serializers import DonorSerializer

class DonorListCreateView(generics.ListCreateAPIView):
    queryset = Donor.objects.all()
    serializer_class = DonorSerializer

    def create(self, request, *args, **kwargs):
        #  Handle Multiple Blood Groups: Only take one value for blood_group
        blood_groups = request.data.get('blood_group', [])  #  Use .get() for dictionary data

        # If blood_group is a list, take the first element
        if isinstance(blood_groups, list) and blood_groups:
            request.data['blood_group'] = blood_groups[0]  #  Only store the first blood group
        elif isinstance(blood_groups, str):
            # If it's just a single string, use it directly
            request.data['blood_group'] = blood_groups

        #  Cloudinary Image Upload
        image_file = request.FILES.get('image')
        if image_file:
            try:
                upload_result = cloudinary.uploader.upload(image_file)
                request.data['image'] = upload_result['secure_url']  #  Cloudinary Image URL Store
            except Exception as e:
                return Response({"error": f"Cloudinary upload failed: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        #  Data Validation & Save
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "✅ রক্তদাতা সফলভাবে যোগ করা হয়েছে!", "data": serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DonorDeleteView(generics.DestroyAPIView):
    queryset = Donor.objects.all()
    serializer_class = DonorSerializer
