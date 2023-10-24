##git 사용법
# git init  # 초기화
# git add .  # 코드 전부 추가
# git commit -m ""  commit과 어떤 작업 했는지  git commit -m "first commit"
# git remote add origin (레포지토리 주소)
# git push origin master (master라는 branch명) #commit 한 것들이 전부 master로 저장
# git add.
# git commit -m ""
# git push origin master
# git branch develop #develop이라는 branch 생성
# git branch -d develop # develop이라는 branch 제거
# git branch  # 만들어진 branch 확인하기
# git switch develop #develop이라는 branch에 들어가기 
# git merge develop #develop branch와 병합 (master branch에서 merge 해주어야함(예시임))

# git branch 로 자기가 작업할 branch 만들고 switch로 접속
# 동일하게 git add .
# git commit -m ""로 저장
#git switch main (메인으로 돌아옴)
#git merge develop(내가 작업한 branch(develop))을 merge(병합)시킴.
#git push origin main
# git remote add upstream https://github.com/유저명/레포지토리명.git(main보다 upstream 에 추가?) 주소는 메인유저의 git주소
# --> 위 코드로 origin 위 upstream에 메인 유저의 깃주소 불러옴
# git remote -v 으로 불러왔는지 확인
# --> 불러오면 
#origin  https://github.com/내이름/레포지토리명.git (fetch)
#origin  https://github.com/내이름/레포지토리명.git (push)
#upstream        https://github.com/메인유저이름/레포지토리명.git (fetch)
#upstream        https://github.com/메인유저이름/레포지토리명.git (push)
# git pull upstream main # upstream에 내가 수정한 main코드 pull 해줌.

