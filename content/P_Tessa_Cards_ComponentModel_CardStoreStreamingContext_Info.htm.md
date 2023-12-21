# CardStoreStreamingContext.Info - свойство
Дополнительная информация, передаваемая между потоковым сохранением карточки с
файлами и сохранением собственно карточки. Не используется в реализации по
умолчанию.
## __Definition
 **Пространство имён:**
[Tessa.Cards.ComponentModel](N_Tessa_Cards_ComponentModel.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public ISerializableObject Info { get; }
VB __Копировать
     Public ReadOnly Property Info As ISerializableObject
    	Get
C++ __Копировать
     public:
    virtual property ISerializableObject^ Info {
    	ISerializableObject^ get () sealed;
    }
F# __Копировать
     abstract Info : ISerializableObject with get
    override Info : ISerializableObject with get
#### Значение свойства
[ISerializableObject](T_Tessa_Platform_Storage_ISerializableObject.htm)
#### Реализации
[ICardStoreStreamingContext.Info](P_Tessa_Cards_ComponentModel_ICardStoreStreamingContext_Info.htm)  
##  __Заметки
Значение свойства никогда не равно null.
## __См. также
#### Ссылки
[CardStoreStreamingContext -
](T_Tessa_Cards_ComponentModel_CardStoreStreamingContext.htm)
[Tessa.Cards.ComponentModel - пространство
имён](N_Tessa_Cards_ComponentModel.htm)
