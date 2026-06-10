from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls,user):
        token=super().get_token(user)
        
        token['id']=user.id
        token['username']=user.username
        token['email']=user.email
        token['role']=user.role

        return token

    
    def validate(self,attrs):
        data=super().validate(attrs)

        data['users']={
            'id':self.user.id,
            'username':self.user.username,
            'email':self.user.email,
            'role':self.user.role,
        }
        
        return data