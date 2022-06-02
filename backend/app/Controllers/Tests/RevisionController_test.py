from Models import RevisionModel, PostModel
from sqlalchemy.orm import Session


def test_create_revision(client, current_active_user, db: Session):
    post = PostModel("jhdfjskhdf", "jhfkjdshdfkh", user=current_active_user)
    revision = RevisionModel("gsdugfsd", post)
    db.add(revision)
    db.commit()

    data = {
        "files": ""

    }
    response = client.post("/users/1/posts/1/revisions/1/files")
    assert response.status_code == 201


def test_create_revision_without_files(client):
    data = {
        "files": []
    }
    response = client.post("/users/1/posts/1/revisions/1/files")
    assert response.status_code == 400

