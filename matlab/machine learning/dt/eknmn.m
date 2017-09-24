function res = eknmn(n)
%syms ms real;
%res = symsum(ms/n*pmukp(ms,n,n),ms,1,n);
res = 0;
for i = 1:n
    res = res + i/n*pmukp(i,n,n);
end