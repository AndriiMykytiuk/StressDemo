from funkload_friendly.test import TestCase, description
import unittest


class MainTest(TestCase):
    @description("Web stress test")
    def test_stress(self):
        get_request = self.get(self.site_url)
        self.assert_(get_request.code == 200, "expecting a 200")

        get_request = self.get(self.site_url + 'contact')
        self.assert_(get_request.code == 200, "expecting a 200")

        get_request = self.get(self.site_url + 'about-us')
        self.assert_(get_request.code == 200, "expecting a 200")

    if __name__ in ('main', '__main__'):
        unittest.main()
