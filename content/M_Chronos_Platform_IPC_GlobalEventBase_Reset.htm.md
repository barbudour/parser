# GlobalEventBase.Reset - метод
Переводит событие в несигнальное состояние, при этом все ожидающие событие
подписчики получают управление.
## __Definition
 **Пространство имён:** [Chronos.Platform.IPC](N_Chronos_Platform_IPC.htm)  
 **Сборка:** Chronos.Platform (в Chronos.Platform.dll) Версия: 3.6.0.17
C# __Копировать
     public void Reset()
VB __Копировать
     Public Sub Reset
C++ __Копировать
     public:
    virtual void Reset() sealed
F# __Копировать
     abstract Reset : unit -> unit 
    override Reset : unit -> unit 
#### Реализации
[IGlobalEvent.Reset()](M_Chronos_Platform_IPC_IGlobalEvent_Reset.htm)  
##  __Исключения
[System.ObjectDisposedException]| Ресурсы, занимаемые объектом, были
освобождены.  
---|---  
##  __См. также
#### Ссылки
[GlobalEventBase - ](T_Chronos_Platform_IPC_GlobalEventBase.htm)
[Chronos.Platform.IPC - пространство имён](N_Chronos_Platform_IPC.htm)
[System.ObjectDisposedException]
