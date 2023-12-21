# ICardStoreExtensionContext.OnContentStoring - событие
Событие, вызываемое перед сохранением содержимого каждого сохраняемого файла.
Событие вызывается только в том случае, если выполняется сохранение хотя бы
одного файла, при этом признак
[ICardStoreExtensionContext.ContentStorePending] равен true.
## __Definition
 **Пространство имён:** [Tessa.Cards.Extensions](N_Tessa_Cards_Extensions.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     event EventHandler<CardOnContentStoringEventArgs> OnContentStoring
VB __Копировать
     Event OnContentStoring As EventHandler(Of CardOnContentStoringEventArgs)
C++ __Копировать
     event EventHandler<CardOnContentStoringEventArgs^>^ OnContentStoring {
    	void add (EventHandler<CardOnContentStoringEventArgs^>^ value);
    	void remove (EventHandler<CardOnContentStoringEventArgs^>^ value);
    }
F# __Копировать
     abstract OnContentStoring : IEvent<EventHandler<CardOnContentStoringEventArgs>,
        CardOnContentStoringEventArgs>
#### Значение
[EventHandler](https://learn.microsoft.com/dotnet/api/system.eventhandler-1)<[CardOnContentStoringEventArgs](T_Tessa_Cards_CardOnContentStoringEventArgs.htm)>
##  __См. также
#### Ссылки
[ICardStoreExtensionContext -
](T_Tessa_Cards_Extensions_ICardStoreExtensionContext.htm)
[Tessa.Cards.Extensions - пространство имён](N_Tessa_Cards_Extensions.htm)
