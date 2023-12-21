# PluginGracefulStopEventToken - конструктор
Создаёт экземпляр класса, который подготавливает объект для синхронизации
события, выполняемого при завершении метода
[EntryPointAsync(CancellationToken)](M_Chronos_Contracts_IPlugin_EntryPointAsync.htm).
## __Definition
 **Пространство имён:**
[Chronos.Platform.Scheduling](N_Chronos_Platform_Scheduling.htm)  
 **Сборка:** Chronos.Platform (в Chronos.Platform.dll) Версия: 3.6.0.17
C# __Копировать
     public PluginGracefulStopEventToken(
    	CancellationTokenSource cancellationTokenSource = null
    )
VB __Копировать
     Public Sub New ( 
    	Optional cancellationTokenSource As CancellationTokenSource = Nothing
    )
C++ __Копировать
     public:
    PluginGracefulStopEventToken(
    	CancellationTokenSource^ cancellationTokenSource = nullptr
    )
F# __Копировать
     new : 
            ?cancellationTokenSource : CancellationTokenSource 
    (* Defaults:
            let _cancellationTokenSource = defaultArg cancellationTokenSource null
    *)
    -> PluginGracefulStopEventToken
#### Параметры
cancellationTokenSource
[CancellationTokenSource](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtokensource)
(Optional)
     Объект, посредством которого можно отменить выполнение метода [EntryPointAsync(CancellationToken)](M_Chronos_Contracts_IPlugin_EntryPointAsync.htm), а также обычно токен остановки передаётся в метод [WaitUntilEntryPointFinishedAsync(CancellationToken)](M_Chronos_Platform_Scheduling_PluginGracefulStopEventToken_WaitUntilEntryPointFinishedAsync.htm). Укажите null, если будет создан новый объект. 
## __Заметки
Конструктор создаёт объект
[ManualResetEvent](https://learn.microsoft.com/dotnet/api/system.threading.manualresetevent)
для события, выполняемого при завершении метода
[EntryPointAsync(CancellationToken)](M_Chronos_Contracts_IPlugin_EntryPointAsync.htm).
Для такого объекта будет вызван метод
[Dispose()](https://learn.microsoft.com/dotnet/api/system.idisposable.dispose#system-
idisposable-dispose) в методе
[Dispose()](M_Chronos_Platform_Scheduling_PluginGracefulStopEventToken_Dispose.htm)
этого класса.
## __См. также
#### Ссылки
[PluginGracefulStopEventToken -
](T_Chronos_Platform_Scheduling_PluginGracefulStopEventToken.htm)
[Chronos.Platform.Scheduling - пространство
имён](N_Chronos_Platform_Scheduling.htm)
