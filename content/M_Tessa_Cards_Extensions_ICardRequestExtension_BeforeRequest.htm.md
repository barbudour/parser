# ICardRequestExtension.BeforeRequest - метод
Действие, выполняемое перед универсальным взаимодействием с сервисом карточек
стандартными средствами. Может установить ответ на запрос для того, чтобы
взаимодействие с сервисом карточек стандартными средствами не выполнялось.
## __Definition
 **Пространство имён:** [Tessa.Cards.Extensions](N_Tessa_Cards_Extensions.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     Task BeforeRequest(
    	ICardRequestExtensionContext context
    )
VB __Копировать
     Function BeforeRequest ( 
    	context As ICardRequestExtensionContext
    ) As Task
C++ __Копировать
    Task^ BeforeRequest(
    	ICardRequestExtensionContext^ context
    )
F# __Копировать
     abstract BeforeRequest : 
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
