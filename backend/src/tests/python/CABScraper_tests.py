import unittest
from main.python.cabscraper.scripts.scraping.CABScraper import CABScraper
import time
from scrapy import Selector

class TestCABScraper(unittest.TestCase):
    def setUp(self):
        self.scraper = CABScraper()
        self.department_codes = ['ENGL']

    def test_setup(self):
        self.assertEqual(len(self.scraper.driver.arguments), 3)
        self.assertEqual(len(self.scraper.department_codes), 1)
        self.assertEqual(len(self.scraper.scraped_info), 0)
        self.assertEqual(len(self.scraper.courses), 0)

    def test_get_department_codes(self):
        simple_contents = ['hi', 'hello']
        dept_contents = ['AFRI', 'AMST', 'ANTH', 'APMA', 'CLAS', 'GREK',
        'LATN', 'ECON', 'EEPS', 'ENGN', 'HIAA', 'CLPS', 'CSCI', 'BIOL',
        'NEUR', 'PHYS', 'CHEM', 'ENVS', 'MATH', 'SANS', 'COLT', 'COST',
        'PHIL', 'RELS', 'UNIV', 'POLS', 'EMOW', 'HIST', 'ITAL', 'ENGL',
            'CHIN', 'EAST', 'JAPN', 'KREA', 'EDUC', 'ARCH', 'ASYR', 'EGYT',
            'PHP', 'SOC', 'URBN', 'ETHN', 'GNSS', 'GRMN', 'HISP', 'LACA', 'NAHU',
            'POBS', 'IAPA', 'HEBR', 'LITR', 'MDVL', 'MES', 'MCM', 'MUSC', 'STS',
            'CZCH', 'PLSH', 'RUSS', 'HNDI', 'SAST', 'TAPS', 'VISA']
        self.assertEqual(self.scraper.get_dept_codes('backend/src/main/python/cabscraper/data/simple_file.txt'),
         simple_contents)
        self.assertEqual(self.scraper.get_dept_codes('backend/src/main/python/cabscraper/data/department_codes.txt'),
         dept_contents)
        
    def test_scrape(self):
        self.scraper.scrape()
        self.assertTrue('26271' in self.scraper.scraped_info)
        self.assertEqual(len(self.scraper.scraped_info['26271']), 6)
        self.assertEqual(self.scraper.scraped_info['26271']['name'], 'Writing War')
        self.assertEqual(self.scraper.driver.current_url, "https://cab.brown.edu/?subj=ENGL")
    
    
    def set_curr_selector(self):
        self.scraper.driver.get('https://cab.brown.edu/?subj=ENGL')
        panel_body_found = len(self.scraper.driver.find_elements("xpath", "//div[@class='panel__body']"))
        panel_info_found = len(self.scraper.driver.find_elements("xpath", "//div[@class='panel__info-bar']"))
        while panel_info_found != 1 or panel_body_found != 2:
            time.sleep(0.5)
            panel_info_found = len(self.scraper.driver.find_elements("xpath","//div[@class='panel__info-bar']"))
            panel_body_found = len(self.scraper.driver.find_elements("xpath","//div[@class='panel__body']"))
        panel_body = self.scraper.driver.find_elements("xpath","//div[@class='panel__body']")[-1]
        panel_info_div = self.scraper.driver.find_elements("xpath","//div[@class='panel__info-bar']")[-1]
        panel_info_bar = panel_info_div.find_element("xpath",".//div[@class='panel__info-bar-text']")
        self.scraper.info_bar_selector = Selector(text=panel_info_bar.get_attribute('outerHTML'))
        num_course = self.scraper.find_num_course()
        course_panels = panel_body.find_elements("xpath",".//div[@class='result result--group-start']")
        while len(course_panels) != num_course: #ensures that all courses are found
            time.sleep(0.5)
            course_panels = panel_body.find_elements("xpath",".//div[@class='result result--group-start']")
        self.scraper.course_panel_el = course_panels[0]
        self.scraper.curr_selector = Selector(text=self.course_panel_el.get_attribute("outerHTML")) 

    def set_curr_course_link(self):
        self.set_curr_selector()
        self.scraper.curr_course_link = self.scraper.course_panel_el.find_element("xpath",'.//a[@href]')

    def test_check_reg_status(self):
        self.set_curr_selector()
        self.assertEqual(self.scraper.check_reg_status(), True)
    
    def test_get_course_code(self):
        self.set_curr_selector()
        self.assertEqual(self.scraper.get_course_code(), 'ENGL 0100M')
    
    def test_get_course_name(self):
        self.set_curr_selector()
        self.assertEqual(self.scraper.get_course_name(), 'Writing War')
    
    def test_get_course_time(self):
        self.set_curr_selector()
        self.assertEqual(self.scraper.get_course_time(), 'MWF 11-11:50a')
    
    def test_get_instructor(self):
        self.set_curr_selector()
        self.assertEqual(self.scraper.get_instructor(), 'R. Reichman')
    
    def test_find_num_courses(self):
        self.set_curr_selector()
        self.assertEqual(self.scraper.find_num_course(), 67)
    
    def test_get_crn(self):
        self.set_curr_course_link()
        self.assertEqual(self.scraper.get_crn(), '26271')
    
    def test_find_course_info(self):
        self.set_curr_course_link()
        self.set_curr_selector()
        expected_course_info = {
            "code": "ENGL 0100M",
            "enrollment status": True,
            "instructor": "R. Reichman",
            "name": "Writing War",
            "time": "MWF 11-11:50a"
        }
        self.assertEqual(self.scraper.scraped_info['26271'], expected_course_info)


if __name__ == '__main__':
    unittest.main()
