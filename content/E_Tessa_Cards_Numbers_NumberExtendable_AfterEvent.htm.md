# NumberExtendable.AfterEvent - событие
Событие, выполняемое в процессе постобработки события, происходящего с
номером. Это предоставляет возможность изменить результат обработанного
события или сохранить результат во внешнем хранилище.
## __Definition
 **Пространство имён:** [Tessa.Cards.Numbers](N_Tessa_Cards_Numbers.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public event EventHandler<NumberContextEventArgs> AfterEvent
VB __Копировать
     Public Event AfterEvent As EventHandler(Of NumberContextEventArgs)
C++ __Копировать
     public:
    virtual  event EventHandler<NumberContextEventArgs^>^ AfterEvent {
    	void add (EventHandler<NumberContextEventArgs^>^ value);
    	void remove (EventHandler<NumberContextEventArgs^>^ value);
    }
F# __Копировать
     abstract AfterEvent : IEvent<EventHandler<NumberContextEventArgs>,
        NumberContextEventArgs>
    override AfterEvent : IEvent<EventHandler<NumberContextEventArgs>,
        NumberContextEventArgs>
#### Значение
[EventHandler](https://learn.microsoft.com/dotnet/api/system.eventhandler-1)<[NumberContextEventArgs](T_Tessa_Cards_Numbers_NumberContextEventArgs.htm)>
#### Реализации
[INumberExtendable.AfterEvent](E_Tessa_Cards_Numbers_INumberExtendable_AfterEvent.htm)  
##  __См. также
#### Ссылки
[NumberExtendable - ](T_Tessa_Cards_Numbers_NumberExtendable.htm)
[Tessa.Cards.Numbers - пространство имён](N_Tessa_Cards_Numbers.htm)
