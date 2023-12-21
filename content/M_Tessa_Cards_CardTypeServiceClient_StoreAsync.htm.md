# CardTypeServiceClient.StoreAsync - метод
Добавляет, обновляет и удаляет типы карточек.
##  __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public Task StoreAsync(
    	IReadOnlyCollection<CardType> cardTypes,
    	IReadOnlyCollection<Guid> cardTypeIDListToDelete,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Function StoreAsync ( 
    	cardTypes As IReadOnlyCollection(Of CardType),
    	cardTypeIDListToDelete As IReadOnlyCollection(Of Guid),
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task
C++ __Копировать
     public:
    virtual Task^ StoreAsync(
    	IReadOnlyCollection<CardType^>^ cardTypes, 
    	IReadOnlyCollection<Guid>^ cardTypeIDListToDelete, 
    	CancellationToken cancellationToken = CancellationToken()
    ) sealed
F# __Копировать
     abstract StoreAsync : 
            cardTypes : IReadOnlyCollection<CardType> * 
            cardTypeIDListToDelete : IReadOnlyCollection<Guid> * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task 
    override StoreAsync : 
            cardTypes : IReadOnlyCollection<CardType> * 
            cardTypeIDListToDelete : IReadOnlyCollection<Guid> * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task 
#### Параметры
cardTypes
[IReadOnlyCollection](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlycollection-1)<[CardType](T_Tessa_Cards_CardType.htm)>
    Объекты, описывающие типы карточек, которые будут добавлены или обновлены.
cardTypeIDListToDelete
[IReadOnlyCollection](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlycollection-1)<[Guid](https://learn.microsoft.com/dotnet/api/system.guid)>
    Список идентификаторов типов карточек. которые требуется удалить.
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)  
Асинхронная задача.
#### Реализации
[ICardTypeService.StoreAsync(IReadOnlyCollection<CardType>,
IReadOnlyCollection<Guid>,
CancellationToken)](M_Tessa_Cards_ICardTypeService_StoreAsync.htm)  
##  __См. также
#### Ссылки
[CardTypeServiceClient - ](T_Tessa_Cards_CardTypeServiceClient.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
