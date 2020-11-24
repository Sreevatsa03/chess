# chess

> ## da files
>
> - **game.py**: contains game logic for chess, intializes two players as imports and plays them against each other
> - **randomMover.py**: game agent that plays chess based on random moves
> - **slowMover.py**: randomMover but sleeps for random amounts of time to slow itself down
> - **smartMover.py**: game agent that uses AI (minimax with alphaBetaPruning, negamax with quiescence, evaluation and fancified eval)
> - **humanMover.py**: agent that accepts human input in CLI as uci-formatted strings e.g. 'g1f3'
> - **dumbMover.py**: agent based that's modeled after surya, earlier version of our AI
> - **Workflow.md**: a helper file for some of the less intellectually gifted members
> - **README.md**: the thing you're reading, says the stuff about the things

> ## da homies
>
> - **toast**: fearlessly led the team, more of an ideas man, didn't really write the code but all of it basically came from his brain or something, minimax, human input, sorting
> - **sree**: wrote most of the code(every search a.k.a. the stuff that wins us games), was the prophet to toast's god, pvSearch with fail-hard zero-window, iterative deepening, negamax, minimax, abPruning
> - **surya**: eval function, weighting, fancier eval, quiescence, receptionist and morale booster
