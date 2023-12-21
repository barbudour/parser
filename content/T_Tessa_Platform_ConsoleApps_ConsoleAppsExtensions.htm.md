# ConsoleAppsExtensions - класс
Методы-расширения для пространства имён Tessa.Platform.ConsoleApps.
## __Definition
 **Пространство имён:**
[Tessa.Platform.ConsoleApps](N_Tessa_Platform_ConsoleApps.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static class ConsoleAppsExtensions
VB __Копировать
    <ExtensionAttribute>
    Public NotInheritable Class ConsoleAppsExtensions
C++ __Копировать
    [ExtensionAttribute]
    public ref class ConsoleAppsExtensions abstract sealed
F# __Копировать
     [<AbstractClassAttribute>]
    [<SealedAttribute>]
    [<ExtensionAttribute>]
    type ConsoleAppsExtensions = class end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ ConsoleAppsExtensions
##  __Методы
[ConfigureConsoleForClient(IUnityContainer,
IConsoleScriptOptions)](M_Tessa_Platform_ConsoleApps_ConsoleAppsExtensions_ConfigureConsoleForClient_1.htm)|
Выполняет конфигурацию контейнера для консоли.  
---|---  
[ConfigureConsoleForClient(IUnityContainer, TextWriter, TextWriter, Boolean,
String,
String)](M_Tessa_Platform_ConsoleApps_ConsoleAppsExtensions_ConfigureConsoleForClient.htm)|
Выполняет конфигурацию контейнера для консоли.  
[FinalizeConsoleClientRegistration](M_Tessa_Platform_ConsoleApps_ConsoleAppsExtensions_FinalizeConsoleClientRegistration.htm)|
Выполняет финализацию регистрации зависимостей для консольной команды,
использующей клиентское API и подключение к веб-сервису. Регистрация основных
API выполняется предварительными вызовами
[RegisterClientForConsole(IUnityContainer, String, String,
Assembly)](M_Tessa_Platform_ConsoleApps_ConsoleAppsExtensions_RegisterClientForConsole.htm)
и [RegisterConsoleOperationLogger(IUnityContainer, TextWriter, TextWriter,
Boolean)](M_Tessa_Platform_ConsoleApps_ConsoleAppsExtensions_RegisterConsoleOperationLogger.htm).
После финализации не рекомендуется выполнять другие регистрации. Используйте
метод [ConfigureConsoleForClient(IUnityContainer, TextWriter, TextWriter,
Boolean, String,
String)](M_Tessa_Platform_ConsoleApps_ConsoleAppsExtensions_ConfigureConsoleForClient.htm),
если требуется выполнить полную конфигурацию консольного приложения для
клиента с параметрами по умолчанию, в этом случае вызывать другие методы на
контейнере не требуется.  
[OrderBySpecifiedOrder](M_Tessa_Platform_ConsoleApps_ConsoleAppsExtensions_OrderBySpecifiedOrder.htm)|
Упорядочивает типы
[ConsoleRegistratorImportingItem](T_Tessa_Platform_ConsoleApps_ConsoleRegistratorImportingItem.htm)
по их явно заданному порядку.  
[RegisterClientForConsole](M_Tessa_Platform_ConsoleApps_ConsoleAppsExtensions_RegisterClientForConsole.htm)|
Выполняет регистрацию зависимостей для консольной команды, использующей
клиентское API и подключение к веб-сервису. Рекомендуется также вызвать методы
[RegisterConsoleOperationLogger(IUnityContainer, TextWriter, TextWriter,
Boolean)](M_Tessa_Platform_ConsoleApps_ConsoleAppsExtensions_RegisterConsoleOperationLogger.htm)
и
[FinalizeConsoleClientRegistration(IUnityContainer)](M_Tessa_Platform_ConsoleApps_ConsoleAppsExtensions_FinalizeConsoleClientRegistration.htm).
Используйте метод [ConfigureConsoleForClient(IUnityContainer, TextWriter,
TextWriter, Boolean, String,
String)](M_Tessa_Platform_ConsoleApps_ConsoleAppsExtensions_ConfigureConsoleForClient.htm),
если требуется выполнить полную конфигурацию консольного приложения для
клиента с параметрами по умолчанию, в этом случае вызывать другие методы на
контейнере не требуется.  
[RegisterConsoleOperationLogger(IUnityContainer,
IConsoleScriptOptions)](M_Tessa_Platform_ConsoleApps_ConsoleAppsExtensions_RegisterConsoleOperationLogger_1.htm)|
Выполняет регистрацию объекта
[IConsoleLogger](T_Tessa_Platform_ConsoleApps_IConsoleLogger.htm) для вывода
на консоль.  
[RegisterConsoleOperationLogger(IUnityContainer, TextWriter, TextWriter,
Boolean)](M_Tessa_Platform_ConsoleApps_ConsoleAppsExtensions_RegisterConsoleOperationLogger.htm)|
Выполняет регистрацию объекта
[IConsoleLogger](T_Tessa_Platform_ConsoleApps_IConsoleLogger.htm) для вывода
на консоль.  
[RegisterDatabaseForConsole](M_Tessa_Platform_ConsoleApps_ConsoleAppsExtensions_RegisterDatabaseForConsole.htm)|
Выполняет регистрацию зависимостей для базы данных и контейнеров расширений
для консольной команды tadmin.  
[RegisterServerForConsole](M_Tessa_Platform_ConsoleApps_ConsoleAppsExtensions_RegisterServerForConsole.htm)|
Выполняет регистрацию зависимостей для консольной команды, использующей
серверное API и прямое подключение к БД.  
[RegisterServerSettingsForConsole](M_Tessa_Platform_ConsoleApps_ConsoleAppsExtensions_RegisterServerSettingsForConsole.htm)|
Выполняет регистрацию настроек сервера
[ITessaServerSettings](T_Tessa_Platform_ITessaServerSettings.htm) с
использованием списка папок ProbingPath с конфигурационным файлом.  
## __См. также
#### Ссылки
[Tessa.Platform.ConsoleApps - пространство
имён](N_Tessa_Platform_ConsoleApps.htm)
