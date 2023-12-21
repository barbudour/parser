# CommandException(String, String) - конструктор
Initializes a new instance of the CommandException class with the specified
command name and error message.
## __Definition
 **Пространство имён:**
[Tessa.Platform.CommandLine](N_Tessa_Platform_CommandLine.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public CommandException(
    	string commandName,
    	string message
    )
VB __Копировать
     Public Sub New ( 
    	commandName As String,
    	message As String
    )
C++ __Копировать
     public:
    CommandException(
    	String^ commandName, 
    	String^ message
    )
F# __Копировать
     new : 
            commandName : string * 
            message : string -> CommandException
#### Параметры
commandName [String](https://learn.microsoft.com/dotnet/api/system.string)
    The name of the command that causes this exception.
message [String](https://learn.microsoft.com/dotnet/api/system.string)
    The message that describes the error.
##  __См. также
#### Ссылки
[CommandException - ](T_Tessa_Platform_CommandLine_CommandException.htm)
[CommandException -
перегрузка](Overload_Tessa_Platform_CommandLine_CommandException__ctor.htm)
[Tessa.Platform.CommandLine - пространство
имён](N_Tessa_Platform_CommandLine.htm)
