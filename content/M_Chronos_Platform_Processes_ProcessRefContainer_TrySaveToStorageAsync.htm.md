# ProcessRefContainer.TrySaveToStorageAsync - метод
Пытается сохранить информацию в изолированное хранилище
## __Definition
 **Пространство имён:**
[Chronos.Platform.Processes](N_Chronos_Platform_Processes.htm)  
 **Сборка:** Chronos.Platform (в Chronos.Platform.dll) Версия: 3.6.0.17
C# __Копировать
     public Task<bool> TrySaveToStorageAsync()
VB __Копировать
     Public Function TrySaveToStorageAsync As Task(Of Boolean)
C++ __Копировать
     public:
    Task<bool>^ TrySaveToStorageAsync()
F# __Копировать
     member TrySaveToStorageAsync : unit -> Task<bool> 
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)<[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)>  
true, если все объекты
[ProcessRef](T_Chronos_Platform_Processes_ProcessRef.htm) этого контейнера
были успешно сохранены; false в противном случае.
## __См. также
#### Ссылки
[ProcessRefContainer - ](T_Chronos_Platform_Processes_ProcessRefContainer.htm)
[Chronos.Platform.Processes - пространство
имён](N_Chronos_Platform_Processes.htm)
