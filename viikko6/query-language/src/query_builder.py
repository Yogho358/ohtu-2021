from matchers import All, And, PlaysIn, HasAtLeast, HasFewerThan, Or

class QueryBuilder:
    def __init__(self, matcher = All()):
        self._matcher = matcher

    def build(self):
        return self._matcher

    def playsIn(self, team):
        return QueryBuilder(And(self._matcher, PlaysIn(team)))

    def hasAtLeast(self, value, attr):
        return QueryBuilder(And(self._matcher, HasAtLeast(value, attr)))

    def hasFewerThan(self, value, attr):
        return QueryBuilder(And(self._matcher, HasFewerThan(value, attr)))

    def oneOf(self, q1, q2):
        return QueryBuilder(And(self._matcher, Or(q1, q2)))


