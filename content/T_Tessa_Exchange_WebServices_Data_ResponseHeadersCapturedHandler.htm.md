# ResponseHeadersCapturedHandler - делегат
Delegate method to handle capturing http response headers.
## __Definition
 **Пространство имён:**
[Tessa.Exchange.WebServices.Data](N_Tessa_Exchange_WebServices_Data.htm)  
 **Сборка:** Tessa.Server (в Tessa.Server.dll) Версия: 3.6.0.17
C# __Копировать
     public delegate void ResponseHeadersCapturedHandler(
    	HttpResponseHeaders responseHeaders
    )
VB __Копировать
     Public Delegate Sub ResponseHeadersCapturedHandler ( 
    	responseHeaders As HttpResponseHeaders
    )
C++ __Копировать
     public delegate void ResponseHeadersCapturedHandler(
    	HttpResponseHeaders^ responseHeaders
    )
F# __Копировать
     type ResponseHeadersCapturedHandler = 
        delegate of 
            responseHeaders : HttpResponseHeaders -> unit
#### Параметры
responseHeaders
[HttpResponseHeaders](https://learn.microsoft.com/dotnet/api/system.net.http.headers.httpresponseheaders)
    Http response headers.
##  __См. также
#### Ссылки
[Tessa.Exchange.WebServices.Data - пространство
имён](N_Tessa_Exchange_WebServices_Data.htm)
