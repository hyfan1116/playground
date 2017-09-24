function [ypredict]=evaltree(T,xTe)
% function [ypredict]=evaltree(T,xTe);
%
% input:
% T0  | tree structure
% xTe | Test data (dxn matrix)
%
% output:
%
% ypredict : predictions of labels for xTe
%

%% fill in code here
[~, q] = size(T); %q: total number of nodes
[~,n] = size(xTe);
ypredict = zeros(1,n);
 

for i = 1:n %
    node = 1; %
    while node < q;
        if T(4,node)==0 && T(5,node)==0 %
            break; % 
        end;
       
        if xTe(T(2,node), i) <= T(3,node) 
            node =T(4,node);
        else
            node = T(5,node);
        end;
    end;
    ypredict(1,i) = T(1, node); %
end;

