library IEEE;
use IEEE.Std_Logic_1164.all;

entity e1 is port (
	HEX5, HEX4, HEX3, HEX2, HEX1, HEX0: out std_logic_vector(6 downto 0);
);
end e1;

architecture e1_arch of e1 is begin
	HEX0 <= "1000110"; -- C
	
	HEX1 <= "0011100"; -- º
	
	HEX2 <= "0100100" when SW(0) = '0' else -- 5
			  "1000000";						  -- 0
	
	HEX3 <= "0100100" when SW = "00" else -- 2 0100100
			  "0110000" when SW = "01" else -- 3
			  "0011001" when SW = "10" else -- 4
		     "0000000";						  -- 0

	HEX4 <= "0000111" when SW = "11" else
			  "1111111";
	
	HEX5 <= "0001011" when SW = "11" else
			  "1111111";
end e1_arch;