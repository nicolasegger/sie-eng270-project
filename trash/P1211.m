surface = uint8(zeros(100,100,3));
surface(40:60,:) = 60;
surface(1:40, :, 2)=200;
surface(1:40, :, 1)=150;
surface(1:40, :, 3)=90;
surface(60:100,:) = 200;
imshow(surface);

emissivite = zeros(100,100);
emissivite(1:40,:)= 0.98;
emissivite(40:60,:) = 0.91;
emissivite(60:100,:)= 0.85;

Llambda = 100;
lambda = 10.895e-6;
K1 = 1321.08;
K2 = 777.89;
rho = 1.438e-2;
%A typical top-of-atmosphere (TOA) spectral radiance example would be a value 
% like \(3.5\text{\ W\ m}^{-2}\text{\ sr}^{-1}\text{\ m}^{-1}\) for a specific band and sensor, 
% although the exact value varies widely depending on the surface, the atmosphere, and sensor characteristics.
BT = K2/log((K1./Llambda)+1);
emissivite_smooth = imgaussfilt(emissivite,2);


land_surface_temperature = LST(emissivite_smooth, BT,rho, lambda);
tempC = land_surface_temperature - 273.15;
disp([min(tempC(:)), max(tempC(:))])
imagesc(tempC, [min(tempC(:)) max(tempC(:))]);


colorbar;
title('Temperature de surface(°C)');


function land_surface_temperature = LST(emissivite,BT, rho, lambda)
    land_surface_temperature = BT./(1+(lambda* BT/rho)*log(emissivite));
end