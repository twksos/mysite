from django import test
from django.test.client import RequestFactory
from pair.models import Pair
from pair.models import Programmer
from pair.views import index

class TestView(test.TestCase):
    def test_index_should_success(self):
        request=RequestFactory().get('/pair/')
        response=index(request)
        self.assertEqual(response.status_code, 200)

    def test_get_pair_table_should_success(self):
        request=RequestFactory().get('/pair/get_pair_table')
        response=index(request)
        self.assertEqual(response.status_code, 200)

    def test_new_programmer(self):
        response=self.client.post('/pair/programmer/',data={'new_programmer_name':'wei'})
        self.assertRedirects(response=response,expected_url='/pair/')
        self.assertIn('wei',map(lambda x:x.name,Programmer.objects.all()))

    def test_new_programmer_with_empty_name_should_return_error_message(self):
        response=self.client.post('/pair/programmer/',data={'new_programmer_name':''})
        self.assertContains(response=response,text='Error:programmer name needed')
        self.assertNotIn('',map(lambda x:x.name,Programmer.objects.all()))

    def test_delete_programmer(self):
        Programmer(name='new_programmer').save()
        programmer = Programmer.objects.all()[0]
        response = self.client.delete('/pair/programmer/'+str(programmer.id))
        self.assertNotIn(programmer,Programmer.objects.all())
        self.assertContains(response=response, text='programmer '+programmer.name+' deleted.')

    def test_pair_should_increase_pair_time(self):
        programmer_0=Programmer(name='programmer_0')
        programmer_0.save()
        programmer_1 = Programmer(name='programmer_1')
        programmer_1.save()
        old_times=len(Pair.objects.filter(programmer_0=programmer_0,programmer_1=programmer_1))
        response = self.client.post('/pair/do_pair/'+str(programmer_0.id)+'/'+str(programmer_1.id))
        new_times=len(Pair.objects.filter(programmer_0=programmer_0,programmer_1=programmer_1))
        self.assertEqual(old_times+1,new_times)
        self.assertContains(response=response, text=programmer_0.name+' and '+programmer_1.name+' paired.')
