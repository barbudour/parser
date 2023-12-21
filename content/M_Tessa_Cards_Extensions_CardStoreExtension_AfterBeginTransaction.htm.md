# CardStoreExtension.AfterBeginTransaction - метод
Действие, выполняемое после начала транзакции.
##  __Definition
 **Пространство имён:** [Tessa.Cards.Extensions](N_Tessa_Cards_Extensions.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public virtual Task AfterBeginTransaction(
    	ICardStoreExtensionContext context
    )
VB __Копировать
     Public Overridable Function AfterBeginTransaction ( 
    	context As ICardStoreExtensionContext
    ) As Task
C++ __Копировать
     public:
    virtual Task^ AfterBeginTransaction(
    	ICardStoreExtensionContext^ context
    )
F# __Копировать
     abstract AfterBeginTransaction : 
            context : ICardStoreExtensionContext -> Task 
    override AfterBeginTransaction : 
            context : ICardStoreExtensionContext -> Task 
#### Параметры
context
[ICardStoreExtensionContext](T_Tessa_Cards_Extensions_ICardStoreExtensionContext.htm)
    Контекст процесса сохранения карточки.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)  
Асинхронная задача.
#### Реализации
[ICardStoreExtension.AfterBeginTransaction(ICardStoreExtensionContext)](M_Tessa_Cards_Extensions_ICardStoreExtension_AfterBeginTransaction.htm)  
##  __Заметки
По умолчанию метод не выполняет действий.
##  __См. также
#### Ссылки
[CardStoreExtension - ](T_Tessa_Cards_Extensions_CardStoreExtension.htm)
[Tessa.Cards.Extensions - пространство имён](N_Tessa_Cards_Extensions.htm)
