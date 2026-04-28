# week4/test_radio_button.py

from pages.radio_button_page import RadioButtonPage


def test_yes_selection(page):
    radio = RadioButtonPage(page)
    radio.navigate()
    radio.select("Yes")
    radio.verify_selected("Yes")


def test_impressive_selection(page):
    radio = RadioButtonPage(page)
    radio.navigate()
    radio.select("Impressive")
    radio.verify_selected("Impressive")

    