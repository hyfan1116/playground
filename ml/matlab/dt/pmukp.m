function res=pmukp(m,k,n)
%n=k;
if(m>1 && k>1)
    res=pmukp(m,k-1,n)*m/n+pmukp(m-1,k-1,n)*(1-(m-1)/n);
elseif(m==1)
    if(k==1)
        res=1;
    else
        res=(1/n).^(k-1);
    end;
else
    res=0;
end;