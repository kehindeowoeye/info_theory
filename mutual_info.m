function gr = mutual_info(dez)
%Download the mutual information function from the
%Matlab information theory File exchange site.
%The input should be a columnn wise matrix of the
%time-series of interest. 
gh = [];gr = []; 
for j = 1:size(dez,2)
    for k = 1:size(dez,2)
        gh = horzcat(gh,MutualInfo((dez(:,j)),(dez(:,k)))); 
    end 
    gr = vertcat(gr,gh); 
    gh = []; 
end 
