import unittest
from pyramid import testing
from pyramid.i18n import TranslationStringFactory

_ = TranslationStringFactory('ziggurat_form_demo')


class ViewTests(unittest.TestCase):

    def setUp(self):
        testing.setUp()
        
    def tearDown(self):
        testing.tearDown()

    def test_my_view(self):
        from ziggurat_form_demo.views import my_view
        request = testing.DummyRequest()
        response = my_view(request)
        self.assertEqual(response['project'], 'ziggurat_form_demo')
