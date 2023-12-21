# INumberExtendable.AfterEvent - событие
Событие, выполняемое в процессе постобработки события, происходящего с
номером. Это предоставляет возможность изменить результат обработанного
события или сохранить результат во внешнем хранилище.
## __Definition
 **Пространство имён:** [Tessa.Cards.Numbers](N_Tessa_Cards_Numbers.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     event EventHandler<NumberContextEventArgs> AfterEvent
VB __Копировать
     Event AfterEvent As EventHandler(Of NumberContextEventArgs)
C++ __Копировать
     event EventHandler<NumberContextEventArgs^>^ AfterEvent {
    	void add (EventHandler<NumberContextEventArgs^>^ value);
    	void remove (EventHandler<NumberContextEventArgs^>^ value);
    }
F# __Копировать
     abstract AfterEvent : IEvent<EventHandler<NumberContextEventArgs>,
        NumberContextEventArgs>
#### Значение
[EventHandler](https://learn.microsoft.com/dotnet/api/system.eventhandler-1)<[NumberContextEventArgs](T_Tessa_Cards_Numbers_NumberContextEventArgs.htm)>
##  __См. также
#### Ссылки
[INumberExtendable - ](T_Tessa_Cards_Numbers_INumberExtendable.htm)
[Tessa.Cards.Numbers - пространство имён](N_Tessa_Cards_Numbers.htm)
