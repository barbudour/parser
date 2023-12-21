# ICardRequestExtension.AfterRequestFinally - метод
Действие, выполняемое при возникновении исключения или после универсального
взаимодействия с сервисом карточек как при успешном, так и при неудачном
результате. Необработанные исключения не прерывают выполнение цепочки
расширений.
## __Definition
 **Пространство имён:** [Tessa.Cards.Extensions](N_Tessa_Cards_Extensions.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     Task AfterRequestFinally(
    	ICardRequestExtensionContext context
    )
VB __Копировать
     Function AfterRequestFinally ( 
    	context As ICardRequestExtensionContext
    ) As Task
C++ __Копировать
    Task^ AfterRequestFinally(
    	ICardRequestExtensionContext^ context
    )
F# __Копировать
     abstract AfterRequestFinally : 
            context : ICardRequestExtensionContext -> Task 
#### Параметры
context
[ICardRequestExtensionContext](T_Tessa_Cards_Extensions_ICardRequestExtensionContext.htm)
    Контекст процесса универсального взаимодействия с сервисом карточек.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)  
Асинхронная задача.
##  __См. также
#### Ссылки
[ICardRequestExtension - ](T_Tessa_Cards_Extensions_ICardRequestExtension.htm)
[Tessa.Cards.Extensions - пространство имён](N_Tessa_Cards_Extensions.htm)
