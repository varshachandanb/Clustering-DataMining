import math
import sys
import copy
import re

def calc_centroid():
    initial_cluster={}
    all_points=[]
    cluster={}
    final_cluster=[]
    cl_names=[]
    inpt2=open(dataFileName,"r")
    otpt=open("output1.txt","w")
    lines2=inpt2.readlines()
    for m in range(len(lines2)):
        if(lines2[m]=='\n'):
            break
        lines2[m]=lines2[m].strip()
        temp2=lines2[m].split(',')
        val=[]
        for n in range(len(temp2)-1):
            val.append(float(temp2[n]))
        all_points.append(val)
        vl=''.join(str(val))
        initial_cluster[vl]=str(temp2[len(temp2)-1])
    inpt2.close()
    min=99999.9999
    centroid=copy.deepcopy(initial_centroid)
    for p in range(Iter):
        cluster={}
        temp_all_points=copy.deepcopy(all_points)
        for q in range (len(temp_all_points)):
            min=99999.999
            min_index=0
            for r in range(k):
                if r not in cluster:
                    cluster[r]=[]
                sm=0.0
                sqsum=0.0
                for s in range(points):
                    sm+=(float(temp_all_points[q][s])-float(centroid[r][s]))**2
                sqsum=math.sqrt(sm)
                if(sqsum<min):
                    min=sqsum
                    min_index=r
            cluster[min_index].append(temp_all_points[q])
        centroid={}
        sum=0.0
        avg=0.0
        for l in range(k):
            sum=0.0
            avg=0.0
            centroid[l]=[]
            for m in range(points):
                sum=0.0
                avg=0.0
                for n in range(len(cluster[l])):
                    sum=sum+float(cluster[l][n][m])
                avg=sum/len(cluster[l])
                centroid[l].append(avg)
        count=0
        if(p==(Iter-1)):
            for x in range(k):
                final_cluster=[]
                cl_names=[]
                cluster_count=[]
                max=0
                mx_name=""
                #otpt.write("Cluster "+cluster_name[x]+'\n')
                for y in range(len(cluster[x])):
                    name=initial_cluster[str(cluster[x][y])]
                    if name not in str(cluster_name[x]):
                        count+=1
                    subs=", '"+str(name)+"']"
                    temp = re.sub(']',subs, str(cluster[x][y]))
                    final_cluster.append(str(temp))
                    cl_names.append(name)
                for z in range(len(cluster_name)):
                    cnt=cl_names.count(cluster_name[z])
                    if(cnt>max):
                        max=cnt
                        mx_name=cluster_name[z]
                otpt.write("Cluster "+mx_name+'\n')
                for a in range(len(final_cluster)):
                    otpt.write(str(final_cluster[a])+'\n')
                otpt.write('\n')
            otpt.write("Number of points assigned to wrong cluster:"+'\n'+str(count))
    otpt.close()

if __name__ == '__main__':
    cluster_name={}
    initial_centroid={}
    points=0
    k=3
    Iter=10
    dataFileName="iris.data"
    initialPoints="initialPoints"
    inpt=open(initialPoints,"r")
    lines=inpt.readlines()
    line_count=0
    for m in range(len(lines)):
        if(lines[m]=='\n'):
            break
        line_count+=1

    if(k != line_count):
        print "The initial centroid count is not equal to value of k given in the input"
        sys.exit()
    for i in range(k):
        if(lines[i]=='\n'):
            break
        lines[i]=lines[i].strip()
        temp=lines[i].split(',')
        points=len(temp)-1
        key=temp[len(temp)-1]
        val=[]
        for j in range(len(temp)-1):
            val.append(temp[j])
        initial_centroid[i]=val
        cluster_name[i]=key
    inpt.close()
    calc_centroid()

