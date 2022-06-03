from Models import RevisionModel, PostModel
from sqlalchemy.orm import Session
import tempfile


def test_create_files_for_revision(client, current_active_user, db: Session):
    post = PostModel("jhdfjskhdf", "jhfkjdshdfkh", user=current_active_user)
    revision = RevisionModel("gsdugfsd", post)
    db.add(revision)
    db.commit()
    file = tempfile.TemporaryFile()
    data = {
        "files": [file]
    }
    response = client.post("/users/1/posts/1/revisions/1/files", json=data)
    assert response.status_code == 201
    assert response.json()['files'] == file
    file.close()
