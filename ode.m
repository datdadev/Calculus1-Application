clc; clearvars;

% User input for the derivative function dy/dt
dydt_func = input("Enter the derivative function dy/dt: ", 's');

% User input for the initial condition y0
y0 = input("Enter the initial condition y0: ");

% Define the time range for simulation
t_min = 0;
t_max = input("Enter the duration: ");

% Generate the time values
t_exact = linspace(t_min, t_max);

% Convert the derivative function to a function handle
dydt = str2func(['@(t, y)', dydt_func]);

% Solve the ODE using ode45
[t, y] = ode45(@(t, y) dydt(t, y), t_exact, y0);

% Plot the numerical solution
plot(t, y, 'r-', 'LineWidth', 1, 'MarkerSize', 20)

% Define the symbolic variable
syms y(t)

% Solve the ODE symbolically using dsolve
exact_sol = dsolve(diff(y,t) == dydt(t, y), y(0) == y0);

% Set the plot title as the exact solution
title(['Exact Solution: ', char(exact_sol)]);
