function T=prunetree(T,xTe,y)
% function T=prunetree(T,xTe,y)
%
% Prunes a tree to minimal size such that performance on data xTe,y does not
% suffer.
%
% Input:
% T = tree
% xTe = validation data x (dxn matrix)
% y = labels (1xn matrix)
%
% Output:
% T = pruned tree
%

%% fill in code here
parent = unique(T(6,:));
[~, num_parent] = size(parent);

for i = 1: num_parent
    p = parent(1,num_parent+1-i); % prune from bottom 
    if p ==0 %root node
        break;
    end;
    index = T(6,:)~= p; % 
    T_ = T(:,index); % 
    T_(2:5, p) = 0;
    j = p + 1;
    while j <= size(T_,2)
        if T_(4,j) ~= 0
            T_(4,j) = T_(4,j) -2;
        end;
        if  T_(5,j)~= 0
            T_(5,j) = T_(5,j) -2;
        end;
        j = j + 1;
    end
    [ypredict]=evaltree(T,xTe);
    error = (y-ypredict)*(y-ypredict)';
    [ypredict_]=evaltree(T_,xTe);
    error_ = (y-ypredict_)*(y-ypredict_)';
    if error_<= error %if pruned tree has smaller testing error 
        T = T_; % then trim the original tree
    end;
end;