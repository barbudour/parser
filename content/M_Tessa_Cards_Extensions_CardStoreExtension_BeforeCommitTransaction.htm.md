# CardStoreExtension.BeforeCommitTransaction - метод
Действие, выполняемое перед коммитом транзакции.
##  __Definition
 **Пространство имён:** [Tessa.Cards.Extensions](N_Tessa_Cards_Extensions.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public virtual Task BeforeCommitTransaction(
    	ICardStoreExtensionContext context
    )
VB __Копировать
     Public Overridable Function BeforeCommitTransaction ( 
    	context As ICardStoreExtensionContext
    ) As Task
C++ __Копировать
     public:
    virtual Task^ BeforeCommitTransaction(
    	ICardStoreExtensionContext^ context
    )
F# __Копировать
     abstract BeforeCommitTransaction : 
            context : ICardStoreExtensionContext -> Task 
    override BeforeCommitTransaction : 
            context : ICardStoreExtensionContext -> Task 
#### Параметры
context
[ICardStoreExtensionContext](T_Tessa_Cards_Extensions_ICardStoreExtensionContext.htm)
    Контекст процесса сохранения карточки.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)  
Асинхронная задача.
#### Реализации
[ICardStoreExtension.BeforeCommitTransaction(ICardStoreExtensionContext)](M_Tessa_Cards_Extensions_ICardStoreExtension_BeforeCommitTransaction.htm)  
##  __Заметки
По умолчанию метод не выполняет действий.
##  __См. также
#### Ссылки
[CardStoreExtension - ](T_Tessa_Cards_Extensions_CardStoreExtension.htm)
[Tessa.Cards.Extensions - пространство имён](N_Tessa_Cards_Extensions.htm)
