n= int(input("enter the number of nodes to chech wheather it is a mesh topology :"))
l=[]
x = True
for i in range(n):
    r =input(f"enter {i+1} row:" )
    l.append(r)
    if r.count("0")>0:
        x = False
if x == True:
    print("it's a Mesh Topology")
else:
    print("it's not a Mesh Topology")