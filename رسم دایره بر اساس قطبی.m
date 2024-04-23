img = zeros (300,300);
x = 150;
y = 150;
radius = 100;
for zaveye = linspace (0,2*pi,1000)
    
    x1 = round (x+radius*cos (zaveye));
    y1 = round (y+radius*sin (zaveye));
    if x >= 1 && x<=300 && y>=1 && y<=300 
        
        img (x1,y1)= 255;
    end
end
imshow(img);