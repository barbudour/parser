# ICardGetExtension.BeforeRequest - метод
Действие, выполняемое перед получением карточки стандартными средствами. Может
установить ответ на запрос для того, чтобы получение карточки стандартными
средствами не выполнялось.
## __Definition
 **Пространство имён:** [Tessa.Cards.Extensions](N_Tessa_Cards_Extensions.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     Task BeforeRequest(
    	ICardGetExtensionContext context
    )
VB __Копировать
     Function BeforeRequest ( 
    	context As ICardGetExtensionContext
    ) As Task
C++ __Копировать
    Task^ BeforeRequest(
    	ICardGetExtensionContext^ context
    )
F# __Копировать
     abstract BeforeRequest : 
            context : ICardGetExtensionContext -> Task 
#### Параметры
context
[ICardGetExtensionContext](T_Tessa_Cards_Extensions_ICardGetExtensionContext.htm)
    Контекст процесса получения карточки.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)  
Асинхронная задача.
##  __См. также
#### Ссылки
[ICardGetExtension - ](T_Tessa_Cards_Extensions_ICardGetExtension.htm)
[Tessa.Cards.Extensions - пространство имён](N_Tessa_Cards_Extensions.htm)
