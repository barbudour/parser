# CommandContext(String, Command[]) - конструктор
Initializes a new instance of the CommandContext class using the specified
command name and child commands.
## __Definition
 **Пространство имён:**
[Tessa.Platform.CommandLine](N_Tessa_Platform_CommandLine.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public CommandContext(
    	string name,
    	params Command[] commands
    )
VB __Копировать
     Public Sub New ( 
    	name As String,
    	ParamArray commands As Command()
    )
C++ __Копировать
     public:
    CommandContext(
    	String^ name, 
    	... array<Command^>^ commands
    )
F# __Копировать
     new : 
            name : string * 
            commands : Command[] -> CommandContext
#### Параметры
name [String](https://learn.microsoft.com/dotnet/api/system.string)
    The name of a command.
commands [Command](T_Tessa_Platform_CommandLine_Command.htm)[]
    The collection of child commands.
##  __Заметки
A name can contain letters, digits and underscore characters.
## __Исключения
[ArgumentNullException](https://learn.microsoft.com/dotnet/api/system.argumentnullexception)|
name is null.  
---|---  
[ArgumentException](https://learn.microsoft.com/dotnet/api/system.argumentexception)|
name is an empty string (""), or contains one or more invalid characters.  
##  __См. также
#### Ссылки
[CommandContext - ](T_Tessa_Platform_CommandLine_CommandContext.htm)
[CommandContext -
перегрузка](Overload_Tessa_Platform_CommandLine_CommandContext__ctor.htm)
[Tessa.Platform.CommandLine - пространство
имён](N_Tessa_Platform_CommandLine.htm)
