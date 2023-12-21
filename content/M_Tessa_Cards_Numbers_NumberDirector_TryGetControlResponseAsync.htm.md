# NumberDirector.TryGetControlResponseAsync - метод
Возвращает объект ответа на запрос к элементу управления по ответу на запрос к
API номеров на сервере. Возвращает null, если объект отсутствует в ответе на
запрос.
## __Definition
 **Пространство имён:** [Tessa.Cards.Numbers](N_Tessa_Cards_Numbers.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     protected virtual ValueTask<NumberControlResponse> TryGetControlResponseAsync(
    	INumberContext context,
    	CardRequest request,
    	CardResponse response,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Protected Overridable Function TryGetControlResponseAsync ( 
    	context As INumberContext,
    	request As CardRequest,
    	response As CardResponse,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As ValueTask(Of NumberControlResponse)
C++ __Копировать
     protected:
    virtual ValueTask<NumberControlResponse^> TryGetControlResponseAsync(
    	INumberContext^ context, 
    	CardRequest^ request, 
    	CardResponse^ response, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     abstract TryGetControlResponseAsync : 
            context : INumberContext * 
            request : CardRequest * 
            response : CardResponse * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<NumberControlResponse> 
    override TryGetControlResponseAsync : 
            context : INumberContext * 
            request : CardRequest * 
            response : CardResponse * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<NumberControlResponse> 
#### Параметры
context [INumberContext](T_Tessa_Cards_Numbers_INumberContext.htm)
    Контекст действия с номером, которое связано с элементом управления.
request [CardRequest](T_Tessa_Cards_CardRequest.htm)
    Запрос к API номеров на сервере.
response [CardResponse](T_Tessa_Cards_CardResponse.htm)
    Ответ на запрос к API номеров на сервере.
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask-1)<[NumberControlResponse](T_Tessa_Cards_Numbers_NumberControlResponse.htm)>  
Объект ответа на запрос к элементу управления по ответу на запрос к API
номеров на сервере или null, если объект отсутствует в ответе на запрос.
## __См. также
#### Ссылки
[NumberDirector - ](T_Tessa_Cards_Numbers_NumberDirector.htm)
[Tessa.Cards.Numbers - пространство имён](N_Tessa_Cards_Numbers.htm)
