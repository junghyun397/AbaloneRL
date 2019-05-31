import random

from abalone.env.AbaloneEnvironment import AbaloneEnvironment

if __name__ == '__main__':
    env = AbaloneEnvironment()
    
    while True:
        print(env.action(random.randrange(0, env.action_space)))
