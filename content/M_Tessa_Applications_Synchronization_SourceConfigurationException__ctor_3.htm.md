# SourceConfigurationException(String, Exception) - конструктор
Initializes a new instance of the
[SourceConfigurationException](T_Tessa_Applications_Synchronization_SourceConfigurationException.htm)
class. Выполняет инициализацию нового экземпляра класса
[Exception](https://learn.microsoft.com/dotnet/api/system.exception) с
указанным сообщением об ошибке и ссылкой на внутреннее исключение, которое
стало причиной данного исключения.
## __Definition
 **Пространство имён:**
[Tessa.Applications.Synchronization](N_Tessa_Applications_Synchronization.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public SourceConfigurationException(
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
    SourceConfigurationException(
    	String^ message, 
    	Exception^ innerException
    )
F# __Копировать
     new : 
            message : string * 
            innerException : Exception -> SourceConfigurationException
#### Параметры
message [String](https://learn.microsoft.com/dotnet/api/system.string)
     Сообщение об ошибке с объяснением причины исключения. 
innerException
[Exception](https://learn.microsoft.com/dotnet/api/system.exception)
     Исключение, вызвавшее текущее исключение, или указатель NULL (Nothing в Visual Basic), если внутреннее исключение не задано. 
## __См. также
#### Ссылки
[SourceConfigurationException -
](T_Tessa_Applications_Synchronization_SourceConfigurationException.htm)
[SourceConfigurationException -
перегрузка](Overload_Tessa_Applications_Synchronization_SourceConfigurationException__ctor.htm)
[Tessa.Applications.Synchronization - пространство
имён](N_Tessa_Applications_Synchronization.htm)
