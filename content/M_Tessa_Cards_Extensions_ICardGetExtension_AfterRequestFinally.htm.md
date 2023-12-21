# ICardGetExtension.AfterRequestFinally - метод
Действие, выполняемое при возникновении исключения или после получения
карточки как при успешном, так и при неудачном результате. Необработанные
исключения не прерывают выполнение цепочки расширений.
## __Definition
 **Пространство имён:** [Tessa.Cards.Extensions](N_Tessa_Cards_Extensions.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     Task AfterRequestFinally(
    	ICardGetExtensionContext context
    )
VB __Копировать
     Function AfterRequestFinally ( 
    	context As ICardGetExtensionContext
    ) As Task
C++ __Копировать
    Task^ AfterRequestFinally(
    	ICardGetExtensionContext^ context
    )
F# __Копировать
     abstract AfterRequestFinally : 
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
