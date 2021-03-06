# JLib
*持續補完中，歡迎協助開發。*
*(Still in development, welcome to send pull request.)*

**自用 Python 函式庫**

此函式庫所有回傳值皆為統一 JSON 格式，非常適合用來作為 API 調用。 

## 自訂函式 (Function)
此函式庫包含許多自訂函式檔案，其中必定會用到 **JConfig** 套件。

### 功能性
為達到模組效用，每個函式撰寫 **只做一件事**，並且盡量在有使用到 **傳入參數**(特別是非文字型態或需要判斷特定文字內容時) 及其他可能出現例外的情況下，包入 try-except 以免發生預期之外的錯誤。

### 傳入值
盡可能讓每個函式功能清晰易用，並保留傳入內容之彈性。
此外，必須在函式內撰寫功能說明及用法，撰寫方式如下：
```
from JLib.JConfig import Rsp

def Example(parameter1, parameter2):
    """
    此處撰寫功能說明及用法，力求精簡扼要，但不過度省略。
    parameter1: 參數 1 說明。
    parameter2: 參數 2 說明。
    return: 回傳值一律為 JSON 格式，若有必要請於此處稍作說明。
    """
    return Rsp.Dumps(...)
```


### 回傳值
所有 Function 都使用 JSON 格式作為回傳內容，並應包含 try-except， 
JSON 格式一律使用 JConfig 裡面的 Rsp Class 的 **Dumps()** ，以下統一格式如下說明： 
 
##### 程式正常執行結果：
{  
     "message": 自訂,  
     "result": (True | False),  
     "error": False,  
     "createTime": "2018-01-18 14:58:48.082225 (UTC)"  
}
  
  
##### 程式發生例外狀況：
{  
     "message": "{{必為文字}}",  
     "result": False,  
     "error": True,  
     "debug": "{{錯誤原因}}",  
     "createTime": "2018-01-18 14:58:48.082225 (UTC)"  
}  

##### JSON 內容說明
在使用 GetApiJson() 時，需傳入四項參數，分別為
1. message  
此參數為主要回傳內容，在 **執行失敗(發生例外)** 的情況下，必為一段文字；其他情況無任何限制，可自由設定回傳內容，亦可回傳 List, Dict 等。
2. result  
此參數為自訂的程式判斷結果，可用來當作判斷式是否正確的回傳值(例如：帳號密碼驗證），預設為 True。
3. error  
此參數用以判斷程式是否發生錯誤，建議在接收回傳時，先判斷此參數，確認程式正常執行後再做其他判斷。
4. debug  
此參數只在 Config.py 內的 DEBUG_MODE 設為 True 時，於程式發生例外錯誤時回傳，其他情況不回傳，請在每個函式內的 Except 將 Exception 以字串(str)形式傳入。

撰寫前請參考既有程式碼及以上說明，以保持程式彈性和穩定。

### 讀取回傳值
除了直接使用 `json.loads()` 讀取回傳值外，也可以使用 `Rsp.Loads()` 來讀取，此函式將回傳一個 `RspJson` Object，讓您可以直接呼叫各屬性。
