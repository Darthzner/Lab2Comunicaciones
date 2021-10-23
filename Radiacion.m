samples = [ 0:22.5:360 ];
values  = [-62 -61 -52.5 -50 -43 -40 -39 -38 -41.2 -45 -50.5 -66 -66 -65.5 -61 -54.5 -62];
test    = [0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0];


figure;
patternCustom(values,samples,test, "CoordinateSystem", ...
    "polar","Slice",'phi','SliceValue',0)