from django.test import TestCase
from .models import User

# Create your tests here.
class TestUser(TestCase):
  '''
  test case to test user methods, create user, delete user, update user, Get user
  '''
  def setUp(self):
      self.new_user = User(username = 'Alfred', first_name = 'Alfred', last_name = 'Tito', email = 'tito@gmail.com')

  def testinstance(self):
    self.assertTrue(isinstance(self.new_user, User))
