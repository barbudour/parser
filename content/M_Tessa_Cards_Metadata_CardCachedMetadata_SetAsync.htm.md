# CardCachedMetadata.SetAsync - метод
Устанавливает заданную метаинформацию в кэше. При этом метаинформация
защищается от изменений, если кэш также защищён от изменений.
## __Definition
 **Пространство имён:** [Tessa.Cards.Metadata](N_Tessa_Cards_Metadata.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public Task SetAsync(
    	ICardMetadata metadata,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Function SetAsync ( 
    	metadata As ICardMetadata,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task
C++ __Копировать
     public:
    virtual Task^ SetAsync(
    	ICardMetadata^ metadata, 
    	CancellationToken cancellationToken = CancellationToken()
    ) sealed
F# __Копировать
     abstract SetAsync : 
            metadata : ICardMetadata * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task 
    override SetAsync : 
            metadata : ICardMetadata * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task 
#### Параметры
metadata [ICardMetadata](T_Tessa_Cards_ICardMetadata.htm)
     Устанавливаемая метаинформация. Не может быть равна null. 
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)  
Асинхронная задача.
#### Реализации
[ICardCachedMetadata.SetAsync(ICardMetadata,
CancellationToken)](M_Tessa_Cards_ICardCachedMetadata_SetAsync.htm)  
##  __См. также
#### Ссылки
[CardCachedMetadata - ](T_Tessa_Cards_Metadata_CardCachedMetadata.htm)
[Tessa.Cards.Metadata - пространство имён](N_Tessa_Cards_Metadata.htm)
