# CardTypeServerRepository.InsertManyAsync - метод
Добавляет несколько типов карточек оптимальным способом.
##  __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public Task InsertManyAsync(
    	IReadOnlyCollection<CardTypeRepositoryData> cardTypes,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Function InsertManyAsync ( 
    	cardTypes As IReadOnlyCollection(Of CardTypeRepositoryData),
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task
C++ __Копировать
     public:
    virtual Task^ InsertManyAsync(
    	IReadOnlyCollection<CardTypeRepositoryData^>^ cardTypes, 
    	CancellationToken cancellationToken = CancellationToken()
    ) sealed
F# __Копировать
     abstract InsertManyAsync : 
            cardTypes : IReadOnlyCollection<CardTypeRepositoryData> * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task 
    override InsertManyAsync : 
            cardTypes : IReadOnlyCollection<CardTypeRepositoryData> * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task 
#### Параметры
cardTypes
[IReadOnlyCollection](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlycollection-1)<[CardTypeRepositoryData](T_Tessa_Cards_CardTypeRepositoryData.htm)>
    Список объектов, описывающих типы карточек.
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)  
Асинхронная задача.
#### Реализации
[ICardTypeServerRepository.InsertManyAsync(IReadOnlyCollection<CardTypeRepositoryData>,
CancellationToken)](M_Tessa_Cards_ICardTypeServerRepository_InsertManyAsync.htm)  
##  __См. также
#### Ссылки
[CardTypeServerRepository - ](T_Tessa_Cards_CardTypeServerRepository.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
