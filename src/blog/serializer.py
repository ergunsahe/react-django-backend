# from django.db.models import fields
from django.db.models import fields
from rest_framework import  serializers
from .models import Post, Comment, Like, PostView


class CommentSerializer(serializers.ModelSerializer):
    user = serializers.CharField( source="user.username", read_only=True)
    
    class Meta:
        model = Comment
        fields = ( "content",  "user", "time")
        read_only_fields = ["post","time", "user"]
        
class PostSerializer(serializers.ModelSerializer):
    author = serializers.CharField( source="author.username", read_only=True)
    class Meta:
        model = Post
        fields=(
            'id',
            'title',
            'image',
            'publish_date',
            'update_date',
            'content',
            'status',
            'author',
            'comment_count',
            'view_count',
            'like_count',
            'slug',
           
        )
        read_only_fields = ["id","publish_date", "author", 'comment_count', 'view_count', 'like_count', 'slug']
class PostDetailSerializer(serializers.ModelSerializer):
    author = serializers.CharField( source="author.username", read_only=True)
    comments = CommentSerializer(many= True)
    class Meta:
        model = Post
        fields=(
            'id',
            'title',
            'image',
            'publish_date',
            'update_date',
            'content',
            'author',
            'status',
            'comment_count',
            'view_count',
            'like_count',
            'slug',
            'comments'
        )
        read_only_fields = ["id","publish_date", "author", 'comment_count', 'view_count', 'like_count', 'slug', 'comments']
        
class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ("user", "post")
        
class PostViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostView
        fields = ("user", "post", "time")
        





        