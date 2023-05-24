from sqlalchemy.orm import Session
from unittest import TestCase
from unittest.mock import create_autospec, patch
from repositories.card_repository import CardRepository


class TestCardRepository(TestCase):
    session : Session
    card_repository : CardRepository


    def setUp(self) -> None:
        super().setUp()
        self.session = create_autospec(Session)
        self.card_repository = CardRepository(
            self.session
        )
    
    @patch("models.card_model.Card", autospec=True)
    def test_create(self, Card):
        name = Card(name="Jose")
        self.card_repository.create(name)
        self.session.add.assert_called_once_with(name)


    @patch("models.card_model.Card", autospec=True)
    def test_delete(self, Card):
        _id = Card(id=9)
        self.card_repository.delete(_id)
        self.session.delete.assert_called_once_with(_id)  
        

    
