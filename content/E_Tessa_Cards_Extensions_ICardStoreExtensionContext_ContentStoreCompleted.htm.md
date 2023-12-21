# ICardStoreExtensionContext.ContentStoreCompleted - событие
Событие, вызываемое при завершении сохранения содержимого файлов. Событие
вызывается только в том случае, если выполняется сохранение хотя бы одного
файла, при этом признак [ICardStoreExtensionContext.ContentStorePending] равен
true.
## __Definition
 **Пространство имён:** [Tessa.Cards.Extensions](N_Tessa_Cards_Extensions.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     event EventHandler<CardContentStoreCompletedEventArgs> ContentStoreCompleted
VB __Копировать
     Event ContentStoreCompleted As EventHandler(Of CardContentStoreCompletedEventArgs)
C++ __Копировать
     event EventHandler<CardContentStoreCompletedEventArgs^>^ ContentStoreCompleted {
    	void add (EventHandler<CardContentStoreCompletedEventArgs^>^ value);
    	void remove (EventHandler<CardContentStoreCompletedEventArgs^>^ value);
    }
F# __Копировать
     abstract ContentStoreCompleted : IEvent<EventHandler<CardContentStoreCompletedEventArgs>,
        CardContentStoreCompletedEventArgs>
#### Значение
[EventHandler](https://learn.microsoft.com/dotnet/api/system.eventhandler-1)<[CardContentStoreCompletedEventArgs](T_Tessa_Cards_CardContentStoreCompletedEventArgs.htm)>
##  __См. также
#### Ссылки
[ICardStoreExtensionContext -
](T_Tessa_Cards_Extensions_ICardStoreExtensionContext.htm)
[Tessa.Cards.Extensions - пространство имён](N_Tessa_Cards_Extensions.htm)
