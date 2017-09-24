%t = linspace(-90,90);
t = [0,-45,45,90]';

E1 = 18.7*10^6;
E2 = 1.9*10^6;
G12 = 0.85*10^6;
v12 = 0.30;
v21 = v12*E2/E1;

q11 = E1/(1-v12*v21);
q22 = E2/(1-v12*v21);
q66 = G12;
q12 = v12*E2/(1-v12*v21);

% qbar: q11, q12, q22, q16, q26, q66
qb1 = q11.*(cosd(t)).^4 + 2.*(q12+2*q66).*(sind(t).^2).*(cosd(t).^2)+q22.*(sind(t).^4);
qb2 = (q11 + q22 - 4*q66).*(sind(t).^2).*(cosd(t).^2)+q12.*(sind(t).^4+cosd(t).^4);
qb3 = q11.*(sind(t).^4) + 2.*(q12+2*q66).*(sind(t).^2).*(cosd(t).^2)+q22.*(cosd(t).^4);
qb4 = (q11 - q12 - 2*q66).*sind(t).*(cosd(t).^3)+(q12 - q22 +2*q66).*(sind(t).^3).*cosd(t);
qb5 = (q11 - q12 - 2*q66).*(sind(t).^3).*cosd(t)+(q12 - q22 +2*q66).*sind(t).*(cosd(t).^3);
qb6 = (q11+q22-2*q12-2*q66)*(sind(t).^2).*(cosd(t).^2)+q66.*(sind(t).^4+cosd(t).^4);

q = [qb1,qb2,qb3,qb4,qb5,qb6]; % [||||||]
q00 = q(1,:);
q45m = q(2,:);
q45 = q(3,:);
q90 = q(4,:);

% num of ply 
% on one side
thickness = 0.052;
numofply = 4;
zk = thickness*linspace(1-numofply,numofply,2*numofply);
zkm1 = thickness*linspace(-numofply,numofply-1,2*numofply);
zkd1 = (zk - zkm1);
zkd3 = (zk.^3-zkm1.^3)/3;
zkd1rep = repmat(zkd1',1,6);
zkd3rep = repmat(zkd3',1,6);

% arrangement
% should be full
%qa = [q00;q45;q45m;q90;q90;q45m;q45;q00];
qa = [q45;q45m;q90;q90;q90;q90;q45m;q45];

qaA = qa.*zkd1rep;
qaAsum = sum(qaA);
Aa = [qaAsum(1),qaAsum(2),qaAsum(4);qaAsum(2),qaAsum(3),qaAsum(5);qaAsum(4),qaAsum(5),qaAsum(6)];
qaD = qa.*zkd3rep;
qaDsum = sum(qaD);
Da = [qaDsum(1),qaDsum(2),qaDsum(4);qaDsum(2),qaDsum(3),qaDsum(5);qaDsum(4),qaDsum(5),qaDsum(6)];

aa = inv(Aa);
ttt = thickness*numofply*2;
Ex = 1/(ttt*aa(1,1));
Ey = 1/(ttt*aa(2,2));
Gxy = 1/(ttt*aa(3,3));
vxy = -aa(1,2)/aa(1,1);
XY = [Ex, Ey, Gxy, vxy];
disp(Aa);
disp(aa);
disp(Da);
disp(XY);
