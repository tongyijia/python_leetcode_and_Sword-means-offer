#设置opr数组是为了存储数字的符号，应对+0,-0的情形
def to_subnormal(seq,opr):#将输入的序列转化为半法式
    le,i=len(seq),0
    print('转换成半法式:')
    while 1:
        if opr[i]==opr[i+1]:#都是正数的情形
            if seq[i]>seq[1+i]:
                if opr[i]=='+':# apply R1
                    old=opr_seq(opr,seq)
                    #print('R1:%d,%d->%d,%d'%(seq[i],seq[i+1],seq[i+1],seq[i]+1))
                    seq[i],seq[1+i]=seq[i+1],seq[i]+1
                    new=opr_seq(opr,seq)
                    print('R1:%s->%s'%(old,new))
                    i=0#当前的两个字进行了修改，需要从头重新进行判断
                elif opr[i]=='-':#apply R4
                    old=opr_seq(opr,seq)
                    #print('R4:%d,%d->%d,%d'%(seq[i],seq[i+1],seq[i+1]-1,seq[i]))
                    seq[i],seq[1+i]=seq[i+1]-1,seq[i]
                    new=opr_seq(opr,seq)
                    print('R4:%s->%s'%(old,new))
                    i=0#当前的两个字进行了修改，需要从头重新进行判断
            else:i+=1#当前的两个字合法，继续向后推进
        else:#符号相异的情形
            if opr[i]=='-' and opr[i+1]=='+':#此类情形肯定需要调整
                if abs(seq[i])>seq[i+1]:#apply R2
                    old=opr_seq(opr,seq)
                    #print('R2:%d,%d->%d,%d'%(seq[i],seq[i+1],seq[i+1],seq[i]-1))
                    seq[i],seq[1+i]=seq[i+1],seq[i]-1
                    opr[i],opr[i+1]='+','-'
                    new=opr_seq(opr,seq)
                    print('R2:%s->%s'%(old,new))
                    i=0#当前的两个字进行了修改，需要从头重新进行判断
                elif abs(seq[i])<seq[i+1]:#apply R3
                    old=opr_seq(opr,seq)
                    #print('R3:%d,%d->%d,%d'%(seq[i],seq[i+1],seq[i+1]+1,seq[i]))
                    seq[i],seq[1+i]=seq[i+1]+1,seq[i]
                    opr[i],opr[i+1]='+','-'
                    new=opr_seq(opr,seq)
                    print('R3:%s->%s'%(old,new))
                    i=0#当前的两个字进行了修改，需要从头重新进行判断
                else:#apply R5
                    old=opr_seq(opr,seq)
                    seq.remove(seq[i])#删掉这两个字
                    seq.remove(seq[i])
                    opr.remove(opr[i])
                    opr.remove(opr[i])
                    new=opr_seq(opr,seq)
                    print('R5:%s->%s'%(old,new))
                    le=len(seq)
                    i=0#当前的两个字进行了修改，需要从头重新进行判断
            else:i+=1#正负的情形，合法，向后推进
        if i==le-1:break#判断到了最后，所有的字都是合法的
    print('半法式:',opr_seq(opr,seq))
    
def opr_seq(opr,seq):
    l,s=len(seq),''
    for i in range(l):
        if seq[i]<0:
            s+=str(seq[i])+','
        elif seq[i]>0:
            s+='+'+str(seq[i])+','
        else:s+=opr[i]+str(seq[i])+','
    return s[:-1]#返回一个可以直接输出的序列,有符号和数字，例如-5,+3,+7,-9,-4,+0,-0
    
def proc(seq,opr,left,right):
    for i in range(len(seq)-1):
        if opr[i]!=opr[i+1]:#找到正负分界线
            lefto,righto=i,i+1
            break
    while left!=right-1:#循环到正负边界线
        if left!=lefto:
            old=opr_seq(opr,seq)
            #print('R1:%d,%d->%d,%d'%(seq[left],seq[1+left],seq[left+1]-1,seq[left]))
            seq[left],seq[left+1]=seq[left+1]-1,seq[left]
            new=opr_seq(opr,seq)
            print('R1逆:%s->%s'%(old,new))#应用R1的逆
            left+=1
        if right!=righto:
            print(str(right) +"----")
            old=opr_seq(opr,seq)
            #print('R4:%d,%d->%d,%d'%(seq[right-1],seq[right],seq[right],seq[right-1]+1))
            seq[right-1],seq[right]=seq[right],seq[right-1]+1
            new=opr_seq(opr,seq)
            print('R4逆:%s->%s'%(old,new))#应用R4的逆
            right-=1
    if seq[left]+seq[right]==0:
        old=opr_seq(opr,seq)
        seq.remove(seq[left])#删掉这两个字
        seq.remove(seq[left])
        opr.remove(opr[left])
        opr.remove(opr[left])
        new=opr_seq(opr,seq)
        print('删除正负二元组:%s->%s'%(old,new))#删除正负二元组
    #print('R5:%d,%d->1'%(seq[left],seq[right]))
    #return seq[:left]+seq[right+1:]


def to_normal(seq,opr):#将输入的半法式序列转化为法式
    print('转换成法式:')
    le,bound=len(seq),0
    for i in range(le):#找到正负分界线
        if opr[i]=='-':
            bound=i-1
            break
    while 1:
        for i in range(bound,-1,-1):#从正负分界线先前搜索非法的片段前端
            if -seq[i] in seq:
                if seq[i]+1 in seq or -seq[i]-1 in seq:
                    pass
                else:
                    for j in range(bound+1,le):#哭唧唧，为了应对后面有重复元素的情形
                        if seq[j]==-seq[i]:
                            break
                    proc(seq,opr,i,j)#处理这个片段
                    break
                    
        if i==0:#搜索到最前面，没有非法的了
            break
        else:
            for i in range(le):#更新bound重新搜索，要应对有多个非法元组的情形
                if opr[i]=='-':
                    bound=i-1
                    break

    print('法式:',opr_seq(opr,seq))  

def get_seq(seq,opr):#从输入得到目标序列
    temp=input('(示例：+4,-2,-5,+6)输入序列:')
    
    temp=temp.split(',')
    for i in range(len(temp)):#从输入序列得到seq和opr数组
        opr.append(temp[i][0])
        seq.append(int(temp[i]))
    print('Input sequence:',opr_seq(opr,seq))

def main():
    opr,seq=[],[]
    #opr,seq分别存储seq数组中的正负号和数值
    get_seq(seq,opr)
    to_subnormal(seq,opr)#得到半法式序列
    to_normal(seq,opr)#得到法式序列
    # print('最后结果：',seq)

        
if __name__=='__main__':
    main()
