function [pxy]=p_mkde(x,X,h)

s1=size(X);
d=s1(1);
N=s1(2);

Sxy=cov(X');
sum=0;
%p1=1/sqrt((2*pi)^d*det(Sxy))*1/(N*h^d);

invS=inv(Sxy);
detS=det(Sxy);
for ix=1:N
    p2=(x-X(:,ix))'*invS*(x-X(:,ix));
    sum=sum+1/sqrt((2*pi)^d*detS)*exp(-p2/(2*h^2));
end
pxy=1/(N*h^d)*sum;
