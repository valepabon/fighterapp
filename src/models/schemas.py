from pydantic import BaseModel
from datetime import date

#Actúa como una clase base,reduciendo la duplicación 
#de código y asegurando que los campos comunes estén centralizados.
class NoticiaBase(BaseModel):
    titulo: str
    cuerpo: str
    archivo: str
    fecha: date

#Extiende NoticiaBase y añade campos específicos necesarios solo para la creación.
class NoticiaCreate(NoticiaBase):
    id_noticia: int

# Extiende NoticiaBase y añade campos necesarios para la respuesta de la API,
# junto con configuraciones específicas para la interoperabilidad con SQLAlchemy.
class NoticiaSchema(NoticiaBase):
    id_noticia: int

    class Config:
        orm_mode = True

