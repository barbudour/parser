# CommandContextScope(Command[]) - конструктор
Initializes a new instance of the CommandContextScope class that uses the
specified array of Command and escaped name of the entry point
[Assembly](https://learn.microsoft.com/dotnet/api/system.reflection.assembly)
to create a new CommandContext for the scope.
## __Definition
 **Пространство имён:**
[Tessa.Platform.CommandLine](N_Tessa_Platform_CommandLine.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public CommandContextScope(
    	params Command[] commands
    )
VB __Копировать
     Public Sub New ( 
    	ParamArray commands As Command()
    )
C++ __Копировать
     public:
    CommandContextScope(
    	... array<Command^>^ commands
    )
F# __Копировать
     new : 
            commands : Command[] -> CommandContextScope
#### Параметры
commands [Command](T_Tessa_Platform_CommandLine_Command.htm)[]
    The array of commands to use when creating the scope for a new CommandContext.
##  __См. также
#### Ссылки
[CommandContextScope - ](T_Tessa_Platform_CommandLine_CommandContextScope.htm)
[CommandContextScope -
перегрузка](Overload_Tessa_Platform_CommandLine_CommandContextScope__ctor.htm)
[Tessa.Platform.CommandLine - пространство
имён](N_Tessa_Platform_CommandLine.htm)
