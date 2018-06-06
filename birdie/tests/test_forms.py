import pytest

from .. import forms


pytestmark = pytest.mark.django_db


class TestPostForm:
    def test_form(self):
        form = forms.PostForm(data={})
        assert False == form.is_valid(), "Should be invalid if no data is given"

        form = forms.PostForm(data={"body": "Hello"})
        assert False == form.is_valid(), "Should be invalid if too short"
        assert "body" in form.errors, "Should have body field error"

        form = forms.PostForm(data={"body": "Hello World!!!"})
        assert True == form.is_valid(), "Should be valid if long enough"
