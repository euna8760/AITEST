import os
from github import Github

def main():
    print("AI Code Review 시작!")
    
    # 환경 변수에서 정보 가져오기
    github_token = os.environ.get('GITHUB_TOKEN')
    pr_number = int(os.environ.get('PR_NUMBER'))
    repo_name = os.environ.get('GITHUB_REPOSITORY')
    
    # GitHub API 연결
    g = Github(github_token)
    repo = g.get_repo(repo_name)
    pr = repo.get_pull(pr_number)
    
    # PR 정보 출력
    print(f"PR 제목: {pr.title}")
    print(f"변경된 파일 수: {pr.changed_files}")
    
    # 간단한 댓글 남기기
    pr.create_issue_comment("🤖 AI 리뷰가 곧 시작됩니다!")

if __name__ == "__main__":
    main()
