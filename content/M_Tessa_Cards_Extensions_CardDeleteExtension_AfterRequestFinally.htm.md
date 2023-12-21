# CardDeleteExtension.AfterRequestFinally - метод
Действие, выполняемое при возникновении исключения или после удаления карточки
как при успешном, так и при неудачном результате. Необработанные исключения не
прерывают выполнение цепочки расширений.
## __Definition
 **Пространство имён:** [Tessa.Cards.Extensions](N_Tessa_Cards_Extensions.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public virtual Task AfterRequestFinally(
    	ICardDeleteExtensionContext context
    )
VB __Копировать
     Public Overridable Function AfterRequestFinally ( 
    	context As ICardDeleteExtensionContext
    ) As Task
C++ __Копировать
     public:
    virtual Task^ AfterRequestFinally(
    	ICardDeleteExtensionContext^ context
    )
F# __Копировать
     abstract AfterRequestFinally : 
            context : ICardDeleteExtensionContext -> Task 
    override AfterRequestFinally : 
            context : ICardDeleteExtensionContext -> Task 
#### Параметры
context
[ICardDeleteExtensionContext](T_Tessa_Cards_Extensions_ICardDeleteExtensionContext.htm)
    Контекст процесса удаления карточки.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)  
Асинхронная задача.
#### Реализации
[ICardDeleteExtension.AfterRequestFinally(ICardDeleteExtensionContext)](M_Tessa_Cards_Extensions_ICardDeleteExtension_AfterRequestFinally.htm)  
##  __Заметки
По умолчанию метод не выполняет действий.
##  __См. также
#### Ссылки
[CardDeleteExtension - ](T_Tessa_Cards_Extensions_CardDeleteExtension.htm)
[Tessa.Cards.Extensions - пространство имён](N_Tessa_Cards_Extensions.htm)
