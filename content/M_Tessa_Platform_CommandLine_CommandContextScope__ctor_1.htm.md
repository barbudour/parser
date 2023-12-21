# CommandContextScope(CommandContext) - конструктор
Initializes a new instance of the CommandContextScope class with the specified
CommandContext.
## __Definition
 **Пространство имён:**
[Tessa.Platform.CommandLine](N_Tessa_Platform_CommandLine.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public CommandContextScope(
    	CommandContext context
    )
VB __Копировать
     Public Sub New ( 
    	context As CommandContext
    )
C++ __Копировать
     public:
    CommandContextScope(
    	CommandContext^ context
    )
F# __Копировать
     new : 
            context : CommandContext -> CommandContextScope
#### Параметры
context [CommandContext](T_Tessa_Platform_CommandLine_CommandContext.htm)
    The root command context.
##  __Исключения
[ArgumentNullException](https://learn.microsoft.com/dotnet/api/system.argumentnullexception)|
context is null.  
---|---  
##  __См. также
#### Ссылки
[CommandContextScope - ](T_Tessa_Platform_CommandLine_CommandContextScope.htm)
[CommandContextScope -
перегрузка](Overload_Tessa_Platform_CommandLine_CommandContextScope__ctor.htm)
[Tessa.Platform.CommandLine - пространство
имён](N_Tessa_Platform_CommandLine.htm)
