# PluginFacade.GracefulStopExceptionOccured - событие
Событие, происходящее при возникновении исключения в процессе вежливой
остановки плагина методом
[StopAsync(IGracefulStopToken)](M_Chronos_Contracts_ISupportGracefulStop_StopAsync.htm).
## __Definition
 **Пространство имён:**
[Chronos.Platform.Scheduling](N_Chronos_Platform_Scheduling.htm)  
 **Сборка:** Chronos.Platform (в Chronos.Platform.dll) Версия: 3.6.0.17
C# __Копировать
     public event EventHandler<PluginGracefulStopExceptionEventArgs> GracefulStopExceptionOccured
VB __Копировать
     Public Event GracefulStopExceptionOccured As EventHandler(Of PluginGracefulStopExceptionEventArgs)
C++ __Копировать
     public:
     event EventHandler<PluginGracefulStopExceptionEventArgs^>^ GracefulStopExceptionOccured {
    	void add (EventHandler<PluginGracefulStopExceptionEventArgs^>^ value);
    	void remove (EventHandler<PluginGracefulStopExceptionEventArgs^>^ value);
    }
F# __Копировать
     member GracefulStopExceptionOccured : IEvent<EventHandler<PluginGracefulStopExceptionEventArgs>,
        PluginGracefulStopExceptionEventArgs>
#### Значение
[EventHandler](https://learn.microsoft.com/dotnet/api/system.eventhandler-1)<[PluginGracefulStopExceptionEventArgs](T_Chronos_Platform_Scheduling_PluginGracefulStopExceptionEventArgs.htm)>
##  __Заметки
Событие возникает на стороне плагина в процессе вежливой остановки, поэтому
его обработчики должны выполняться быстро, пока хост не выполнил аварийное
завершение процесса плагина.
## __См. также
#### Ссылки
[PluginFacade - ](T_Chronos_Platform_Scheduling_PluginFacade.htm)
[Chronos.Platform.Scheduling - пространство
имён](N_Chronos_Platform_Scheduling.htm)
