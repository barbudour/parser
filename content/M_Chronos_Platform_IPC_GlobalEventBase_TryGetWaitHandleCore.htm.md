# GlobalEventBase.TryGetWaitHandleCore - метод
Возвращает объект WaitHandle для ожидания сигнального состояния у события, или
null, если используемый объект синхронизации не предоставляет объекта
WaitHandle и требуется вызвать метод Wait для ожидания.
## __Definition
 **Пространство имён:** [Chronos.Platform.IPC](N_Chronos_Platform_IPC.htm)  
 **Сборка:** Chronos.Platform (в Chronos.Platform.dll) Версия: 3.6.0.17
C# __Копировать
     protected virtual WaitHandle TryGetWaitHandleCore()
VB __Копировать
     Protected Overridable Function TryGetWaitHandleCore As WaitHandle
C++ __Копировать
     protected:
    virtual WaitHandle^ TryGetWaitHandleCore()
F# __Копировать
     abstract TryGetWaitHandleCore : unit -> WaitHandle 
    override TryGetWaitHandleCore : unit -> WaitHandle 
#### Возвращаемое значение
[WaitHandle](https://learn.microsoft.com/dotnet/api/system.threading.waithandle)  
Объект WaitHandle для ожидания сигнального состояния у события, или null, если
используемый объект синхронизации не предоставляет объекта WaitHandle.
## __См. также
#### Ссылки
[GlobalEventBase - ](T_Chronos_Platform_IPC_GlobalEventBase.htm)
[Chronos.Platform.IPC - пространство имён](N_Chronos_Platform_IPC.htm)
