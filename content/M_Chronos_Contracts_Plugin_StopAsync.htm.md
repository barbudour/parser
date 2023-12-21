# Plugin.StopAsync - метод
Метод, вызываемый хостом при вежливой остановке плагина. Он должен максимально
быстро завершить выполнение плагина, но не завершать свою работу до тех пор,
пока потоки, с которыми работает плагин, не будут завершены. Реализация по
умолчанию устанавливает свойство
[StopRequested](P_Chronos_Contracts_Plugin_StopRequested.htm), после чего
ожидает завершение метода
[EntryPointAsync(CancellationToken)](M_Chronos_Contracts_Plugin_EntryPointAsync.htm).
## __Definition
 **Пространство имён:** [Chronos.Contracts](N_Chronos_Contracts.htm)  
 **Сборка:** Chronos.Contracts (в Chronos.Contracts.dll) Версия: 3.6.0.17
C# __Копировать
     public virtual Task StopAsync(
    	IGracefulStopToken token
    )
VB __Копировать
     Public Overridable Function StopAsync ( 
    	token As IGracefulStopToken
    ) As Task
C++ __Копировать
     public:
    virtual Task^ StopAsync(
    	IGracefulStopToken^ token
    )
F# __Копировать
     abstract StopAsync : 
            token : IGracefulStopToken -> Task 
    override StopAsync : 
            token : IGracefulStopToken -> Task 
#### Параметры
token [IGracefulStopToken](T_Chronos_Contracts_IGracefulStopToken.htm)
    Токен, позволяющий определить состояние плагина из метода его вежливой остановки.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)
#### Реализации
[ISupportGracefulStop.StopAsync(IGracefulStopToken)](M_Chronos_Contracts_ISupportGracefulStop_StopAsync.htm)  
##  __Заметки
Хост вызовет этот метод в потоке, отличном от потока, в котором выполняется
метод
[EntryPointAsync(CancellationToken)](M_Chronos_Contracts_IPlugin_EntryPointAsync.htm).
## __См. также
#### Ссылки
[Plugin - ](T_Chronos_Contracts_Plugin.htm)
[Chronos.Contracts - пространство имён](N_Chronos_Contracts.htm)
