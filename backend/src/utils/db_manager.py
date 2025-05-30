from backend.src.CRUD.tasks import TasksCRUD


# Асинхронный контекстный менеджер для управления сессиями базы данных
# Создает новую сессию с БД и инициализирует репозитории для работы с ними
class DBManager:
    def __init__(self, session_factory):
        self.session_factory = session_factory

    # Создается новая сессия и инициализируются классы для работы с данными,
    # которые будут работать с помощью этой сессии
    async def __aenter__(self):
        self.session = self.session_factory()

        self.tasks = TasksCRUD(self.session)

        return self

    # Происходит откат изменений и закрытие сессии, для избежания
    # утечек ресурсов и гарантирии, что сессия будет корректно завершена
    async def __aexit__(self, *args):
        await self.session.rollback()
        await self.session.close()

    # Коммит для фиксации и сохранения изменений в БД
    async def commit(self):
        await self.session.commit()
