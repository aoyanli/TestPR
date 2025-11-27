import requests
import json

def get_public_pull_requests(owner: str, repo: str):
    """
    获取一个公开仓库的所有 pull requests (默认最多返回30个)。
    
    Args:
        owner: 仓库的所有者 (例如: 'microsoft')
        repo: 仓库的名称 (例如: 'vscode')
    """
    # 构造 API URL
    url = f"https://api.github.com/repos/{owner}/{repo}/pulls"
    
    print(f"Fetching pull requests from: {url}")
    
    try:
        # 发送 GET 请求
        response = requests.get(url)
        
        # 检查响应状态码，如果不是 2xx，则抛出异常
        response.raise_for_status()
        
        # 将返回的 JSON 字符串解析为 Python 列表
        pull_requests = response.json()
        base_sha= pull_requests[0]['base']['sha']
        with open('first_pr.txt','w') as f:
            json.dump(base_sha,f)
    

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        # 打印更详细的错误信息
        if e.response is not None:
            print(f"Status Code: {e.response.status_code}")
            print(f"Response Body: {e.response.text}")
        return None

# --- 示例用法 ---
if __name__ == "__main__":
    # 尝试获取一个著名的公开仓库的 PR
    OWNER = "aoyanli"
    REPO = "TestPR"
    get_public_pull_requests(OWNER, REPO)