transcript on
if {[file exists rtl_work]} {
	vdel -lib rtl_work -all
}
vlib rtl_work
vmap work rtl_work

vcom -93 -work work {/home/allan/Desktop/UFSC/1/EEL5105/exe2/e1.vhd}

