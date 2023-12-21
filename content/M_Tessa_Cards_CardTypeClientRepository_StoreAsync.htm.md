# CardTypeClientRepository.StoreAsync - метод
Добавляет или обновляет тип карточки.
##  __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public Task StoreAsync(
    	CardType cardType,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Function StoreAsync ( 
    	cardType As CardType,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task
C++ __Копировать
     public:
    virtual Task^ StoreAsync(
    	CardType^ cardType, 
    	CancellationToken cancellationToken = CancellationToken()
    ) sealed
F# __Копировать
     abstract StoreAsync : 
            cardType : CardType * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task 
    override StoreAsync : 
            cardType : CardType * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task 
#### Параметры
cardType [CardType](T_Tessa_Cards_CardType.htm)
    Объект, описывающий тип карточки.
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)  
Асинхронная задача.
#### Реализации
[ICardTypeClientRepository.StoreAsync(CardType,
CancellationToken)](M_Tessa_Cards_ICardTypeClientRepository_StoreAsync.htm)  
##  __См. также
#### Ссылки
[CardTypeClientRepository - ](T_Tessa_Cards_CardTypeClientRepository.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
