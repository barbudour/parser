# GlobalMutexBase.DisposeAsync(Boolean) - метод
Освобождает ресурсы, занимаемые объектом.
##  __Definition
 **Пространство имён:** [Chronos.Platform.IPC](N_Chronos_Platform_IPC.htm)  
 **Сборка:** Chronos.Platform (в Chronos.Platform.dll) Версия: 3.6.0.17
C# __Копировать
     protected virtual ValueTask DisposeAsync(
    	bool disposing
    )
VB __Копировать
     Protected Overridable Function DisposeAsync ( 
    	disposing As Boolean
    ) As ValueTask
C++ __Копировать
     protected:
    virtual ValueTask DisposeAsync(
    	bool disposing
    )
F# __Копировать
     abstract DisposeAsync : 
            disposing : bool -> ValueTask 
    override DisposeAsync : 
            disposing : bool -> ValueTask 
#### Параметры
disposing [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)
    true, если метод вызван до финализации; false, если метод вызван из финализатора. 
#### Возвращаемое значение
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask)  
Асинхронная задача.
##  __См. также
#### Ссылки
[GlobalMutexBase - ](T_Chronos_Platform_IPC_GlobalMutexBase.htm)
[DisposeAsync -
перегрузка](Overload_Chronos_Platform_IPC_GlobalMutexBase_DisposeAsync.htm)
[Chronos.Platform.IPC - пространство имён](N_Chronos_Platform_IPC.htm)
