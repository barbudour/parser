# AssemblySynchronizationSource.RequireAdministrator - метод
Устанавливает признак необходимости наличия административных прав платформы
Tessa для запуска приложения.
## __Definition
 **Пространство имён:**
[Tessa.Applications.Synchronization](N_Tessa_Applications_Synchronization.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public IAssemblySynchronizationSource RequireAdministrator(
    	bool administratorRequired
    )
VB __Копировать
     Public Function RequireAdministrator ( 
    	administratorRequired As Boolean
    ) As IAssemblySynchronizationSource
C++ __Копировать
     public:
    virtual IAssemblySynchronizationSource^ RequireAdministrator(
    	bool administratorRequired
    ) sealed
F# __Копировать
     abstract RequireAdministrator : 
            administratorRequired : bool -> IAssemblySynchronizationSource 
    override RequireAdministrator : 
            administratorRequired : bool -> IAssemblySynchronizationSource 
#### Параметры
administratorRequired
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)
     Признак необходимости наличия административных прав 
#### Возвращаемое значение
[IAssemblySynchronizationSource](T_Tessa_Applications_Synchronization_IAssemblySynchronizationSource.htm)  
Источник синхронизации
[AssemblySynchronizationSource](T_Tessa_Applications_Synchronization_AssemblySynchronizationSource.htm).
#### Реализации
[IAssemblySynchronizationSource.RequireAdministrator(Boolean)](M_Tessa_Applications_Synchronization_IAssemblySynchronizationSource_RequireAdministrator.htm)  
##  __См. также
#### Ссылки
[AssemblySynchronizationSource -
](T_Tessa_Applications_Synchronization_AssemblySynchronizationSource.htm)
[Tessa.Applications.Synchronization - пространство
имён](N_Tessa_Applications_Synchronization.htm)
