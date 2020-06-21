from .base import BaseTestCase
from ..models import Puppy


class PuppiesTestCase(BaseTestCase):

    def test_unauthorized_user_cannot_get_puppies(self):
        response = self.client.get('/puppies/')
        self.assertEqual(response.status_code, 401)

    def test_unauthorized_user_cannot_get_single_puppy(self):
        response = self.client.get(f'/puppies/{self.ricky.pk}/')
        self.assertEqual(response.status_code, 401)

    def test_unauthorized_user_cannot_create_puppies(self):
        response = self.client.post('/puppies/')
        self.assertEqual(response.status_code, 401)

    def test_unauthorized_user_cannot_update_an_existing_puppy(self):
        response = self.client.put(f'/puppies/{self.rambo.pk}/', {
            "breed": "Chihuahua"
        })
        self.assertEqual(response.status_code, 401)

    def test_unauthorized_user_cannot_delete_an_existing_puppy(self):
        response = self.client.delete(f'/puppies/{self.ricky.pk}/')
        self.assertEqual(response.status_code, 401)

    def test_authorized_user_can_get_all_puppies(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)
        response = self.client.get('/puppies/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Puppy.objects.count(), 2)

    def test_authorized_user_can_get_one_puppy(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)
        response = self.client.get(f'/puppies/{self.ricky.id}/')
        self.assertEqual(response.status_code, 200)

    def test_authorized_user_cannot_get_nonexistent_puppy(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)
        response = self.client.get('/puppies/4/')
        self.assertEqual(response.status_code, 404)

    def test_authorized_user_can_create_new_puppy(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)
        self.new_puppy = {
            'name': 'Her',
            'age': 3,
            'breed': 'Lhasa',
            'colour': 'Black'
        }
        response = self.client.post('/puppies/', self.new_puppy)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Puppy.objects.count(), 3)

    def test_authorized_user_cannot_create_an_invalid_puppy(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)
        self.invalid_puppy = {
            "name": "",
            "age": 1,
            "breed": "Lab",
            "colour": "Black"
        }
        response = self.client.post('/puppies/', self.invalid_puppy)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(Puppy.objects.count(), 2)

    def test_authorized_user_can_update_valid_puppy(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)
        response = self.client.put(f'/puppies/{self.ricky.pk}/', {
            "breed": "Chihuahua"
        })
        updated_puppy = Puppy.objects.get(pk=self.ricky.pk)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(updated_puppy.breed, "Chihuahua")

    def test_delete_valid_single_puppy(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)
        response = self.client.delete(f'/puppies/{self.ricky.pk}/')
        self.assertEqual(response.status_code, 204)

    def test_delete_invalid_single_puppy(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)
        response = self.client.delete('/puppies/10/')
        self.assertEqual(response.status_code, 404)
