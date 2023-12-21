# NumberControlRequestExtension.TryLoadOrCreateCardAsync - метод
Загружает или создаёт карточку по заданному идентификатору и возвращает
карточку или null, если карточка не была создана или загружена. Создание
выполняется в случае, если в запросе request указано, что карточка ещё ни разу
не была сохранена.
## __Definition
 **Пространство имён:** [Tessa.Cards.Numbers](N_Tessa_Cards_Numbers.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     protected virtual Task<Card> TryLoadOrCreateCardAsync(
    	ICardRequestExtensionContext context,
    	NumberControlRequest request,
    	Guid cardID
    )
VB __Копировать
     Protected Overridable Function TryLoadOrCreateCardAsync ( 
    	context As ICardRequestExtensionContext,
    	request As NumberControlRequest,
    	cardID As Guid
    ) As Task(Of Card)
C++ __Копировать
     protected:
    virtual Task<Card^>^ TryLoadOrCreateCardAsync(
    	ICardRequestExtensionContext^ context, 
    	NumberControlRequest^ request, 
    	Guid cardID
    )
F# __Копировать
     abstract TryLoadOrCreateCardAsync : 
            context : ICardRequestExtensionContext * 
            request : NumberControlRequest * 
            cardID : Guid -> Task<Card> 
    override TryLoadOrCreateCardAsync : 
            context : ICardRequestExtensionContext * 
            request : NumberControlRequest * 
            cardID : Guid -> Task<Card> 
#### Параметры
context
[ICardRequestExtensionContext](T_Tessa_Cards_Extensions_ICardRequestExtensionContext.htm)
    Контекст выполнения расширений.
request [NumberControlRequest](T_Tessa_Cards_Numbers_NumberControlRequest.htm)
    Запрос на выполнение действий с номерами.
cardID [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
    Идентификатор загружаемой карточки.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)<[Card](T_Tessa_Cards_Card.htm)>  
Загруженная или созданная карточка, или null, если карточка не была создана
или загружена.
## __См. также
#### Ссылки
[NumberControlRequestExtension -
](T_Tessa_Cards_Numbers_NumberControlRequestExtension.htm)
[Tessa.Cards.Numbers - пространство имён](N_Tessa_Cards_Numbers.htm)
