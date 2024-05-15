from fastapi import HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from conexionbd import SessionLocal
from src.models.noticiamodel import get_noticias as get_noticias_db, get_noticia as get_noticia_db
from src.models.noticiamodel import eliminar_noticia as eliminar_noticia_db
from src.models.schemas import NoticiaDelete, NoticiaSchema
from src.models.noticiamodel import eliminar_noticia

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.delete("/noticias/{noticia_id}")
def delete_noticia(noticia_id: int, db: Session = Depends(get_db)):
    """Deletes a noticia from the database by its ID.

    Args:
        noticia_id: ID of the noticia to be deleted.
        db: SQLAlchemy session object.

    Returns:
        JSON response with a success message or error details.
    """

    success = eliminar_noticia(db, noticia_id)
    if not success:
        raise HTTPException(status_code=404, detail="Noticia no encontrada")
    return {"message": "Noticia eliminada correctamente"}

@router.get("/noticias/", response_model=list[NoticiaSchema])
def read_noticias(db: Session = Depends(get_db)):
    return get_noticias_db(db)

@router.get("/noticias/{noticia_id}", response_model=NoticiaSchema)
def read_publicacion(noticia_id: int, db: Session = Depends(get_db)):
    db_noticia = get_noticia_db(db, noticia_id)
    if db_noticia is None:
        raise HTTPException(status_code=404, detail="Publicación no encontrada")
    return db_noticia
