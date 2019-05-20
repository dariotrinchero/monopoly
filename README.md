# Markov Monopoly

Simulates the movement of players around the board for a game of *US Standard 2008 Edition Monopoly*, using a Markov process, in order to model the likelihood of landing on each tile.

## Running the Script

The script was written for, and tested on, MATLAB version R2017b. On execution, it should produce a plot titled "Turn 0". Click to transfer focus to the plot, then press any key to begin the simulation. The probability distribution will evolve in real time as the turn count increases.

## Interpreting the Output

The plot displayed by the script represents the probability of finding any given player on a specific tile, after a certain number of turns have been taken by that player. The probability is shown on the vertical axis, for each of the tiles on the horizontal axis. The tiles are numbered from 1 (corresponding to the "Go" tile) clockwise around the board (in the direction of play) up until tile 40 (*Boardwalk*). The probability distribution starts at turn 0 (before any rolls), at which time the player has a 100% chance of being on the "Go" tile.

After turn 60 (or the turn given by `finalFrame` - see *Modifying Output* section below), the simulation will cease, and black dots will be overlayed onto the probability distribution. These black dots show the *limiting distribution* (as the turn count tends to infinity), obtained as the (normalized) eigenvector of the transition matrix corresponding to eigenvalue 1. Finally, the total sum under the distribution will be output, as a consistency check (of course, this should simply be 1).

## Modifying the Script

### Adding & Modifying Transitions

The main function `monopoly` contains a function `jumpTo(from, to, prob)`. Once the initial transition matrix has been constructed (based on dice rolls alone), this function is used to add possible transitions (jumps) from one tile to another with a given probability. These are added based on the official *Monopoly* rules, and may include such things as a "Go to Jail" square, or "Chance" cards which send the player to another tile. The order in which these jumps are added matters, in that all possible transitions **to** any given tile should be established before adding a transition **from** that tile. As such, the jumps from the *Chance* tiles are added before the jumps from the *Community Chest* tiles, since one of the 16 *Chance* cards (if drawn on one of the 3 *Chance* tiles) may send the player (back 3 spaces) to a *Community Chest* tile.

### Modifying Output

The number of turns simulated may be changed simply be changing the global variable `finalFrame` at the top of the script. The visual style of the frames plotted during the simulation may be changed simply by editing the `frame(p0, turn)` function which follows the main `monopoly` function.

## Contributing

Pull requests are welcome - in fact, encouraged.

## Licence

This project is licensed under the [MIT](https://choosealicense.com/licenses/mit/) licence. 

All effort has been made to avoid infringing on copyright held by Parker Brothers or related corporations. It is believed that this project is general enough so as to be applicable to many board games, although Monopoly was used for testing. Should a holder of copyright claim wish for me to take this repository down, please raise an issue, and I will prompty do so. 
