# CardRepairExtension.AfterRequestFinally - метод
Действие, выполняемое при возникновении исключения или после исправления
структуры карточки как при успешном, так и при неудачном результате.
Необработанные исключения не прерывают выполнение цепочки расширений.
## __Definition
 **Пространство имён:** [Tessa.Cards.Extensions](N_Tessa_Cards_Extensions.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public virtual Task AfterRequestFinally(
    	ICardRepairExtensionContext context
    )
VB __Копировать
     Public Overridable Function AfterRequestFinally ( 
    	context As ICardRepairExtensionContext
    ) As Task
C++ __Копировать
     public:
    virtual Task^ AfterRequestFinally(
    	ICardRepairExtensionContext^ context
    )
F# __Копировать
     abstract AfterRequestFinally : 
            context : ICardRepairExtensionContext -> Task 
    override AfterRequestFinally : 
            context : ICardRepairExtensionContext -> Task 
#### Параметры
context
[ICardRepairExtensionContext](T_Tessa_Cards_Extensions_ICardRepairExtensionContext.htm)
    Контекст процесса исправления структуры карточки.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)  
Асинхронная задача.
#### Реализации
[ICardRepairExtension.AfterRequestFinally(ICardRepairExtensionContext)](M_Tessa_Cards_Extensions_ICardRepairExtension_AfterRequestFinally.htm)  
##  __Заметки
По умолчанию метод не выполняет действий.
##  __См. также
#### Ссылки
[CardRepairExtension - ](T_Tessa_Cards_Extensions_CardRepairExtension.htm)
[Tessa.Cards.Extensions - пространство имён](N_Tessa_Cards_Extensions.htm)
