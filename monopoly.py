import numpy as np
import matplotlib.pyplot as plt

# NOTE Written for Python3, Numpy 1.16.3, & Matplotlib 3.0.3

# Global parameters
final_frame = 60

def jump_to(A, f, t, p):
    ''' Add a transition to transition matrix A from state(s) f to state t with probability p.
    All transitions to any state should be added before adding a transition from that state. '''
    try:
        for state in f: A[t, :] += p * A[state, :]
    except TypeError: A[t, :] += p * A[f, :]

def add_jumps(A):
    ''' Add transitions to matrix A for each jump from one tile to another according to the rules
    of US Standard 2008 Edition of Monopoly, assuming A already has dice roll transitions. '''
    # "Go to Jail" tile
    jump_to(A, 30, 10, 1)
    A[30, :] *= 0

    # Chance cards
    jump_to(A, [7, 22, 36], 10, 1.0 / 16) # -> Jail
    jump_to(A, [7, 22, 36], 0, 1.0 / 16)  # -> Start
    jump_to(A, [7, 22, 36], 24, 1.0 / 16) # -> Illinois Ave
    jump_to(A, [7, 22, 36], 11, 1.0 / 16) # -> St. Charles Place
    jump_to(A, 7, 12, 1.0 / 16)           # -> Nearest utility
    jump_to(A, [22, 36], 28, 1.0 / 16)    # -> Nearest utility
    jump_to(A, 7, 5, 1.0 / 16)            # -> Nearest railroad
    jump_to(A, 22, 25, 1.0 / 16)          # -> Nearest railroad
    jump_to(A, 36, 35, 1.0 / 16)          # -> Nearest railroad
    jump_to(A, [7, 22, 36], 5, 1.0 / 16)  # -> Reading Railroad
    jump_to(A, [7, 22, 36], 39, 1.0 / 16) # -> Boardwalk
    jump_to(A, 7, 4, 1.0 / 16)            # <- Back 3 spaces
    jump_to(A, 22, 19, 1.0 / 16)          # <- Back 3 spaces
    jump_to(A, 36, 33, 1.0 / 16)          # <- Back 3 spaces (-> Community Chest)

    # Ending on Chance tiles
    A[7, :] *= 7.0 / 16
    A[22, :] *= 7.0 / 16
    A[36, :] *= 7.0 / 16

    # Community Chests
    jump_to(A, [2, 17, 33], 10, 1.0 / 17) # -> Jail
    jump_to(A, [2, 17, 33], 0, 1.0 / 17)  # -> Start

    # Ending on Community Chest tiles
    A[2, :] *= 15.0 / 17
    A[17, :] *= 15.0 / 17
    A[33, :] *= 15.0 / 17

def transition_matrix():
    ''' Create transition matrix representing all movements from one tile to another in US
    Standard 2008 Edition of Monopoly. '''
    A = np.block([[np.zeros((1, 28)), np.array([[1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 0]])],
        [np.zeros((39, 40))]]) / 36
    for j in range(39): A[j + 1, :] = np.concatenate(([A[j, -1]], A[j, :-1]))
    add_jumps(A)
    return A

if __name__ == '__main__':
    # Initial probability & roll transition matrix
    p0 = np.block([[np.array([[1]])], [np.zeros((39, 1))]])
    A = transition_matrix()

'''
    # Displaying game
    fig = figure
    frame(p0, 0)
    pause
    for roll = 0:final_frame
        if ~ishandle(fig), break end
        frame(p0, roll)
        p0 = A * p0

    # Check probability sum and eigenvector
    format long; fprintf('Sum of probabilities: %g\n', sum(p0));

    [S, ~] = eig(A);
    if ishandle(fig)
        hold on;
        plot(S(:, 1)/sum(S(:, 1)), 'k.');
        hold off;

def frame(p0, turn):
    # Shows frame of distribution
    plot(p0, 'k-');

    hold on;
    scatter(1:40, p0, 70, linspace(1, 2, length(p0)), 'filled', 's');
    hold off;

    title(sprintf('Turn %g', turn));
    xlabel('Position'); ylabel('Probability');
    axis([0 41 0 0.1]); grid on; drawnow;
    pause(0.016);
'''
