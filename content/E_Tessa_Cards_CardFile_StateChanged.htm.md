# CardFile.StateChanged - событие
Событие, возникающее при изменении состояния файла
[State](P_Tessa_Cards_CardFile_State.htm).
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public event EventHandler<CardFileStateEventArgs> StateChanged
VB __Копировать
     Public Event StateChanged As EventHandler(Of CardFileStateEventArgs)
C++ __Копировать
     public:
     event EventHandler<CardFileStateEventArgs^>^ StateChanged {
    	void add (EventHandler<CardFileStateEventArgs^>^ value);
    	void remove (EventHandler<CardFileStateEventArgs^>^ value);
    }
F# __Копировать
     member StateChanged : IEvent<EventHandler<CardFileStateEventArgs>,
        CardFileStateEventArgs>
#### Значение
[EventHandler](https://learn.microsoft.com/dotnet/api/system.eventhandler-1)<[CardFileStateEventArgs](T_Tessa_Cards_CardFileStateEventArgs.htm)>
##  __См. также
#### Ссылки
[CardFile - ](T_Tessa_Cards_CardFile.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
