function monopoly % US Standard 2008 Edition
%% Global parameters
finalFrame = 60;

%% Initial probability & roll transition matrix
p0 = [1; zeros(39, 1)];
A = [zeros(1, 28) 1 2 3 4 5 6 5 4 3 2 1 0; zeros(39, 40)]./36;
for j = 2:40, A(j, :) = [A(j-1, end) A(j-1, 1:end-1)]; end

%% Jumps between squares
    function jumpTo(from, to, prob)
        for f = from, A(to, :) = A(to, :) + prob.*A(f, :); end
    end

%%% "Go to Jail" square
jumpTo(31, 11, 1);
A(31, :) = zeros(1, 40);

%%% Community chests
jumpTo([3 18 34], 11, 1/17); % -> Jail
jumpTo(37, 11, 1/272); % -> Jail, via Chance
jumpTo([3 18 34], 1, 1/17); % -> Start
jumpTo(37, 1, 1/272); % -> Start, via Chance

%%% Ending on community chests
A(3, :) = A(3, :).*(15/17);
A(18, :) = A(18, :).*(15/17);
A(34, :) = A(34, :).*(15/17);

%%% Chance cards
jumpTo([8 23 37], 11, 1/16); % -> Jail
jumpTo([8 23 37], 1, 1/16); % -> Start
jumpTo([8 23 37], 25, 1/16); % -> Illinois Ave
jumpTo([8 23 37], 12, 1/16); % -> St. Charles Place
jumpTo(8, 13, 1/16); % -> Nearest utility
jumpTo([23 37], 29, 1/16); % -> Nearest utility
jumpTo(8, 6, 1/16); % -> Nearest railroad
jumpTo(23, 26, 1/16); % -> Nearest railroad
jumpTo(37, 36, 1/16); % -> Nearest railroad
jumpTo([8 23 37], 6, 1/16); % -> Reading Railroad
jumpTo([8 23 37], 40, 1/16); % -> Boardwalk
jumpTo(8, 5, 1/16); % <- Back 3 spaces
jumpTo(23, 20, 1/16); % <- Back 3 spaces
jumpTo(37, 34, 15/272); % <- Back 3 spaces (assumes further card draw)

%%% Ending on chance squares
A(8, :) = A(8, :).*(7/16);
A(23, :) = A(23, :).*(7/16);
A(37, :) = A(37, :).*(7/16);

%% Displaying game
fig = figure;
frame(p0, 0);
pause;
for roll = 0:finalFrame
    if ~ishandle(fig), break; end
    frame(p0, roll);
    p0 = A * p0;
end

%% Check probability sum and eigenvector
format long; fprintf('Sum of probabilities: %g\n', sum(p0));

[S, ~] = eig(A);
if ishandle(fig)
    hold on;
    plot(S(:, 1)/sum(S(:, 1)), 'k.');
    hold off;
end
end

function frame(p0, turn)
%% Shows frame of distribution
plot(p0, 'k-');

hold on;
scatter(1:40, p0, 70, linspace(1, 2, length(p0)), 'filled', 's');
hold off;

title(sprintf('Turn %g', turn)); 
xlabel('Position'); ylabel('Probability');
axis([0 41 0 0.1]); grid on; drawnow;
pause(0.016);
end
