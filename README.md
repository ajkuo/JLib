# JLib
自用 Python 函式庫 
  
 所有 Function 都使用 JSON 格式作為回傳內容，  
一律使用 Utils.GetApiJson() 統一回傳格式如下：  
   
 ### Success:  
{  
     "message": 自訂,   
     "result": True|False (此欄位為回傳結果，可用於判斷式，例如：傳入兩值判斷是否大於、是否相等), 
     "error": False  
}  
  
### Failure: 
{  
     "message": 必為文字,  
     "result": False,  
     "error": True,  
     "debug": 錯誤原因 (只在 Config.py 內 DEBUG_MODE = True 時顯示)  
}  
  
  
