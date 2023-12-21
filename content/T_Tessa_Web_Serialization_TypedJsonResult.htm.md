# TypedJsonResult - класс
##  __Definition
 **Пространство имён:**
[Tessa.Web.Serialization](N_Tessa_Web_Serialization.htm)  
 **Сборка:** Tessa.Web (в Tessa.Web.dll) Версия: 3.6.0.17
C# __Копировать
     public class TypedJsonResult : JsonResult
VB __Копировать
     Public Class TypedJsonResult
    	Inherits JsonResult
C++ __Копировать
     public ref class TypedJsonResult : public JsonResult
F# __Копировать
     type TypedJsonResult = 
        class
            inherit JsonResult
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[ActionResult](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.actionresult) __[JsonResult](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.jsonresult) __ TypedJsonResult
##  __Конструкторы
[TypedJsonResult](M_Tessa_Web_Serialization_TypedJsonResult__ctor.htm)|
Инициализирует новый экземпляр класса TypedJsonResult  
---|---  
##  __Свойства
[ContentType](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.jsonresult.contenttype#microsoft-
aspnetcore-mvc-jsonresult-contenttype)|  Gets or sets the
[MediaTypeHeaderValue](https://learn.microsoft.com/dotnet/api/microsoft.net.http.headers.mediatypeheadervalue)
representing the Content-Type header of the response.  
(Унаследован от
[JsonResult](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.jsonresult))  
---|---  
[SerializerSettings](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.jsonresult.serializersettings#microsoft-
aspnetcore-mvc-jsonresult-serializersettings)|  Gets or sets the serializer
settings.
When using System.Text.Json, this should be an instance of
[JsonSerializerOptions](https://learn.microsoft.com/dotnet/api/system.text.json.jsonserializeroptions)
When using Newtonsoft.Json, this should be an instance of
JsonSerializerSettings.
(Унаследован от
[JsonResult](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.jsonresult))  
[StatusCode](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.jsonresult.statuscode#microsoft-
aspnetcore-mvc-jsonresult-statuscode)|  Gets or sets the HTTP status code.  
(Унаследован от
[JsonResult](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.jsonresult))  
[Value](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.jsonresult.value#microsoft-
aspnetcore-mvc-jsonresult-value)|  Gets or sets the value to be formatted.  
(Унаследован от
[JsonResult](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.jsonresult))  
##  __Методы
[ExecuteResult](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.actionresult.executeresult#microsoft-
aspnetcore-mvc-actionresult-executeresult\(microsoft-aspnetcore-mvc-
actioncontext\))|  Executes the result operation of the action method
synchronously. This method is called by MVC to process the result of an action
method.  
(Унаследован от
[ActionResult](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.actionresult))  
---|---  
[ExecuteResultAsync](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.jsonresult.executeresultasync#microsoft-
aspnetcore-mvc-jsonresult-executeresultasync\(microsoft-aspnetcore-mvc-
actioncontext\))|  
(Унаследован от
[JsonResult](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.jsonresult))  
##  __См. также
#### Ссылки
[Tessa.Web.Serialization - пространство имён](N_Tessa_Web_Serialization.htm)
