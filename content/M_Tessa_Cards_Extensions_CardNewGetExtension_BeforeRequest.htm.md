# CardNewGetExtension.BeforeRequest(ICardGetExtensionContext) - метод
Действие, выполняемое перед получением карточки стандартными средствами. Может
установить ответ на запрос для того, чтобы получение карточки стандартными
средствами не выполнялось.
## __Definition
 **Пространство имён:** [Tessa.Cards.Extensions](N_Tessa_Cards_Extensions.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public virtual Task BeforeRequest(
    	ICardGetExtensionContext context
    )
VB __Копировать
     Public Overridable Function BeforeRequest ( 
    	context As ICardGetExtensionContext
    ) As Task
C++ __Копировать
     public:
    virtual Task^ BeforeRequest(
    	ICardGetExtensionContext^ context
    )
F# __Копировать
     abstract BeforeRequest : 
            context : ICardGetExtensionContext -> Task 
    override BeforeRequest : 
            context : ICardGetExtensionContext -> Task 
#### Параметры
context
[ICardGetExtensionContext](T_Tessa_Cards_Extensions_ICardGetExtensionContext.htm)
    Контекст процесса получения карточки.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)  
Асинхронная задача.
#### Реализации
[ICardGetExtension.BeforeRequest(ICardGetExtensionContext)](M_Tessa_Cards_Extensions_ICardGetExtension_BeforeRequest.htm)  
##  __Заметки
По умолчанию метод не выполняет действий.
##  __См. также
#### Ссылки
[CardNewGetExtension - ](T_Tessa_Cards_Extensions_CardNewGetExtension.htm)
[BeforeRequest -
перегрузка](Overload_Tessa_Cards_Extensions_CardNewGetExtension_BeforeRequest.htm)
[Tessa.Cards.Extensions - пространство имён](N_Tessa_Cards_Extensions.htm)
