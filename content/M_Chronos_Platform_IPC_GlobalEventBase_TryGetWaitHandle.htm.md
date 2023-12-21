# GlobalEventBase.TryGetWaitHandle - метод
Возвращает объект WaitHandle для ожидания сигнального состояния у события, или
null, если используемый объект синхронизации не предоставляет объекта
WaitHandle и требуется вызвать метод Wait для ожидания.
## __Definition
 **Пространство имён:** [Chronos.Platform.IPC](N_Chronos_Platform_IPC.htm)  
 **Сборка:** Chronos.Platform (в Chronos.Platform.dll) Версия: 3.6.0.17
C# __Копировать
     public WaitHandle TryGetWaitHandle()
VB __Копировать
     Public Function TryGetWaitHandle As WaitHandle
C++ __Копировать
     public:
    virtual WaitHandle^ TryGetWaitHandle() sealed
F# __Копировать
     abstract TryGetWaitHandle : unit -> WaitHandle 
    override TryGetWaitHandle : unit -> WaitHandle 
#### Возвращаемое значение
[WaitHandle](https://learn.microsoft.com/dotnet/api/system.threading.waithandle)  
Объект WaitHandle для ожидания сигнального состояния у события, или null, если
используемый объект синхронизации не предоставляет объекта WaitHandle.
#### Реализации
[IGlobalEvent.TryGetWaitHandle()](M_Chronos_Platform_IPC_IGlobalEvent_TryGetWaitHandle.htm)  
##  __См. также
#### Ссылки
[GlobalEventBase - ](T_Chronos_Platform_IPC_GlobalEventBase.htm)
[Chronos.Platform.IPC - пространство имён](N_Chronos_Platform_IPC.htm)
