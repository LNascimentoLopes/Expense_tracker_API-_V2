from dependencies import engine
from base import Base
import models

Base.metadata.create_all(bind=engine)