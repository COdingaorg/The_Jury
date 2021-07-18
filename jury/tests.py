from django.db.models.query_utils import refs_expression
from django.test import TestCase
from .models import User

# Create your tests here.
class TestUser(TestCase):
  '''
  test case to test user methods, create user, delete user, Get user
  '''
  def setUp(self):
      self.new_user = User(username = 'Alfred', first_name = 'Alfred', last_name = 'Tito', email = 'tito@gmail.com')

  def testinstance(self):
    self.assertTrue(isinstance(self.new_user, User))

  def testSaveuser(self):
    self.new_user.save()
    users = User.objects.all()

    self.assertTrue(len(users)> 0)

  def testdeleteuser(self):
    self.new_user.save()
    self.new_user.delete()
    users = User.objects.all()

    self.assertTrue(len(users)== 0)

  def testgetuser(self):
    self.new_user.save()
    user = User.objects.get(username = 'Alfred') 

    self.assertTrue(user.username == 'Alfred')
    