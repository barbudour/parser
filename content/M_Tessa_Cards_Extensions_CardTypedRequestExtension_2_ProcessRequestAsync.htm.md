# CardTypedRequestExtension<TRequest, TResponse>.ProcessRequestAsync - метод
Выполняет обработку заданного запроса и возвращает ответ на запрос. Метод
может вернуть null, если устанавливать ответ на запрос не требуется.
## __Definition
 **Пространство имён:** [Tessa.Cards.Extensions](N_Tessa_Cards_Extensions.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     protected abstract Task<TResponse> ProcessRequestAsync(
    	ICardRequestExtensionContext context,
    	TRequest request
    )
VB __Копировать
     Protected MustOverride Function ProcessRequestAsync ( 
    	context As ICardRequestExtensionContext,
    	request As TRequest
    ) As Task(Of TResponse)
C++ __Копировать
     protected:
    virtual Task<TResponse>^ ProcessRequestAsync(
    	ICardRequestExtensionContext^ context, 
    	TRequest request
    ) abstract
F# __Копировать
     abstract ProcessRequestAsync : 
            context : ICardRequestExtensionContext * 
            request : 'TRequest -> Task<'TResponse> 
#### Параметры
context
[ICardRequestExtensionContext](T_Tessa_Cards_Extensions_ICardRequestExtensionContext.htm)
    Контекст универсального взаимодействия с сервисом карточек.
request [TRequest](T_Tessa_Cards_Extensions_CardTypedRequestExtension_2.htm)
     Строготипизированный запрос. Не равен null. 
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)<[TResponse](T_Tessa_Cards_Extensions_CardTypedRequestExtension_2.htm)>  
Ответ на запрос или null, если устанавливать ответ на запрос не требуется.
## __См. также
#### Ссылки
[CardTypedRequestExtension<TRequest, TResponse> \-
](T_Tessa_Cards_Extensions_CardTypedRequestExtension_2.htm)
[Tessa.Cards.Extensions - пространство имён](N_Tessa_Cards_Extensions.htm)
