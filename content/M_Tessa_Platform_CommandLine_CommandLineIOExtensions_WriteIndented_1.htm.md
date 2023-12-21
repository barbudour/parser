# CommandLineIOExtensions.WriteIndented(TextWriter, String, Int32, Boolean) -
метод
Writes a string to the text string or stream with indentation of every line of
the string.
## __Definition
 **Пространство имён:**
[Tessa.Platform.CommandLine](N_Tessa_Platform_CommandLine.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static void WriteIndented(
    	this TextWriter output,
    	string value,
    	int indent,
    	bool indentFirstLine
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Sub WriteIndented ( 
    	output As TextWriter,
    	value As String,
    	indent As Integer,
    	indentFirstLine As Boolean
    )
C++ __Копировать
     public:
    [ExtensionAttribute]
    static void WriteIndented(
    	TextWriter^ output, 
    	String^ value, 
    	int indent, 
    	bool indentFirstLine
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member WriteIndented : 
            output : TextWriter * 
            value : string * 
            indent : int * 
            indentFirstLine : bool -> unit 
#### Параметры
output
[TextWriter](https://learn.microsoft.com/dotnet/api/system.io.textwriter)
    A [TextWriter](https://learn.microsoft.com/dotnet/api/system.io.textwriter) that represents an output stream.
value [String](https://learn.microsoft.com/dotnet/api/system.string)
    The string to write.
indent [Int32](https://learn.microsoft.com/dotnet/api/system.int32)
    The space count to indent.
indentFirstLine
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)
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
##  __Заметки
If value is null, nothing is written to the text stream.
## __Исключения
[ArgumentNullException](https://learn.microsoft.com/dotnet/api/system.argumentnullexception)|
output is null.  
---|---  
[ArgumentOutOfRangeException](https://learn.microsoft.com/dotnet/api/system.argumentoutofrangeexception)|
indent is less than zero.  
##  __См. также
#### Ссылки
[CommandLineIOExtensions -
](T_Tessa_Platform_CommandLine_CommandLineIOExtensions.htm)
[WriteIndented -
перегрузка](Overload_Tessa_Platform_CommandLine_CommandLineIOExtensions_WriteIndented.htm)
[Tessa.Platform.CommandLine - пространство
имён](N_Tessa_Platform_CommandLine.htm)
