# ProcessRefContainer.TryLoadFromStorageAsync - метод
Пытается загрузить информацию из изолированного хранилища.
## __Definition
 **Пространство имён:**
[Chronos.Platform.Processes](N_Chronos_Platform_Processes.htm)  
 **Сборка:** Chronos.Platform (в Chronos.Platform.dll) Версия: 3.6.0.17
C# __Копировать
     public Task<bool> TryLoadFromStorageAsync()
VB __Копировать
     Public Function TryLoadFromStorageAsync As Task(Of Boolean)
C++ __Копировать
     public:
    Task<bool>^ TryLoadFromStorageAsync()
F# __Копировать
     member TryLoadFromStorageAsync : unit -> Task<bool> 
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)<[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)>  
true, если объекты [ProcessRef](T_Chronos_Platform_Processes_ProcessRef.htm)
были успешно загружены; false в противном случае.
## __См. также
#### Ссылки
[ProcessRefContainer - ](T_Chronos_Platform_Processes_ProcessRefContainer.htm)
[Chronos.Platform.Processes - пространство
имён](N_Chronos_Platform_Processes.htm)
