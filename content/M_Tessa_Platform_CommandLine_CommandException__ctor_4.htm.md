# CommandException(String, String, Exception) - конструктор
Initializes a new instance of the CommandException class with the specified
command name, error message and the exception that is the cause of this
exception.
## __Definition
 **Пространство имён:**
[Tessa.Platform.CommandLine](N_Tessa_Platform_CommandLine.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public CommandException(
    	string commandName,
    	string message,
    	Exception innerException
    )
VB __Копировать
     Public Sub New ( 
    	commandName As String,
    	message As String,
    	innerException As Exception
    )
C++ __Копировать
     public:
    CommandException(
    	String^ commandName, 
    	String^ message, 
    	Exception^ innerException
    )
F# __Копировать
     new : 
            commandName : string * 
            message : string * 
            innerException : Exception -> CommandException
#### Параметры
commandName [String](https://learn.microsoft.com/dotnet/api/system.string)
    The name of the command that causes this exception.
message [String](https://learn.microsoft.com/dotnet/api/system.string)
    The message that describes the error.
innerException
[Exception](https://learn.microsoft.com/dotnet/api/system.exception)
    The exception that is the cause of the current exception, or a null reference (Nothing in Visual Basic) if no inner exception is specified.
##  __См. также
#### Ссылки
[CommandException - ](T_Tessa_Platform_CommandLine_CommandException.htm)
[CommandException -
перегрузка](Overload_Tessa_Platform_CommandLine_CommandException__ctor.htm)
[Tessa.Platform.CommandLine - пространство
имён](N_Tessa_Platform_CommandLine.htm)
