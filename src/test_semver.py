from semver import *


def test_semver_valid1():
    assert isSemVer('1.2.3') == True


def test_semver_valid2():
    assert isSemVer('1.2.99') == True


def test_semver_valid3():
    assert isSemVer('1.2.0') == True


def test_semver_valid4():
    assert isSemVer('0.0.0') == True


def test_semver_valid5():
    assert isSemVer('10.20.30') == True


def test_semver_valid6():
    assert isSemVer(
        '99999999999999999.99999999999999999.99999999999999999') == True


def test_semver_invalid():
    assert isSemVer('1') == False


def test_semver_invalid():
    assert isSemVer('1.2') == False


def test_semver_invalid():
    assert isSemVer('1.2.') == False


def test_semver_invalid():
    assert isSemVer('1.2.3.') == False


def test_semver_invalid():
    assert isSemVer('1..3') == False


def test_semver_invalid():
    assert isSemVer('aaa') == False


def test_semver_invalid():
    assert isSemVer('1.2.a') == False


def test_semver_invalid():
    assert isSemVer('1.01.1') == False


def test_semver_invalid():
    assert isSemVer('1. 2.3') == False


def test_semver_invalid():
    assert isSemVer('1.-2.3') == False
