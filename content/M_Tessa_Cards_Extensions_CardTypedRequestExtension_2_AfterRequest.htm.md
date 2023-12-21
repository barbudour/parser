# CardTypedRequestExtension<TRequest, TResponse>.AfterRequest - метод
Действие, выполняемое после универсального взаимодействия с сервисом карточек
как при успешном, так и при неудачном результате.
##  __Definition
 **Пространство имён:** [Tessa.Cards.Extensions](N_Tessa_Cards_Extensions.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public override Task AfterRequest(
    	ICardRequestExtensionContext context
    )
VB __Копировать
     Public Overrides Function AfterRequest ( 
    	context As ICardRequestExtensionContext
    ) As Task
C++ __Копировать
     public:
    virtual Task^ AfterRequest(
    	ICardRequestExtensionContext^ context
    ) override
F# __Копировать
     abstract AfterRequest : 
            context : ICardRequestExtensionContext -> Task 
    override AfterRequest : 
            context : ICardRequestExtensionContext -> Task 
#### Параметры
context
[ICardRequestExtensionContext](T_Tessa_Cards_Extensions_ICardRequestExtensionContext.htm)
    Контекст процесса универсального взаимодействия с сервисом карточек.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)  
Асинхронная задача.
#### Реализации
[ICardRequestExtension.AfterRequest(ICardRequestExtensionContext)](M_Tessa_Cards_Extensions_ICardRequestExtension_AfterRequest.htm)  
##  __См. также
#### Ссылки
[CardTypedRequestExtension<TRequest, TResponse> \-
](T_Tessa_Cards_Extensions_CardTypedRequestExtension_2.htm)
[Tessa.Cards.Extensions - пространство имён](N_Tessa_Cards_Extensions.htm)
