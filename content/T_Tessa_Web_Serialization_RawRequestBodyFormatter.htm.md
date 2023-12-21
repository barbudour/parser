# RawRequestBodyFormatter - класс
Formatter that allows content of type text/plain and application/octet stream
or no content type to be parsed to raw data. Allows for a single input
parameter in the form of: public string RawString([FromBody] string data)
public byte[] RawData([FromBody] byte[] data)
## __Definition
 **Пространство имён:**
[Tessa.Web.Serialization](N_Tessa_Web_Serialization.htm)  
 **Сборка:** Tessa.Web (в Tessa.Web.dll) Версия: 3.6.0.17
C# __Копировать
     public class RawRequestBodyFormatter : InputFormatter
VB __Копировать
     Public Class RawRequestBodyFormatter
    	Inherits InputFormatter
C++ __Копировать
     public ref class RawRequestBodyFormatter : public InputFormatter
F# __Копировать
     type RawRequestBodyFormatter = 
        class
            inherit InputFormatter
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[InputFormatter](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.formatters.inputformatter) __ RawRequestBodyFormatter
##  __Конструкторы
[RawRequestBodyFormatter](M_Tessa_Web_Serialization_RawRequestBodyFormatter__ctor.htm)|
Инициализирует новый экземпляр класса RawRequestBodyFormatter  
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
[CanRead](M_Tessa_Web_Serialization_RawRequestBodyFormatter_CanRead.htm)|
Allow text/plain, application/octet-stream and no content type to be processed  
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
[ReadRequestBodyAsync(InputFormatterContext)](M_Tessa_Web_Serialization_RawRequestBodyFormatter_ReadRequestBodyAsync.htm)|
Handle text/plain or no content type for string results Handle
application/octet-stream for byte[] results  
ReadRequestBodyAsync(Void)|  
(Унаследован от
[InputFormatter](https://learn.microsoft.com/dotnet/api/microsoft.aspnetcore.mvc.formatters.inputformatter))  
##  __См. также
#### Ссылки
[Tessa.Web.Serialization - пространство имён](N_Tessa_Web_Serialization.htm)
