# GlobalEventBase.CheckDisposed - метод
Выбрасывает исключение [ObjectDisposedException], если ресурсы текущего
объекта были освобождены.
## __Definition
 **Пространство имён:** [Chronos.Platform.IPC](N_Chronos_Platform_IPC.htm)  
 **Сборка:** Chronos.Platform (в Chronos.Platform.dll) Версия: 3.6.0.17
C# __Копировать
     protected void CheckDisposed()
VB __Копировать
     Protected Sub CheckDisposed
C++ __Копировать
     protected:
    void CheckDisposed()
F# __Копировать
     member CheckDisposed : unit -> unit 
## __Исключения
[System.ObjectDisposedException]| Ресурсы, занимаемые объектом, были
освобождены.  
---|---  
##  __См. также
#### Ссылки
[GlobalEventBase - ](T_Chronos_Platform_IPC_GlobalEventBase.htm)
[Chronos.Platform.IPC - пространство имён](N_Chronos_Platform_IPC.htm)
[System.ObjectDisposedException]
