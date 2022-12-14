# shooter!: Final Project Plan + Reflection
Over the course of the past few weeks, there have been numerous changes to our initial project plan and proposal for one reason or another. Regardless of that, this is what we decided about for our final project plan.

## Final Plan
### 01. Basic Gameplay
shooter! is a 8-bit platform shooter game where your only goal is to stay alive as long as possible while avoiding obstacles in your journey from one side of the level to the other. If the player is shot by the enemy, they lose the game. If the player makes it to the designated finish line at the end of the level, then they win the game.

### 02. Minimum Target
Our minimum deliverables are as follows:
- move the player using WASD keys
- allow the player to shoot ammo at the enemy
- have the enemy move autonomously
- have the player be able to kill the enemy
- ~~have the enemies shoot ammo at the player~~
- ~~include on screen point system~~
- ~~build a level of the game~~

### 03. Possible Extensions
Possible extensions for the game in future iterations, or if there is enough time include:
- adding a score system within the game
- adding different levels using the lore laid out in the README.md file
- adding power ups to modify game play (eg. speed multipliers, extra ammunition, boosting strength of ammunition, shield, etc)
- adding a health bar (which would allow for the player to lose health due to hits, but also gain health from a possible health bar throughout the level)
- allowing players to choose their character
- adding different types of enemies (variety in size, hit points, strength, speed, etc)
- adding different types of weapons (eg. a bow and arrow would have different benefits to using a slingshot, a sword would accommodate for short-range combat better, etc)
- adding a boss battle at the end of the level

### Credits and Acknowledgements
Our project was only possible thanks to the help of a few external libraries. They are as follows:
- [pygame](https://www.pygame.org/wiki/about)
- [random](https://docs.python.org/3/library/random.html?highlight=random#module-random)
- [abc](https://docs.python.org/3/library/abc.html)

### What changed between the proposal and final
- Fewer final deliverables --> There were a few problems with collision and GitHub that caused us to be very behind on our progress based on our initial schedule. As such, some of the final deliverables that we thought we would have been able to achieve, we did not get around to implementing, or at least implementing fully
- More realistic expectations --> We were very much in over our heads at the beginning of the project, expecting to get some very large scale things done in not a large scale amount of time. I think we got our bearings as we went along, and managed to develop a final product that we're all reluctantly okay with (even though we had hopeed for it to be better) 

---
## Reflections
### What We Learned
- Good communication is key! We had a group chat where we figured out when to meet outside of class. We took a couple of group work nights and spent the time in class to discuss where we were and what we could do to further our progress (even when that meant starting over halfway through)
- Git is a pain to use! Branching, pulling, and pushing galore. I think some of our progress got delayed just because of how much time we had to put into figuring out git.
- Pygame isn't hard, just a lot to learn. If we had played around with Pygame a bit like how we did with the graphics module, I think we would have been better off. It draws on similar ideas but it isn't the same.

### Difficulties 
Like any good project, we had our fair share of difficulties throughout the process of designing, coding, and debugging the game. Using Git effectively also proved to be challenging with there being many problems in pushing and pulling, and then keeping everyone's code up to date. We also had problems in terms of how big our sights were bs what we could realistically create. We ended up having to start over at the end of Thanksgiving Break because a lot of our old code really just didn't work, despite it being a joint attempt. Now, while learning and implementing concepts at the same time, it was a bit more difficult to know what we really wanted to do and execute it efficiently. I think if we were to start over again once more, with another two weeks, the game would have worked a lot better.

### Division of Labor
We all had kind of distinct roles which allowed us to focus on individual topics and problems, but still help each other when we needed it. In terms of dealing with problems, we could explain any issues we had to each other in a rather civil manner. Between all three of us, we were able to moderate and compromise where needed
| Name | Roles |
| ---------- | ----------|
| Raihana Zahra | player movement, bullets, background music  | 
| Rayane Tarazi | autonomous enemy movement, background, 
| Lauren Campbell | general graphics, menu screen, game states, looping the main game together with menu screen