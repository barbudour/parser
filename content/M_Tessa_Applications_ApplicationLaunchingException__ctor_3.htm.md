# ApplicationLaunchingException(String, Exception) - конструктор
Initializes a new instance of the
[Exception](https://learn.microsoft.com/dotnet/api/system.exception) class
with a specified error message and a reference to the inner exception that is
the cause of this exception.
##  __Definition
 **Пространство имён:** [Tessa.Applications](N_Tessa_Applications.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public ApplicationLaunchingException(
    	string message,
    	Exception innerException
    )
VB __Копировать
     Public Sub New ( 
    	message As String,
    	innerException As Exception
    )
C++ __Копировать
     public:
    ApplicationLaunchingException(
    	String^ message, 
    	Exception^ innerException
    )
F# __Копировать
     new : 
            message : string * 
            innerException : Exception -> ApplicationLaunchingException
#### Параметры
message [String](https://learn.microsoft.com/dotnet/api/system.string)
    The error message that explains the reason for the exception.
innerException
[Exception](https://learn.microsoft.com/dotnet/api/system.exception)
    The exception that is the cause of the current exception, or a null reference (null in Visual Basic) if no inner exception is specified.
##  __См. также
#### Ссылки
[ApplicationLaunchingException -
](T_Tessa_Applications_ApplicationLaunchingException.htm)
[ApplicationLaunchingException -
перегрузка](Overload_Tessa_Applications_ApplicationLaunchingException__ctor.htm)
[Tessa.Applications - пространство имён](N_Tessa_Applications.htm)
