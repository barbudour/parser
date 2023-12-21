# PluginGracefulStopEventToken - свойства
##  __Свойства
[CancellationTokenSource](P_Chronos_Platform_Scheduling_PluginGracefulStopEventToken_CancellationTokenSource.htm)|
Объект, посредством которого можно отменить выполнение метода
[EntryPointAsync(CancellationToken)](M_Chronos_Contracts_IPlugin_EntryPointAsync.htm),
а также обычно токен остановки передаётся в метод
[WaitUntilEntryPointFinishedAsync(CancellationToken)](M_Chronos_Platform_Scheduling_PluginGracefulStopEventToken_WaitUntilEntryPointFinishedAsync.htm).  
---|---  
[EntryPointFinished](P_Chronos_Platform_Scheduling_PluginGracefulStopEventToken_EntryPointFinished.htm)|
Признак того, что метод
[EntryPointAsync(CancellationToken)](M_Chronos_Contracts_IPlugin_EntryPointAsync.htm)
плагина был завершён.  
[EntryPointFinishedEventHandle](P_Chronos_Platform_Scheduling_PluginGracefulStopEventToken_EntryPointFinishedEventHandle.htm)|
Объект, используемый для синхронизации потоков при наступлении события
вежливой остановки плагина.  
## __См. также
#### Ссылки
[PluginGracefulStopEventToken -
](T_Chronos_Platform_Scheduling_PluginGracefulStopEventToken.htm)
[Chronos.Platform.Scheduling - пространство
имён](N_Chronos_Platform_Scheduling.htm)
