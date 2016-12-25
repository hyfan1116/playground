function preds=evalboost(BDT,xTe)
% function preds=evalboost(BDT,xTe);
%
% Evaluates a boosted decision tree on a test set xTe.
%
% input:
% BDT | Boosted Decision Trees
% xTe | matrix of m input vectors (matrix size dxm)
%
% output:
%
% preds | predictions of labels for xTe
%

%% fill in code here
alpha = cell2mat(BDT(2)); % 
BDT = cell2mat(BDT(1)); % 

[~,n] = size(alpha); 
[d, m] = size(xTe);

% predictions from all weak trees
preds_tree = ones(n, m);
for i = 1:n
	T = BDT(6 * (i - 1) + 1 : 6 * i, :); %
	preds_tree(i, :) =  evaltree(T,xTe); % 
end

% 
preds = ones(1, m);
labels = unique(preds_tree); %
[l,~] = size(labels); % 
votes = zeros(1, l); % vector used to store weighted votes for each label
for i = 1:m
	for j = 1:l
		indice_label = find(preds_tree(:, i) == labels(j)); 
		preds_tree_temp = preds_tree(:, i);
        votes(j) = alpha(indice_label) * preds_tree_temp(indice_label); 
	end %
	[~, index_pred] = max(votes); %
	preds(i) = labels(index_pred); % 
end;
