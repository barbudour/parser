# AutodiscoverRedirectionUrlValidationCallback - делегат
Defines a delegate that is used by the AutodiscoverService to ask whether a
redirectionUrl can be used.
## __Definition
 **Пространство имён:**
[Tessa.Exchange.WebServices.Autodiscover](N_Tessa_Exchange_WebServices_Autodiscover.htm)  
 **Сборка:** Tessa.Server (в Tessa.Server.dll) Версия: 3.6.0.17
C# __Копировать
     public delegate bool AutodiscoverRedirectionUrlValidationCallback(
    	string redirectionUrl
    )
VB __Копировать
     Public Delegate Function AutodiscoverRedirectionUrlValidationCallback ( 
    	redirectionUrl As String
    ) As Boolean
C++ __Копировать
     public delegate bool AutodiscoverRedirectionUrlValidationCallback(
    	String^ redirectionUrl
    )
F# __Копировать
     type AutodiscoverRedirectionUrlValidationCallback = 
        delegate of 
            redirectionUrl : string -> bool
#### Параметры
redirectionUrl [String](https://learn.microsoft.com/dotnet/api/system.string)
    Redirection URL that Autodiscover wants to use.
#### Возвращаемое значение
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)  
Delegate returns true if Autodiscover is allowed to use this URL.
##  __См. также
#### Ссылки
[Tessa.Exchange.WebServices.Autodiscover - пространство
имён](N_Tessa_Exchange_WebServices_Autodiscover.htm)
