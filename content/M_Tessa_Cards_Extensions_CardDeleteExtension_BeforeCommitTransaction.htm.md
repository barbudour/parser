# CardDeleteExtension.BeforeCommitTransaction - метод
Действие, выполняемое перед коммитом транзакции.
##  __Definition
 **Пространство имён:** [Tessa.Cards.Extensions](N_Tessa_Cards_Extensions.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public virtual Task BeforeCommitTransaction(
    	ICardDeleteExtensionContext context
    )
VB __Копировать
     Public Overridable Function BeforeCommitTransaction ( 
    	context As ICardDeleteExtensionContext
    ) As Task
C++ __Копировать
     public:
    virtual Task^ BeforeCommitTransaction(
    	ICardDeleteExtensionContext^ context
    )
F# __Копировать
     abstract BeforeCommitTransaction : 
            context : ICardDeleteExtensionContext -> Task 
    override BeforeCommitTransaction : 
            context : ICardDeleteExtensionContext -> Task 
#### Параметры
context
[ICardDeleteExtensionContext](T_Tessa_Cards_Extensions_ICardDeleteExtensionContext.htm)
    Контекст процесса удаления карточки.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)  
Асинхронная задача.
#### Реализации
[ICardDeleteExtension.BeforeCommitTransaction(ICardDeleteExtensionContext)](M_Tessa_Cards_Extensions_ICardDeleteExtension_BeforeCommitTransaction.htm)  
##  __Заметки
По умолчанию метод не выполняет действий.
##  __См. также
#### Ссылки
[CardDeleteExtension - ](T_Tessa_Cards_Extensions_CardDeleteExtension.htm)
[Tessa.Cards.Extensions - пространство имён](N_Tessa_Cards_Extensions.htm)
