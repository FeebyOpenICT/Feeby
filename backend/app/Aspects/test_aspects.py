import pytest

from Models.Rating import RatingModel
from Models.Aspect import AspectModel


def test_create_aspect(client, db):
    rating = RatingModel('sdjkfh', 'askdjfh', 'sdf')
    rating.save_self(db)

    data = {
        "title": "test",
        "short_description": "testshort",
        "description": "testdesc",
        "external_url": "testurl",
        "rating_ids": [rating.id]
    }
    response = client.post("/aspects/", json=data)
    assert response.status_code == 201
    assert response.json()['title'] == "test"
    assert response.json()['short_description'] == "testshort"
    assert response.json()['description'] == "testdesc"
    assert response.json()['external_url'] == "testurl"
    assert response.json()['ratings'][0]['id'] == rating.id
    assert response.json()['ratings'][0]['title'] == rating.title
    assert response.json()['ratings'][0]['description'] == rating.description
    assert response.json()[
        'ratings'][0]['short_description'] == rating.short_description


def test_create_aspect_without_ratings(client):
    data = {
        "title": "test",
        "short_description": "testshort",
        "description": "testdesc",
        "external_url": "testurl",
        "rating_ids": []
    }
    response = client.post("/aspects/", json=data)
    assert response.status_code == 422


def test_empty_get_aspect(client):
    response = client.get("/aspects/")
    assert response.status_code == 200
    assert response.json() == []


def test_patch_aspect_without_ratings(client, db):
    rating = RatingModel('sdjkfh', 'askdjfh', 'sdf')
    new_aspect_json = {
        "title": "test",
        "short_description": "testshort",
        "description": "testdesc",
        "external_url": "testurl",
        "ratings": [rating.id]
    }
    new_aspect = AspectModel(**new_aspect_json)
    new_aspect.save_self(db)

    data = {
        "title": "test2",
        "rating_ids": []
    }

    response = client.patch("/aspects/1", json=data)
    assert response.status_code == 422
    assert response.json()['title'] == "test"
    assert response.json()['rating_ids'] == []

