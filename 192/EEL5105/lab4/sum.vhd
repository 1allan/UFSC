library IEEE;
use IEEE.Std_Logic_1164.all;
use IEEE.std_logic_unsigned.all;

entity sum is port (
	A: in std_logic_vector(3 downto 0);
	B: in std_logic_vector(3 downto 0);
	F: out std_logic_vector(3 downto 0)
);
end sum;

architecture sum_arch of sum is begin
	F <= A + B;
end sum_arch; 