import sys

if __name__=="__main__":
    if len(sys.argv) < 2:
        print("Usage: python script.py <input_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    count = 0
    name_score = {}
    with open(input_file, 'r') as file:
        for line in file:
            count += 1
            if (len(line.split()) != 2):
                print(f"Invalid input file format.({count})")
                print("Use: Name /t Score")
                sys.exit(1)
            name, score = line.split()
            try:
                name_score[name] = int(score)
            except ValueError:
                print(f"Invalid input file format.({count})")
                print("Score must be integer.")
                sys.exit(1)
    

# name_score = {Student1 : 91, Student2 : 54, ...}
# 코드 작성할 때 모든 line에 한 칸 들여쓰고 작성하는 것을 권장
# 코드 실행 방법: VScode 왼쪽 위 터미널 -> 새 터미널 -> "python 등급계산기.py score.txt" 입력


# [mission 1]
# 90점 이상은 A, 90점 미만 80점 이상은 B, 80점 미만 70점 이상은 C, 
# 70점 미만 60점 이상은 D, 60점 미만은 F이다. 
# 이를 기준으로 score.txt의 학생들의 등급을 출력하는 기능을 구현하고
# "등급 출력 구현"이라는 제목으로 commit
################################## < TO DO > ##################################
for studentName in name_score:
    a=name_score[studentName]
    if a>=90:
        grade='A'
    elif a>=80:
        grade='B'
    elif a>=70:
        grade='C'
    elif a>=60:
        grade='D'
    else:
        grade='F'

    print(f"{studentName}-{grade}")


###############################################################################


# [mission 2] 
# 전체 평균 출력 구현하고 "평균 출력 구현"이라는 제목으로 commit
################################## < TO DO > ##################################
def 개수(node):
    if node is None:
        return 0
    return 개수(node.left)+개수(node.right)+1
def 중앙값(node,fromL=0,fromR=0):
    if node is None:
        return -250
    L=fromL+개수(node.left)
    R=fromR+개수(node.right)
    if L==R or abs(L-R)==1:
        return node.value
    elif L<R:
        return 중앙값(node.right,L+1,fromR)
    else:
        return 중앙값(node.left,fromL,R+1)

class Node:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None
    def push(self,node:"Node"):
        if self.value<node.value:
            if self.right==None:
                self.right=node
            else:
                self.right.push(node)
        else:
            if self.left==None:
                self.left=node
            else:
                self.left.push(node)
root=None
for studentName in name_score:
    tmp=Node(name_score[studentName])
    if root==None:
        root=tmp
    else:
        root.push(tmp)
print(중앙값(root))









###############################################################################


# [mission 3]
# 현재까지 수행한 과정을 push하여 원격 레포지토리에 올리기


# [mission 4]
# "등급 출력 구현" commit으로 checkout하여 mission 1의 코드만 작성되어 있는 것을
# 확인해본 후 다시 원래 위치로 돌아오기


# [mission 5] 
# 평균보다 중앙값을 출력하는 것이 더 유용할 수 있겠다는 생각이 들어서
# 평균 대신 중앙값을 출력하려고 한다. 단, 아직 어느 것이 더 유용할지 모르기 때문에
# "등급 출력 구현" commit에서 "feature"라는 이름의 branch를 생성하여 구현한 후 
# "평균값->중앙값 대체"라는 제목으로 commit. 코드는 mission 2의 < TO DO >에 구현


# [mission 6]
# "feature" 브랜치를 작업하다보니 최고점과 최저점도 출력을 하는게 유용할 것이라는
# 생각이 들었다. 해당 브랜치에서 최고점과 최저점도 출력하도록 코드를 구현하고 
# "Min,Max 출력 구현" 라는 제목으로 commit
################################## < TO DO > ##################################
    






    
###############################################################################


# [mission 7]
# 중앙값보다는 평균을 출력하는 것이 더 유용하다는 결론이 나왔다. 
# 그러나 "feature" 브랜치에서 구현한 최고점과 최저점 출력 기능은은 유지하려한다.
# "feature" 브랜치를 main 브랜치에 merge 하기 


# [mission 8]
# 현재까지 수행한 과정을 push하여 원격 레포지토리에 올리기