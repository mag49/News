class TestStories(unittest.TestCase):
    '''
    Test Class to test the behaviour of our Story class
    '''
    def setUp(self):
        '''
         Set up method that will run before every Test
         '''
         self.new_story = Stories("the-pulse","Danny Lake","What's Going to Happen With Willy pauls music?","Since his transition to secular music?","https://pulse.com/whats-going-to-happen-to-willy music"")
        
    def test_instance(self):
        self.assertTrue(isinstance(self.new_story,Stories))
if __name__ == "__main__":
    unittest.main()