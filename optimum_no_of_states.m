%selects the optimum number of states using GMM
rng default

yp=[];yp = 0;
acc = data;


for j = 1:100
  AIC = zeros(1,20);
   obj = cell(1,20);

 for k = 1:20
   obj{k} = fitgmdist(acc,k,'RegularizationValue',0.1);
   AIC(k)= obj{k}.AIC;
 end
 [minAIC,numComponents] = min(AIC);yp = horzcat(yp,numComponents);
end
yp = mean(yp);
