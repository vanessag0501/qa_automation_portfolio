# week4/test_radio_button.py

import pytest

from week4.pages.radio_button_page import RadioButtonPage

@pytest.mark.smoke
@pytest.mark.parametrize("option", ["Yes", "Impressive"])
def test_radio_selection(page, option):
    radio = RadioButtonPage(page)
    radio.navigate()
    radio.select(option)
    radio.verify_selected(option)

    