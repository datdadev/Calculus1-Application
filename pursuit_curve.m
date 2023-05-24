clc; clearvars;

% User input for the positions of points A and B
posA = input("Enter the position of point A [x, y]: ");
x1 = posA(1);
y1 = posA(2);
% User input for the vector A
A = input("Enter the vector A [x, y]: ");
A = A / norm(A);  % Convert A to a unit vector

posB = input("Enter the position of point B [x, y]: ");
x2 = posB(1);
y2 = posB(2);

% User input for the duration of the simulation
duration = input("Enter the duration of the simulation: ");

% Define the velocity of point A
v = 1;

% Set the time span
tspan = [0 duration];

% Define the initial conditions
initial_condition = [x1, y1, x2, y2];

% Solve the system of ordinary differential equations
[t, positions] = ode45(@(t, y) pursuitCurve(t, y, v, A), tspan, initial_condition);

% Extract the positions of points A and B
x1 = positions(:, 1);
y1 = positions(:, 2);
x2 = positions(:, 3);
y2 = positions(:, 4);

% Animate the pursuit curve
figure;
for i = 1:length(t)
    plot(x1(i), y1(i), 'ro', 'MarkerSize', 10, 'MarkerFaceColor', 'r');  % Point A
    hold on;
    plot(x2(i), y2(i), 'bo', 'MarkerSize', 10, 'MarkerFaceColor', 'b');  % Point B
    plot(x1(1:i), y1(1:i), 'r-', 'LineWidth', 2);  % Trajectory of point A
    plot(x2(1:i), y2(1:i), 'b--', 'LineWidth', 2);  % Trajectory of point B
    xlim([min([x1; x2])-1, max([x1; x2])+1]);
    ylim([min([y1; y2])-1, max([y1; y2])+1]);
    xlabel('x');
    ylabel('y');
    title('Pursuit Curve Simulation');
    grid on;
    hold off;
    pause(0.1);
end

% Function defining the system of ordinary differential equations
function dydt = pursuitCurve(~, y, v, A)
    x1 = y(1);
    y1 = y(2);
    x2 = y(3);
    y2 = y(4);
    
    dx1dt = v * A(1);
    dy1dt = v * A(2);
    dx2dt = (x1 - x2) / norm([x1 - x2, y1 - y2]);
    dy2dt = (y1 - y2) / norm([x1 - x2, y1 - y2]);
    
    dydt = [dx1dt; dy1dt; dx2dt; dy2dt];
end