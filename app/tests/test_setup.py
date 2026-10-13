from datetime import datetime
from zoneinfo import ZoneInfo

import pytest
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient


def test_api_responds():
    response = APIClient().get("/api/ping/")
    assert response.status_code == 200
    assert response.data["status"] == "ok"


@pytest.mark.django_db
def test_database_works():
    get_user_model().objects.create_user("someone", password="secret")
    assert get_user_model().objects.count() == 1


def test_timezone_data_available():
    # On Windows this needs the tzdata package, which the lockfile installs.
    summer = datetime(2026, 7, 1, 12, tzinfo=ZoneInfo("Europe/Amsterdam"))
    assert summer.utcoffset().total_seconds() == 2 * 3600
