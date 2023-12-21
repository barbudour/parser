# ICardMetadataExtensionContext.DelayedSchemeCheckCardTypeIDSet - свойство
Идентификаторы типов карточек, проверка схемы для которых выполняется после
выполнения всех расширений на метаинформацию.
Рекомендуется добавить идентификатор типа карточки в методе расширения
[ModifyTypes(ICardMetadataExtensionContext)](M_Tessa_Cards_Extensions_ICardMetadataExtension_ModifyTypes.htm),
чтобы позже в методе расширения
[ModifyMetadata(ICardMetadataExtensionContext)](M_Tessa_Cards_Extensions_ICardMetadataExtension_ModifyMetadata.htm)
добавить секции и колонки, отсутствующие в схеме данных.
Если по завершении этого метода в типе карточки cardType.SchemeItems
присутствуют ссылки на секции или колонки, отсутствующие в секциях
cardMetadata.GetSectionsAsync(), то тип считается повреждённым, и добавляется
такое же сообщение об ошибке, как если бы проверка типа не была отложена.
## __Definition
 **Пространство имён:** [Tessa.Cards.Extensions](N_Tessa_Cards_Extensions.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
    ISet<Guid> DelayedSchemeCheckCardTypeIDSet { get; }
VB __Копировать
     ReadOnly Property DelayedSchemeCheckCardTypeIDSet As ISet(Of Guid)
    	Get
C++ __Копировать
    property ISet<Guid>^ DelayedSchemeCheckCardTypeIDSet {
    	ISet<Guid>^ get ();
    }
F# __Копировать
     abstract DelayedSchemeCheckCardTypeIDSet : ISet<Guid> with get
#### Значение свойства
[ISet](https://learn.microsoft.com/dotnet/api/system.collections.generic.iset-1)<[Guid](https://learn.microsoft.com/dotnet/api/system.guid)>
##  __См. также
#### Ссылки
[ICardMetadataExtensionContext -
](T_Tessa_Cards_Extensions_ICardMetadataExtensionContext.htm)
[Tessa.Cards.Extensions - пространство имён](N_Tessa_Cards_Extensions.htm)
