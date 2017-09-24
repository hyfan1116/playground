function [ num_iters, bounds] = perceptron_experiment ( N, d, num_samples )
%perceptron_experiment Code for running the perceptron experiment in HW1
%   Inputs: N is the number of training examples
%           d is the dimensionality of each example (before adding the 1)
%           num_samples is the number of times to repeat the experiment
%   Outputs: num_iters is the # of iterations PLA takes for each sample
%            bound_minus_ni is the difference between the theoretical bound
%               and the actual number of iterations
%      (both the outputs should be num_samples long)
resultpexp = zeros(2,num_samples);
    for samplenum = 1:num_samples
        sizeofdata = N;
        ws = rand((d+1),1);
        ws(1) = 0;
        xtest = -1+2*rand((d+1),sizeofdata);
        xtest(1,:) = ones(1,sizeofdata);
        ytest = sign(ws'*xtest);
        datatest = [xtest;ytest];
        [rw,ri] = perceptron_learn(datatest');
        num_iters = ri;
        bRho = min(ytest.*(ws'*xtest));
        bR2 = max(sum(xtest.*xtest));
        tbound = (bR2)*(ws'*ws)/(bRho*bRho);
        bounds = tbound - num_iters;
        resultpexp(1,samplenum) = num_iters;
        resultpexp(2,samplenum) = bounds;
    end
    histogram(resultpexp(1,:));
    xlabel('num iters');
    ylabel('times')
    figure;
    histogram(log(resultpexp(2,:)));
    xlabel('log(bounds)');
    ylabel('counts')
end

