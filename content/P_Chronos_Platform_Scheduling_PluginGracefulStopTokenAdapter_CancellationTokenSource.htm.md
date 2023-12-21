# PluginGracefulStopTokenAdapter.CancellationTokenSource - свойство
Объект, посредством которого можно отменить выполнение метода
[EntryPointAsync(CancellationToken)](M_Chronos_Contracts_IPlugin_EntryPointAsync.htm),
а также обычно токен остановки передаётся в метод
[WaitUntilEntryPointFinishedAsync(CancellationToken)](M_Chronos_Platform_Scheduling_PluginGracefulStopTokenAdapter_WaitUntilEntryPointFinishedAsync.htm).
## __Definition
 **Пространство имён:**
[Chronos.Platform.Scheduling](N_Chronos_Platform_Scheduling.htm)  
 **Сборка:** Chronos.Platform (в Chronos.Platform.dll) Версия: 3.6.0.17
C# __Копировать
     public CancellationTokenSource CancellationTokenSource { get; }
VB __Копировать
     Public ReadOnly Property CancellationTokenSource As CancellationTokenSource
    	Get
C++ __Копировать
     public:
    virtual property CancellationTokenSource^ CancellationTokenSource {
    	CancellationTokenSource^ get () sealed;
    }
F# __Копировать
     abstract CancellationTokenSource : CancellationTokenSource with get
    override CancellationTokenSource : CancellationTokenSource with get
#### Значение свойства
[CancellationTokenSource](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtokensource)
#### Реализации
[IGracefulStopToken.CancellationTokenSource](P_Chronos_Contracts_IGracefulStopToken_CancellationTokenSource.htm)  
##  __См. также
#### Ссылки
[PluginGracefulStopTokenAdapter -
](T_Chronos_Platform_Scheduling_PluginGracefulStopTokenAdapter.htm)
[Chronos.Platform.Scheduling - пространство
имён](N_Chronos_Platform_Scheduling.htm)
