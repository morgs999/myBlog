# tests/blog/models/test_post.py

from model_bakery import baker
import pytest
from blog.models import Post
import datetime as dt
from freezegun import freeze_time

pytestmark = pytest.mark.django_db

def test_published_posts_only_returns_those_with_published_status():
    # Create a published Post by setting the status to "published"
    published = baker.make('blog.Post', status=Post.PUBLISHED)
    # Create a draft Post
    baker.make('blog.Post', status=Post.DRAFT)

    # We expect only the "published" object to be returned
    expected = [published]
    # Cast the result as a list so we can compare apples with apples!
    # Lists and querysets are of different types.
    result = list(Post.objects.published())

    assert result == expected

def test_publish_sets_status_to_published():
    post = baker.make('blog.Post', status=Post.DRAFT)
    post.publish()
    assert post.status == Post.PUBLISHED

@freeze_time(dt.datetime(2030, 6, 1, 12), tz_offset=0)
def test_publish_sets_published_to_current_datetime():
    # Create a new post, and ensure no published datetime is set
    post = baker.make('blog.Post', published=None)
    post.publish()

    # Set the timezone to UTC (to match tz_offset=0)
    assert post.published == dt.datetime(2030, 6, 1, 12, tzinfo=dt.timezone.utc)

def test_draft_posts_only_returns_those_with_draft_status():
    draft = baker.make('blog.Post', status=Post.DRAFT)

    baker.make('blog.Post', status=Post.PUBLISHED)

    expected = [draft]

    result = list(Post.objects.draft())

    assert result == expected