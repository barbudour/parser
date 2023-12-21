# CardStoreStreamingContext.ExtensionContext - свойство
Контекст расширений, выполняемых при сохранении карточки, или null, если
расширения не выполнялись или если контекст ещё не задан.
## __Definition
 **Пространство имён:**
[Tessa.Cards.ComponentModel](N_Tessa_Cards_ComponentModel.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public ICardStoreExtensionContext ExtensionContext { get; set; }
VB __Копировать
     Public Property ExtensionContext As ICardStoreExtensionContext
    	Get
    	Set
C++ __Копировать
     public:
    virtual property ICardStoreExtensionContext^ ExtensionContext {
    	ICardStoreExtensionContext^ get () sealed;
    	void set (ICardStoreExtensionContext^ value) sealed;
    }
F# __Копировать
     abstract ExtensionContext : ICardStoreExtensionContext with get, set
    override ExtensionContext : ICardStoreExtensionContext with get, set
#### Значение свойства
[ICardStoreExtensionContext](T_Tessa_Cards_Extensions_ICardStoreExtensionContext.htm)
#### Реализации
[ICardStoreStreamingContext.ExtensionContext](P_Tessa_Cards_ComponentModel_ICardStoreStreamingContext_ExtensionContext.htm)  
##  __См. также
#### Ссылки
[CardStoreStreamingContext -
](T_Tessa_Cards_ComponentModel_CardStoreStreamingContext.htm)
[Tessa.Cards.ComponentModel - пространство
имён](N_Tessa_Cards_ComponentModel.htm)
