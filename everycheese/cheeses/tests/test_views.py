from test_plus.test import CBVTestCase
from ..views import  CheeseDetailView, CheeseListView, CheeseCreateView


class TestCheeseView(CBVTestCase):

    def setUp(self):
        super(TestCheeseView, self).setUp()
        self.user = self.make_user()

    def test_auth(self):
        # print self.reverse('cheeses:create')
        # self.assertLoginRequired(self.reverse('cheeses:create'))
        pass