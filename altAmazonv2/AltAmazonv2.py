from tools import  *
from objects import *
from routines import *
from routinesUnderConstruction import *


#This file is for strategy

## TODO: investigate why module imports are requested by PyCharm, yet they break the bot (everything's in the same module)
# from altAmazonv2.objects import GoslingAgent
# from altAmazonv2.routines import kickoff, atba
# from altAmazonv2.tools import find_hits
# from altAmazonv2.utils import defaultPD, defaultThrottle
# from altAmazonv2.routinesUnderConstruction import always_shoot


class BotLogic(GoslingAgent):

    def run(agent):
        if len(agent.stack) < 1:
            agent.push(short_shot(agent.foe_goal.location))

    '''
    ## BASIC FUNCTIONALITY - uncomment this block to get 'Pro' level bot
    def run(agent):
        ## Routines interacting with the stack:
        if len(agent.stack) < 1:
            # if agent.kickoff_flag:
            #     agent.push(kickoff())
            targets = {"goal" : (agent.foe_goal.left_post, agent.foe_goal.right_post)}
            shots = find_hits(agent, targets)
            if len(shots["goal"]) > 0:
                agent.push(shots["goal"][0])
            else:
                relative = agent.friend_goal.location - agent.me.location
                defaultPD(agent, agent.me.local(relative))
                defaultThrottle(agent, 1410)
    '''

    '''
        ## TODO: add z axis interpretation
        close = (agent.me.location - agent.ball.location).magnitude() < 2000
        have_boost = agent.me.boost >= 18
        my_net_to_ball = (agent.ball.location - agent.friend_goal.location).normalize()
        my_distance = mynet2ball.dot()

        my_poorpos = abs(agent.friend_goal.location.y - agent.me.location.y) - 200 > abs(
            agent.friend_goal.location.y - agent.ball.location.y)
        foe_poorpos = abs(agent.foe_goal.location.y - agent.foes[0].location.y) - 200 > abs(
            agent.foe_boal.location.y - agent.ball.location.y)

        if agent.team == 0:
            agent.debug_stack()
            print(close)

        if len(agent.stack) < 1:
            if agent.kickoff_flag:
                agent.push(kickoff())
    '''
