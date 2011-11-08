from nose.plugins.attrib import attr
import time
from framework.base_test import BaseTest
from framework.utils.common_utils import CommonUtilities, by_css
from pages.pair_index.pair_stair_page import PairStairPage
from pair_index_data import PAIR_STAIR_PAGE

class TestPairStairs(BaseTest):

    def setUp(self):
        super(TestPairStairs, self).setUp()
        pair_stair_page = PairStairPage(self.driver)
        self.driver.go_to(PAIR_STAIR_PAGE)
        pair_stair_page.delete_all_programmer()
        pair_stair_page.add_programmer_with_name('programmer0')
        pair_stair_page.add_programmer_with_name('programmer1')
        pair_stair_page.add_programmer_with_name('programmer2')
        pair_stair_page.add_programmer_with_name('programmer3')

    @attr('functional_test')
    def test_should_view_pair_stair_page(self):
        pair_stair_page = PairStairPage(self.driver)
        self.driver.go_to(PAIR_STAIR_PAGE)
        self.assertEqual(pair_stair_page.get_title(), 'Pair Stair')

    @attr('functional_test')
    def test_view_pair_stair_page_should_see_add_button(self):
        pair_stair_page = PairStairPage(self.driver)
        self.driver.go_to(PAIR_STAIR_PAGE)
        self.assertEqual(pair_stair_page.get_add_button().text, 'add')

    @attr('functional_test')
    def test_view_pair_stair_page_should_see_add_button(self):
        pair_stair_page = PairStairPage(self.driver)
        self.driver.go_to(PAIR_STAIR_PAGE)
        pair_stair_page.add_programmer_with_name('')
        self.assertEqual(pair_stair_page.get_error_message().text, "Error:programmer name needed")

    @attr('functional_test')
    def test_add_programmer_should_see_new_programmer(self):
        pair_stair_page = PairStairPage(self.driver)
        self.driver.go_to(PAIR_STAIR_PAGE)
        programmer_name = "test_name"
        pair_stair_page.add_programmer_with_name(programmer_name)
        self.assertIn(programmer_name,pair_stair_page.get_programmer_names())
        
    @attr('functional_test')
    def test_delete_programmer_should_not_see_programmer(self):
        pair_stair_page = PairStairPage(self.driver)
        self.driver.go_to(PAIR_STAIR_PAGE)
        programmer_name = 'programmer3'
        pair_stair_page.delete_with_name(programmer_name)
        self.assertNotIn(programmer_name, pair_stair_page.get_programmer_names())
        
    @attr('functional_test')
    def test_do_pair_should_see_pair_time_increase(self):
        pair_stair_page = PairStairPage(self.driver)
        self.driver.go_to(PAIR_STAIR_PAGE)
        programmer_0_name = 'programmer0'
        programmer_1_name = 'programmer1'
        old_times = pair_stair_page.get_pair_time(programmer_0_name, programmer_1_name)
        pair_stair_page.do_pair(programmer_0_name, programmer_1_name)
        new_times = pair_stair_page.get_pair_time(programmer_0_name, programmer_1_name)

        self.assertEqual(int(old_times)+1,int(new_times))

    def tearDown(self):
        pair_stair_page = PairStairPage(self.driver)
        self.driver.go_to(PAIR_STAIR_PAGE)
        pair_stair_page.delete_all_programmer()
        super(TestPairStairs, self).tearDown()


