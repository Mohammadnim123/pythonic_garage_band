from pythonic_garage_band import __version__
from pythonic_garage_band.pythonic_garage_band import Band,Musician,Guitarist,Bassist,Drummer

def test_version():
    assert __version__ == '0.1.0'

nemrawi = Band('nemrawi')
abo_anwar = Musician('abo_anwar')
shareef = Guitarist('shareef')
mahmoud = Drummer('mahmoud')
ali = Bassist('ali')


def test_Band_band_list():
    expected = [nemrawi]
    actual = Band.band_list
    assert expected == actual

def test_add_members_to_list():
    nemrawi.add_members('jafar')
    nemrawi.add_members('9ob7y')
    
    expected = ['jafar', '9ob7y']
    actual = nemrawi.to_list()
    assert expected == actual

def test_Musician_play_solo():
    expected = "Musician abo_anwar Play solo"
    actual = abo_anwar.play_solo()
    assert expected == actual

def test_Guitarist():
    expected = 'shareef'
    actual = shareef.name
    assert expected == actual

def test_Bassist():
    expected = 'ali'
    actual = ali.name
    assert expected == actual

def test_Drummer():
    expected = 'mahmoud'
    actual = mahmoud.name
    assert expected == actual

