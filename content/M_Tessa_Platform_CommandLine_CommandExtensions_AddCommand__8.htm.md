# CommandExtensions.AddCommand<T1, T2, T3, T4, T5, T6, T7, T8>(CommandContext,
Func<T1, T2, T3, T4, T5, T6, T7, T8, Task>) - метод
##  __Definition
 **Пространство имён:**
[Tessa.Platform.CommandLine](N_Tessa_Platform_CommandLine.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static CommandContext AddCommand<T1, T2, T3, T4, T5, T6, T7, T8>(
    	this CommandContext commandContext,
    	Func<T1, T2, T3, T4, T5, T6, T7, T8, Task> commandDelegate
    )
VB __Копировать
    <ExtensionAttribute>
    Public Shared Function AddCommand(Of T1, T2, T3, T4, T5, T6, T7, T8) ( 
    	commandContext As CommandContext,
    	commandDelegate As Func(Of T1, T2, T3, T4, T5, T6, T7, T8, Task)
    ) As CommandContext
C++ __Копировать
     public:
    [ExtensionAttribute]
    generic<typename T1, typename T2, typename T3, typename T4, typename T5, typename T6, typename T7, typename T8>
    static CommandContext^ AddCommand(
    	CommandContext^ commandContext, 
    	Func<T1, T2, T3, T4, T5, T6, T7, T8, Task^>^ commandDelegate
    )
F# __Копировать
     [<ExtensionAttribute>]
    static member AddCommand : 
            commandContext : CommandContext * 
            commandDelegate : Func<'T1, 'T2, 'T3, 'T4, 'T5, 'T6, 'T7, 'T8, Task> -> CommandContext 
#### Параметры
commandContext
[CommandContext](T_Tessa_Platform_CommandLine_CommandContext.htm)
commandDelegate
[Func](https://learn.microsoft.com/dotnet/api/system.func-9)<T1, T2, T3, T4,
T5, T6, T7, T8,
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)>
#### Параметры типа
T1
T2
T3
T4
T5
T6
T7
T8
#### Возвращаемое значение
[CommandContext](T_Tessa_Platform_CommandLine_CommandContext.htm)
#### Примечание об использовании
В Visual Basic и C# этот метод можно вызывать как метод экземпляра для любого
объекта типа
[CommandContext](T_Tessa_Platform_CommandLine_CommandContext.htm). При вызове
метода для экземпляра следует опускать первый параметр. Дополнительные
сведения см. в разделе [Методы расширения (Visual
Basic)](https://docs.microsoft.com/dotnet/visual-basic/programming-
guide/language-features/procedures/extension-methods) или [Методы расширения
(Руководство по программированию в
C#)](https://docs.microsoft.com/dotnet/csharp/programming-guide/classes-and-
structs/extension-methods).
##  __См. также
#### Ссылки
[CommandExtensions - ](T_Tessa_Platform_CommandLine_CommandExtensions.htm)
[AddCommand -
перегрузка](Overload_Tessa_Platform_CommandLine_CommandExtensions_AddCommand.htm)
[Tessa.Platform.CommandLine - пространство
имён](N_Tessa_Platform_CommandLine.htm)
