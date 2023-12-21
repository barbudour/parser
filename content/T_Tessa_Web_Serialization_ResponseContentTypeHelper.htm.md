# ResponseContentTypeHelper - класс
##  __Definition
 **Пространство имён:**
[Tessa.Web.Serialization](N_Tessa_Web_Serialization.htm)  
 **Сборка:** Tessa.Web (в Tessa.Web.dll) Версия: 3.6.0.17
C# __Копировать
     public static class ResponseContentTypeHelper
VB __Копировать
     Public NotInheritable Class ResponseContentTypeHelper
C++ __Копировать
     public ref class ResponseContentTypeHelper abstract sealed
F# __Копировать
     [<AbstractClassAttribute>]
    [<SealedAttribute>]
    type ResponseContentTypeHelper = class end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ ResponseContentTypeHelper
##  __Методы
[ResolveContentTypeAndEncoding](M_Tessa_Web_Serialization_ResponseContentTypeHelper_ResolveContentTypeAndEncoding.htm)|
Gets the content type and encoding that need to be used for the response. The
priority for selecting the content type is: 1\. ContentType property set on
the action result 2\.
[ContentType](https://learn.microsoft.com/dotnet/api/system.net.mime.contenttype)
property set on
[HttpResponse](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.http.httpresponse)
3\. Default content type set on the action result  
---|---  
## __См. также
#### Ссылки
[Tessa.Web.Serialization - пространство имён](N_Tessa_Web_Serialization.htm)
