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

d.mip_solver="cbc" #mip solver such as cbc or cplex
d.spatial_contiguity=1 # constraints on spatial contiguity
d.operators_selected=[0,1]
#local search operators
#0-one unit shift
#1-two units shift
#2-three unit shift
d.solver_message=0
d.solution_similarity_limit=6.0
#edit the file path
d.readfile("C:\\PDP\\fldp_second\\arcgis\\zys_units.txt", "C:\\PDP\\fldp_second\\arcgis\\zys_connectivity.txt")
d.set_solver_params(n,"ils",20,t,2,-1)
# parameters: num of facilities, algorithm, population size, time limit, spp procedure,and random seed
d.solve()
print "selected facilities and service areas:"
print "Id X Y demand suppy selected RID"
for x in range(d.num_units):
    print d.nodes[x][4],d.nodes[x][1],d.nodes[x][2],d.nodes[x][3],d.nodes[x][5],
    selected=0
    if x in d.centersID:
        selected=1
    rid=d.node_groups[x]
    uid=d.centersID[rid] 
    print selected, d.nodes[uid][4]
        
