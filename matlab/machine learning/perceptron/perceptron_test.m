sizeofdata = 100;
ws = rand(11,1);
ws(1) = 0;
xtest = -1+2*rand(11,sizeofdata);
xtest(1,:) = ones(1,sizeofdata);
ytest = sign(ws'*xtest);
datatest = [xtest;ytest];
%[weight,iter] = perceptron_learn(datatest');

%rho = min(ytest.*(ws'*xtest));
%R*R = max(sum(xtest.*xtest))