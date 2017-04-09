%t = linspace(-90,90);
t = [0,-45,45,90,22.5,-22.5]';

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

% each term of t
q = [qb1,qb2,qb3,qb4,qb5,qb6]; % [||||||]
q00 = q(1,:);
qr(:,:,1) = q126toqreal(q00);
q45m = q(2,:);
qr(:,:,2) = q126toqreal(q45m);
q45 = q(3,:);
qr(:,:,3) = q126toqreal(q45);
q90 = q(4,:);
qr(:,:,4) = q126toqreal(q90);
q225 = q(5,:);
qr(:,:,5) = q126toqreal(q225);
q225m = q(6,:);
qr(:,:,6) = q126toqreal(q225m);

% num of ply 
% on one side 
thickness = 0.0052;
numofply = 2;
zk = thickness*linspace(1-numofply,numofply,2*numofply);
zkm1 = thickness*linspace(-numofply,numofply-1,2*numofply);
zkd1 = (zk - zkm1);
zkd3 = (zk.^3-zkm1.^3)/3;
zkd1rep = repmat(zkd1',1,6);
zkd3rep = repmat(zkd3',1,6);

% arrangement
% should be full
qa = [q00;q90;q90;q00];

qaA = qa.*zkd1rep;
qaAsum = sum(qaA);
Aa = [qaAsum(1),qaAsum(2),qaAsum(4);qaAsum(2),qaAsum(3),qaAsum(5);qaAsum(4),qaAsum(5),qaAsum(6)];
qaD = qa.*zkd3rep;
qaDsum = sum(qaD);
Da = [qaDsum(1),qaDsum(2),qaDsum(4);qaDsum(2),qaDsum(3),qaDsum(5);qaDsum(4),qaDsum(5),qaDsum(6)];

aa = inv(Aa);

%disp(Aa);
%disp(aa);
%disp(Da);

wxy = zeros(3);
for i = 1:3
    for j = 1:3
        m = 2*i-1;
        n = 2*j-1;
        wT = Da(1)*(m/20).^4+2*(Da(2)+2*Da(9))*(m*n/20/20).^2+Da(5)*(n/20).^4;
        wxy(i,j) = (16*0.01/pi^6)*(sin(m*pi*10/20)*sin(n*pi*10/20)/(m*n*wT));
    end
end
disp(sum(sum(wxy)))