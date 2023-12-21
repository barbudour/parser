# CardNewGetExtension.AfterRequestFinally(ICardGetExtensionContext) - метод
Действие, выполняемое при возникновении исключения или после получения
карточки как при успешном, так и при неудачном результате. Необработанные
исключения не прерывают выполнение цепочки расширений.
## __Definition
 **Пространство имён:** [Tessa.Cards.Extensions](N_Tessa_Cards_Extensions.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public virtual Task AfterRequestFinally(
    	ICardGetExtensionContext context
    )
VB __Копировать
     Public Overridable Function AfterRequestFinally ( 
    	context As ICardGetExtensionContext
    ) As Task
C++ __Копировать
     public:
    virtual Task^ AfterRequestFinally(
    	ICardGetExtensionContext^ context
    )
F# __Копировать
     abstract AfterRequestFinally : 
            context : ICardGetExtensionContext -> Task 
    override AfterRequestFinally : 
            context : ICardGetExtensionContext -> Task 
#### Параметры
context
[ICardGetExtensionContext](T_Tessa_Cards_Extensions_ICardGetExtensionContext.htm)
    Контекст процесса получения карточки.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)  
Асинхронная задача.
#### Реализации
[ICardGetExtension.AfterRequestFinally(ICardGetExtensionContext)](M_Tessa_Cards_Extensions_ICardGetExtension_AfterRequestFinally.htm)  
##  __Заметки
По умолчанию метод не выполняет действий.
##  __См. также
#### Ссылки
[CardNewGetExtension - ](T_Tessa_Cards_Extensions_CardNewGetExtension.htm)
[AfterRequestFinally -
перегрузка](Overload_Tessa_Cards_Extensions_CardNewGetExtension_AfterRequestFinally.htm)
[Tessa.Cards.Extensions - пространство имён](N_Tessa_Cards_Extensions.htm)
