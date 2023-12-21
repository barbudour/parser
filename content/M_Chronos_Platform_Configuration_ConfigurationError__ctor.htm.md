# ConfigurationError - конструктор
Создаёт экземпляр класса с указанием значений его свойств.
## __Definition
 **Пространство имён:**
[Chronos.Platform.Configuration](N_Chronos_Platform_Configuration.htm)  
 **Сборка:** Chronos.Platform (в Chronos.Platform.dll) Версия: 3.6.0.17
C# __Копировать
     public ConfigurationError(
    	string filePath,
    	Exception exception
    )
VB __Копировать
     Public Sub New ( 
    	filePath As String,
    	exception As Exception
    )
C++ __Копировать
     public:
    ConfigurationError(
    	String^ filePath, 
    	Exception^ exception
    )
F# __Копировать
     new : 
            filePath : string * 
            exception : Exception -> ConfigurationError
#### Параметры
filePath [String](https://learn.microsoft.com/dotnet/api/system.string)
    Путь к файлу конфигурации, при обработке которого возникло исключение.
exception [Exception](https://learn.microsoft.com/dotnet/api/system.exception)
    Исключение, которое возникло при обработке файла конфигурации.
##  __См. также
#### Ссылки
[ConfigurationError -
](T_Chronos_Platform_Configuration_ConfigurationError.htm)
[Chronos.Platform.Configuration - пространство
имён](N_Chronos_Platform_Configuration.htm)
