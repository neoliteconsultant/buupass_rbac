from unittest import skip
from django.test import TestCase
from .models import User, SubUser
from .status_code import HTTP_201_CREATED, HTTP_200_OK


class TestRBAC(TestCase):

    def setUp(self):
        self.user = User()
        self.user.username = 'lewism'
        self.user.first_name= 'Lewis'
        self.user.last_name = 'Markus'
        self.user.email =  'lewis@buupass.com'
        self.user.password =  'TOm!Z&6lsw8'
        self.user.save()

        self.sub_user = SubUser()
        self.sub_user.user = self.user
        self.sub_user.username = "nexusva"
        self.sub_user.first_name = "Nexus"
        self.sub_user.last_name = "Vanguard"
        self.sub_user.password = "QuP8L0ri!to"
        self.sub_user.email = "nexus.vanguard@gmail.com"
        self.sub_user.save()

    def test_user_creation(self):
        data = {'username':'tonys','first_name': 'Tony', 'last_name': 'Sonia', 'email':'tonys@gmail.com','password':'P*LpH3wrUd9'}
        response = self.client.post('/auth/user', data, content_type= "application/json")
        json_output = response.json()

        self.assertEqual(response.status_code, HTTP_201_CREATED)
        self.assertEqual(json_output['username'], 'tonys')
        self.assertEqual(json_output['first_name'],'Tony')
        self.assertEqual(json_output['last_name'], 'Sonia')
        self.assertEqual(json_output['email'], 'tonys@gmail.com')

    def test_subuser_creation(self):
        data = {'user_id':self.user.id, 'username':'maxwellk','first_name': 'Maxwell', 'last_name': 'Kaxuri', 'email':'maxwell.kaxuri@gmail.com','password':'s=Eju8?iWIt'}
        response = self.client.post('/auth/sub_user', data, content_type= "application/json")
        json_output = response.json()

        self.assertEqual(response.status_code, HTTP_201_CREATED)
        self.assertEqual(json_output['username'], 'maxwellk')
        self.assertEqual(json_output['first_name'],'Maxwell')
        self.assertEqual(json_output['last_name'], 'Kaxuri')
        self.assertEqual(json_output['email'], 'maxwell.kaxuri@gmail.com')

     
    def test_get_users(self):
        response = self.client.get('/auth/user')
        json_output = response.json()
        
    
        self.assertEqual(response.status_code, HTTP_200_OK)
        self.assertEqual(json_output[0]['username'], 'lewism')
        self.assertEqual(json_output[0]['first_name'],'Lewis')
        self.assertEqual(json_output[0]['last_name'], 'Markus')
        self.assertEqual(json_output[0]['email'], 'lewis@buupass.com')

    def test_get_subusers(self):
        response = self.client.get('/auth/sub_user')
        json_output = response.json()

        self.assertEqual(response.status_code, HTTP_200_OK)
        self.assertEqual(json_output[0]['username'], 'nexusva')
        self.assertEqual(json_output[0]['first_name'],'Nexus')
        self.assertEqual(json_output[0]['last_name'], 'Vanguard')
        self.assertEqual(json_output[0]['email'], 'nexus.vanguard@gmail.com')