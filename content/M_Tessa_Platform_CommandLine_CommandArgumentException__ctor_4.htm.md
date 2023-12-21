# CommandArgumentException(String, String, String, Exception) - конструктор
Initializes a new instance of the CommandArgumentException class with the
specified command name, argument name, error message and the exception that is
the cause of this exception.
## __Definition
 **Пространство имён:**
[Tessa.Platform.CommandLine](N_Tessa_Platform_CommandLine.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public CommandArgumentException(
    	string commandName,
    	string argumentName,
    	string message,
    	Exception innerException
    )
VB __Копировать
     Public Sub New ( 
    	commandName As String,
    	argumentName As String,
    	message As String,
    	innerException As Exception
    )
C++ __Копировать
     public:
    CommandArgumentException(
    	String^ commandName, 
    	String^ argumentName, 
    	String^ message, 
    	Exception^ innerException
    )
F# __Копировать
     new : 
            commandName : string * 
            argumentName : string * 
            message : string * 
            innerException : Exception -> CommandArgumentException
#### Параметры
commandName [String](https://learn.microsoft.com/dotnet/api/system.string)
    The name of the command that causes this exception.
argumentName [String](https://learn.microsoft.com/dotnet/api/system.string)
    The name of the argument that causes this exception.
message [String](https://learn.microsoft.com/dotnet/api/system.string)
    The message that describes the error.
innerException
[Exception](https://learn.microsoft.com/dotnet/api/system.exception)
    The exception that is the cause of the current exception, or a null reference (Nothing in Visual Basic) if no inner exception is specified.
##  __См. также
#### Ссылки
[CommandArgumentException -
](T_Tessa_Platform_CommandLine_CommandArgumentException.htm)
[CommandArgumentException -
перегрузка](Overload_Tessa_Platform_CommandLine_CommandArgumentException__ctor.htm)
[Tessa.Platform.CommandLine - пространство
имён](N_Tessa_Platform_CommandLine.htm)
