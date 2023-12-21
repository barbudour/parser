# CommandExtensions.ExecuteSingleAsync(Command, TextReader, TextWriter,
TextWriter) - метод
Executes a command using specified IO streams.
## __Definition
 **Пространство имён:**
[Tessa.Platform.CommandLine](N_Tessa_Platform_CommandLine.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static Task ExecuteSingleAsync(
    	this Command command,
    	TextReader input,
    	TextWriter output,
    	TextWriter error
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Function ExecuteSingleAsync ( 
    	command As Command,
    	input As TextReader,
    	output As TextWriter,
    	error As TextWriter
    ) As Task
C++ __Копировать
     public:
    [ExtensionAttribute]
    static Task^ ExecuteSingleAsync(
    	Command^ command, 
    	TextReader^ input, 
    	TextWriter^ output, 
    	TextWriter^ error
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member ExecuteSingleAsync : 
            command : Command * 
            input : TextReader * 
            output : TextWriter * 
            error : TextWriter -> Task 
#### Параметры
command [Command](T_Tessa_Platform_CommandLine_Command.htm)
    The Command to execute.
input
[TextReader](https://learn.microsoft.com/dotnet/api/system.io.textreader)
    The [TextReader](https://learn.microsoft.com/dotnet/api/system.io.textreader) that represents an input stream.
output
[TextWriter](https://learn.microsoft.com/dotnet/api/system.io.textwriter)
    The [TextWriter](https://learn.microsoft.com/dotnet/api/system.io.textwriter) that represents an output stream.
error
[TextWriter](https://learn.microsoft.com/dotnet/api/system.io.textwriter)
    The [TextWriter](https://learn.microsoft.com/dotnet/api/system.io.textwriter) that represents an error stream.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)
#### Примечание об использовании
В Visual Basic и C# этот метод можно вызывать как метод экземпляра для любого
объекта типа [Command](T_Tessa_Platform_CommandLine_Command.htm). При вызове
метода для экземпляра следует опускать первый параметр. Дополнительные
сведения см. в разделе [Методы расширения (Visual
Basic)](https://docs.microsoft.com/dotnet/visual-basic/programming-
guide/language-features/procedures/extension-methods) или [Методы расширения
(Руководство по программированию в
C#)](https://docs.microsoft.com/dotnet/csharp/programming-guide/classes-and-
structs/extension-methods).
##  __Заметки
This method catches all exceptions of type CommandException and writes them to
the standard error stream.
## __Исключения
[ArgumentNullException](https://learn.microsoft.com/dotnet/api/system.argumentnullexception)|
command, input, output, or error is null.  
---|---  
##  __См. также
#### Ссылки
[CommandExtensions - ](T_Tessa_Platform_CommandLine_CommandExtensions.htm)
[ExecuteSingleAsync -
перегрузка](Overload_Tessa_Platform_CommandLine_CommandExtensions_ExecuteSingleAsync.htm)
[Tessa.Platform.CommandLine - пространство
имён](N_Tessa_Platform_CommandLine.htm)
