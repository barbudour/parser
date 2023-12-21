# FakeWorkplaceService.SaveWorkplaceSettingsAsync - метод
Осуществляет сохранение пользовательских настроек рабочего места.
## __Definition
 **Пространство имён:** [Tessa.Applications](N_Tessa_Applications.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public Task SaveWorkplaceSettingsAsync(
    	IEnumerable<IWorkplaceSettingsMetadata> settings,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Function SaveWorkplaceSettingsAsync ( 
    	settings As IEnumerable(Of IWorkplaceSettingsMetadata),
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task
C++ __Копировать
     public:
    virtual Task^ SaveWorkplaceSettingsAsync(
    	IEnumerable<IWorkplaceSettingsMetadata^>^ settings, 
    	CancellationToken cancellationToken = CancellationToken()
    ) sealed
F# __Копировать
     abstract SaveWorkplaceSettingsAsync : 
            settings : IEnumerable<IWorkplaceSettingsMetadata> * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task 
    override SaveWorkplaceSettingsAsync : 
            settings : IEnumerable<IWorkplaceSettingsMetadata> * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task 
#### Параметры
settings
[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)<[IWorkplaceSettingsMetadata](T_Tessa_Views_Workplaces_IWorkplaceSettingsMetadata.htm)>
     Сохраняемые настройки рабочих места. 
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)  
Асинхронная задача.
#### Реализации
[IWorkplaceService.SaveWorkplaceSettingsAsync(IEnumerable<IWorkplaceSettingsMetadata>,
CancellationToken)](M_Tessa_Views_Workplaces_IWorkplaceService_SaveWorkplaceSettingsAsync.htm)  
##  __См. также
#### Ссылки
[FakeWorkplaceService - ](T_Tessa_Applications_FakeWorkplaceService.htm)
[Tessa.Applications - пространство имён](N_Tessa_Applications.htm)
