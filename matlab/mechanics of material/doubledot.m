A= [8,0,0;0,8,0;0,0,8];
B= [-5,6,0;6,1,0;0,0,4];

idx = max(0, ndims(A) - 1); %// Index of first common dimension
B_t = permute(B, circshift(1:ndims(A) + ndims(B), [0, idx - 1]));
double_dot_prod = squeeze(sum(squeeze(sum(bsxfun(@times, A, B_t), idx)), idx));
double_dot_prod

