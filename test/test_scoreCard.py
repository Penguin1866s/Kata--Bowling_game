import pytest
from src.scoreCard import scoreCard

@pytest.mark.test_divideFrameScore
def test_divideFrameScore():
    assert scoreCard('12345123451234512345').divideFrameScore() == ['12', '34', '51', '23', '45', '12', '34', '51', '23', '45']
    assert scoreCard('9-9-9-9-9-9-9-9-9-9-').divideFrameScore() == ['9-', '9-', '9-', '9-', '9-', '9-', '9-', '9-', '9-', '9-']
    assert scoreCard('5/5/5/5/5/5/5/5/5/5/5').divideFrameScore() == ['5/', '5/', '5/', '5/', '5/', '5/', '5/', '5/', '5/', '5/5']
    assert scoreCard('XXXXXXXXXXXX').divideFrameScore() == ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'XXX']
    assert scoreCard('3/6/9/4/7/2/5/8/1/3/6').divideFrameScore() == ['3/', '6/', '9/', '4/', '7/', '2/', '5/', '8/', '1/', '3/6']

@pytest.mark.test_singleShot
def test_singleShot():
    assert scoreCard('12345123451234512345').finalScore() == 60

@pytest.mark.test_singleFailShot
def test_singleFailShot():
    assert scoreCard('9-9-9-9-9-9-9-9-9-9-').finalScore() == 90

@pytest.mark.test_spareShot
def test_spareShot():
    assert scoreCard('5/5/5/5/5/5/5/5/5/5/5').finalScore() == 150
    assert scoreCard('3/6/9/4/7/2/5/8/1/3/6').finalScore() == 151

@pytest.mark.test_strikeShot
def test_strikeShot():
    assert scoreCard('XXXXXXXXXXXX').finalScore() == 300
    #assert scoreCard('81-92/X637-52X-62/X').finalScore() == 122


@pytest.mark.test_finalScore
def test_finalScore():
    assert scoreCard('12345123451234512345').finalScore() == 60
    assert scoreCard('9-9-9-9-9-9-9-9-9-9-').finalScore() == 90

    assert scoreCard('123451234512345-2345').finalScore() == 59
