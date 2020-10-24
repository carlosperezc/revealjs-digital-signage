from selenium import webdriver
from flask import Flask
from flask import render_template
from selenium.webdriver.chrome.options import Options
import sys
app = Flask(__name__)


def runChrome():
    option = Options()
    option.add_experimental_option("excludeSwitches", ["enable-automation"])
    # option.add_argument("--start-fullscreen")
    option.add_argument("--kiosk")
    driver = webdriver.Chrome(options=option, executable_path='chromedriver')
    driver.get("http://localhost:5000")
    return driver


driver = runChrome()


@app.route("/next")
def next():
    driver.execute_script("Reveal.next();")
    return "Next :)"


@app.route("/back")
def back():
    driver.execute_script("Reveal.prev();")
    return "Back :)"


@app.route("/slide/<int:slide>")
def jump(slide):
    driver.execute_script(f"Reveal.slide({slide})")
    return f"Slide {slide}"


@app.route("/close")
def close():
    try:
        driver.close()
    except:
        pass
    sys.exit(1)
    return "Close"


if __name__ == "__main__":
    app.run(host="localhost", port=5001, debug=False)
