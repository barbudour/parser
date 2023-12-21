# CardTask.StateChanged - событие
Событие, возникающее при изменении состояния задания
[State](P_Tessa_Cards_CardTask_State.htm).
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public event EventHandler<CardRowStateEventArgs> StateChanged
VB __Копировать
     Public Event StateChanged As EventHandler(Of CardRowStateEventArgs)
C++ __Копировать
     public:
     event EventHandler<CardRowStateEventArgs^>^ StateChanged {
    	void add (EventHandler<CardRowStateEventArgs^>^ value);
    	void remove (EventHandler<CardRowStateEventArgs^>^ value);
    }
F# __Копировать
     member StateChanged : IEvent<EventHandler<CardRowStateEventArgs>,
        CardRowStateEventArgs>
#### Значение
[EventHandler](https://learn.microsoft.com/dotnet/api/system.eventhandler-1)<[CardRowStateEventArgs](T_Tessa_Cards_CardRowStateEventArgs.htm)>
##  __См. также
#### Ссылки
[CardTask - ](T_Tessa_Cards_CardTask.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
