from rest_framework import serializers
from django.contrib.auth import get_user_model, authenticate
from .service import AccountService
from rest_framework.validators import UniqueValidator

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'phone', 'role', 'createdAt', 'status']
        read_only_fields = ['id', 'createAt']

class RegisterSerializer(serializers.ModelSerializer):
    username = serializers.CharField(
        validators=[
            UniqueValidator(
                queryset=User.objects.all(),
                message="Username đã tồn tại."
            )
        ],
        error_messages= {
            'blank': 'Username không được để trống.',
            'required': 'Username là bắt buộc.'
        }
    )
    first_name = serializers.CharField(
        error_messages= {
            'blank': 'Họ và tên đệm không được để trống.',
            'required': 'Họ và tên đệm là bắt buộc.'
        }
    )
    last_name = serializers.CharField(
        error_messages= {
            'blank': 'Tên không được để trống.',
            'required': 'Tên là bắt buộc.'
        }
    )
    phone = serializers.CharField(
        max_length=10,
        validators=[
            UniqueValidator(
                queryset=User.objects.all(),
                message="Số điện thoại đã tồn tại."
            )
        ],
        error_messages= {
            'blank': 'Số điện thoại không được để trống.',
            'required': 'Số điện thoại là bắt buộc.',
            'max_length': 'Số điện thoại không được quá 10 số',
        }
    )
    email = serializers.CharField(
        validators=[
            UniqueValidator(
                queryset=User.objects.all(),
                message="Email đã tồn tại."
            )
        ],
        error_messages= {
            'blank': 'Email không được để trống.',
            'required': 'Email là bắt buộc.'
        }
    )
    password = serializers.CharField(
        write_only=True, 
        style={'input_type': 'password'},
        min_length=6,
        error_messages= {
            'min_length': 'Mật khẩu phải có ít nhất 6 ký tự.',
            'blank': 'Password không được để trống.',
            'required': 'Password là bắt buộc.'
        })

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'password', 'email', 'phone', 'role']
        
    def validate_phone(self, value):
        if not value.isdigit():
            raise serializers.ValidationError("Số điện thoại chỉ được chứa chữ số.")
        return value
    
    def validate_email(self, value):
        email = value.strip().lower()
        if '@' not in email or '.' not in email.split('@')[1]:
            raise serializers.ValidationError("Email phải có định dạng example@domain.com.")
        return email

    def create(self, validated_data):
        return AccountService.register(**validated_data)

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(
        required=True,
        write_only=True,
        error_messages={'blank': 'Username không được để trống.'}
    )
    password = serializers.CharField(
        write_only=True, 
        required=True, 
        style={'input_type': 'password'},
        error_messages={'black': 'Password không được để trống.'}
    )
    
    default_error_messages = {
        'invalid_credentials': 'Tài khoản hoặc mật khẩu không chính xác.'
    }

    def validate(self, data):
        user = authenticate(
            username=data.get('username'),
            password=data.get('password')
        )
        if not user:
            raise serializers.ValidationError({'detail': self.error_messages['invalid_credentials']})
        data['user'] = user
        return data


    

