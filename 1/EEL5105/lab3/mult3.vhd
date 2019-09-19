library IEEE;
use IEEE.Std_Logic_1164.all;

entity mult3 is port (
	Z: in std_logic_vector(3 downto 0);
	R: out std_logic_vector(4 downto 0));
end mult3;

architecture mult3arch of mult3 is signal E: std_logic_vector(4 downto 0);

component somador is port (
	X3,X2,X1,X0: in std_logic;
	Y3,Y2,Y1,Y0: in std_logic;
	S4,S3,S2,S1,S0: out std_logic
);
end component somador;

begin
	SUM1: somador port map (Z(3),Z(2),Z(1),Z(0),Z(3),Z(2),Z(1),Z(0),E(4),E(3),E(2),E(1),E(0));
	SUM2: somador port map (Z(3),Z(2),Z(1),Z(0),E(3),E(2),E(1),E(0),R(4),R(3),R(2),R(1),R(0));
end mult3arch;