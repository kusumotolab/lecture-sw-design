import pytest
from semver import *


@pytest.mark.parametrize('semver', [
    '1.2.3',
    '1.2.99',
    '1.2.0',
    '0.0.0',
    '10.20.30',
    '99999999999999999.99999999999999999.99999999999999999',
])
def test_semver_valid(semver):
    assert isSemVer(semver) == True


@pytest.mark.parametrize('semver', [
    '1',
    '1.2',
    '1.2.',
    '1.2.3.',
    '1..3',
    'aaa',
    '1.2.a',
    '1.01.1',
    '1. 2.3',
    '1.-2.3',
])
def test_semver_invalid(semver):
    assert isSemVer(semver) == False
