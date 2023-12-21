# LinuxGlobalEvent.DisposeAsync(Boolean) - метод
Освобождает ресурсы, занимаемые объектом.
##  __Definition
 **Пространство имён:** [Chronos.Platform.IPC](N_Chronos_Platform_IPC.htm)  
 **Сборка:** Chronos.Platform.Linux (в Chronos.Platform.Linux.dll) Версия:
3.6.0.17
C# __Копировать
     protected override ValueTask DisposeAsync(
    	bool disposing
    )
VB __Копировать
     Protected Overrides Function DisposeAsync ( 
    	disposing As Boolean
    ) As ValueTask
C++ __Копировать
     protected:
    virtual ValueTask DisposeAsync(
    	bool disposing
    ) override
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
[LinuxGlobalEvent - ](T_Chronos_Platform_IPC_LinuxGlobalEvent.htm)
[DisposeAsync -
перегрузка](Overload_Chronos_Platform_IPC_LinuxGlobalEvent_DisposeAsync.htm)
[Chronos.Platform.IPC - пространство имён](N_Chronos_Platform_IPC.htm)
