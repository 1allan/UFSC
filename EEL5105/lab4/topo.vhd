library IEEE;
use IEEE.Std_Logic_1164.all;

entity topo is port (
	SW: in std_logic_vector(9 downto 0);
	LEDR: out std_logic_vector(3 downto 0);
	HEX0: out std_logic_vector(6 downto 0);
);
end topo;

architecture topo_arch of topo is signal F: std_logic_vector(4 downto 0), G: std_logic;

component circuito1 is port (
	
);

end topo_arch; 