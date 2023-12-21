# CardDeleteExtension.BeforeRequest - метод
Действие, выполняемое перед удалением карточки стандартными средствами. Может
установить ответ на запрос для того, чтобы удаление карточки стандартными
средствами не выполнялось.
## __Definition
 **Пространство имён:** [Tessa.Cards.Extensions](N_Tessa_Cards_Extensions.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public virtual Task BeforeRequest(
    	ICardDeleteExtensionContext context
    )
VB __Копировать
     Public Overridable Function BeforeRequest ( 
    	context As ICardDeleteExtensionContext
    ) As Task
C++ __Копировать
     public:
    virtual Task^ BeforeRequest(
    	ICardDeleteExtensionContext^ context
    )
F# __Копировать
     abstract BeforeRequest : 
            context : ICardDeleteExtensionContext -> Task 
    override BeforeRequest : 
            context : ICardDeleteExtensionContext -> Task 
#### Параметры
context
[ICardDeleteExtensionContext](T_Tessa_Cards_Extensions_ICardDeleteExtensionContext.htm)
    Контекст процесса удаления карточки.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)  
Асинхронная задача.
#### Реализации
[ICardDeleteExtension.BeforeRequest(ICardDeleteExtensionContext)](M_Tessa_Cards_Extensions_ICardDeleteExtension_BeforeRequest.htm)  
##  __Заметки
По умолчанию метод не выполняет действий.
##  __См. также
#### Ссылки
[CardDeleteExtension - ](T_Tessa_Cards_Extensions_CardDeleteExtension.htm)
[Tessa.Cards.Extensions - пространство имён](N_Tessa_Cards_Extensions.htm)
