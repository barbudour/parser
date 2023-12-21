# ClientViewServiceImplementer.GetViewsMetadataAsync - метод
Возвращает список доступных представлений
## __Definition
 **Пространство имён:** [Tessa.Applications](N_Tessa_Applications.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     protected virtual Task<IReadOnlyList<IViewMetadata>> GetViewsMetadataAsync(
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Protected Overridable Function GetViewsMetadataAsync ( 
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task(Of IReadOnlyList(Of IViewMetadata))
C++ __Копировать
     protected:
    virtual Task<IReadOnlyList<IViewMetadata^>^>^ GetViewsMetadataAsync(
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     abstract GetViewsMetadataAsync : 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<IReadOnlyList<IViewMetadata>> 
    override GetViewsMetadataAsync : 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<IReadOnlyList<IViewMetadata>> 
#### Параметры
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)<[IReadOnlyList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist-1)<[IViewMetadata](T_Tessa_Views_Metadata_IViewMetadata.htm)>>  
Список доступных представлений
## __См. также
#### Ссылки
[ClientViewServiceImplementer -
](T_Tessa_Applications_ClientViewServiceImplementer.htm)
[Tessa.Applications - пространство имён](N_Tessa_Applications.htm)
