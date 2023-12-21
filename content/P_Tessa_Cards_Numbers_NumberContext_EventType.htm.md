# NumberContext.EventType - свойство
Тип события, происходящего с номером. Если событие не было установлено, то
возвращается [Tessa.Cards.Numbers.NumberEventTypes.Unknown]. Установить
значение можно единственный раз, причём нельзя установить null или
[Tessa.Cards.Numbers.NumberEventTypes.Unknown].
## __Definition
 **Пространство имён:** [Tessa.Cards.Numbers](N_Tessa_Cards_Numbers.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public NumberEventType EventType { get; set; }
VB __Копировать
     Public Property EventType As NumberEventType
    	Get
    	Set
C++ __Копировать
     public:
    virtual property NumberEventType^ EventType {
    	NumberEventType^ get () sealed;
    	void set (NumberEventType^ value) sealed;
    }
F# __Копировать
     abstract EventType : NumberEventType with get, set
    override EventType : NumberEventType with get, set
#### Значение свойства
[NumberEventType](T_Tessa_Cards_Numbers_NumberEventType.htm)
#### Реализации
[INumberContext.EventType](P_Tessa_Cards_Numbers_INumberContext_EventType.htm)  
##  __Заметки
Значение свойства никогда не равно null.
## __См. также
#### Ссылки
[NumberContext - ](T_Tessa_Cards_Numbers_NumberContext.htm)
[Tessa.Cards.Numbers - пространство имён](N_Tessa_Cards_Numbers.htm)
