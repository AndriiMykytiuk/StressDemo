import time

from funkload_friendly.test import TestCase, description


class MainTest(TestCase):

    @description("Stress realistic")
    def test_realistic(self):
        self.get(self.site_url + 'index.php?id_category=3&controller=category')
        self.get(self.site_url + 'index.php?id_category=8&controller=category')
        self.get(self.site_url + 'index.php?id_product=2&controller=product')
        self.get(self.site_url + 'index.php?id_category=3&controller=category#/size-s/styles-dressy/condition-new')
        self.get(self.site_url + 'index.php?controller=search&orderby=position&orderway=desc&search_query=jeans&submit_search=')
        self.get(self.site_url + 'index.php?controller=search&orderby=position&orderway=desc&search_query=blouse&submit_search=')
        self.clear_session_id()
