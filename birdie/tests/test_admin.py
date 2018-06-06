import pytest
from mixer.backend.django import mixer

from django.contrib.admin.sites import AdminSite

from .. import models
from .. import admin

pytestmark = pytest.mark.django_db

class TestPostAdmin:
    def test_excerpt(self):
        site = AdminSite()
        post_admin = admin.PostAdmin(models.Post, site)

        obj = mixer.blend("birdie.Post", body="Hello World!")
        result = post_admin.excerpt(obj)
        assert "Hello" == result, "Should return first few characters"

