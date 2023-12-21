# AutodiscoverErrorCode - перечисление
Defines the error codes that can be returned by the Autodiscover service.
## __Definition
 **Пространство имён:**
[Tessa.Exchange.WebServices.Autodiscover](N_Tessa_Exchange_WebServices_Autodiscover.htm)  
 **Сборка:** Tessa.Server (в Tessa.Server.dll) Версия: 3.6.0.17
C# __Копировать
     public enum AutodiscoverErrorCode
VB __Копировать
     Public Enumeration AutodiscoverErrorCode
C++ __Копировать
     public enum class AutodiscoverErrorCode
F# __Копировать
     type AutodiscoverErrorCode
##  __Члены
NoError| 0|  There was no Error.  
---|---|---  
RedirectAddress| 1|  The caller must follow the e-mail address redirection
that was returned by Autodiscover.  
RedirectUrl| 2|  The caller must follow the URL redirection that was returned
by Autodiscover.  
InvalidUser| 3|  The user that was passed in the request is invalid.  
InvalidRequest| 4|  The request is invalid.  
InvalidSetting| 5|  A specified setting is invalid.  
SettingIsNotAvailable| 6|  A specified setting is not available.  
ServerBusy| 7|  The server is too busy to process the request.  
InvalidDomain| 8|  The requested domain is not valid.  
NotFederated| 9|  The organization is not federated.  
InternalServerError| 10|  Internal server error.  
## __См. также
#### Ссылки
[Tessa.Exchange.WebServices.Autodiscover - пространство
имён](N_Tessa_Exchange_WebServices_Autodiscover.htm)
