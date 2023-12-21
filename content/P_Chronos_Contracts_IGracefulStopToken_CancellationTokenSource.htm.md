# IGracefulStopToken.CancellationTokenSource - свойство
Объект, посредством которого можно отменить выполнение метода
[EntryPointAsync(CancellationToken)](M_Chronos_Contracts_IPlugin_EntryPointAsync.htm),
а также обычно токен остановки передаётся в метод
[WaitUntilEntryPointFinishedAsync(CancellationToken)](M_Chronos_Contracts_IGracefulStopToken_WaitUntilEntryPointFinishedAsync.htm).
## __Definition
 **Пространство имён:** [Chronos.Contracts](N_Chronos_Contracts.htm)  
 **Сборка:** Chronos.Contracts (в Chronos.Contracts.dll) Версия: 3.6.0.17
C# __Копировать
    CancellationTokenSource CancellationTokenSource { get; }
VB __Копировать
     ReadOnly Property CancellationTokenSource As CancellationTokenSource
    	Get
C++ __Копировать
    property CancellationTokenSource^ CancellationTokenSource {
    	CancellationTokenSource^ get ();
    }
F# __Копировать
     abstract CancellationTokenSource : CancellationTokenSource with get
#### Значение свойства
[CancellationTokenSource](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtokensource)
##  __См. также
#### Ссылки
[IGracefulStopToken - ](T_Chronos_Contracts_IGracefulStopToken.htm)
[Chronos.Contracts - пространство имён](N_Chronos_Contracts.htm)
