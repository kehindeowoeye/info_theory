function [Ixy,lambda]=MutualInfo(X,Y)
%%
% Estimating Mutual Information with Moon et al. 1995
% between X and Y
% Input parameter
% X and Y : data column vectors (nL*1, nL is the record length)
%
% Output 
% Ixy : Mutual Information
% lambda: scaled mutual information similar comparabble to
% cross-correlation coefficient
%
%  Programmed by 
%  Taesam Lee, Ph.D., Research Associate
%  INRS-ETE, Quebecc
%  Hydrologist 
%  Oct. 2010
%
%




%X=X';
%Y=Y';

d=2;
nx=length(X);
hx=(4/(d+2))^(1/(d+4))*nx^(-1/(d+4));

Xall=[X;Y];
sum1=0;
for i=1:nx

    pxy=p_mkde([X(i),Y(i)]',Xall,hx);
    px=p_mkde(X(i),X,hx);
    py=p_mkde(Y(i),Y,hx);
    sum1=sum1+log(pxy/(px*py));
end

Ixy=sum1/nx;

lambda=sqrt(1-exp(-2*Ixy));