# CardTypesWebProxy.GetCardTypeAsync - метод
Возвращает объект, описывающий тип карточки, со всей необходимой информацией.
##  __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public Task<CardType> GetCardTypeAsync(
    	Guid cardTypeID,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Function GetCardTypeAsync ( 
    	cardTypeID As Guid,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task(Of CardType)
C++ __Копировать
     public:
    Task<CardType^>^ GetCardTypeAsync(
    	Guid cardTypeID, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     member GetCardTypeAsync : 
            cardTypeID : Guid * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<CardType> 
#### Параметры
cardTypeID [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
    Идентификатор типа карточки.
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)<[CardType](T_Tessa_Cards_CardType.htm)>  
Объект, описывающий тип карточки.
##  __См. также
#### Ссылки
[CardTypesWebProxy - ](T_Tessa_Cards_CardTypesWebProxy.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
