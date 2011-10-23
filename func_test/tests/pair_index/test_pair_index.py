from nose.plugins.attrib import attr
from framework.base_test import BaseTest
from pages.pair_index.pair_stair_page import PairStairPage
from pair_index_data import PAIR_STAIR_PAGE

class TestPairStairs(BaseTest):

    def setUp(self):
        super(TestPairStairs, self).setUp()

    @attr('functional_test')
    def test_can_see_add_button(self):
        pair_stair_page = PairStairPage(self.driver)
        self.driver.go_to(PAIR_STAIR_PAGE)
        self.assertRegexpMatches(pair_stair_page.get_button_text(), 'add')

    def tearDown(self):
        super(TestPairStairs, self).tearDown()

