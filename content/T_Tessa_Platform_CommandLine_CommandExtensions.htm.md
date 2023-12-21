# CommandExtensions - класс
Provides a set of static (Shared in Visual Basic) methods for working objects
that implement Command instances.
## __Definition
 **Пространство имён:**
[Tessa.Platform.CommandLine](N_Tessa_Platform_CommandLine.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static class CommandExtensions
VB __Копировать
    <ExtensionAttribute>
    Public NotInheritable Class CommandExtensions
C++ __Копировать
    [ExtensionAttribute]
    public ref class CommandExtensions abstract sealed
F# __Копировать
     [<AbstractClassAttribute>]
    [<SealedAttribute>]
    [<ExtensionAttribute>]
    type CommandExtensions = class end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ CommandExtensions
##  __Методы
[AddCommand(CommandContext,
Func<Task>)](M_Tessa_Platform_CommandLine_CommandExtensions_AddCommand.htm)|  
---|---  
[AddCommand<T1>(CommandContext, Func<T1,
Task>)](M_Tessa_Platform_CommandLine_CommandExtensions_AddCommand__1.htm)|  
[AddCommand<T1, T2>(CommandContext, Func<T1, T2,
Task>)](M_Tessa_Platform_CommandLine_CommandExtensions_AddCommand__2.htm)|  
[AddCommand<T1, T2, T3>(CommandContext, Func<T1, T2, T3,
Task>)](M_Tessa_Platform_CommandLine_CommandExtensions_AddCommand__3.htm)|  
[AddCommand<T1, T2, T3, T4>(CommandContext, Func<T1, T2, T3, T4,
Task>)](M_Tessa_Platform_CommandLine_CommandExtensions_AddCommand__4.htm)|  
[AddCommand<T1, T2, T3, T4, T5>(CommandContext, Func<T1, T2, T3, T4, T5,
Task>)](M_Tessa_Platform_CommandLine_CommandExtensions_AddCommand__5.htm)|  
[AddCommand<T1, T2, T3, T4, T5, T6>(CommandContext, Func<T1, T2, T3, T4, T5,
T6, Task>)](M_Tessa_Platform_CommandLine_CommandExtensions_AddCommand__6.htm)|  
[AddCommand<T1, T2, T3, T4, T5, T6, T7>(CommandContext, Func<T1, T2, T3, T4,
T5, T6, T7,
Task>)](M_Tessa_Platform_CommandLine_CommandExtensions_AddCommand__7.htm)|  
[AddCommand<T1, T2, T3, T4, T5, T6, T7, T8>(CommandContext, Func<T1, T2, T3,
T4, T5, T6, T7, T8,
Task>)](M_Tessa_Platform_CommandLine_CommandExtensions_AddCommand__8.htm)|  
[AddCommand<T1, T2, T3, T4, T5, T6, T7, T8, T9>(CommandContext, Func<T1, T2,
T3, T4, T5, T6, T7, T8, T9,
Task>)](M_Tessa_Platform_CommandLine_CommandExtensions_AddCommand__9.htm)|  
[AddCommand<T1, T2, T3, T4, T5, T6, T7, T8, T9, T10>(CommandContext, Func<T1,
T2, T3, T4, T5, T6, T7, T8, T9, T10,
Task>)](M_Tessa_Platform_CommandLine_CommandExtensions_AddCommand__10.htm)|  
[AddCommand<T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11>(CommandContext,
Func<T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11,
Task>)](M_Tessa_Platform_CommandLine_CommandExtensions_AddCommand__11.htm)|  
[AddCommand<T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12>(CommandContext,
Func<T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12,
Task>)](M_Tessa_Platform_CommandLine_CommandExtensions_AddCommand__12.htm)|  
[AddCommand<T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12,
T13>(CommandContext, Func<T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12,
T13,
Task>)](M_Tessa_Platform_CommandLine_CommandExtensions_AddCommand__13.htm)|  
[AddCommand<T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, T13,
T14>(CommandContext, Func<T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12,
T13, T14,
Task>)](M_Tessa_Platform_CommandLine_CommandExtensions_AddCommand__14.htm)|  
[AddCommand<T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, T13, T14,
T15>(CommandContext, Func<T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12,
T13, T14, T15,
Task>)](M_Tessa_Platform_CommandLine_CommandExtensions_AddCommand__15.htm)|  
[AddCommand<T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, T13, T14, T15,
T16>(CommandContext, Func<T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12,
T13, T14, T15, T16,
Task>)](M_Tessa_Platform_CommandLine_CommandExtensions_AddCommand__16.htm)|  
[ExecuteAllAsync(Command)](M_Tessa_Platform_CommandLine_CommandExtensions_ExecuteAllAsync.htm)|
Continuously executes a command using standard IO streams until the input
stream returns null or a CommandCanceledException was thrown.  
[ExecuteAllAsync(Command,
Char)](M_Tessa_Platform_CommandLine_CommandExtensions_ExecuteAllAsync_1.htm)|  
[ExecuteAllAsync(Command, TextReader,
TextWriter)](M_Tessa_Platform_CommandLine_CommandExtensions_ExecuteAllAsync_2.htm)|
Continuously executes a command using specified IO streams until the input
stream returns null or a CommandCanceledException was thrown.  
[ExecuteAllAsync(Command, TextReader, TextWriter,
TextWriter)](M_Tessa_Platform_CommandLine_CommandExtensions_ExecuteAllAsync_3.htm)|
Continuously executes a command using specified IO streams until the input
stream returns null or a CommandCanceledException was thrown.  
[ExecuteAllAsync(Command, TextReader, TextWriter, TextWriter,
Char)](M_Tessa_Platform_CommandLine_CommandExtensions_ExecuteAllAsync_4.htm)|  
[ExecuteSingleAsync(Command)](M_Tessa_Platform_CommandLine_CommandExtensions_ExecuteSingleAsync.htm)|
Executes a command using standard IO streams.  
[ExecuteSingleAsync(Command,
Char)](M_Tessa_Platform_CommandLine_CommandExtensions_ExecuteSingleAsync_1.htm)|  
[ExecuteSingleAsync(Command, TextReader,
TextWriter)](M_Tessa_Platform_CommandLine_CommandExtensions_ExecuteSingleAsync_2.htm)|
Executes a command using specified IO streams.  
[ExecuteSingleAsync(Command, TextReader, TextWriter,
TextWriter)](M_Tessa_Platform_CommandLine_CommandExtensions_ExecuteSingleAsync_3.htm)|
Executes a command using specified IO streams.  
[ExecuteSingleAsync(Command, TextReader, TextWriter, TextWriter,
Char)](M_Tessa_Platform_CommandLine_CommandExtensions_ExecuteSingleAsync_4.htm)|  
## __См. также
#### Ссылки
[Tessa.Platform.CommandLine - пространство
имён](N_Tessa_Platform_CommandLine.htm)
