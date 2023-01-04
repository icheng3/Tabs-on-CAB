import time
import json
from selenium import webdriver
from scrapy import Selector

CAB_URL = 'https://cab.brown.edu/'
DEPT_CODES_PATH = '/Users/irischeng/Documents/CS32/term-project-icheng3-ngramaj1-ssokolow-ycruztri/backend/src/main/python/cabscraper/data/department_codes.txt'
JSON_SAVE_PATH = '/Users/irischeng/Documents/CS32/term-project-icheng3-ngramaj1-ssokolow-ycruztri/backend/src/main/python/Scraper/cabscraper/spiders/data_final.json'

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")

class CABScraper():
    """
    Class employed to scrape CAB for all courses being offered during the current semester.
    A combination of selenium of Scrapy are employed with the former handling the website's dynamic behavior
    and the latter used to quickly extract relevant text information.
    """
    def __init__(self):
        self.department_codes = self.get_dept_codes(DEPT_CODES_PATH)
        self.driver = webdriver.Chrome(options=chrome_options)
        self.scraped_info = {} #a nested dictionary with outer keys as crn's and inner
        #keys as a dictionary with the following keys: registration status,
        #course name, course code, instructor, section number, and time.
        self.courses = {} #a dictionary with course code keys and course name values
    
    def write_json(self):
        with open(JSON_SAVE_PATH, "w") as f:
            json.dump(self.scraped_info, f)
        print('new file written')
        
    def get_dept_codes(self, filepath : str) -> list:
        """Retrieves a list of Brown's department codes by converting a file's contents into a list of strings 
        where each individual string corresponds to the contents of a single line in said file."""
        with open(filepath) as file:
            codes = [line.rstrip() for line in file]
        return codes
    
    def check_reg_status(self) -> bool:
        """Retrieves a course's enrollment status by checking to see if a warning icon exists. The presence of
        such an icon according the CAB DOM, indicates that the course is full and open to registration otherwise."""
        maybe_full = self.curr_selector.xpath(
            ".//i[contains(@class, 'fa fa-fw icon--warn')]")
        return not maybe_full 
    
    def get_course_code(self) -> str:
        """Retrieves a course's code (ie ENGL0010), if unable to be found, an empty string is returned instead."""
        return self.curr_selector.xpath(
            './/span[@class="result__code"]/text()').get(default='').strip()


    def get_course_name(self) -> str:
        """Retrieves a course's name (ie Principles of Economics), if unable to be found, an empty string is returned instead."""
        return self.curr_selector.xpath(
            './/span[@class="result__title"]/text()').get(default='').strip()

    def get_course_section_no(self) -> str:
        """Retrieves a course's section number (ie S01), if unable to be found, an empty string is returned instead."""
        return self.curr_selector.xpath(
            './/span[@class="result__flex--3"]/text()').get(default='').strip()

    def get_course_time(self) -> str:
        """Retrieves a course's time (ie MWF 10-10:50), if unable to be found, an empty string is returned instead."""
        return self.curr_selector.xpath(
            './/span[@class="flex--grow"]/text()').get(default='').strip()

    def get_instructor(self) -> str:
        """Retrieves a course's instructor, if unable to be found, an empty string is returned instead."""
        return self.curr_selector.xpath(
            './/span[@class="result__flex--9 text--right"]/text()').get(default='').strip()

    def scrape(self) -> dict:
        """Iterates across the list of departments and scrapes the information of all courses within the department.
        Returns the scraped information as a doubly nested dictionary."""
        for dep in self.department_codes:
            self.scrape_by_dept(dep)
        return self.scraped_info

    def find_num_course(self) -> int:
        """Retrieves the number of courses available for a given department, employed to ensure that 
        the correct number of course panels are retrieved in scrape_by_dept"""
        num_course = self.info_bar_selector.xpath(
            './/strong/text()').get(default='').strip()
        if num_course == '':
            return 0
        else:
            return int(num_course)

    def scrape_by_dept(self, dept_code : str):
        """Uses the webdriver to load the CAB page for a given department. Then retrieves a list of WebElements corresponding
        to all courses being offered within a given department for the current semester."""
        self.driver.get(CAB_URL + '?subj=' + dept_code)
        panel_body_found = len(self.driver.find_elements("xpath", "//div[@class='panel__body']"))
        panel_info_found = len(self.driver.find_elements("xpath", "//div[@class='panel__info-bar']"))
        while panel_info_found != 1 or panel_body_found != 2:
            time.sleep(0.5)
            panel_info_found = len(self.driver.find_elements("xpath","//div[@class='panel__info-bar']"))
            panel_body_found = len(self.driver.find_elements("xpath","//div[@class='panel__body']"))
        panel_body = self.driver.find_elements("xpath","//div[@class='panel__body']")[-1]
        panel_info_div = self.driver.find_elements("xpath","//div[@class='panel__info-bar']")[-1]
        panel_info_bar = panel_info_div.find_element("xpath",".//div[@class='panel__info-bar-text']")
        self.info_bar_selector = Selector(text=panel_info_bar.get_attribute('outerHTML'))
        num_course = self.find_num_course()
        course_panels = panel_body.find_elements("xpath",".//div[@class='result result--group-start']")
        while len(course_panels) != num_course: #ensures that all courses are found
            #print('course panel length', len(course_panels))
            time.sleep(0.5)
            course_panels = panel_body.find_elements("xpath",".//div[@class='result result--group-start']")
        self.handle_course_links(course_panels)
    
    def get_crn(self) -> str:
        """Retrieves the crn for a given course, first by inspecting the 'data-key' attribute, and if unsuccessful, 
        then the 'data-matched' attribute."""
        maybe_crn  = self.curr_course_link.get_attribute('data-key').split(":")[-1]
        if maybe_crn == "":
            maybe_crn = self.curr_course_link.get_attribute('data-matched').split(":")[-1]
            maybe_crn = maybe_crn.split(",")[0]
        return maybe_crn

    def handle_course_links(self, course_panels):
        """Handles the list of webelements corresponding to the courses being offered for a given department.
        Iterates across each individual course, retrieving information as needed, and populating the dictionary."""
        for course in course_panels:
            self.curr_selector = Selector(text=course.get_attribute("outerHTML")) 
            self.curr_course_link = course.find_element("xpath",'.//a[@href]')
            self.find_course_info()
    
    def find_course_info(self):
        instructor = self.get_instructor()
        if "See details" not in instructor: 
            crn = self.get_crn()
            course_dic = {}
            course_dic['instructor'] = self.get_instructor()
            course_dic['time'] = self.get_course_time()
            course_dic['enrollment status'] = self.check_reg_status()
            course_dic['crn'] = self.curr_course_link.get_attribute('data-key').split(":")[-1]
            course_dic['code'] = code = self.get_course_code()
            course_dic['name'] = name = self.get_course_name()
            print(name)
            if code == '':
                course_dic['code'] = code = self.curr_course_link.get_attribute('data-group').split(':')[-1]
                self.courses[course_dic['code']] = course_dic['name']
            if name == '':
                course_dic['name'] = self.courses[course_dic['code']]
            self.scraped_info[crn] = course_dic


