Title: Phase Plot and Phase Portrait
Date: 2020-07-23 20:14
Modified: 2020-07-23 22:28
Tags: MATLAB, Control Systems
Slug: phase-plot-and-phase-portrait
Author: Pranabendra Prasad Chandra
Summary: How to plot a phase plot and a phase portrait for a system


## Phase Plot and Phase Portrait

Using Simulink&reg; and MATLAB&reg;

## Contents
- ODE
- Simulink Model
- Defining the state equation
- Phase plane
- Calculating gradient and plotting the vector field
- Check for different initial conditions

### ODE
```matlab
imshow('VDP.png')
```
![image info]({static}/images/t1-phase-plots/van_der_pol_01.png)

### Simulink Model
```matlab
close
% Assuming initial condition = (1,0)
open_system('van_der_pol_model')
fprintf('\n')
plot(simout_x1.data, simout_x2.data)
xlim([-3 3])
xlabel('x_1')
ylabel('x_2')
```
![image info]({static}/images/t1-phase-plots/van_der_pol_02.png)
![image info]({static}/images/t1-phase-plots/van_der_pol_03.png)

### Defining the state equation
```matlab
f = @(t,X) [X(2); X(2)*(1 - X(1)^2) - X(1)];
```

### Phase plane
```matlab
x1 = linspace(-5,5,20);
x2 = linspace(-5,5,20);
[x,y] = meshgrid(x1,x2);
```

### Calculating gradient and plotting the vector field
```matlab
u = zeros(size(x));
v = zeros(size(x));
t=0;

for i = 1:numel(x)
    Xdot = f(t,[x(i); y(i)]);
    u(i) = Xdot(1);
    v(i) = Xdot(2);
end

quiver(x,y,u,v,'r'); figure(gcf)
xlabel('x_1')
ylabel('x_2')
axis tight equal;
hold on;
```

![image info]({static}/images/t1-phase-plots/van_der_pol_04.png)

### Check for different initial conditions
```matlab
for y20 = -4:2:4
    [ts,ys] = ode45(f,[0,20],[0;y20]);
    plot(ys(:,1),ys(:,2))
    plot(ys(1,1),ys(1,2),'x')
end

for y10 = -4:2:4
    [ts,ys] = ode45(f,[0,20],[y10;0]);
    plot(ys(:,1),ys(:,2))
    plot(ys(1,1),ys(1,2),'x')
end
hold off
```

![image info]({static}/images/t1-phase-plots/van_der_pol_05.png)
