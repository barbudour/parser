# FakeWorkplaceService.StoreMetadataAsync - метод
Осуществляет сохранение метаданных пользователя.
## __Definition
 **Пространство имён:** [Tessa.Applications](N_Tessa_Applications.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public Task StoreMetadataAsync(
    	IWorkplaceComponentMetadata metadata,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Function StoreMetadataAsync ( 
    	metadata As IWorkplaceComponentMetadata,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task
C++ __Копировать
     public:
    virtual Task^ StoreMetadataAsync(
    	IWorkplaceComponentMetadata^ metadata, 
    	CancellationToken cancellationToken = CancellationToken()
    ) sealed
F# __Копировать
     abstract StoreMetadataAsync : 
            metadata : IWorkplaceComponentMetadata * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task 
    override StoreMetadataAsync : 
            metadata : IWorkplaceComponentMetadata * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task 
#### Параметры
metadata
[IWorkplaceComponentMetadata](T_Tessa_Views_Workplaces_IWorkplaceComponentMetadata.htm)
     Создаваемые метаданные. 
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)  
Асинхронная задача.
#### Реализации
[IWorkplaceService.StoreMetadataAsync(IWorkplaceComponentMetadata,
CancellationToken)](M_Tessa_Views_Workplaces_IWorkplaceService_StoreMetadataAsync.htm)  
##  __См. также
#### Ссылки
[FakeWorkplaceService - ](T_Tessa_Applications_FakeWorkplaceService.htm)
[Tessa.Applications - пространство имён](N_Tessa_Applications.htm)
