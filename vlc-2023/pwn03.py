import subprocess

# 二分探索対象の文字列の長さの下限と上限
lower_bound = 0
upper_bound = 1000

# 接続先情報
host = "10.10.10.15"
port = 1003

# コマンド実行を行う関数
def run_command(command):
    try:
        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        stdout, stderr = process.communicate(timeout=5)  # タイムアウトを5秒に設定
        return stdout.strip()
    except subprocess.CalledProcessError as e:
        return e.output.strip()
    except subprocess.TimeoutExpired:
        # タイムアウトが発生した場合も接続を閉じる
        process.kill()
        process.communicate()

# 二分探索を実行する関数
def binary_search_length(lower, upper):
    while upper - lower >  1:
        # 中央の長さを計算
        mid = (lower + upper) // 2
        # 中央の長さで接続を試す
        query = "flag" * mid
        print(query)
        command = f'echo {query} | nc {host} {port}'
        output = run_command(command)
        print(output)
        # 応答によって次に試す範囲を絞り込む
        # if "success" in output:
        #     # 成功した場合は上限を下げる
        #     upper = mid - 1
        is_ng = "flag" not in output
        if is_ng:
            upper = mid - 1
        else:
            lower = mid
        #     # 失敗した場合は下限を上げる
        #     lower = mid + 1
        # else:
        #     # 不明な応答の場合も下限を上げる
        #     lower = mid + 1

    # 最終的な長さを返す
    return lower

# 二分探索を実行して最適な長さを取得
optimal_length = binary_search_length(lower_bound, upper_bound)
print("Optimal length:", optimal_length)
