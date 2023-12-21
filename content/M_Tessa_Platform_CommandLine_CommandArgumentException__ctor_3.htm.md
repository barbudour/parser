# CommandArgumentException(String, String, String) - конструктор
Initializes a new instance of the CommandArgumentException class with the
specified command name, argument name and error message.
## __Definition
 **Пространство имён:**
[Tessa.Platform.CommandLine](N_Tessa_Platform_CommandLine.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public CommandArgumentException(
    	string commandName,
    	string argumentName,
    	string message
    )
VB __Копировать
     Public Sub New ( 
    	commandName As String,
    	argumentName As String,
    	message As String
    )
C++ __Копировать
     public:
    CommandArgumentException(
    	String^ commandName, 
    	String^ argumentName, 
    	String^ message
    )
F# __Копировать
     new : 
            commandName : string * 
            argumentName : string * 
            message : string -> CommandArgumentException
#### Параметры
commandName [String](https://learn.microsoft.com/dotnet/api/system.string)
    The name of the command that causes this exception.
argumentName [String](https://learn.microsoft.com/dotnet/api/system.string)
    The name of the argument that causes this exception.
message [String](https://learn.microsoft.com/dotnet/api/system.string)
    The message that describes the error.
##  __См. также
#### Ссылки
[CommandArgumentException -
](T_Tessa_Platform_CommandLine_CommandArgumentException.htm)
[CommandArgumentException -
перегрузка](Overload_Tessa_Platform_CommandLine_CommandArgumentException__ctor.htm)
[Tessa.Platform.CommandLine - пространство
имён](N_Tessa_Platform_CommandLine.htm)
