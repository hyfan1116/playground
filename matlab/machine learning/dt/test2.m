x = 1:10;
y = zeros(1,length(x));
n = 6;
for i = 1:length(x)
    y(i) = 1-pmukp(n,x(i)*n,n);
end
figure
plot(x,y)

title('2-D Line Plot')
xlabel('x')
ylabel('E')