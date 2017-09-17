function D=l2distance(X,Z)
% function D=l2distance(X,Z)
%	
% Computes the Euclidean distance matrix. 
% Syntax:
% D=l2distance(X,Z)
% Input:
% X: dxn data matrix with n vectors (columns) of dimensionality d
% Z: dxm data matrix with m vectors (columns) of dimensionality d
%
% Output:
% Matrix D of size nxm 
% D(i,j) is the Euclidean distance of X(:,i) and Z(:,j)
%
% call with only one input:
% l2distance(X)=l2distance(X,X)
%

if (nargin==1) % case when there is only one input (X)
	%% fill in code here
    %display('Syntax: D=l2distance(X,Z)');
    D = l2distance(X,X);
else  % case when there are two inputs (X,Z)
	%% fill in code here
    [d,n]=size(X); % dimension of X
    [~,m]=size(Z);
    S = repmat(diag(X'*X),1,m);
    R = repmat(diag(Z'*Z),1,n);
    D2 = S - 2*X'*Z + R'; % nxm
    D = sqrt(abs(D2)); %D = D2;
    
end;
%

