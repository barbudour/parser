# CardNewExtension.AfterRequestFinally - метод
Действие, выполняемое при возникновении исключения или после создания
структуры карточки как при успешном, так и при неудачном результате.
Необработанные исключения не прерывают выполнение цепочки расширений.
## __Definition
 **Пространство имён:** [Tessa.Cards.Extensions](N_Tessa_Cards_Extensions.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public virtual Task AfterRequestFinally(
    	ICardNewExtensionContext context
    )
VB __Копировать
     Public Overridable Function AfterRequestFinally ( 
    	context As ICardNewExtensionContext
    ) As Task
C++ __Копировать
     public:
    virtual Task^ AfterRequestFinally(
    	ICardNewExtensionContext^ context
    )
F# __Копировать
     abstract AfterRequestFinally : 
            context : ICardNewExtensionContext -> Task 
    override AfterRequestFinally : 
            context : ICardNewExtensionContext -> Task 
#### Параметры
context
[ICardNewExtensionContext](T_Tessa_Cards_Extensions_ICardNewExtensionContext.htm)
    Контекст процесса создания структуры карточки.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)  
Асинхронная задача.
#### Реализации
[ICardNewExtension.AfterRequestFinally(ICardNewExtensionContext)](M_Tessa_Cards_Extensions_ICardNewExtension_AfterRequestFinally.htm)  
##  __Заметки
По умолчанию метод не выполняет действий.
##  __См. также
#### Ссылки
[CardNewExtension - ](T_Tessa_Cards_Extensions_CardNewExtension.htm)
[Tessa.Cards.Extensions - пространство имён](N_Tessa_Cards_Extensions.htm)
