library IEEE;
use IEEE.Std_Logic_1164.all;

entity somador is
port (
	X3,X2,X1,X0: in std_logic;
	Y3,Y2,Y1,Y0: in std_logic;
	S4,S3,S2,S1,S0: out std_logic
);
end somador;

architecture soma of somador is signal C0,C1,C2: std_logic;

component halfadder is port (
	A: in std_logic;
	B: in std_logic;
	Sum: out std_logic;
	Cout: out std_logic
);
end component halfadder;

component fulladder is port (
	A: in std_logic;
	B: in std_logic;
	Cin: in std_logic;
	Sum: out std_logic;
	Cout: out std_logic
);
end component fulladder;

begin
	HA: halfadder port map (X0,Y0,S0,C0);
	FA1: fulladder port map(X1,Y1,C0,S1,C1);
	FA2: fulladder port map(X2,Y2,C1,S2,C2);
	FA3: fulladder port map(X3,Y3,C2,S3,S4);
end soma;