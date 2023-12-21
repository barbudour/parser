# TessaBsonResult - класс
##  __Definition
 **Пространство имён:**
[Tessa.Web.Serialization](N_Tessa_Web_Serialization.htm)  
 **Сборка:** Tessa.Web (в Tessa.Web.dll) Версия: 3.6.0.17
C# __Копировать
     public class TessaBsonResult : ActionResult
VB __Копировать
     Public Class TessaBsonResult
    	Inherits ActionResult
C++ __Копировать
     public ref class TessaBsonResult : public ActionResult
F# __Копировать
     type TessaBsonResult = 
        class
            inherit ActionResult
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[ActionResult](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.actionresult) __ TessaBsonResult
##  __Конструкторы
[TessaBsonResult](M_Tessa_Web_Serialization_TessaBsonResult__ctor.htm)|
Инициализирует новый экземпляр класса TessaBsonResult  
---|---  
##  __Свойства
[CompressionMode](P_Tessa_Web_Serialization_TessaBsonResult_CompressionMode.htm)|
Алгоритм сжатия содержимого.  
---|---  
[ContentType](P_Tessa_Web_Serialization_TessaBsonResult_ContentType.htm)|
Gets or sets the
[MediaTypeHeaderValue](https://learn.microsoft.com/dotnet/api/microsoft.net.http.headers.mediatypeheadervalue)
representing the Content-Type header of the response.  
[StatusCode](P_Tessa_Web_Serialization_TessaBsonResult_StatusCode.htm)|  Gets
or sets the HTTP status code.  
[Value](P_Tessa_Web_Serialization_TessaBsonResult_Value.htm)|  Gets or sets
the value to be formatted.  
## __Методы
[ExecuteResult](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.actionresult.executeresult#microsoft-
aspnetcore-mvc-actionresult-executeresult\(microsoft-aspnetcore-mvc-
actioncontext\))|  Executes the result operation of the action method
synchronously. This method is called by MVC to process the result of an action
method.  
(Унаследован от
[ActionResult](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.actionresult))  
---|---  
[ExecuteResultAsync](M_Tessa_Web_Serialization_TessaBsonResult_ExecuteResultAsync.htm)|  
(Переопределяет
[ActionResult.ExecuteResultAsync(ActionContext)](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.actionresult.executeresultasync#microsoft-
aspnetcore-mvc-actionresult-executeresultasync\(microsoft-aspnetcore-mvc-
actioncontext\)))  
##  __См. также
#### Ссылки
[Tessa.Web.Serialization - пространство имён](N_Tessa_Web_Serialization.htm)
