# DefaultChronosPlatformDependencies.CreateProcessManagerWithJob - метод
Создаёт объект [Chronos.Platform.Processes.IProcessManager] для создания
других процессов. При наличии возможности будет создан объект, объединяющий
текущий и дочерние процессы в Job. Метод может вызываться даже в том случае,
платформой не поддерживается [ChronosPlatformFeature.ProcessJob].
## __Definition
 **Пространство имён:** [Chronos.Platform](N_Chronos_Platform.htm)  
 **Сборка:** Chronos.Platform (в Chronos.Platform.dll) Версия: 3.6.0.17
C# __Копировать
     public virtual IProcessManager CreateProcessManagerWithJob()
VB __Копировать
     Public Overridable Function CreateProcessManagerWithJob As IProcessManager
C++ __Копировать
     public:
    virtual IProcessManager^ CreateProcessManagerWithJob()
F# __Копировать
     abstract CreateProcessManagerWithJob : unit -> IProcessManager 
    override CreateProcessManagerWithJob : unit -> IProcessManager 
#### Возвращаемое значение
[IProcessManager](T_Chronos_Platform_Processes_IProcessManager.htm)  
Созданный объект. Не должен быть равен null.
#### Реализации
[IChronosPlatformDependencies.CreateProcessManagerWithJob()](M_Chronos_Platform_IChronosPlatformDependencies_CreateProcessManagerWithJob.htm)  
##  __См. также
#### Ссылки
[DefaultChronosPlatformDependencies -
](T_Chronos_Platform_DefaultChronosPlatformDependencies.htm)
[Chronos.Platform - пространство имён](N_Chronos_Platform.htm)
