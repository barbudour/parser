# MultipartResult - класс
##  __Definition
 **Пространство имён:** [Tessa.Web.Services](N_Tessa_Web_Services.htm)  
 **Сборка:** Tessa.Web (в Tessa.Web.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class MultipartResult : ActionResult, 
    	IStatusCodeActionResult, IActionResult
VB __Копировать
     Public NotInheritable Class MultipartResult
    	Inherits ActionResult
    	Implements IStatusCodeActionResult, IActionResult
C++ __Копировать
     public ref class MultipartResult sealed : public ActionResult, 
    	IStatusCodeActionResult, IActionResult
F# __Копировать
     [<SealedAttribute>]
    type MultipartResult = 
        class
            inherit ActionResult
            interface IStatusCodeActionResult
            interface IActionResult
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[ActionResult](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.actionresult) __ MultipartResult
Implements
    [IActionResult](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.iactionresult), [IStatusCodeActionResult](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.infrastructure.istatuscodeactionresult)
##  __Конструкторы
[MultipartResult](M_Tessa_Web_Services_MultipartResult__ctor.htm)|
Инициализирует новый экземпляр класса MultipartResult  
---|---  
##  __Свойства
[StatusCode](P_Tessa_Web_Services_MultipartResult_StatusCode.htm)|  
---|---  
## __Методы
[ExecuteResult](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.actionresult.executeresult#microsoft-
aspnetcore-mvc-actionresult-executeresult\(microsoft-aspnetcore-mvc-
actioncontext\))|  Executes the result operation of the action method
synchronously. This method is called by MVC to process the result of an action
method.  
(Унаследован от
[ActionResult](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.actionresult))  
---|---  
[ExecuteResultAsync](M_Tessa_Web_Services_MultipartResult_ExecuteResultAsync.htm)|  
(Переопределяет
[ActionResult.ExecuteResultAsync(ActionContext)](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.actionresult.executeresultasync#microsoft-
aspnetcore-mvc-actionresult-executeresultasync\(microsoft-aspnetcore-mvc-
actioncontext\)))  
##  __См. также
#### Ссылки
[Tessa.Web.Services - пространство имён](N_Tessa_Web_Services.htm)
