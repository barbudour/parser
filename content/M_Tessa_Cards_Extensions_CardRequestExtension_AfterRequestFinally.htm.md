# CardRequestExtension.AfterRequestFinally - метод
Действие, выполняемое при возникновении исключения или после универсального
взаимодействия с сервисом карточек как при успешном, так и при неудачном
результате. Необработанные исключения не прерывают выполнение цепочки
расширений.
## __Definition
 **Пространство имён:** [Tessa.Cards.Extensions](N_Tessa_Cards_Extensions.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public virtual Task AfterRequestFinally(
    	ICardRequestExtensionContext context
    )
VB __Копировать
     Public Overridable Function AfterRequestFinally ( 
    	context As ICardRequestExtensionContext
    ) As Task
C++ __Копировать
     public:
    virtual Task^ AfterRequestFinally(
    	ICardRequestExtensionContext^ context
    )
F# __Копировать
     abstract AfterRequestFinally : 
            context : ICardRequestExtensionContext -> Task 
    override AfterRequestFinally : 
            context : ICardRequestExtensionContext -> Task 
#### Параметры
context
[ICardRequestExtensionContext](T_Tessa_Cards_Extensions_ICardRequestExtensionContext.htm)
    Контекст процесса универсального взаимодействия с сервисом карточек.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)  
Асинхронная задача.
#### Реализации
[ICardRequestExtension.AfterRequestFinally(ICardRequestExtensionContext)](M_Tessa_Cards_Extensions_ICardRequestExtension_AfterRequestFinally.htm)  
##  __Заметки
По умолчанию метод не выполняет действий.
##  __См. также
#### Ссылки
[CardRequestExtension - ](T_Tessa_Cards_Extensions_CardRequestExtension.htm)
[Tessa.Cards.Extensions - пространство имён](N_Tessa_Cards_Extensions.htm)
