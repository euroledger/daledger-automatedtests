from selenium import webdriver
from PasswordProvider import getPassword
import time
import sys


class GlobalTests:
    driver = None

    def testSignOut(self):
        button = self.findElementByCSS("loginButtonComponent")
        button.click()
        print("button loginButtonComponent clicked!")

    def doLogin(self):
         # Logs the user in -> rerouted to clienthome screen
        email = self.findElementByName("identifier")
        email.send_keys("geominat@gmail.com")
        nextButton = self.findElementByID("identifierNext")
        nextButton.click()
        time.sleep(1)
        password = self.findElementByName("password")
        password.send_keys(getPassword())
        nextButton = self.findElementByID("passwordNext")
        nextButton.click()

    def testSignInWithGoogle(self):
        button = self.findElementByCSS("projectButton")
        button.click()

        time.sleep(2)
        firstName = self.findElementByName("firstName")
        firstName.send_keys("Mike")

        lastName = self.findElementByName("lastName")
        lastName.send_keys("Richardson")

        email = self.findElementByName("email")
        email.send_keys("emerysolutions@yahoo.co.uk")

        button = self.findElementByCSS("registerButton")
        button.click()

        # wait for 5 seconds or screen to load, whichever comes first
        # self.driver.implicitly_wait(5)
        time.sleep(6)

        self.doLogin()
        # time.sleep(60)

    def editTableCell(self, tablename, row, column, value):
        try:
            tableCell = self.driver.find_element_by_xpath(
                '//div[@data-test="{}"]//table/tbody/tr[{}]/td[{}]'.format(tablename, row, column))

        except:
            print("No such luck buddy!", sys.exc_info()[0], "occured.")
            print("element not found")
            return None

        if tableCell is not None:
            tableCell.click()

            try:
                # time.sleep(0.5)
                editableCell = self.driver.find_element_by_xpath(
                    '//div[@data-test="{}"]//table/tbody/tr[{}]/td[{}]//input'.format(tablename, row, column))
            except:
                print(">>>>>>>>>>No such luck buddy!",
                      sys.exc_info()[0], "occured.")
                print(">>>>>>>>>>editable cell element not found")
                return None
            # time.sleep(1)
            print("setting table cell ({},{}) to ".format(row, column), value)
            editableCell.send_keys(value)

    def goToNextScreen(self):
        button = self.findElementByCSS("continueButton")
        button.click()
        time.sleep(2)
        
    def testLaunchCompetition(self):
        # project definition
        button = self.findElementByCSS("launchButton")
        button.click()
        time.sleep(2)
        button = self.findElementByCSS("objective-remodelling")
        button.click()
        countryDropDown = self.findElementByName("country")
        countryDropDown.click()
        countryDropDown.send_keys("Brazil")

        # project style
        self.editTableCell("right", 4, 2, "4")

        self.goToNextScreen()
     
        self.editTableCell("left", 1, 2, "4")
        self.editTableCell("left", 1, 3, "3")
        self.editTableCell("left", 1, 3, "3")
        self.editTableCell("left", 1, 4, "7")
        self.editTableCell("left", 1, 4, "7")
        self.editTableCell("left", 2, 2, "1")
        self.editTableCell("left", 2, 2, "1")
        self.editTableCell("left", 2, 3, "7")
        self.editTableCell("left", 2, 3, "7")
        self.editTableCell("left", 2, 4, "8")
        self.editTableCell("left", 2, 4, "8")

        self.editTableCell("left", 3, 2, "1")
        self.editTableCell("left", 3, 2, "1")
        self.editTableCell("left", 3, 3, "2")
        self.editTableCell("left", 3, 3, "2")
        self.editTableCell("left", 3, 4, "1")
        self.editTableCell("left", 3, 4, "1")
        self.editTableCell("left", 4, 2, "4")
        self.editTableCell("left", 4, 2, "4")
        self.editTableCell("left", 4, 3, "2")
        self.editTableCell("left", 4, 3, "2")
        self.editTableCell("left", 4, 4, "1")
        self.editTableCell("left", 4, 4, "1")
        self.editTableCell("left", 5, 2, "5")
        self.editTableCell("left", 5, 2, "5")
        self.editTableCell("left", 5, 3, "7")
        self.editTableCell("left", 5, 3, "7")
        self.editTableCell("left", 5, 4, "3")
        self.editTableCell("left", 5, 4, "3")

        self.editTableCell("right", 1, 2, "4")
        self.editTableCell("right", 1, 2, "4")
        self.editTableCell("right", 1, 3, "3")
        self.editTableCell("right", 1, 3, "3")
        self.editTableCell("right", 1, 4, "7")
        self.editTableCell("right", 1, 4, "7")
        self.editTableCell("right", 2, 2, "1")
        self.editTableCell("right", 2, 2, "1")
        self.editTableCell("right", 2, 3, "7")
        self.editTableCell("right", 2, 3, "7")
        self.editTableCell("right", 2, 4, "8")
        self.editTableCell("right", 2, 4, "8")
        self.editTableCell("right", 3, 2, "1")
        self.editTableCell("right", 3, 2, "1")
        self.editTableCell("right", 3, 3, "2")
        self.editTableCell("right", 3, 3, "2")
        self.editTableCell("right", 3, 4, "1")
        self.editTableCell("right", 3, 4, "1")

        self.editTableCell("right", 4, 1, "Bogs")
        self.editTableCell("right", 4, 1, "Bogs")
        self.editTableCell("right", 4, 2, "4")
        self.editTableCell("right", 4, 2, "4")
        self.editTableCell("right", 4, 3, "2")
        self.editTableCell("right", 4, 3, "2")
        self.editTableCell("right", 4, 4, "1")
        self.editTableCell("right", 4, 4, "1")

        self.editTableCell("right", 5, 1, "Cat Boxes")
        self.editTableCell("right", 5, 1, "Cat Boxes")
        self.editTableCell("right", 5, 2, "5")
        self.editTableCell("right", 5, 2, "5")
        self.editTableCell("right", 5, 3, "7")
        self.editTableCell("right", 5, 3, "7")
        self.editTableCell("right", 5, 4, "3")
        self.editTableCell("right", 5, 4, "3")
        time.sleep(1)
        self.goToNextScreen()

        
    def findElementByName(self, name):
        print("looking for: ", name)
        try:
            element = self.driver.find_element_by_name(name)
        except:
            print("No such luck buddy!", sys.exc_info()[0], "occured.")
            print("element not found")
            return None
        if element is not None:
            print("We found an element", name, "by name")
            return element

    def findElementByID(self, name):
        print("looking for: ", name)
        try:
            element = self.driver.find_element_by_id(name)
        except:
            print("No such luck buddy!", sys.exc_info()[0], "occured.")
            print("element not found")
            return None
        if element is not None:
            print("We found an element", name, "by id")
            return element

    def findElementByCSS(self, name):
        searchString = "[data-test='{}']".format(name)
        print("looking for: ", searchString)
        try:
            element = self.driver.find_element_by_css_selector(searchString)
        except:
            print("No such luck buddy!", sys.exc_info()[0], "occured.")
            print("element not found")
            return None
        if element is not None:
            print("We found an element", name, "by css selector")
            return element


