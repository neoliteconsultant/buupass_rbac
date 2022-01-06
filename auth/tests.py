
from django.test import TestCase

from django.contrib.auth.models import User
from .models import User, SubUser
from .status_code import HTTP_201_CREATED, HTTP_200_OK


class TestRBAC(TestCase):

    @classmethod
    def setUpClass(cls):
        user = User()
        user.username = 'lewism'
        user.first_name= 'Lewis'
        user.last_name = 'Markus'
        user.email =  'lewis@buupass.com'
        user.password =  'TOm!Z&6lsw8'
        user.save()

        sub_user = SubUser()
        sub_user.user = user
        sub_user.username = "nexusva"
        sub_user.first_name = "Nexus"
        sub_user.last_name = "Vanguard"
        sub_user.password = "QuP8L0ri!to"
        sub_user.email = "nexus.vanguard@gmail.com"
        sub_user.save()


    def test_user_creation(self):
        data = {'username':'tonys','first_name': 'Tony', 'last_name': 'Sonia', 'email':'tonys@gmail.com','password':'P*LpH3wrUd9'}
        response = self.client.post('/v1/auth/users', data)
        json_output = response.json()

        self.assertEqual(response.status_code, HTTP_201_CREATED)
        self.assertEqual(json_output['username'], 'tonys')
        self.assertEqual(json_output['first_name'],'Tony')
        self.assertEqual(json_output['last_name'], 'Sonia')
        self.assertEqual(json_output['email'], 'tonys@gmail.com')

    def test_subuser_creation(self):
        data = {'user':self.user.id, 'username':'maxwellk','first_name': 'Maxwell', 'last_name': 'Kaxuri', 'email':'maxwell.kaxuri@gmail.com','password':'s=Eju8?iWIt'}
        response = self.client.post('/v1/auth/users/subusers', data)
        json_output = response.json()

        self.assertEqual(response.status_code, HTTP_201_CREATED)
        self.assertEqual(json_output['username'], 'maxwellk')
        self.assertEqual(json_output['first_name'],'Maxwell')
        self.assertEqual(json_output['last_name'], 'Kaxuri')
        self.assertEqual(json_output['email'], 'maxwell.kaxuri@gmail.com')

   
        
    def test_get_users(self):
        response = self.client.get('/v1/auth/users')
        json_output = response.json()
    
        self.assertEqual(response.status_code, HTTP_200_OK)
        self.assertEqual(json_output[0]['username'], 'lewism')
        self.assertEqual(json_output[0]['first_name'],'Lewis')
        self.assertEqual(json_output[0]['last_name'], 'Markus')
        self.assertEqual(json_output[0]['email'], 'lewis@buupass.com')

    def test_get_subusers(self):
        response = self.client.get('/v1/auth/users/subusers')
        json_output = response.json()

        self.assertEqual(response.status_code, HTTP_200_OK)
        self.assertEqual(json_output[0]['username'], 'nexusva')
        self.assertEqual(json_output[0]['first_name'],'Nexus')
        self.assertEqual(json_output[0]['last_name'], 'Vanguard')
        self.assertEqual(json_output[0]['email'], 'nexus.vanguard@gmail.com')