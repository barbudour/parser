# TessaBsonOutputFormatter - класс
##  __Definition
 **Пространство имён:**
[Tessa.Web.Serialization](N_Tessa_Web_Serialization.htm)  
 **Сборка:** Tessa.Web (в Tessa.Web.dll) Версия: 3.6.0.17
C# __Копировать
     public class TessaBsonOutputFormatter : OutputFormatter
VB __Копировать
     Public Class TessaBsonOutputFormatter
    	Inherits OutputFormatter
C++ __Копировать
     public ref class TessaBsonOutputFormatter : public OutputFormatter
F# __Копировать
     type TessaBsonOutputFormatter = 
        class
            inherit OutputFormatter
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[OutputFormatter](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.formatters.outputformatter) __ TessaBsonOutputFormatter
##  __Конструкторы
[TessaBsonOutputFormatter](M_Tessa_Web_Serialization_TessaBsonOutputFormatter__ctor.htm)|
Инициализирует новый экземпляр класса TessaBsonOutputFormatter  
---|---  
##  __Свойства
[SupportedMediaTypes](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.formatters.outputformatter.supportedmediatypes#microsoft-
aspnetcore-mvc-formatters-outputformatter-supportedmediatypes)|  Gets the
mutable collection of media type elements supported by this
[OutputFormatter](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.formatters.outputformatter).  
(Унаследован от
[OutputFormatter](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.formatters.outputformatter))  
---|---  
##  __Методы
[CanWriteResult](M_Tessa_Web_Serialization_TessaBsonOutputFormatter_CanWriteResult.htm)|  
(Переопределяет
[OutputFormatter.CanWriteResult(OutputFormatterCanWriteContext)](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.formatters.outputformatter.canwriteresult#microsoft-
aspnetcore-mvc-formatters-outputformatter-canwriteresult\(microsoft-
aspnetcore-mvc-formatters-outputformattercanwritecontext\)))  
---|---  
[CanWriteType](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.formatters.outputformatter.canwritetype#microsoft-
aspnetcore-mvc-formatters-outputformatter-canwritetype\(system-type\))|
Returns a value indicating whether or not the given type can be written by
this serializer.  
(Унаследован от
[OutputFormatter](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.formatters.outputformatter))  
GetSupportedContentTypes|  
(Унаследован от
[OutputFormatter](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.formatters.outputformatter))  
[WriteAsync](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.formatters.outputformatter.writeasync#microsoft-
aspnetcore-mvc-formatters-outputformatter-writeasync\(microsoft-aspnetcore-
mvc-formatters-outputformatterwritecontext\))|  
(Унаследован от
[OutputFormatter](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.formatters.outputformatter))  
[WriteResponseBodyAsync](M_Tessa_Web_Serialization_TessaBsonOutputFormatter_WriteResponseBodyAsync.htm)|  
(Переопределяет
[OutputFormatter.WriteResponseBodyAsync(OutputFormatterWriteContext)](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.formatters.outputformatter.writeresponsebodyasync#microsoft-
aspnetcore-mvc-formatters-outputformatter-writeresponsebodyasync\(microsoft-
aspnetcore-mvc-formatters-outputformatterwritecontext\)))  
[WriteResponseHeaders](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.formatters.outputformatter.writeresponseheaders#microsoft-
aspnetcore-mvc-formatters-outputformatter-writeresponseheaders\(microsoft-
aspnetcore-mvc-formatters-outputformatterwritecontext\))|  Sets the headers on
[HttpResponse](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.http.httpresponse)
object.  
(Унаследован от
[OutputFormatter](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.formatters.outputformatter))  
##  __См. также
#### Ссылки
[Tessa.Web.Serialization - пространство имён](N_Tessa_Web_Serialization.htm)
