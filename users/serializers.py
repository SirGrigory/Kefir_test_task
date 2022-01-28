from rest_framework import serializers
from .models import CustomUser


class DetailedUserSerializer(serializers.ModelSerializer):
    extra_fields = (
        "city",
        "about",
        "is_superuser",
        "password",
    )

    def __init__(self, *args, **kwargs):
        private = kwargs.pop("private", True)
        super().__init__(*args, **kwargs)
        if not private:
            for field_name in self.extra_fields:
                self.fields.pop(field_name)

    def create(self, validated_data):
        password = validated_data.pop("password", None)
        user = self.Meta.model(**validated_data)
        if password is not None:
            user.set_password(password)
        user.save()
        return user

    class Meta:
        model = CustomUser
        exclude = (
            "last_login",
            "groups",
            "user_permissions",
        )
        extra_kwargs = {"password": {"write_only": True}}


class BasicUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = (
            "id",
            "first_name",
            "last_name",
            "email",
        )
