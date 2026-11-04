# UI Test Automation Framework

Automated browser tests for the [SauceDemo](https://www.saucedemo.com/) shopping application using Python, Selenium WebDriver, and pytest.

## Features

- Page Object Model structure for maintainable UI tests
- Automated ChromeDriver management with `webdriver-manager`
- End-to-end coverage for:
  - User login
  - Adding a product to the cart
  - Starting the checkout flow
- Self-contained HTML test reports

## Technology Stack

- Python
- Selenium WebDriver
- pytest
- pytest-html
- webdriver-manager

## Project Structure

```text
.
├── pages/
│   ├── checkout_page.py
│   ├── inventory_page.py
│   └── login_page.py
├── tests/
│   ├── test_add_to_cart.py
│   ├── test_checkout.py
│   └── test_login.py
├── utils/
│   ├── config.py
│   └── driver_factory.py
├── conftest.py
├── pytest.ini
├── requirements.txt
└── .gitignore
```

## Prerequisites

- Python 3.9 or newer
- Google Chrome
- Internet access for the SauceDemo application and automatic ChromeDriver installation

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/rohazshaik/UI-Test-Automation-Framework.git
   cd UI-Test-Automation-Framework
   ```

2. Create and activate a virtual environment.

   **Windows PowerShell:**

   ```powershell
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```

   **macOS/Linux:**

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. Install dependencies:

   ```bash
   python -m pip install -r requirements.txt
   ```

## Running Tests

Run the complete test suite:

```bash
pytest
```

Run a specific test file:

```bash
pytest tests/test_login.py
```

Run a specific test:

```bash
pytest tests/test_checkout.py::test_checkout_process
```

Tests run in a maximized Chrome browser. The configured pytest options generate a self-contained report at:

```text
reports/report.html
```

## Test Credentials

The framework uses the public SauceDemo test account configured in `utils/config.py`:

| Setting | Value |
|---|---|
| URL | `https://www.saucedemo.com/` |
| Username | `standard_user` |
| Password | `secret_sauce` |

## Design

The test suite uses a Page Object Model:

- Page classes contain locators and user actions.
- Test modules contain business-focused scenarios and assertions.
- The shared `driver` fixture starts the browser, opens the application, and closes the browser after each test.

## Notes

- Chrome must be installed locally.
- `webdriver-manager` downloads a compatible ChromeDriver when the tests run.
- Generated reports, caches, virtual environments, and local project documentation are excluded from version control.

## License

This project is intended for learning and test automation practice.
