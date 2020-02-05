#! /usr/bin/env python3.7

import animal
import island

if __name__ == "__main__":
    royale = island.Island(10)
    animal1 = animal.Animal(island=royale, x=0, y=8, name="a1")
    print(animal1.position())

    print(royale)
