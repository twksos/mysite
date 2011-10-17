"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""
from datetime import datetime

from django.test import TestCase
from mysite.pair.models import Programmer, Pair

class ModelTest(TestCase):
    def setUp(self):
        self.programmer_ada = Programmer(name='ada')
        self.programmer_ada.save()
        self.programmer_van = Programmer(name='van')
        self.programmer_van.save()
        self.programmer_zoi = Programmer(name='zoi')
        self.programmer_zoi.save()

        self.pair_record1 = Pair(programmer_0=self.programmer_ada, programmer_1=self.programmer_van,
                                 date=datetime.now())
        self.pair_record1.save()
        self.pair_record2 = Pair(programmer_0=self.programmer_ada, programmer_1=self.programmer_zoi,
                                 date=datetime.now())
        self.pair_record2.save()
        self.pair_record3 = Pair(programmer_0=self.programmer_ada, programmer_1=self.programmer_van,
                                 date=datetime.now())
        self.pair_record3.save()

    def test_added_programmer_should_exist(self):
        """
        Tests that programmer ada, van, zoi exist
        """
        self.assertTrue(Programmer.objects.filter(name='ada').__contains__(self.programmer_ada))
        self.assertTrue(Programmer.objects.filter(name='van').__contains__(self.programmer_van))
        self.assertTrue(Programmer.objects.filter(name='zoi').__contains__(self.programmer_zoi))

    def test_added_pair_should_exist(self):
        """
        Test that pair record should exist
        """
        self.assertIn(self.pair_record1, Pair.objects.all())
        self.assertIn(self.pair_record2, Pair.objects.all())
        self.assertIn(self.pair_record3, Pair.objects.all())

    def test_pair_time_of_ada_should_return_3(self):
        """
        Test that ada pair time should be 3
        """
        self.assertEqual(self.programmer_ada.pair_time(), 3)

    def test_pair_time_of_van_should_return_2(self):
        """
        Test that van pair time should be 2
        """
        self.assertEqual(self.programmer_van.pair_time(), 2)

    def test_ada_pair_time_with_van_should_return_2(self):
        """
        Test that ada pair time with van should be 2
        """
        self.assertEqual(self.programmer_ada.pair_time_with(self.programmer_van), 2)
    def test_ada_pair_with_van_should_add_a_new_pair_record(self):
        """
        Test that ada pair with van and pair record should increase by 1
        """
        pair_record_count=Pair.objects.all().__len__()
        self.programmer_ada.pair_with(self.programmer_van)
        self.assertEqual(pair_record_count+1,Pair.objects.all().__len__())
        pair_record_count=Pair.objects.all().__len__()
        self.programmer_ada.pair_with(self.programmer_van)
        self.assertEqual(pair_record_count+1,Pair.objects.all().__len__())

    def tearDown(self):
        self.programmer_ada.delete()
        self.programmer_van.delete()
        self.programmer_zoi.delete()

