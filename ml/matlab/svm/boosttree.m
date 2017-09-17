function BDT=boosttree(x,y,nt,maxdepth)
% function BDT=boosttree(x,y,nt,maxdepth)
%
% Learns a boosted decision tree on data X with labels y.
% It performs at most nt boosting iterations. Each decision tree has maximum depth "maxdepth".
%
% INPUT:
% X  | input vectors dxn
% y  | input labels 1xn
% nt | number of trees (default = 100)
% maxdepth | depth of each tree (default = 3)
%
% OUTPUT:
% BDT | Boosted DTree
%


%% fill in code here

[d, n] = size(x);

if nargin < 4
	maxdepth = 3;
end

if nargin < 3
	nt = 100;
end

% initialize parameters
w = ones(1, n) / n;
alpha = zeros(1, nt);
eps = zeros(1, nt);
BDT = zeros(6*nt, 2^maxdepth - 1); % 6*nt rows for trees' nodes (each node need 6 rows)

for t = 1:nt
	h = id3tree(x,y,maxdepth,w);
	pred = evaltree(h, x);
	indicate = (pred ~= y);
	eps = w * indicate'; 
	
	% exit when h(t) has become so large that alpha(t) is meaningless
	if eps > 0.5
		break; 
	end
	
	alpha(t) = 0.5 * log2((1-eps)/eps); % update the weight for h(t)
	
	% update weights for training points
	w = w .* exp(alpha(t) * (2*(pred ~= y) - 1)); % amazing exp() can take an array!!! as parameter
	z = sum(w);
	w = w / z; % rescale weights so that they add to 1
	
	% add the T into BDT, starting from row 1
	BDT(6 * (t - 1) + 1 : 6 * t, :) = h;
end

BDT = {BDT, alpha}; % again, I hate the cell array. It' so much worse than R list.
