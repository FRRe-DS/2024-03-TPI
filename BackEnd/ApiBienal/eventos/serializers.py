from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import *

class escultoresSerializer(serializers.ModelSerializer):
    class Meta:
        model= Escultores
        fields= ('id','nombre','apellido','fecha_nacimiento','nacionalidad','eventos_ganados', 'foto_perfil', 'instagram', 'facebook', 'twitter')
        read_only_fields= ('id',)

class eventosSerializer(serializers.ModelSerializer):
    class Meta:
        model= Eventos
        fields= ('id','nombre','fecha_inicio','fecha_final','lugar','descripcion','evento_en_transcurso', 'foto1', 'foto2')
        read_only_fields= ('id',)

    def get_evento_en_transcurso(self, obj):
        return obj.evento_en_transcurso()

class obrasSerializer(serializers.ModelSerializer):
    class Meta:
        model= Obras
        fields= ('id','titulo','fecha_creacion','descripcion','material','id_escultor','id_evento', 'foto1', 'foto2','votacion_en_transcurso')
        #read_only_fields= ('id', 'id_escultor', 'id_evento')

    def get_votacion_en_transcurso(self, obj):
        return obj.votacion_en_transcurso()

class userSerializer(serializers.ModelSerializer):
    class Meta:
        model= User 
        fields= ('id','username','first_name','last_name','email','password')
        extra_kwargs = {'password': {'write_only': True}}
        read_only_fields=('id',)

class usuariosSerializer(serializers.ModelSerializer):
    class Meta:
        model= UsuariosExtra
        fields = ('birthdate', 'country')
        read_only_fields=('id',)

class UsuariosCompleteSerializer(serializers.ModelSerializer):
    user = userSerializer()
    class Meta:
        model = UsuariosExtra
        fields = ['user', 'birthdate', 'country']

class UserRegisterSerializer(serializers.Serializer):
    user = userSerializer()
    user_extra = usuariosSerializer()

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user_extra_data = validated_data.pop('user_extra')

        user = User.objects.create_user(**user_data)
        user_extra = UsuariosExtra.objects.create(user=user, **user_extra_data)
        return user

class UserProfileSerializer(serializers.Serializer):
    user = userSerializer()
    user_extra = usuariosSerializer()

    def update(self, instance, validated_data):
        user_data = validated_data.pop('user')
        user_extra_data = validated_data.pop('user_extra')

        # Actualizar el usuario
        user = instance['user']
        update_fields = []
        for attr, value in user_data.items():
            if attr != 'username':  # No actualizar el username
                setattr(user, attr, value)
                update_fields.append(attr)
        user.save(update_fields=update_fields)

        # Actualizar la información extra del usuario
        user_extra = instance['user_extra']
        for attr, value in user_extra_data.items():
            setattr(user_extra, attr, value)
        user_extra.save()

        return instance
    
class votacionesSerializer(serializers.ModelSerializer):
    class Meta:
        model= Votaciones
        fields= ('id','puntuacion','id_usuario','id_obra')
        #read_only_fields=('id','id_usuario','id_obra')

class loginSerializer(serializers.Serializer):
    email = serializers.EmailField(required=False, allow_blank=True)
    username = serializers.CharField(required=False, allow_blank=True)
    password = serializers.CharField(required=True, write_only=True)

    def validate(self, data):
        email = data.get('email')
        username = data.get('username')
        password = data.get('password')

        # Asegúrate de que al menos uno de los dos campos (email o username) sea provisto
        if not email and not username:
            raise serializers.ValidationError("Debe proporcionar al menos el correo electrónico o el nombre de usuario.")

        # Utiliza authenticate para verificar las credenciales
        user = authenticate(
            request=self.context.get('request'),
            email=email,
            username=username,
            password=password
        )

        # Si la autenticación falla, levantamos una excepción
        if not user:
            raise serializers.ValidationError("Credenciales inválidas.")

        # Si la autenticación es exitosa, retornamos los datos del usuario
        data['user'] = user

        return data
    
class VotosUserSerializer(serializers.Serializer):
    id_voto= serializers.IntegerField()
    id_obra = serializers.IntegerField()
    titulo_obra = serializers.CharField(max_length=100)
    puntuacion = serializers.IntegerField()
    id_evento = serializers.IntegerField()
    nombre_evento = serializers.CharField(max_length=100)
    id_usuario = serializers.IntegerField()
    nombre_escultor = serializers.CharField(max_length=50)
    apellido_escultor = serializers.CharField(max_length=100)


class PasswordResetRequestSerializer(serializers.Serializer):
    email = serializers.EmailField()

    def validate_email(self, value):
        if not User.objects.filter(email=value).exists():
            raise serializers.ValidationError("No user is associated with this email address.")
        return value
    

class PasswordResetSerializer(serializers.Serializer):
    token = serializers.CharField()
    new_password = serializers.CharField()

    def validate_token(self, value):
        if not User.objects.filter(profile__password_reset_token=value).exists():
            raise serializers.ValidationError("Invalid or expired token.")
        return value

    def validate_new_password(self, value):
        # agregar validaciones adicionales para la nueva contraseña aquí
        return value