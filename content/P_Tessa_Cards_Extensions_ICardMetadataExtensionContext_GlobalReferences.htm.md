# ICardMetadataExtensionContext.GlobalReferences - свойство
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
    ISet<CardSerializableObject> GlobalReferences { get; }
VB __Копировать
     ReadOnly Property GlobalReferences As ISet(Of CardSerializableObject)
    	Get
C++ __Копировать
    property ISet<CardSerializableObject^>^ GlobalReferences {
    	ISet<CardSerializableObject^>^ get ();
    }
F# __Копировать
     abstract GlobalReferences : ISet<CardSerializableObject> with get
#### Значение свойства
[ISet](https://learn.microsoft.com/dotnet/api/system.collections.generic.iset-1)<[CardSerializableObject](T_Tessa_Cards_CardSerializableObject.htm)>
##  __См. также
#### Ссылки
[ICardMetadataExtensionContext -
](T_Tessa_Cards_Extensions_ICardMetadataExtensionContext.htm)
[Tessa.Cards.Extensions - пространство имён](N_Tessa_Cards_Extensions.htm)
