ville_matrix = [2 2 2 0 1 1 1;
        2 2 2 0 1 0 1;
        0 0 0 0 1 1 1;
        3 3 0 2 2 1 2;
        3 3 0 1 1 2 2;
        2 2 0 0 1 1 1;
        2 2 2 0 1 0 1;
        0 0 0 0 1 1 1;
        3 3 0 2 2 1 2;
        3 3 0 1 1 2 2];
disp(ville_matrix)


ville_struct(1).type = 'Route';      % correspond aux 0
ville_struct(1).emissivite = 0.99;

ville_struct(2).type = 'Maison';     % correspond aux 1
ville_struct(2).emissivite = 0.85;

ville_struct(3).type = 'Parc';       % correspond aux 2
ville_struct(3).emissivite = 0.98;

ville_struct(4).type = 'Stabilisé';  % correspond aux 3
ville_struct(4).emissivite = 0.91;


ville_ligne = ville_matrix(:);
emissivites = zeros(size(ville_ligne));

for i = 1:length(ville_ligne)
    type = ville_ligne(i);       % 0,1,2,3
    emissivites(i) = ville_struct(type+1).emissivite;
end

Llambda = 100;
lambda = 10.895e-6;
K1 = 1321.08;
K2 = 777.89;
rho = 1.438e-2;
BT = K2/log((K1./Llambda)+1);
emissivite_smooth = imgaussfilt(reshape(emissivites,size(ville_matrix)),2);


land_surface_temperature = LST(emissivite_smooth, BT,rho, lambda);
tempC = land_surface_temperature - 273.15;
disp([min(tempC(:)), max(tempC(:))])
imagesc(tempC, [min(tempC(:)) max(tempC(:))]);


colorbar;
title('Temperature de surface(°C)');


function land_surface_temperature = LST(emissivite,BT, rho, lambda)
    land_surface_temperature = BT./(1+(lambda* BT/rho)*log(emissivite));
end

