from music_type import MusicType

def test_sort():
    mt = MusicType(0, 0, 0, 0)
    mt.add('country')
    mt.add('rap')
    mt.add('rap')
    result = mt.sort()
    assert result == 'rap'

    mt.clear()

def test_sort() : 
    mt = MusicType(0,0,0,0)   
    mt.add('pop')
    mt.add('r&b') 
    mt.add('r&b')
    result = mt.sort()
    assert result == 'r&b'

    mt.clear()

def test_sort() :
    mt = MusicType(0,0,0,0)
    mt.add('country')
    mt.add('pop')
    mt.add('pop')
    result = mt.sort()
    assert result == 'pop'
    