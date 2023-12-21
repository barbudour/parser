# ICardDeleteExtension.AfterBeginTransaction - метод
Действие, выполняемое после начала транзакции.
##  __Definition
 **Пространство имён:** [Tessa.Cards.Extensions](N_Tessa_Cards_Extensions.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     Task AfterBeginTransaction(
    	ICardDeleteExtensionContext context
    )
VB __Копировать
     Function AfterBeginTransaction ( 
    	context As ICardDeleteExtensionContext
    ) As Task
C++ __Копировать
    Task^ AfterBeginTransaction(
    	ICardDeleteExtensionContext^ context
    )
F# __Копировать
     abstract AfterBeginTransaction : 
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
