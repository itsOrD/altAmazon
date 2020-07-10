from tools import  *
from objects import *
from routines import *


#This file is for strategy

## TODO: investigate why module imports are requested by PyCharm, yet they break the bot (everything's in the same module)
# from altAmazonv2.objects import GoslingAgent
# from altAmazonv2.routines import kickoff, atba
# from altAmazonv2.tools import find_hits
# from altAmazonv2.utils import defaultPD, defaultThrottle


class BotLogic(GoslingAgent):
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
