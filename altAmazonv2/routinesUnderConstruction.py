# My temp routines are below for potential optimizations

## flip into opponent routine
class bully_flip():
    def __init__(self):
        self.step = 0
    def run(selfself, agent):
        if len(agent.stack) < 1:
            relative_target = agent.foes[0].location - agent.me.location
            local_target = agent.me.local(relative_target)
            agent.push(flip(local_target))

## that one guy who just crouch kicks the whole game...
class always_shoot():
    def __init__(self):
        self.step = 0
    def run(selfself, agent):
        if len(agent.stack) < 1:
            agent.push(short_shot(agent.foe_goal.location))


## 'braindead' boost collection routine (and turn towards ball)
class goto_boostv1():
    def __init__(self):
        self.step = 0
    def run(selfself, agent):
        if len(agent.stack) < 1:
            large_boosts = [boost for boost in agent.boosts if boost.large and boost.active]
            closest = large_boosts[0]
            closest_distance = (large_boosts[0].location - agent.me.location).magnitude()

            for item in large_boosts:
                item_distance = (item.location - agent.me.location).magnitude()
                if item_distance < closest_distance:
                    closest = item
                    closest_distance = item_distance
            # attempt to orient back towards ball after collecting boost
            agent.push(goto_boostv1(closest, agent.ball.location))

## performs adequate kickoffs
class simple_kickoff():
    def __init__(self):
        self.step = 0
    def run(selfself, agent):
        if len(agent.stack) < 1:
            if agent.kickoff_flag:
                agent.push(kickoff())
            else:
                agent.push(atba())
