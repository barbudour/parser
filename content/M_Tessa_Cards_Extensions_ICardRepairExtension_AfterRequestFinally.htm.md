# ICardRepairExtension.AfterRequestFinally - метод
Действие, выполняемое при возникновении исключения или после исправления
структуры карточки как при успешном, так и при неудачном результате.
Необработанные исключения не прерывают выполнение цепочки расширений.
## __Definition
 **Пространство имён:** [Tessa.Cards.Extensions](N_Tessa_Cards_Extensions.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     Task AfterRequestFinally(
    	ICardRepairExtensionContext context
    )
VB __Копировать
     Function AfterRequestFinally ( 
    	context As ICardRepairExtensionContext
    ) As Task
C++ __Копировать
    Task^ AfterRequestFinally(
    	ICardRepairExtensionContext^ context
    )
F# __Копировать
     abstract AfterRequestFinally : 
            context : ICardRepairExtensionContext -> Task 
#### Параметры
context
[ICardRepairExtensionContext](T_Tessa_Cards_Extensions_ICardRepairExtensionContext.htm)
    Контекст процесса исправления структуры карточки.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)  
Асинхронная задача.
##  __См. также
#### Ссылки
[ICardRepairExtension - ](T_Tessa_Cards_Extensions_ICardRepairExtension.htm)
[Tessa.Cards.Extensions - пространство имён](N_Tessa_Cards_Extensions.htm)
