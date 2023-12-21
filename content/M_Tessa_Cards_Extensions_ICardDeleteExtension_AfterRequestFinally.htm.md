# ICardDeleteExtension.AfterRequestFinally - метод
Действие, выполняемое при возникновении исключения или после удаления карточки
как при успешном, так и при неудачном результате. Необработанные исключения не
прерывают выполнение цепочки расширений.
## __Definition
 **Пространство имён:** [Tessa.Cards.Extensions](N_Tessa_Cards_Extensions.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     Task AfterRequestFinally(
    	ICardDeleteExtensionContext context
    )
VB __Копировать
     Function AfterRequestFinally ( 
    	context As ICardDeleteExtensionContext
    ) As Task
C++ __Копировать
    Task^ AfterRequestFinally(
    	ICardDeleteExtensionContext^ context
    )
F# __Копировать
     abstract AfterRequestFinally : 
            context : ICardDeleteExtensionContext -> Task 
#### Параметры
context
[ICardDeleteExtensionContext](T_Tessa_Cards_Extensions_ICardDeleteExtensionContext.htm)
    Контекст процесса удаления карточки.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)  
Асинхронная задача.
##  __См. также
#### Ссылки
[ICardDeleteExtension - ](T_Tessa_Cards_Extensions_ICardDeleteExtension.htm)
[Tessa.Cards.Extensions - пространство имён](N_Tessa_Cards_Extensions.htm)
