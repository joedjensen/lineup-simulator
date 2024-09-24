import pytest
from pybaseball import batting_stats_bref

from baseball.events import *
from baseball.state import *

def test_single():
    state = SimpleGameState([])
    state.updateState(1)
    assert state.runners == [1,0,0]
    state.updateState(1)
    assert state.runners == [1,1,0]
    state.updateState(1)
    assert state.runners == [1,1,1]
    state.updateState(1)
    assert state.runners == [1,1,1]
    assert state.score == 1
    state.updateState(1)
    assert state.score == 2

def test_double():
    state = SimpleGameState([])
    state.updateState(2)
    assert state.runners == [0,1,0]
    state.updateState(2)
    assert state.runners == [0,1,0]
    assert state.score == 1
    state.updateState(2)
    assert state.score == 2

def test_triple():
    state = SimpleGameState([])
    state.updateState(3)
    assert state.runners == [0,0,1]
    state.updateState(3)
    assert state.runners == [0,0,1]
    assert state.score == 1
    state.updateState(3)
    assert state.score == 2

def test_hr():
    state = SimpleGameState([])
    state.updateState(4)
    assert state.runners == [0,0,0]
    assert state.score == 1
    state.updateState(1)
    state.updateState(4)
    assert state.score == 3
    assert state.runners == [0, 0, 0]

def test_bb():
    state = SimpleGameState([])
    state.updateState(5)
    assert state.runners == [1,0,0]
    state.updateState(5)
    state.updateState(5)
    state.updateState(5)
    assert state.runners == [1,1,1]
    assert state.score == 1
    state.runners = [0,1,0]
    state.updateState(5)
    assert state.runners == [1,1,0]

def test_sequence():
    state = SimpleGameState([])
    state.updateState(1)
    state.updateState(1)
    state.updateState(2)
    assert state.runners == [0,1,1]
    assert state.score == 1
    state.updateState(3)
    assert state.runners ==[0,0,1]
    assert state.score == 3
    state.updateState(1)
    assert state.runners == [1,0,0]
    assert state.score == 4
    state.updateState(4)
    assert state.runners == [0,0,0]
    assert state.score == 6

def test_hitter_lineup():
    data = (batting_stats_bref(2023))
    player = data.Hitter(data, 'Lindor')
    state = SimpleGameState([player] * 9)
    eventGenerator = SimpleEventGenerator()