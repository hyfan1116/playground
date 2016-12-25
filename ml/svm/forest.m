function F=forest(x,y,nt)
% function F=forest(x,y,nt)
%
% INPUT:
% X  | input vectors dxn
% y  | input labels 1xn
% nt | number of trees
%
% OUTPUT:
% F | Forest
%

%% fill in code here
F = cell(1,nt);
[~,n] = size(x);
for t = 1:nt
    s = randsample(n, n,true);
    xTr = x(:,s); %
    yTr = y(1,s);
    T = id3tree(xTr,yTr);
    C = setxor(1:n,s);
    xTe = x(:,C);
    yTe = y(1,C);
    T = prunetree(T,xTe,yTe) ;
    F{1, t} = T; %add the tree to a cell array
end;
