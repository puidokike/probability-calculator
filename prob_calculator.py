import copy
import random


class Hat:
    def __init__(self, **kwargs):
        self.contents = []
        for k, v in kwargs.items():
            for _ in range(v):
                self.contents.append(k)

    def draw(self, nr_of_balls):
        balls = []
        if nr_of_balls > len(self.contents):
            return self.contents
        else:
            for x in range(nr_of_balls):
                random_nr = random.randrange(len(self.contents))
                balls.append(self.contents.pop(random_nr))
            return balls


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    counter = 0
    new_hat = copy.deepcopy(hat)
    balls_drawn = new_hat.draw(num_balls_drawn)

    for x in range(num_experiments):
        balls_required = 0
        for k, v in expected_balls.items():
            if balls_drawn.count(k) >= v:
                balls_required += 1
        if balls_required == len(expected_balls):
            counter += 1

    return counter / num_experiments

