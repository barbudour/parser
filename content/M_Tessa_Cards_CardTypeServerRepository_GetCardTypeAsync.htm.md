# CardTypeServerRepository.GetCardTypeAsync - метод
Возвращает объект, описывающий тип карточки, со всей необходимой информацией.
##  __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public Task<CardTypeRepositoryData> GetCardTypeAsync(
    	Guid cardTypeID,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Function GetCardTypeAsync ( 
    	cardTypeID As Guid,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task(Of CardTypeRepositoryData)
C++ __Копировать
     public:
    virtual Task<CardTypeRepositoryData^>^ GetCardTypeAsync(
    	Guid cardTypeID, 
    	CancellationToken cancellationToken = CancellationToken()
    ) sealed
F# __Копировать
     abstract GetCardTypeAsync : 
            cardTypeID : Guid * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<CardTypeRepositoryData> 
    override GetCardTypeAsync : 
            cardTypeID : Guid * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<CardTypeRepositoryData> 
#### Параметры
cardTypeID [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
    Идентификатор типа карточки.
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)<[CardTypeRepositoryData](T_Tessa_Cards_CardTypeRepositoryData.htm)>  
Объект, описывающий тип карточки.
#### Реализации
[ICardTypeServerRepository.GetCardTypeAsync(Guid,
CancellationToken)](M_Tessa_Cards_ICardTypeServerRepository_GetCardTypeAsync.htm)  
##  __См. также
#### Ссылки
[CardTypeServerRepository - ](T_Tessa_Cards_CardTypeServerRepository.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
