mport unittest
import chromedriver_autoinstaller
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Ensure ChromeDriver is installed and available for use
chromedriver_autoinstaller.install()


class HerokuAppTests(unittest.TestCase):

    def setUp(self):
        """clear
        Step 1: Set up the WebDriver and open the Heroku website.
        - Initialize the Selenium WebDriver for Chrome (or another preferred browser).
        - Open the Heroku Test Website (https://the-internet.herokuapp.com/).
        """
        self.driver = webdriver.Chrome()
        self.driver.get("https://the-internet.herokuapp.com/")


    def test_login(self):
        """
        Task 1: Automate the login process for the Heroku website.
        - Navigate to the 'Form Authentication' page.
        - Input credentials:
            - Username: tomsmith
            - Password: SuperSecretPassword!
        - Click the 'Login' button.
        - After logging in, assert that the 'Logout' button is visible on the page.
        """
        #WebElement form_authentication
        form_authentication = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.Xpath("//a[contains(text(),'Form Authentication')]")))
        )
        form_authentication.click()

        userName = self.driver.fin_element(By.Xpath('//*[@id="username"]'))
        password = self.driver.find_element(By.Xpath('//*[@id="password"]'))

        userName.sendKeys('tomsmith')
        password.sendKeys('SuperSecretPassword!')

        login = self.driver.find_element(By.Xpath('//*[@id="login"]/button/i'))
        login.click()
        #wait = new FluentWait(driver)
        #wait.withTimeout(5000, TimeUnit.MILLISECONDS)
        #wait.pollingEvery(250, TimeUnit.MILLISECONDS)
        #wait.ignoring(NoSuchElementException.class)
        self.driver.wait.until(ExpectedConditions.textToBePresentInElement(self.driver.find_element(By.xpath('//*[@id="content"]/div/a/i')),' Logout'))
        pass

    def test_dynamic_loading(self):
        """
        Task 2: Automate the test for dynamic content loading.
        - Navigate to the 'Dynamic Content' page.
        - Wait for the content to load using either `explicit` or `implicit` waits.
        - Verify that the content is dynamically loaded and not empty.
        """

        dynamic_content =  WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.driver.find_element(By.Xpath('//a[href="/dynamic_content"]'))))
        dynamic_content.click()
        #FluentWait wait = new FluentWait(driver);
        #wait.withTimeout(5000, TimeUnit.MILLISECONDS);
        #wait.pollingEvery(250, TimeUnit.MILLISECONDS);
        #wait.ignoring(NoSuchElementException.class)
        self.driver.wait.until(ExpectedConditions.textToBePresentInElement(self.driver.find_element(By.Xpath("//*[@id='content']/div/p[2]/code[text()='?with_content=static']")),' Logout'))
        content1 = self.driver.find_element(By.Xpath('//*[@id="content"]/div[1]/div[2]'))
        content2 = self.driver.find_element(By.Xpath('//*[@id="content"]/div[2]/div[2]'))
        content3 = self.driver.find_element(By.Xpath('//*[@id="content"]/div[3]/div[2]'))
        val1 = content1.getText()
        val2 = content2.getText()
        val3 = content3.getText()

        pass

    def test_logout(self):
        """
        Task 3: Automate the logout process.
        - Reuse login functionality from `test_login()` method.
        - Click the 'Logout' button.
        - Assert that the page redirects to the 'Login' page.
        """
        pass

    def test_alert_handling(self):
        """
        Task 4: Automate alert handling (JS Alerts, Confirmations, and Prompts).
        - Navigate to the 'JavaScript Alerts' page.
        - Trigger an alert (e.g., 'Click for JS Alert').
        - Accept the alert and verify the expected result.
        """
        pass

    def test_report_generation(self):
        """
        Bonus Task: Automate the test report generation.
        - Use unittest's built-in reporting feature or integrate an external tool like HTMLTestRunner.
        - After running tests, generate a summary report indicating pass/fail status.
        - Optionally, add more details like test durations or additional custom logs.
        """
        pass

    def tearDown(self):
        """
        Final Step: Clean up by closing the browser after each test.
        Ensure the WebDriver is properly closed after each test to avoid memory leaks.
        """
        self.driver.close()
        pass

if __name__ == "__main__":
    unittest.main()