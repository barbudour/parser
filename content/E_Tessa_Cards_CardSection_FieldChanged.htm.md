# CardSection.FieldChanged - событие
Значение поля было изменено, причём валидация уже была выполнена.
##  __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public event EventHandler<CardFieldChangedEventArgs> FieldChanged
VB __Копировать
     Public Event FieldChanged As EventHandler(Of CardFieldChangedEventArgs)
C++ __Копировать
     public:
    virtual  event EventHandler<CardFieldChangedEventArgs^>^ FieldChanged {
    	void add (EventHandler<CardFieldChangedEventArgs^>^ value);
    	void remove (EventHandler<CardFieldChangedEventArgs^>^ value);
    }
F# __Копировать
     abstract FieldChanged : IEvent<EventHandler<CardFieldChangedEventArgs>,
        CardFieldChangedEventArgs>
    override FieldChanged : IEvent<EventHandler<CardFieldChangedEventArgs>,
        CardFieldChangedEventArgs>
#### Значение
[EventHandler](https://learn.microsoft.com/dotnet/api/system.eventhandler-1)<[CardFieldChangedEventArgs](T_Tessa_Cards_CardFieldChangedEventArgs.htm)>
#### Реализации
[ICardFieldContainer.FieldChanged](E_Tessa_Cards_ICardFieldContainer_FieldChanged.htm)  
##  __См. также
#### Ссылки
[CardSection - ](T_Tessa_Cards_CardSection.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
