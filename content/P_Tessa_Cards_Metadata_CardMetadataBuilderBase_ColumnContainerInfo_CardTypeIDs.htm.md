# CardMetadataBuilderBase.ColumnContainerInfo.CardTypeIDs - свойство
Массив идентификаторов типов карточек, в которых используется текущая колонка.
Только
[CardTypeCount](P_Tessa_Cards_Metadata_CardMetadataBuilderBase_ColumnContainerInfo_CardTypeCount.htm)
первых элементов массива заполнены действительными значениями. Для добавления
идентификаторов в массив следует использовать метод
[AddCardTypeID(Guid)](M_Tessa_Cards_Metadata_CardMetadataBuilderBase_ColumnContainerInfo_AddCardTypeID.htm).
## __Definition
 **Пространство имён:** [Tessa.Cards.Metadata](N_Tessa_Cards_Metadata.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public Guid[] CardTypeIDs { get; set; }
VB __Копировать
     Public Property CardTypeIDs As Guid()
    	Get
    	Set
C++ __Копировать
     public:
    property array<Guid>^ CardTypeIDs {
    	array<Guid>^ get ();
    	void set (array<Guid>^ value);
    }
F# __Копировать
     member CardTypeIDs : Guid[] with get, set
#### Значение свойства
[Guid](https://learn.microsoft.com/dotnet/api/system.guid)[]
##  __См. также
#### Ссылки
[CardMetadataBuilderBase.ColumnContainerInfo -
](T_Tessa_Cards_Metadata_CardMetadataBuilderBase_ColumnContainerInfo.htm)
[Tessa.Cards.Metadata - пространство имён](N_Tessa_Cards_Metadata.htm)
