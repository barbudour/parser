# PluginFacade.OnGracefulStopExceptionOccured - метод
Вызывается при возникновении исключения в процессе вежливой остановки плагина
методом
[StopAsync(IGracefulStopToken)](M_Chronos_Contracts_ISupportGracefulStop_StopAsync.htm).
## __Definition
 **Пространство имён:**
[Chronos.Platform.Scheduling](N_Chronos_Platform_Scheduling.htm)  
 **Сборка:** Chronos.Platform (в Chronos.Platform.dll) Версия: 3.6.0.17
C# __Копировать
     protected virtual void OnGracefulStopExceptionOccured(
    	PluginGracefulStopExceptionEventArgs e
    )
VB __Копировать
     Protected Overridable Sub OnGracefulStopExceptionOccured ( 
    	e As PluginGracefulStopExceptionEventArgs
    )
C++ __Копировать
     protected:
    virtual void OnGracefulStopExceptionOccured(
    	PluginGracefulStopExceptionEventArgs^ e
    )
F# __Копировать
     abstract OnGracefulStopExceptionOccured : 
            e : PluginGracefulStopExceptionEventArgs -> unit 
    override OnGracefulStopExceptionOccured : 
            e : PluginGracefulStopExceptionEventArgs -> unit 
#### Параметры
e
[PluginGracefulStopExceptionEventArgs](T_Chronos_Platform_Scheduling_PluginGracefulStopExceptionEventArgs.htm)
    Аргументы события.
##  __Заметки
Метод вызывается на стороне плагина в процессе вежливой остановки, поэтому он
должен выполняться быстро, пока хост не выполнил аварийное завершение процесса
плагина.
## __См. также
#### Ссылки
[PluginFacade - ](T_Chronos_Platform_Scheduling_PluginFacade.htm)
[Chronos.Platform.Scheduling - пространство
имён](N_Chronos_Platform_Scheduling.htm)
