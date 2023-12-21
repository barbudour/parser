# NumberControlRequestExtension.ProcessRequestAsync - метод
Выполняет обработку заданного запроса и возвращает ответ на запрос. Метод
может вернуть null, если устанавливать ответ на запрос не требуется.
## __Definition
 **Пространство имён:** [Tessa.Cards.Numbers](N_Tessa_Cards_Numbers.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     protected override Task<NumberControlResponse> ProcessRequestAsync(
    	ICardRequestExtensionContext context,
    	NumberControlRequest request
    )
VB __Копировать
     Protected Overrides Function ProcessRequestAsync ( 
    	context As ICardRequestExtensionContext,
    	request As NumberControlRequest
    ) As Task(Of NumberControlResponse)
C++ __Копировать
     protected:
    virtual Task<NumberControlResponse^>^ ProcessRequestAsync(
    	ICardRequestExtensionContext^ context, 
    	NumberControlRequest^ request
    ) override
F# __Копировать
     abstract ProcessRequestAsync : 
            context : ICardRequestExtensionContext * 
            request : NumberControlRequest -> Task<NumberControlResponse> 
    override ProcessRequestAsync : 
            context : ICardRequestExtensionContext * 
            request : NumberControlRequest -> Task<NumberControlResponse> 
#### Параметры
context
[ICardRequestExtensionContext](T_Tessa_Cards_Extensions_ICardRequestExtensionContext.htm)
    Контекст универсального взаимодействия с сервисом карточек.
request [NumberControlRequest](T_Tessa_Cards_Numbers_NumberControlRequest.htm)
     Строготипизированный запрос. Не равен null. 
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)<[NumberControlResponse](T_Tessa_Cards_Numbers_NumberControlResponse.htm)>  
Ответ на запрос или null, если устанавливать ответ на запрос не требуется.
## __См. также
#### Ссылки
[NumberControlRequestExtension -
](T_Tessa_Cards_Numbers_NumberControlRequestExtension.htm)
[Tessa.Cards.Numbers - пространство имён](N_Tessa_Cards_Numbers.htm)