class FirefoxTests(GlobalTests):
    def test(self):

        self.driver = webdriver.Firefox()

        self.driver.maximize_window()

        self.driver.get("http://localhost:3000")

        self.testSignInWithGoogle()

        time.sleep(2)
        self.testLaunchCompetition()

        time.sleep(2)
        self.testSignOut()

        time.sleep(3)

        # title = self.driver.title
        # print("Title of the page is", title)

        # currentUrl = self.driver.current_url
        # print("URL of the page is", currentUrl)

        # # Refresh the browser
        # self.driver.refresh()

        # # LINKS
        # linkLocator = "Community"
        # try:
        #     link = self.driver.find_element_by_link_text(linkLocator)
        # except:
        #     # print("No such luck buddy")
        #     print("No such luck buddy!",sys.exc_info()[0],"occured.")
        #     self.driver.quit()
        #     return
        # if link is not None:
        #     print("We found an element designerButton by link")

        # try:
        #     buttons = self.driver.find_elements_by_class_name("MuiButton-root")
        # except:
        #     print("No such luck buddy!",sys.exc_info()[0],"occured.")
        #     self.driver.quit()
        #     return
        # if buttons is not None:
        #     print("We found elements by button class, length = ", len(buttons))
        print("Quitting...")
        self.driver.quit()


class ChromeTests(GlobalTests):

    def test(self):

        self.driver = webdriver.Chrome()

        self.driver.maximize_window()

        self.driver.get("http://localhost:3000")
        # self.driver.get("http://www.letskodeit.com")
        self.testSignInWithGoogle()

        time.sleep(5)
        self.testLaunchCompetition()

        time.sleep(2)
        self.testSignOut()

        time.sleep(5)
        self.driver.quit()


class EdgeTests(GlobalTests):

    # login automatically happens...only one user specified on Edge so don't need to enter user/pass 
    def doLogin(self):
        pass

    def testSignInWithGoogle(self):
        button = self.findElementByCSS("loginButtonComponent")
        button.click()
        print("button loginButtonComponent clicked!")
        time.sleep(4)


    def test(self):

        self.driver = webdriver.Edge()

        # self.driver.maximize_window()

        self.driver.get("http://localhost:3000")

        self.testSignInWithGoogle()

        self.testLaunchCompetition()

        time.sleep(2)
        self.testSignOut()

        time.sleep(5)
        self.driver.quit()


class OperaTests(GlobalTests):

    def test(self):
        options = webdriver.ChromeOptions()
        options.binary_location = "."  # getting error without this line
        driver = webdriver.Opera(options=options)
        # driver = webdriver.Opera()

        # driver.get("http://localhost:3000")
        driver.get("http://www.letskodeit.com")


def runFireFoxTests():
    print("Running Firefox tests...")
    ffTest = FirefoxTests()
    ffTest.test()


def runChromeTests():
    print("Running Chrome tests...")
    chromeTest = ChromeTests()
    chromeTest.test()


def runEdgeTests():
    print("Running Edge tests...")
    edgeTest = EdgeTests()
    edgeTest.test()


def runOperaTests():
    print("Running Opera tests...")
    operaTest = OperaTests()
    operaTest.test()


# Code Main Body
args = len(sys.argv) - 1

if args > 1:
    sys.exit('Usage: BrowserTests <ch|cf|ed|op>')
if args == 0:
    runChromeTests()
    runFireFoxTests()
    runEdgeTests()
elif sys.argv[1] == "ch":
    runChromeTests()
elif sys.argv[1] == "ff":
    runFireFoxTests()
elif sys.argv[1] == "ed":
    while True:
        runEdgeTests()
elif sys.argv[1] == "op":
    runOperaTests()
