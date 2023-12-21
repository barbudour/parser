# CommandExtensions.ExecuteSingleAsync(Command) - метод
Executes a command using standard IO streams.
## __Definition
 **Пространство имён:**
[Tessa.Platform.CommandLine](N_Tessa_Platform_CommandLine.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static Task ExecuteSingleAsync(
    	this Command command
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Function ExecuteSingleAsync ( 
    	command As Command
    ) As Task
C++ __Копировать
     public:
    [ExtensionAttribute]
    static Task^ ExecuteSingleAsync(
    	Command^ command
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member ExecuteSingleAsync : 
            command : Command -> Task 
#### Параметры
command [Command](T_Tessa_Platform_CommandLine_Command.htm)
    The Command to execute.
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
command is null.  
---|---  
##  __См. также
#### Ссылки
[CommandExtensions - ](T_Tessa_Platform_CommandLine_CommandExtensions.htm)
[ExecuteSingleAsync -
перегрузка](Overload_Tessa_Platform_CommandLine_CommandExtensions_ExecuteSingleAsync.htm)
[Tessa.Platform.CommandLine - пространство
имён](N_Tessa_Platform_CommandLine.htm)
