from rest_framework import serializers

from .models import User


class UserRegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={"input_type": "password"}, write_only=True)
    profile_photo_url = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['last_name', 'first_name', 'email', 'username', 'bio', 'profile_photo_url', 'password', 'password2']
        extra_kwargs = {
            'password': {'write_only': True},
            'username': {'read_only': True},

        }

    def generate_filename(self, username, image_extension):
        filename = f"{username.replace(':', '_').lower()}.{image_extension}"
        return filename

    def save(self, *args, **kwargs):
        email = self.validated_data['email']
        username = email.split('@')[0]
        user = User(
            email=email,
            username=username,
            first_name=self.validated_data['first_name'],
            last_name=self.validated_data['last_name'],
            profile_photo=self.validated_data.get('profile_photo', None),
            bio=self.validated_data.get('bio', ''),
        )

        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        if password != password2:
            raise serializers.ValidationError({'password': 'Passwords must match.'})

        user.set_password(password)
        user.save()
        return user


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['last_name', 'first_name', 'email', 'username', 'bio', 'profile_photo', 'password', 'password2']
        extra_kwargs = {
            'password': {'write_only': True},
            'username': {'read_only': True},
        }


class UserDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['last_name', 'first_name', 'email', 'username', 'bio', 'profile_photo', 'password', 'password2']
        extra_kwargs = {
            'password': {'write_only': True},
            'username': {'read_only': True},
        }
