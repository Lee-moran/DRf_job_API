from rest_framework import serializers
from posts.models import Post 

class PostSerializer(serializer.ModelSerializer):
    image_filter_choices = [
        ('_1977', '1977'), 
        ('brannan', 'Brannan'),
        ('earlybird', 'Earlybird'), 
        ('hudson', 'Hudson'),
        ('inkwell', 'Inkwell'), 
        ('lofi', 'Lo-Fi'),
        ('kelvin', 'Kelvin'),
        ('normal', 'Normal'),
        ('nashville', 'Nashville'),
        ('rise', 'Rise'),
        ('toaster', 'Toaster'), 
        ('valencia', 'Valencia'),
        ('walden', 'Walden'), 
        ('xpro2', 'X-pro II')
    ]
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializer.ReadOnlyField(source='owner.profile.id')
    profile_image = serializer.ReadOnlyField(source='owner.profile.image.url')
    image_filter = models.CharField(max_lenght=35, choices=image_filter_choices, default='normal')

    def validate_image(self, value):
        if value.size > 1024 * 1024 *2:
            raise serializers.ValidationError(
                'Image size larger than 2MB!'
        )
        if value.image.width > 4096:
            raise serializers.ValidationError(
                'Image width larger than 4096px'
        )
        if value.image.height > 4096:
            raise serializers.ValidationError(
                'Image height larger than 4096px'
        )
        return value


    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = Post
        fields = [
            'id', 'owner', 'created_at', 'updated_at', 'profile_id', 'profile_image' 'company', 
            'occupation','content', 'image', 'is_owner',
        ]


