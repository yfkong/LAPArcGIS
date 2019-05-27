import laparcgis2 as d
import time,sys
seed=-1
n=16
t=100
if len(sys.argv) >= 2:
    n=int(sys.argv[1])
if len(sys.argv) >= 3:
    t=int(sys.argv[2])
if len(sys.argv) >= 4:
    seed=int(sys.argv[3])

d.mip_solver=""
d.spatial_contiguity=1
d.operators_selected=[0,1]
d.solver_message=0
d.solution_similarity_limit=6.0
#edit the file path
d.readfile("C:\\PDP\\fldp_second\\arcgis\\zys_units.txt", "C:\\PDP\\fldp_second\\arcgis\\zys_connectivity.txt")
d.set_solver_params(n,"ils",20,t,9,-1)
d.solve()
#d.ga(n,20,t,0,0.7,0.03,9,seed)
d.print_solution()
