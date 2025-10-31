from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.db.models import Sum, Q, Count
from blog.models import Comment, Post, Topic

User = get_user_model()

def question_0_return_most_recent_post():
    """
    Returns the most recently published post object
    """
    return Post.objects.all().order_by('-published').first()

def question_1_return_active_users():
    """
    Return the results of a query which returns a list of all
    active users in the database.
    """
    return User.objects.filter(is_active=True)

def question_2_return_regular_users():
    """
    Return the results of a query which returns a list of users that
    are *not* staff and *not* superusers
    """
    return User.objects.filter(is_staff=False, is_superuser=False)

def question_3_return_all_posts_for_user(user):
    """
    Return all the Posts authored by the user provided. Posts should
    be returned in reverse chronological order from when they
    were created.
    """
    return Post.objects.filter(author=User.objects.get(username=user)).order_by('-created')

def question_4_return_all_posts_ordered_by_title():
    """
    Return all Post objects, ordered by their title.
    """
    return Post.objects.order_by('title')

def question_5_return_all_post_comments(post):
    """
    Return all the comments made for the post provided in order
    of last created.
    """
    return Comment.objects.filter(post=post).order_by('-created')

def question_6_return_the_post_with_the_most_comments():
    """
    Return the Post object containing the most comments in
    the database. Do not concern yourself with approval status;
    return the object which has generated the most activity.
    """
    return Post.objects.annotate(num=Count('comments')).order_by('-num')

def question_7_create_a_comment(post):
    """
    Create and return a comment for the post object provided.
    """
    return Comment.objects.create(post=post)

def question_8_set_approved_to_false(comment):
    """
    Update the comment record provided and set approved=False
    """
    return Comment.objects.filter(comment=comment).update(approved=False).save()

def question_9_delete_post_and_all_related_comments(post):
    """
    Delete the post object provided, and all related comments.
    """
    return Post.objects.filter(post=post).delete()
