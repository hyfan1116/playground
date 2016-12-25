function [ w, iterations ] = perceptron_learn( data_in )
%perceptron_learn Run PLA on the input data
%   Inputs: data_in: Assumed to be a matrix with each row representing an
%                    (x,y) pair, with the x vector augmented with an
%                    initial 1, and the label (y) in the last column
%   Outputs: w: A weight vector (should linearly separate the data if it is
%               linearly separable)
%            iterations: The number of iterations the algorithm ran for
    iterations = 0;
    %dim = 
    w = zeros(11,1);
    x = (data_in(:,1:11))';
    y = (data_in(:,12))';
    while true
        updateflag = false;
        tempsize = size(x);
        for i = 1:(tempsize(2))
            %x(:,i)
            if sign(w'*x(:,i))~=y(1,i)
                w = w + y(:,i)*x(:,i);
                iterations = iterations+1;
                updateflag = true;
            end
        end
        if ~updateflag
            break;
        end
    end
    %return;
end

