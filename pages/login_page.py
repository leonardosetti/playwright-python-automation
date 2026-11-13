"""Login page object."""
from playwright.sync_api import Page, Locator
from pages.base_page import BasePage

class LoginPage(BasePage):
    # Selectors
    USERNAME_INPUT = 'input[name="username"], input[type="email"], #username'
    PASSWORD_INPUT = 'input[name="password"], input[type="password"], #password'
    LOGIN_BUTTON = 'button[type="submit"], button:has-text("Login"), button:has-text("Entrar")'
    ERROR_MESSAGE = '.error, .alert-danger, [role="alert"]'
    SUCCESS_INDICATOR = '.user-menu, .profile, [data-testid="user-menu"]'
    
    def __init__(self, page: Page):
        super().__init__(page)
        self.path = "/login"
    
    def login(self, username: str, password: str) -> None:
        """Perform login."""
        self.navigate(self.path)
        self.fill(self.USERNAME_INPUT, username)
        self.fill(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)
        self.page.wait_for_load_state("networkidle")
    
    def get_error_message(self) -> str:
        """Get error message text."""
        if self.is_visible(self.ERROR_MESSAGE):
            return self.get_text(self.ERROR_MESSAGE)
        return ""
    
    def is_logged_in(self) -> bool:
        """Check if login was successful."""
        return self.is_visible(self.SUCCESS_INDICATOR)
    
    def logout(self) -> None:
        """Logout if logged in."""
        if self.is_logged_in():
            self.click('[data-testid="logout"], .logout, button:has-text("Sair")')