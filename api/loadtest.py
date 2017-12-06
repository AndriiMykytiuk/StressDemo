from funkload_friendly.test import TestCase, description
import unittest
from funkload.Lipsum import Lipsum


class MainTest(TestCase):
    @description("Buy tickets positive flow")
    def test_buy_tickets(self):
        get_request = self.get(self.site_url + '/get')
        self.assert_(get_request.code == 200, "expecting a 200")

        item = Lipsum().getWord()
        id_ = Lipsum().getUniqWord()

        post_request = self.post(self.site_url + '/post',
                                 params=[['item', item],
                                         ['id', id_]])

        self.assert_(post_request.code == 200, "expecting a 200")

        put_request = self.put(self.site_url + '/put',
                               params=[['item', item],
                                       ['id', id_]])
        self.assert_(put_request.code == 200, "expecting a 200")

    if __name__ in ('main', '__main__'):
        unittest.main()
