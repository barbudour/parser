# ICardStoreExtension.AfterBeginTransaction - метод
Действие, выполняемое после начала транзакции.
##  __Definition
 **Пространство имён:** [Tessa.Cards.Extensions](N_Tessa_Cards_Extensions.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     Task AfterBeginTransaction(
    	ICardStoreExtensionContext context
    )
VB __Копировать
     Function AfterBeginTransaction ( 
    	context As ICardStoreExtensionContext
    ) As Task
C++ __Копировать
    Task^ AfterBeginTransaction(
    	ICardStoreExtensionContext^ context
    )
F# __Копировать
     abstract AfterBeginTransaction : 
            context : ICardStoreExtensionContext -> Task 
#### Параметры
context
[ICardStoreExtensionContext](T_Tessa_Cards_Extensions_ICardStoreExtensionContext.htm)
    Контекст процесса сохранения карточки.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)  
Асинхронная задача.
##  __См. также
#### Ссылки
[ICardStoreExtension - ](T_Tessa_Cards_Extensions_ICardStoreExtension.htm)
[Tessa.Cards.Extensions - пространство имён](N_Tessa_Cards_Extensions.htm)
