# CardStoreExtensionContext.ContentStoreCompleted - событие
Событие, вызываемое при завершении сохранения содержимого файлов. Событие
вызывается только в том случае, если выполняется сохранение хотя бы одного
файла, при этом признак [ICardStoreExtensionContext.ContentStorePending] равен
true.
## __Definition
 **Пространство имён:** [Tessa.Cards.Extensions](N_Tessa_Cards_Extensions.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public event EventHandler<CardContentStoreCompletedEventArgs> ContentStoreCompleted
VB __Копировать
     Public Event ContentStoreCompleted As EventHandler(Of CardContentStoreCompletedEventArgs)
C++ __Копировать
     public:
    virtual  event EventHandler<CardContentStoreCompletedEventArgs^>^ ContentStoreCompleted {
    	void add (EventHandler<CardContentStoreCompletedEventArgs^>^ value);
    	void remove (EventHandler<CardContentStoreCompletedEventArgs^>^ value);
    }
F# __Копировать
     abstract ContentStoreCompleted : IEvent<EventHandler<CardContentStoreCompletedEventArgs>,
        CardContentStoreCompletedEventArgs>
    override ContentStoreCompleted : IEvent<EventHandler<CardContentStoreCompletedEventArgs>,
        CardContentStoreCompletedEventArgs>
#### Значение
[EventHandler](https://learn.microsoft.com/dotnet/api/system.eventhandler-1)<[CardContentStoreCompletedEventArgs](T_Tessa_Cards_CardContentStoreCompletedEventArgs.htm)>
#### Реализации
[ICardStoreExtensionContext.ContentStoreCompleted](E_Tessa_Cards_Extensions_ICardStoreExtensionContext_ContentStoreCompleted.htm)  
##  __См. также
#### Ссылки
[CardStoreExtensionContext -
](T_Tessa_Cards_Extensions_CardStoreExtensionContext.htm)
[Tessa.Cards.Extensions - пространство имён](N_Tessa_Cards_Extensions.htm)
