function output=analyze(kind,truth,preds)	
% function output=analyze(kind,truth,preds)		
%
% Analyses the accuracy of a prediction
% Input:
% kind='acc' classification error
% kind='abs' absolute loss
% (other values of 'kind' will follow later)
% 

switch kind
	case 'abs'
		% compute the absolute difference between truth and predictions
		%% fill in the code here
        oa = truth - preds;
        output = sum(abs(oa))/length(oa);
		
	case 'acc' 
		%% fill in code here
        ob = (truth==preds);
		output = sum(ob)/length(ob);
        
end;

