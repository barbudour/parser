# IGracefulStopToken - интерфейс
Токен, позволяющий определить состояние плагина из метода его вежливой
остановки.
## __Definition
 **Пространство имён:** [Chronos.Contracts](N_Chronos_Contracts.htm)  
 **Сборка:** Chronos.Contracts (в Chronos.Contracts.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IGracefulStopToken
VB __Копировать
     Public Interface IGracefulStopToken
C++ __Копировать
     public interface class IGracefulStopToken
F# __Копировать
     type IGracefulStopToken = interface end
##  __Заметки
Все открытые методы и свойства класса являются потокобезопасными.
## __Свойства
[CancellationTokenSource](P_Chronos_Contracts_IGracefulStopToken_CancellationTokenSource.htm)|
Объект, посредством которого можно отменить выполнение метода
[EntryPointAsync(CancellationToken)](M_Chronos_Contracts_IPlugin_EntryPointAsync.htm),
а также обычно токен остановки передаётся в метод
[WaitUntilEntryPointFinishedAsync(CancellationToken)](M_Chronos_Contracts_IGracefulStopToken_WaitUntilEntryPointFinishedAsync.htm).  
---|---  
[EntryPointFinished](P_Chronos_Contracts_IGracefulStopToken_EntryPointFinished.htm)|
Признак того, что метод
[EntryPointAsync(CancellationToken)](M_Chronos_Contracts_IPlugin_EntryPointAsync.htm)
плагина был завершён.  
## __Методы
[WaitUntilEntryPointFinishedAsync](M_Chronos_Contracts_IGracefulStopToken_WaitUntilEntryPointFinishedAsync.htm)|
Ожидает, пока метод
[EntryPointAsync(CancellationToken)](M_Chronos_Contracts_IPlugin_EntryPointAsync.htm)
плагина не будет завершён.  
---|---  
## __См. также
#### Ссылки
[Chronos.Contracts - пространство имён](N_Chronos_Contracts.htm)
