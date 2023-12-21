# IGlobalEvent.TryGetWaitHandle - метод
Возвращает объект WaitHandle для ожидания сигнального состояния у события, или
null, если используемый объект синхронизации не предоставляет объекта
WaitHandle и требуется вызвать метод Wait для ожидания.
## __Definition
 **Пространство имён:** [Chronos.Platform.IPC](N_Chronos_Platform_IPC.htm)  
 **Сборка:** Chronos.Platform (в Chronos.Platform.dll) Версия: 3.6.0.17
C# __Копировать
     WaitHandle TryGetWaitHandle()
VB __Копировать
     Function TryGetWaitHandle As WaitHandle
C++ __Копировать
    WaitHandle^ TryGetWaitHandle()
F# __Копировать
     abstract TryGetWaitHandle : unit -> WaitHandle 
#### Возвращаемое значение
[WaitHandle](https://learn.microsoft.com/dotnet/api/system.threading.waithandle)  
Объект WaitHandle для ожидания сигнального состояния у события, или null, если
используемый объект синхронизации не предоставляет объекта WaitHandle.
## __Исключения
[System.ObjectDisposedException]| Ресурсы, занимаемые объектом, были
освобождены.  
---|---  
##  __См. также
#### Ссылки
[IGlobalEvent - ](T_Chronos_Platform_IPC_IGlobalEvent.htm)
[Chronos.Platform.IPC - пространство имён](N_Chronos_Platform_IPC.htm)
[System.ObjectDisposedException]
