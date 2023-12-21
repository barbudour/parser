# ProcessLogger - класс
Средства логирования для жизненного цикла процессов.
## __Definition
 **Пространство имён:** [Chronos.Platform](N_Chronos_Platform.htm)  
 **Сборка:** Chronos.Platform (в Chronos.Platform.dll) Версия: 3.6.0.17
C# __Копировать
     public static class ProcessLogger
VB __Копировать
     Public NotInheritable Class ProcessLogger
C++ __Копировать
     public ref class ProcessLogger abstract sealed
F# __Копировать
     [<AbstractClassAttribute>]
    [<SealedAttribute>]
    type ProcessLogger = class end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ ProcessLogger
##  __Методы
[LogConfigurationNotFound](M_Chronos_Platform_ProcessLogger_LogConfigurationNotFound.htm)|
Выполняет логирование ошибки о том, что файл конфигурации плагина не найден.  
---|---  
[LogHostIsLaunched](M_Chronos_Platform_ProcessLogger_LogHostIsLaunched.htm)|
Логирует отладочную информацию о том, что хост-процесс в текущем процессе был
запущен.  
[LogHostIsLaunchingPlugin](M_Chronos_Platform_ProcessLogger_LogHostIsLaunchingPlugin.htm)|
Логирует отладочную информацию о том, что начался запуск плагина в дочернем
процессе.  
[LogHostIsShutdown](M_Chronos_Platform_ProcessLogger_LogHostIsShutdown.htm)|
Логирует отладочную информацию о том, что хост-процесс в текущем процессе был
остановлен.  
[LogHostIsShuttingDown](M_Chronos_Platform_ProcessLogger_LogHostIsShuttingDown.htm)|
Логирует отладочную информацию о том, что хост-процесс в текущем процессе
начал остановку.  
[LogPluginIsCancelling](M_Chronos_Platform_ProcessLogger_LogPluginIsCancelling.htm)|
Логирует отладочную информацию о том, что плагин в текущем процессе запустил
асинхронную отмену операций в
[EntryPointAsync(CancellationToken)](M_Chronos_Contracts_IPlugin_EntryPointAsync.htm).  
[LogPluginIsDisabled](M_Chronos_Platform_ProcessLogger_LogPluginIsDisabled.htm)|
Выполняет логирование ошибки о том, что плагин был отключён в соответствии с
настройками в своей конфигурации.  
[LogPluginIsLaunched](M_Chronos_Platform_ProcessLogger_LogPluginIsLaunched.htm)|
Логирует отладочную информацию о том, что плагин в дочернем процессе был
запущен.  
[LogPluginIsShutdown](M_Chronos_Platform_ProcessLogger_LogPluginIsShutdown.htm)|
Логирует отладочную информацию о том, что плагин в дочернем процессе завершил
свою работу.  
[LogPluginIsStopped](M_Chronos_Platform_ProcessLogger_LogPluginIsStopped.htm)|
Логирует отладочную информацию о том, что плагин в текущем процессе был
остановлен.  
[LogPluginIsStopping](M_Chronos_Platform_ProcessLogger_LogPluginIsStopping.htm)|
Логирует отладочную информацию о том, что плагин в текущем процессе начал
остановку.  
## __См. также
#### Ссылки
[Chronos.Platform - пространство имён](N_Chronos_Platform.htm)
