# ICardNewExtension.BeforeRequest - метод
Действие, выполняемое перед созданием структуры карточки стандартными
средствами. Может установить ответ на запрос для того, чтобы создание
структуры карточки стандартными средствами не выполнялось.
## __Definition
 **Пространство имён:** [Tessa.Cards.Extensions](N_Tessa_Cards_Extensions.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     Task BeforeRequest(
    	ICardNewExtensionContext context
    )
VB __Копировать
     Function BeforeRequest ( 
    	context As ICardNewExtensionContext
    ) As Task
C++ __Копировать
    Task^ BeforeRequest(
    	ICardNewExtensionContext^ context
    )
F# __Копировать
     abstract BeforeRequest : 
            context : ICardNewExtensionContext -> Task 
#### Параметры
context
[ICardNewExtensionContext](T_Tessa_Cards_Extensions_ICardNewExtensionContext.htm)
    Контекст процесса создания структуры карточки.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)  
Асинхронная задача.
##  __См. также
#### Ссылки
[ICardNewExtension - ](T_Tessa_Cards_Extensions_ICardNewExtension.htm)
[Tessa.Cards.Extensions - пространство имён](N_Tessa_Cards_Extensions.htm)
