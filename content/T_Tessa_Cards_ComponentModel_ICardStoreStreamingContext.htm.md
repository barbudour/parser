# ICardStoreStreamingContext - интерфейс
Контекст, передаваемый от запроса на потоковое сохранение карточки с файлами
до запроса на обычное сохранение карточки.
## __Definition
 **Пространство имён:**
[Tessa.Cards.ComponentModel](N_Tessa_Cards_ComponentModel.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface ICardStoreStreamingContext
VB __Копировать
     Public Interface ICardStoreStreamingContext
C++ __Копировать
     public interface class ICardStoreStreamingContext
F# __Копировать
     type ICardStoreStreamingContext = interface end
##  __Свойства
[ExtensionContext](P_Tessa_Cards_ComponentModel_ICardStoreStreamingContext_ExtensionContext.htm)|
Контекст расширений, выполняемых при сохранении карточки, или null, если
расширения не выполнялись или если контекст ещё не задан.  
---|---  
[Info](P_Tessa_Cards_ComponentModel_ICardStoreStreamingContext_Info.htm)|
Дополнительная информация, передаваемая между потоковым сохранением карточки с
файлами и сохранением собственно карточки. Не используется в реализации по
умолчанию.  
## __См. также
#### Ссылки
[Tessa.Cards.ComponentModel - пространство
имён](N_Tessa_Cards_ComponentModel.htm)
