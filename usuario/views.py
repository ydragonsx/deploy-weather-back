from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from django.contrib.auth import authenticate, get_user_model
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken

from .models import Usuario
from .serializers import UsuarioSerializer

User = get_user_model()


class UsuarioViewSet(ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

@api_view(["POST"])
@authentication_classes([])
@permission_classes([])
def login(request):
    username = request.data.get("username")
    password = request.data.get("password")
    print(username, password)

    if username is not None and password is not None:
        try:
            user = Usuario.objects.get(username=username)
        except User.DoesNotExist:
            user = None
            
    else:
        return Response(
            {"message": "Credenciais inválidas!"}, status='400'
        )

    print(user)

    if user is not None:

        response_data = {
            "username": user.username,
            "email": user.email,
            "id": user.id,
            "message": "Login realizado com sucesso!"
        }
        return Response(response_data, status='200')
    else:
        return Response(
            {"message": "Credenciais inválidas!"}, status='400'
        )
    
@api_view(['POST'])
def register(request):
    username = request.data.get('username')
    email = request.data.get('email')
    password = request.data.get('password')
    if not username or not password or not email:
        return Response({'error': 'Por favor adicione todos os dados.'}, status='400')
    user = User.objects.filter(username=username).first()
    if user:
        return Response({'error': 'Usuario ja cadastrado.'}, status='400')
    user = User.objects.filter(email=email).first()
    if user:
        return Response({'error': 'Email ja cadastrado.'}, status='400')

    user = User.objects.create(username=username)
    user.email = email
    user.set_password(password)
    user.save()

    data = {
        'user': user.username,
        'email': user.email,
        'id': user.id
    }
    return Response({'user': data, 'message': 'Usuario criado com sucesso.'}, status='201')