# CardResponseBase.TryInitFromContext - метод
Инициализирует объект для данных, полученных из заданного контекста действия с
карточкой.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public virtual bool TryInitFromContext(
    	Object context
    )
VB __Копировать
     Public Overridable Function TryInitFromContext ( 
    	context As Object
    ) As Boolean
C++ __Копировать
     public:
    virtual bool TryInitFromContext(
    	Object^ context
    )
F# __Копировать
     abstract TryInitFromContext : 
            context : Object -> bool 
    override TryInitFromContext : 
            context : Object -> bool 
#### Параметры
context [Object](https://learn.microsoft.com/dotnet/api/system.object)
     Контекст действия с карточкой. Если он равен null или его тип не соответствует ожидаемому, метод завершает выполнение без выбрасывания исключений. 
#### Возвращаемое значение
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)  
Признак того, что объект был успешно инициализирован по заданному контексту.
##  __Заметки
По умолчанию метод не выполняет действий.
##  __См. также
#### Ссылки
[CardResponseBase - ](T_Tessa_Cards_CardResponseBase.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
