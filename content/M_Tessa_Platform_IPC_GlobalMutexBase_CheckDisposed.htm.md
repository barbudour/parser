# GlobalMutexBase.CheckDisposed - метод
Выбрасывает исключение [ObjectDisposedException], если ресурсы текущего
объекта были освобождены.
## __Definition
 **Пространство имён:** [Tessa.Platform.IPC](N_Tessa_Platform_IPC.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
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
[GlobalMutexBase - ](T_Tessa_Platform_IPC_GlobalMutexBase.htm)
[Tessa.Platform.IPC - пространство имён](N_Tessa_Platform_IPC.htm)
[System.ObjectDisposedException]
