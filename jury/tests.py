from django.db.models.query_utils import refs_expression
from django.test import TestCase
from .models import User, UserProfile, UserProject

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

class TestUserProject(TestCase):
  '''
  Test class to test UserProject methods, save project, search project, update project description and delete project
  '''
  def setUp(self):
    self.new_user2 = User(1, 'pbkdf2_sha256$260000$kn87lW6tFCXEy2JheYcbc3$zL3x4Qtck9cBeeqnluf75qz7QTY0rDu6bwxzAVJXDFk=', '2021-07-17 22:15:26.357756+03',False,'alfred007','alfred', 'kiko','kiko@gmail.com',False,True,'2021-07-17 21:44:53.340108+03' )
    self.new_user2.save()

    self.new_project = UserProject(1, 'image.png', 'Sauti sol website', 'codinga@sautisol.org', 'A website ...', 1)

  def test_instance_creation(self):
    self.assertTrue(isinstance(self.new_project, UserProject))

  def test_save_project(self):
    self.new_project.save_project()
    projects = UserProject.objects.all()

    self.assertTrue(len(projects)>0)

  def test_search_project(self):
    self.new_project.save_project()
    projects = UserProject.search_project('sauti')

    self.assertTrue(len(projects)>0)

  def test_update_proj_desc(self):
    self.new_project.save_project()
    new_desc = 'An online application'
    UserProject.update_description(1, new_desc)
    UserProject.objects.get(pk = 1).refresh_from_db()

    self.assertTrue((UserProject.objects.get(pk = 1)).project_description == new_desc)

  def test_delete_project(self):
    self.new_project.save_project()
    UserProject.delete_project(1)
    projects = UserProject.objects.all()

    self.assertTrue(len(projects)==0)

class TestUserProfile(TestCase):
  '''
  Test class to test UserProfile methods, save profile, get single profile, update profile bio and delete profile
  '''
  def setUp(self):
    self.new_user2 = User(1, 'pbkdf2_sha256$260000$kn87lW6tFCXEy2JheYcbc3$zL3x4Qtck9cBeeqnluf75qz7QTY0rDu6bwxzAVJXDFk=', '2021-07-17 22:15:26.357756+03',False,'alfred007','alfred', 'kiko','kiko@gmail.com',False,True,'2021-07-17 21:44:53.340108+03' )
    self.new_user2.save()

    self.new_project = UserProject(1, 'image.png', 'Sauti sol website', 'codinga@sautisol.org', 'A website ...', 1)
    self.new_project.save_project()

    self.new_profile= UserProfile(1, 'image.png', 'Live, love laugh', '@Alfred', '@Alfred', '@Alfred',1,1)
    
  def test_instance_creation(self):
    self.assertTrue(isinstance(self.new_profile, UserProfile))

  def test_save_profile(self):
    self.new_profile.save_profile()
    profile = UserProfile.objects.all()

    self.assertEqual(len(profile), 1)

  def test_get_user_profile(self):
    self.new_profile.save_profile()
    usernm = 'alfred007'
    user_found = UserProfile.get_user_profile(usernm).user.username

    self.assertEqual(user_found, usernm)
    