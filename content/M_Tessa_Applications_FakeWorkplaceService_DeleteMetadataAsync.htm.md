# FakeWorkplaceService.DeleteMetadataAsync - метод
Осуществляет удаление объекта метаданных пользователя.
## __Definition
 **Пространство имён:** [Tessa.Applications](N_Tessa_Applications.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public Task DeleteMetadataAsync(
    	IWorkplaceComponentMetadata metadata,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Function DeleteMetadataAsync ( 
    	metadata As IWorkplaceComponentMetadata,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task
C++ __Копировать
     public:
    virtual Task^ DeleteMetadataAsync(
    	IWorkplaceComponentMetadata^ metadata, 
    	CancellationToken cancellationToken = CancellationToken()
    ) sealed
F# __Копировать
     abstract DeleteMetadataAsync : 
            metadata : IWorkplaceComponentMetadata * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task 
    override DeleteMetadataAsync : 
            metadata : IWorkplaceComponentMetadata * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task 
#### Параметры
metadata
[IWorkplaceComponentMetadata](T_Tessa_Views_Workplaces_IWorkplaceComponentMetadata.htm)
     Удаляемые метаданные. 
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)  
Асинхронная задача.
#### Реализации
[IWorkplaceService.DeleteMetadataAsync(IWorkplaceComponentMetadata,
CancellationToken)](M_Tessa_Views_Workplaces_IWorkplaceService_DeleteMetadataAsync.htm)  
##  __См. также
#### Ссылки
[FakeWorkplaceService - ](T_Tessa_Applications_FakeWorkplaceService.htm)
[Tessa.Applications - пространство имён](N_Tessa_Applications.htm)
