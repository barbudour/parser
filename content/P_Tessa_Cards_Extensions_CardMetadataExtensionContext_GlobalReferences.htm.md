# CardMetadataExtensionContext.GlobalReferences - свойство
Словарь, содержащий глобальные объекты
([CardTypeForm](T_Tessa_Cards_CardTypeForm.htm),
[CardTypeBlock](T_Tessa_Cards_CardTypeBlock.htm),
[CardTypeControl](T_Tessa_Cards_CardTypeControl.htm),
[CardTypeValidator](T_Tessa_Cards_CardTypeValidator.htm),
[CardTypeExtension](T_Tessa_Cards_CardTypeExtension.htm)), совместно
использующиеся в типах карточек.
## __Definition
 **Пространство имён:** [Tessa.Cards.Extensions](N_Tessa_Cards_Extensions.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public ISet<CardSerializableObject> GlobalReferences { get; }
VB __Копировать
     Public ReadOnly Property GlobalReferences As ISet(Of CardSerializableObject)
    	Get
C++ __Копировать
     public:
    virtual property ISet<CardSerializableObject^>^ GlobalReferences {
    	ISet<CardSerializableObject^>^ get () sealed;
    }
F# __Копировать
     abstract GlobalReferences : ISet<CardSerializableObject> with get
    override GlobalReferences : ISet<CardSerializableObject> with get
#### Значение свойства
[ISet](https://learn.microsoft.com/dotnet/api/system.collections.generic.iset-1)<[CardSerializableObject](T_Tessa_Cards_CardSerializableObject.htm)>
#### Реализации
[ICardMetadataExtensionContext.GlobalReferences](P_Tessa_Cards_Extensions_ICardMetadataExtensionContext_GlobalReferences.htm)  
##  __См. также
#### Ссылки
[CardMetadataExtensionContext -
](T_Tessa_Cards_Extensions_CardMetadataExtensionContext.htm)
[Tessa.Cards.Extensions - пространство имён](N_Tessa_Cards_Extensions.htm)
