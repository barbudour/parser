# GlobalEventAwaiter.WaitAnyAsync - метод
Выполняет ожидание либо глобального события
[GlobalEvent](P_Chronos_Platform_IPC_GlobalEventAwaiter_GlobalEvent.htm), либо
любого из переданных объектов
[WaitHandle](https://learn.microsoft.com/dotnet/api/system.threading.waithandle).
## __Definition
 **Пространство имён:** [Chronos.Platform.IPC](N_Chronos_Platform_IPC.htm)  
 **Сборка:** Chronos.Platform (в Chronos.Platform.dll) Версия: 3.6.0.17
C# __Копировать
     public Task WaitAnyAsync(
    	CancellationToken cancellationToken,
    	params WaitHandle[] handles
    )
VB __Копировать
     Public Function WaitAnyAsync ( 
    	cancellationToken As CancellationToken,
    	ParamArray handles As WaitHandle()
    ) As Task
C++ __Копировать
     public:
    Task^ WaitAnyAsync(
    	CancellationToken cancellationToken, 
    	... array<WaitHandle^>^ handles
    )
F# __Копировать
     member WaitAnyAsync : 
            cancellationToken : CancellationToken * 
            handles : WaitHandle[] -> Task 
#### Параметры
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
    Объект, посредством которого можно отменить асинхронную задачу.
handles
[WaitHandle](https://learn.microsoft.com/dotnet/api/system.threading.waithandle)[]
     Список объектов [WaitHandle](https://learn.microsoft.com/dotnet/api/system.threading.waithandle), для которых выполняется ожидание первого завершившегося объекта. Может быть равен null или пустому массиву. Значения в массиве также могут быть равны null, в этом случае их ожидание не выполняется. 
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)  
Асинхронная задача.
##  __См. также
#### Ссылки
[GlobalEventAwaiter - ](T_Chronos_Platform_IPC_GlobalEventAwaiter.htm)
[Chronos.Platform.IPC - пространство имён](N_Chronos_Platform_IPC.htm)
