# PackageBinderConfigurationException(String, Exception) - конструктор
Initializes a new instance of the
[PackageBinderConfigurationException](T_Tessa_Applications_Package_PackageBinderConfigurationException.htm)
class. Выполняет инициализацию нового экземпляра класса
[Exception](https://learn.microsoft.com/dotnet/api/system.exception) с
указанным сообщением об ошибке и ссылкой на внутреннее исключение, которое
стало причиной данного исключения.
## __Definition
 **Пространство имён:**
[Tessa.Applications.Package](N_Tessa_Applications_Package.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public PackageBinderConfigurationException(
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
    PackageBinderConfigurationException(
    	String^ message, 
    	Exception^ innerException
    )
F# __Копировать
     new : 
            message : string * 
            innerException : Exception -> PackageBinderConfigurationException
#### Параметры
message [String](https://learn.microsoft.com/dotnet/api/system.string)
     Сообщение об ошибке с объяснением причины исключения. 
innerException
[Exception](https://learn.microsoft.com/dotnet/api/system.exception)
     Исключение, вызвавшее текущее исключение, или указатель NULL (Nothing в Visual Basic), если внутреннее исключение не задано. 
## __См. также
#### Ссылки
[PackageBinderConfigurationException -
](T_Tessa_Applications_Package_PackageBinderConfigurationException.htm)
[PackageBinderConfigurationException -
перегрузка](Overload_Tessa_Applications_Package_PackageBinderConfigurationException__ctor.htm)
[Tessa.Applications.Package - пространство
имён](N_Tessa_Applications_Package.htm)
