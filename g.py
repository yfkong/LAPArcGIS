import laparcgis as d
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

d.spatial_contiguity=1
d.solver_message=0
d.mip_solver="cbc"
#edit the file path
d.readfile("C:\\PDP\\fldp_second\\arcgis\\zys_units.txt", "C:\\PDP\\fldp_second\\arcgis\\zys_connectivity.txt")
d.operators_selected=[0,1]
d.solution_similarity_limit=6.0
d.ga(n,20,t,0,0.7,0.03,9,seed)
print d.centersID
for x in d.all_solutions:
    print x[0],x[1]
