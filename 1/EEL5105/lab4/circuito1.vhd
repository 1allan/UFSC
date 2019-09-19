library IEEE;
use IEEE.Std_Logic_1164.all;

entity circ1 is port (
	A: in std_logic_vector (2 downto 0);
	B: in std_logic_vector (2 downto 0);
	F1, F2, F3, F4: out std_logic_vector (3 downto 0)
);
end circ1;

architecture circ1_arch of circ1 is begin
	F1 <= '0' & A;
	F2 <= A & '0';
	F3 <= '0' & B;
	F4 <= B & '0';
end circ1_arch; 