library IEEE;
use IEEE.Std_Logic_1164.all;

entity mux is port (
	A, B, C, D: in std_logic_vector(3 downto 0);
	S: in std_logic_vector(1 downto 0);
	F: out std_logic_vector(3 downto 0)
);

architecture mux_arch of mux is begin
	F <= A when S = "00" else
		  B when S = "01" else
		  C when S = "10" else
		  D;
end mux_arch;