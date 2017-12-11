import unittest
from home_page_test import HomePageTest
from search_text import SearchText

#search_text = unittest.TestLoader().loadTestsFromTestCase(SearchText)
#home_page_test = unittest.TestLoader().loadTestsFromTestCase(HomePageTest)

#test_suite = unittest.TestSuite([home_page_test, search_text])

#run the tests
#unittest.TextTestRunner(verbosity=2).run(test_suite)

unittest.TextTestRunner(verbosity=2).run(
    unittest.TestSuite([
        unittest.TestLoader().loadTestsFromTestCase(x) for x in [
            HomePageTest, SearchText
        ]
    ])
)
