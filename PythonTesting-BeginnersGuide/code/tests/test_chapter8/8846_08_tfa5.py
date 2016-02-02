from unittest import TestCase
import twill

class test_twill_browser(TestCase):
    def test_slashdot(self):
        browser = twill.get_browser()

        browser.go('http://slashdot.org/')
        self.assertTrue(browser.get_code() in (200, 201))

        html = browser.get_html()
        self.assertTrue(html.count('slashdot') > 150)

        link = browser.find_link('Science')
        browser.follow_link(link)

        form = browser.get_form(2)
        form.set_value('aardvark', name = 'fhfilter')
        browser.clicked(form, None)
        browser.submit()
        self.assertEqual(browser.get_code(), 200)
