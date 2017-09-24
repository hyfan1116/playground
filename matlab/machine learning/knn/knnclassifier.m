function preds=knnclassifier(xTr,yTr,xTe,k)
% function preds=knnclassifier(xTr,yTr,xTe,k);
%
% k-nn classifier 
%
% Input:
% xTr = dxn input matrix with n column-vectors of dimensionality d
% xTe = dxm input matrix with n column-vectors of dimensionality d
% yTr = 1xd?
% k = number of nearest neighbors to be found
%
% Output:
%
% preds = predicted labels, ie preds(j) is the predicted label of xTe(:,j)
%


% output random result as default (you can erase this code)
%[d,n]=size(xTe);
%[d,ntr]=size(xTr);
%if k>ntr,k=ntr;end;

%currently assigning random predictions
%un=unique(yTr);
%preds=un(ceil(rand(1,n)*length(un)));

%% fill in code here
    function res = findmost(col)
        valueCount = histc(col, unique(col));
        valueCount = sort(valueCount, 'descend');
        if(length(valueCount)==1)
            res = col(valueCount(1));
        else
            if(valueCount(1)==valueCount(2))
                res = findmost(col(end-1));
            else
                res = col(valueCount(1));
            end
        end
    end

[indi,dist]=findknn(xTr,xTe,k);
yTe = yTr(indi); % 9 9 9 
m = size(xTe,2);
preds = zeros(1,m);
%preds = mode(yTe); % mode: most frequent and first item
for i=1:m
    currentcol = yTe(:,i);
    preds(i) = findmost(currentcol);
end

%%
end
