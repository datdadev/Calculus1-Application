clc; clearvars;

% User input for the function f(x)
f_str = input("Enter the function f(x): ", 's');
f = str2func(['@(x)', f_str]);

% User input for the initial point x0
x0 = input("Enter the point x0: ");

% Define the step size
h = 2;

% Create a range of x-values
x = linspace(x0 - h, x0 + 2 * h); % Offset the view

% Compute the corresponding y-values
y = f(x);

% Plot the function
plot(x, y, 'linewidth', 2)
hold on
grid on

% Compute the slope of the secant line
secant_line_slope = (f(x0 + h) - f(x0)) / (x0 + h - x0);

% Initialize the secant line
secant_line = secant_line_slope * (x - x0) + f(x0);

% Plot the secant line
secant_plot = plot(x, secant_line, '--', 'linewidth', 2);

% Plot the endpoint
end_point = plot(x0 + h, f(x0 + h), 'g.', 'LineWidth', 2, 'MarkerSize', 25);

% Plot the initial point
plot(x0, f(x0), 'r.', 'LineWidth', 2, 'MarkerSize', 25)

% Set axis labels and title
xlabel('x');
ylabel('y');
title(sprintf('x0 = %.2f, h = %.2f', x0, h));

% Set the initial view
xlim([x0 - h, x0 + 2 * h]);

% Compute the y-axis limits
y_real = real(f(x));
min_f = min(y_real);
max_f = max(y_real);
avg = (abs(max_f) + abs(min_f)) / 2;
ylim([min_f - avg * 1/2, max_f + avg * 1/2]);

pause(0.5)

% Animation loop
for h_ = h:-0.01:0.000000001
    secant_line_slope = (f(x0 + h_) - f(x0)) / (x0 + h_ - x0);

    % Update the secant line
    secant_line = secant_line_slope * (x - x0) + f(x0);
    
    % Update the plot
    set(secant_plot, 'YData', secant_line);
    set(end_point, 'XData', x0 + h_, 'YData', f(x0 + h_));
    
    title(sprintf('x0 = %.2f, h = %.2f', x0, h_));

    % Pause for a short duration to create an animation effect
    pause(0.01);
end

% Set the final secant line type to a straight line
set(secant_plot, 'LineStyle', '-');