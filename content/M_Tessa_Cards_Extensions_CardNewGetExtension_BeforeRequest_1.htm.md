# CardNewGetExtension.BeforeRequest(ICardNewExtensionContext) - метод
Действие, выполняемое перед созданием структуры карточки стандартными
средствами. Может установить ответ на запрос для того, чтобы создание
структуры карточки стандартными средствами не выполнялось.
## __Definition
 **Пространство имён:** [Tessa.Cards.Extensions](N_Tessa_Cards_Extensions.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public virtual Task BeforeRequest(
    	ICardNewExtensionContext context
    )
VB __Копировать
     Public Overridable Function BeforeRequest ( 
    	context As ICardNewExtensionContext
    ) As Task
C++ __Копировать
     public:
    virtual Task^ BeforeRequest(
    	ICardNewExtensionContext^ context
    )
F# __Копировать
     abstract BeforeRequest : 
            context : ICardNewExtensionContext -> Task 
    override BeforeRequest : 
            context : ICardNewExtensionContext -> Task 
#### Параметры
context
[ICardNewExtensionContext](T_Tessa_Cards_Extensions_ICardNewExtensionContext.htm)
    Контекст процесса создания структуры карточки.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)  
Асинхронная задача.
#### Реализации
[ICardNewExtension.BeforeRequest(ICardNewExtensionContext)](M_Tessa_Cards_Extensions_ICardNewExtension_BeforeRequest.htm)  
##  __Заметки
По умолчанию метод не выполняет действий.
##  __См. также
#### Ссылки
[CardNewGetExtension - ](T_Tessa_Cards_Extensions_CardNewGetExtension.htm)
[BeforeRequest -
перегрузка](Overload_Tessa_Cards_Extensions_CardNewGetExtension_BeforeRequest.htm)
[Tessa.Cards.Extensions - пространство имён](N_Tessa_Cards_Extensions.htm)
