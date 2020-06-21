from .base import BaseTestCase
from ..models import Puppy


class PuppyTestCase(BaseTestCase):

    def test_dummy_puppies_are_created(self):
        self.assertEqual(Puppy.objects.count(), 2)
        self.assertEqual(self.rambo.breed, 'Gradane')
        self.assertEqual(self.ricky.colour, 'Black')
