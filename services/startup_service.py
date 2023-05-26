from models.startup_model import Startup
from fastapi import Depends
from typing import Optional, List
from schemas.startup_schema import StartupSchema
from repositories.startup_repository import StartupRepository   


class StartupService:
    startup_repository: StartupRepository

    def __init__(
        self, startup_repository: StartupRepository = Depends()
    ) -> None:
        self.startup_repository = startup_repository

    def list(
        self, 
        page_size: Optional[int] = 100,
        start_index: Optional[int] = 0,
    ) -> List[Startup]:
        return self.startup_repository.list(
            page_size, start_index
        )
    
    def create(self, startup: StartupSchema) -> Startup:
        return self.startup_repository.create(
            Startup(
                id = startup.id,
                name = startup.name,
                id_aplication = startup.id_aplication,
            )
        )
    
    def delete(self, id: int) -> None:
        return self.startup_repository.delete(Startup(id=id))
    
    def update(self, startup: StartupSchema) -> Startup:
        return self.startup_repository.update(
            Startup(
                id = startup.id,
                name = startup.name,
                id_aplication = startup.id_aplication,
            )
        )