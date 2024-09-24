import baseball.data
import baseball.events
import baseball.state
import statistics

from pybaseball import batting_stats_bref


data = (batting_stats_bref(2023))
for col in data.columns:
    print(col)

player = baseball.data.Hitter(data, 'Robert Jr.')
player2 = baseball.data.Hitter(data, 'Nimmo')


eventGenerator = baseball.events.SimpleEventGenerator();
i = 0;
outcomes = ['strikeout', 'single','double','triple','homerun!', 'walk','out' ]
seasonScores = []
seasonScores2 = []
while i < 162:
    state = baseball.state.SimpleGameState([player] * 9)
    while state.gameInProgress:
        event = eventGenerator.generateEvent(state.getCurrentHitter())
        state.updateState(event)
        if not state.gameInProgress:
            seasonScores.append(state.score)
    i += 1

i=0
while i < 162:
    state2 = baseball.state.SimpleGameState([player2] * 9)
    while state2.gameInProgress:
        event = eventGenerator.generateEvent(state2.getCurrentHitter())
        state2.updateState(event)
        if not state2.gameInProgress:
            seasonScores2.append(state2.score)
    i += 1

print(state.getCurrentHitter().name)
print(statistics.mean(seasonScores))
print(statistics.variance(seasonScores))
print(state2.getCurrentHitter().name)
print(statistics.mean(seasonScores2))
print(statistics.variance(seasonScores2))

