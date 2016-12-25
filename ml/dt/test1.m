x = 1:20;
y = zeros(1,length(x));

for i = 1:length(x)
    y(i) = eknmn(x(i));
end
figure
plot(x,y)

title('2-D Line Plot')
xlabel('x')
ylabel('E')