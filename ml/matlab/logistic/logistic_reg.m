function [ w, e_in ] = logistic_reg( X, Y, max_its,w,eta,epsilon )
%LOGISTIC_REG Learn logistic regression model using gradient descent
%   Inputs:
%       X : data matrix
%       Y : data labels (plus or minus 1)
%	max_its : max iteration number
%	w : initial weight vector
%	eta : learning rate
%	epsilon : algorithm terminate tolerance
%   Outputs:
%       w : weight vector
%       e_in : in-sample error (as defined in LFD)
N = size(X,1);
X = [ones(N,1),X];
for i=1:1:max_its
    g = 0;
    for j=1:1:N
        g = g + Y(j) * X(j,:) / (1 + exp(Y(j) * X(j,:) * w));
    end
    g = -g / N;
    v = -g';
    w = w + eta * v;
    if sum(g.^2 > epsilon^2) == 0
        break;
    end
end
e_in = sum(log(1 + exp(-Y .* (X * w)))) / N;
end

