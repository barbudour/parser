# ConsoleAppHelper - класс
Вспомогательные методы для консольных приложений.
## __Definition
 **Пространство имён:**
[Tessa.Platform.ConsoleApps](N_Tessa_Platform_ConsoleApps.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static class ConsoleAppHelper
VB __Копировать
     Public NotInheritable Class ConsoleAppHelper
C++ __Копировать
     public ref class ConsoleAppHelper abstract sealed
F# __Копировать
     [<AbstractClassAttribute>]
    [<SealedAttribute>]
    type ConsoleAppHelper = class end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ ConsoleAppHelper
##  __Свойства
[EnvironmentExitAction](P_Tessa_Platform_ConsoleApps_ConsoleAppHelper_EnvironmentExitAction.htm)|  
---|---  
[EnvironmentExitDefaultAction](P_Tessa_Platform_ConsoleApps_ConsoleAppHelper_EnvironmentExitDefaultAction.htm)|  
## __Методы
[CreateAsyncDbManagerFuncAsync(IConsoleLogger, IConsoleScriptOptions,
CancellationToken)](M_Tessa_Platform_ConsoleApps_ConsoleAppHelper_CreateAsyncDbManagerFuncAsync_1.htm)|  
---|---  
[CreateAsyncDbManagerFuncAsync(IConsoleLogger, String, String,
CancellationToken)](M_Tessa_Platform_ConsoleApps_ConsoleAppHelper_CreateAsyncDbManagerFuncAsync.htm)|  
[CreateDbManagerAsync(IConsoleLogger, IConsoleScriptOptions,
CancellationToken)](M_Tessa_Platform_ConsoleApps_ConsoleAppHelper_CreateDbManagerAsync_1.htm)|  
[CreateDbManagerAsync(IConsoleLogger, String, String,
CancellationToken)](M_Tessa_Platform_ConsoleApps_ConsoleAppHelper_CreateDbManagerAsync.htm)|  
[EnvironmentExit](M_Tessa_Platform_ConsoleApps_ConsoleAppHelper_EnvironmentExit.htm)|  
[LogLoadedExtensionsAsync](M_Tessa_Platform_ConsoleApps_ConsoleAppHelper_LogLoadedExtensionsAsync.htm)|  
[WriteLogo(Boolean)](M_Tessa_Platform_ConsoleApps_ConsoleAppHelper_WriteLogo.htm)|  
[WriteLogo(TextWriter,
Boolean)](M_Tessa_Platform_ConsoleApps_ConsoleAppHelper_WriteLogo_1.htm)|  
## __Поля
[FailedLoginExitCode](F_Tessa_Platform_ConsoleApps_ConsoleAppHelper_FailedLoginExitCode.htm)|
Код возврата консольного приложения при невозможности выполнить логин к веб-
сервису. Рекомендуется вызвать метод
[EnvironmentExit(Int32)](M_Tessa_Platform_ConsoleApps_ConsoleAppHelper_EnvironmentExit.htm)
с указанием этого кода возврата, если логин не выполнен.  
---|---  
[UnhandledExceptionExitCode](F_Tessa_Platform_ConsoleApps_ConsoleAppHelper_UnhandledExceptionExitCode.htm)|
Код возврата консольного приложения при возникновении необработанного
исключения при выполнении консольной команды. Обработка исключения выполняется
автоматически, использовать этот код возврата вручную не требуется.  
## __См. также
#### Ссылки
[Tessa.Platform.ConsoleApps - пространство
имён](N_Tessa_Platform_ConsoleApps.htm)
