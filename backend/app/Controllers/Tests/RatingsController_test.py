from Models import RatingModel
from sqlalchemy.orm import Session


def test_get_ratings(client, db: Session):
    rating1 = RatingModel('lakasdf', 'lkjahsdf', 'lkajsdhflkjashdf')
    rating2 = RatingModel('lakasdfasdf', 'lkjahsdfasdf',
                          'lkajsdhflkjashdasdff')

    db.add_all([rating1, rating2])
    db.commit()

    response = client.get('/ratings')
    json = response.json()
    assert response.status_code == 200
    assert len(json) == 2
    assert json[0]['title'] == rating1.title
    assert json[0]['short_description'] == rating1.short_description
    assert json[0]['description'] == rating1.description
    assert json[0]['id'] is not None
    assert json[0]['time_created'] is not None
    assert json[0]['time_updated'] is not None
    assert json[1]['title'] == rating2.title
    assert json[1]['short_description'] == rating2.short_description
    assert json[1]['description'] == rating2.description
    assert json[1]['id'] is not None
    assert json[1]['time_created'] is not None
    assert json[1]['time_updated'] is not None


def test_create_rating(client):
    rating = {
        "title": "strsdfing",
        "short_description": "strasdgasdfing",
        "description": "strinasdfkajshdgfg"
    }

    response = client.post('/ratings', json=rating)
    json = response.json()

    assert response.status_code == 201
    assert json['title'] == rating['title']
    assert json['description'] == rating['description']
    assert json['short_description'] == rating['short_description']
    assert json['time_created'] is not None
    assert json['time_updated'] is not None
    assert json['id'] is not None


def test_create_faulty_rating(client):
    rating = {
        "asdf": "strsdfing",
        "short_description": "strasdgasdfing",
        "description": "strinasdfkajshdgfg"
    }

    response = client.post('/ratings', json=rating)

    assert response.status_code == 422


def test_patch_rating(client, db):
    new_rating_json = {
        "title": "test",
        "short_description": "testshort",
        "description": "testdesc",
    }
    new_aspect = RatingModel(**new_rating_json)
    new_aspect.save_self(db)

    data = {
        "title": "test2"
    }

    response = client.patch("/ratings/1", json=data)
    assert response.status_code == 200
