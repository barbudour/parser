# CardNewStrategy.CreateResponseAsync - метод
Создаёт ответ на запрос по созданию карточки, содержащий данные секций
карточки.
##  __Definition
 **Пространство имён:**
[Tessa.Cards.ComponentModel](N_Tessa_Cards_ComponentModel.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public ValueTask<CardNewResponse> CreateResponseAsync(
    	CardNewContext context,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Function CreateResponseAsync ( 
    	context As CardNewContext,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As ValueTask(Of CardNewResponse)
C++ __Копировать
     public:
    virtual ValueTask<CardNewResponse^> CreateResponseAsync(
    	CardNewContext^ context, 
    	CancellationToken cancellationToken = CancellationToken()
    ) sealed
F# __Копировать
     abstract CreateResponseAsync : 
            context : CardNewContext * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<CardNewResponse> 
    override CreateResponseAsync : 
            context : CardNewContext * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<CardNewResponse> 
#### Параметры
context [CardNewContext](T_Tessa_Cards_ComponentModel_CardNewContext.htm)
    Контекст операции по созданию карточки.
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask-1)<[CardNewResponse](T_Tessa_Cards_CardNewResponse.htm)>  
Ответ на запрос по созданию карточки, содержащий данные секций карточки.
#### Реализации
[ICardNewStrategy.CreateResponseAsync(CardNewContext,
CancellationToken)](M_Tessa_Cards_ComponentModel_ICardNewStrategy_CreateResponseAsync.htm)  
##  __См. также
#### Ссылки
[CardNewStrategy - ](T_Tessa_Cards_ComponentModel_CardNewStrategy.htm)
[Tessa.Cards.ComponentModel - пространство
имён](N_Tessa_Cards_ComponentModel.htm)
