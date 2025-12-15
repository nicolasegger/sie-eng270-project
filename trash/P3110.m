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
clims = [20 100];
albedo_smooth = imgaussfilt(albedo_absorb,10);


temperature_surface = stefan(albedo_smooth,rayonnement,sigma);
imagesc(temperature_surface-273.15, clims);


colorbar;
title('Temperature de surface(°C)');

function temperature_surface = stefan(albedo_absorb, rayonnement,sigma)
    temperature_surface = (((1-albedo_absorb).*rayonnement)./(0.95*sigma)).^(1/4);
end
