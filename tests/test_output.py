import pytest
from utils import utils

# Not tests. Class for send report to telegram bot.


@pytest.mark.usefixtures('setup_output')
def test_output_smoke():
    utils.bot_sendtext()

