# """
# Write a function which detects if entered string is http/https domain name with optional slash at the and
# Restriction: use re module
# Note that address may have several domain levels
#     >>> is_http_domain('http://wikipedia.org')
#     True
#     >>> is_http_domain('https://ru.wikipedia.org/')
#     True
#     >>> is_http_domain('griddynamics.com')
#     False
# """
import re
import pytest


def is_http_domain(domain: str) -> bool:
    """ returns True if the given domain is a valid HTTP domain """
    return re.match(r'https*:\/\/.*\w+\.\w+', domain) is not None


"""
write tests for is_http_domain function
"""


@pytest.mark.parametrize("domain, expected", [('http://wikipedia.org', True),
                                              ('https://ru.wikipedia.org/', True),
                                              ('griddynamics.com', False),
                                              ('www.https', False),
                                              ('https://grid', False)])
def test_is_http_domain(domain, expected) -> None:
    assert is_http_domain(domain) is expected