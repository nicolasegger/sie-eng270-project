surface = uint8(zeros(100,100,3));
surface(40:60,:) = 60;
surface(1:40, :, 2)=200;
surface(1:40, :, 1)=150;
surface(1:40, :, 3)=90;
surface(60:100,:) = 200;
imshow(surface);

albedo_absorb = zeros(100,100);
albedo_absorb(1:40,:)= 0.25;
albedo_absorb(40:60,:) = 0.05;
albedo_absorb(60:100,:)= 0.4;
rayonnement = 1000;
sigma = 5.67e-8;
T_amb = 300;
k = 0.2;
h = 2;

temperature_h = W(T_amb, temperature_surface,k,h);
imagesc(temperature_h-273.15);
colorbar;
title('Temperature à 2m');

function temperature_h = W(T_amb, temperature_surface,k,h)
    temperature_h = T_amb + (temperature_surface-T_amb)*exp(-k*h);
end