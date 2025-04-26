from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializer import CategorySerializer
from .service import CategoryService
from rest_framework.exceptions import ValidationError
from accounts.permissions import IsAdminUserRole

class CategoryList(APIView):
    def get(self, request):
        try:
            cats = CategoryService.list_categories()
            if not cats.exists():
                return Response(
                    {"message": "Không có danh mục nào."},
                    status=status.HTTP_404_NOT_FOUND
                )
            serializer = CategorySerializer(cats, many=True)
            return Response(serializer.data)
        except Exception as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
  
    
class CategoryById(APIView):
    def get(self, request, pk):
        try:
            cat = CategoryService.get_by_id_category(pk)
            serializer = CategorySerializer(cat).data
            return Response(serializer)
        except Exception as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
            
            
class CategoryCreate(APIView):
    permission_classes = [IsAdminUserRole]
    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        cat = CategoryService.create_category(serializer.validated_data)
        return Response(CategorySerializer(cat).data, status=status.HTTP_201_CREATED)
    
class CategoryDelete(APIView):
    def delete(self, request, pk):
        try:
            CategoryService.delete_category(pk)
            return Response({"message": "Đã xóa thành công"}, status=status.HTTP_200_OK)
        except ValidationError as ve:
            return Response(ve.detail, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)  
    
    