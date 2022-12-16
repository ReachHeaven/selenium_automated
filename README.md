# TestForms
Test case with automatization web page testing. Using Python, Selenium, Pytest and ChromeDriver. Before usage, you need to add chromedriver to $PATH.
Usage: 

**Run all tests:**
```
pytest > .\results\output.txt -s -v --html=.\results\report.html
pytest .\tests\test_output.py   -s -v
```
**Run safe contract tests:**
```
pytest .\tests\test_smoke.py > .\results\output.txt -s -v --html=.\results\report.html
pytest .\tests\test_output.py   -s -v
```
**Run smoke tests:**
```
pytest .\tests\test_smoke.py > .\results\output.txt -s -v --html=.\results\report.html
pytest .\tests\test_output.py   -s -v
```