# CommandLineIOExtensions.WriteLogo - метод
Writes a logo to the specified output stream.
## __Definition
 **Пространство имён:**
[Tessa.Platform.CommandLine](N_Tessa_Platform_CommandLine.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static void WriteLogo(
    	this TextWriter output
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Sub WriteLogo ( 
    	output As TextWriter
    )
C++ __Копировать
     public:
    [ExtensionAttribute]
    static void WriteLogo(
    	TextWriter^ output
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member WriteLogo : 
            output : TextWriter -> unit 
#### Параметры
output
[TextWriter](https://learn.microsoft.com/dotnet/api/system.io.textwriter)
    A [TextWriter](https://learn.microsoft.com/dotnet/api/system.io.textwriter) that represents an output stream.
#### Примечание об использовании
В Visual Basic и C# этот метод можно вызывать как метод экземпляра для любого
объекта типа
[TextWriter](https://learn.microsoft.com/dotnet/api/system.io.textwriter). При
вызове метода для экземпляра следует опускать первый параметр. Дополнительные
сведения см. в разделе [Методы расширения (Visual
Basic)](https://docs.microsoft.com/dotnet/visual-basic/programming-
guide/language-features/procedures/extension-methods) или [Методы расширения
(Руководство по программированию в
C#)](https://docs.microsoft.com/dotnet/csharp/programming-guide/classes-and-
structs/extension-methods).
##  __Исключения
[ArgumentNullException](https://learn.microsoft.com/dotnet/api/system.argumentnullexception)|
output is null.  
---|---  
##  __См. также
#### Ссылки
[CommandLineIOExtensions -
](T_Tessa_Platform_CommandLine_CommandLineIOExtensions.htm)
[Tessa.Platform.CommandLine - пространство
имён](N_Tessa_Platform_CommandLine.htm)
