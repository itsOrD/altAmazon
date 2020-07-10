from tools import  *
from objects import *
from routines import *


#This file is for strategy
from altAmazonv2.objects import BotAgent
from altAmazonv2.routines import kickoff, atba
from altAmazonv2.utils import defaultThrottle, defaultPD


class BotLogic(BotAgent):
    def run(agent):
        #An example of using raw utilities:
        relative_target = agent.ball.location - agent.me.location
        local_target = agent.me.local(relative_target)
        defaultPD(agent, local_target)
        defaultThrottle(agent, 2300)
        # agent.controller.boost = True

        #An example of pushing routines to the stack:
        if len(agent.stack) < 1:
            if agent.kickoff_flag:
                agent.push(kickoff())
            else:
                agent.push(atba())

        
