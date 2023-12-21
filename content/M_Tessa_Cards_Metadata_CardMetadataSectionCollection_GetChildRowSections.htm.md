# CardMetadataSectionCollection.GetChildRowSections(Guid) - метод
Возвращает дочерние коллекционные или древовидные секции для секции с заданным
идентификатором.
## __Definition
 **Пространство имён:** [Tessa.Cards.Metadata](N_Tessa_Cards_Metadata.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public ReadOnlyCollection<CardMetadataSection> GetChildRowSections(
    	Guid sectionID
    )
VB __Копировать
     Public Function GetChildRowSections ( 
    	sectionID As Guid
    ) As ReadOnlyCollection(Of CardMetadataSection)
C++ __Копировать
     public:
    ReadOnlyCollection<CardMetadataSection^>^ GetChildRowSections(
    	Guid sectionID
    )
F# __Копировать
     member GetChildRowSections : 
            sectionID : Guid -> ReadOnlyCollection<CardMetadataSection> 
#### Параметры
sectionID [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
    Идентификатор секции, для которой требуется вернуть дочерние секции.
#### Возвращаемое значение
[ReadOnlyCollection](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.readonlycollection-1)<[CardMetadataSection](T_Tessa_Cards_Metadata_CardMetadataSection.htm)>  
Список коллекционных или древовидных секций, которые являются дочерними для
заданной секции.
##  __Заметки
Метод эффективно работает только в случае, если объект защищён от изменений
вызовом метода [Seal()](M_Tessa_Cards_CardSerializableObject_Seal.htm).
## __См. также
#### Ссылки
[CardMetadataSectionCollection -
](T_Tessa_Cards_Metadata_CardMetadataSectionCollection.htm)
[GetChildRowSections -
перегрузка](Overload_Tessa_Cards_Metadata_CardMetadataSectionCollection_GetChildRowSections.htm)
[Tessa.Cards.Metadata - пространство имён](N_Tessa_Cards_Metadata.htm)
