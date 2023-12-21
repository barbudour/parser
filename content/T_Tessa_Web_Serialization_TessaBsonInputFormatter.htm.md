# TessaBsonInputFormatter - класс
##  __Definition
 **Пространство имён:**
[Tessa.Web.Serialization](N_Tessa_Web_Serialization.htm)  
 **Сборка:** Tessa.Web (в Tessa.Web.dll) Версия: 3.6.0.17
C# __Копировать
     public class TessaBsonInputFormatter : InputFormatter
VB __Копировать
     Public Class TessaBsonInputFormatter
    	Inherits InputFormatter
C++ __Копировать
     public ref class TessaBsonInputFormatter : public InputFormatter
F# __Копировать
     type TessaBsonInputFormatter = 
        class
            inherit InputFormatter
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[InputFormatter](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.formatters.inputformatter) __ TessaBsonInputFormatter
##  __Конструкторы
[TessaBsonInputFormatter](M_Tessa_Web_Serialization_TessaBsonInputFormatter__ctor.htm)|
Инициализирует новый экземпляр класса TessaBsonInputFormatter  
---|---  
##  __Свойства
[SupportedMediaTypes](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.formatters.inputformatter.supportedmediatypes#microsoft-
aspnetcore-mvc-formatters-inputformatter-supportedmediatypes)|  Gets the
mutable collection of media type elements supported by this
[InputFormatter](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.formatters.inputformatter).  
(Унаследован от
[InputFormatter](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.formatters.inputformatter))  
---|---  
##  __Методы
[CanRead](M_Tessa_Web_Serialization_TessaBsonInputFormatter_CanRead.htm)|  
(Переопределяет
[InputFormatter.CanRead(InputFormatterContext)](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.formatters.inputformatter.canread#microsoft-
aspnetcore-mvc-formatters-inputformatter-canread\(microsoft-aspnetcore-mvc-
formatters-inputformattercontext\)))  
---|---  
[CanReadType](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.formatters.inputformatter.canreadtype#microsoft-
aspnetcore-mvc-formatters-inputformatter-canreadtype\(system-type\))|
Determines whether this
[InputFormatter](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.formatters.inputformatter)
can deserialize an object of the given type.  
(Унаследован от
[InputFormatter](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.formatters.inputformatter))  
[GetDefaultValueForType](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.formatters.inputformatter.getdefaultvaluefortype#microsoft-
aspnetcore-mvc-formatters-inputformatter-getdefaultvaluefortype\(system-
type\))|  Gets the default value for a given type. Used to return a default
value when the body contains no content.  
(Унаследован от
[InputFormatter](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.formatters.inputformatter))  
GetSupportedContentTypes|  
(Унаследован от
[InputFormatter](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.formatters.inputformatter))  
ReadAsync|  
(Унаследован от
[InputFormatter](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.formatters.inputformatter))  
[ReadRequestBodyAsync(InputFormatterContext)](M_Tessa_Web_Serialization_TessaBsonInputFormatter_ReadRequestBodyAsync.htm)|  
ReadRequestBodyAsync(Void)|  
(Унаследован от
[InputFormatter](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.formatters.inputformatter))  
##  __См. также
#### Ссылки
[Tessa.Web.Serialization - пространство имён](N_Tessa_Web_Serialization.htm)
