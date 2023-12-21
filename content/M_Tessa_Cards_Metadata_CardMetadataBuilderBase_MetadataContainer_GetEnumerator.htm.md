# CardMetadataBuilderBase.MetadataContainer.GetEnumerator - метод
Returns an enumerator that iterates through a collection.
##  __Definition
 **Пространство имён:** [Tessa.Cards.Metadata](N_Tessa_Cards_Metadata.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public IEnumerator<KeyValuePair<Guid, CardMetadataBuilderBase.SectionContainerInfo>> GetEnumerator()
VB __Копировать
     Public Function GetEnumerator As IEnumerator(Of KeyValuePair(Of Guid, CardMetadataBuilderBase.SectionContainerInfo))
C++ __Копировать
     public:
    virtual IEnumerator<KeyValuePair<Guid, CardMetadataBuilderBase.SectionContainerInfo^>>^ GetEnumerator() sealed
F# __Копировать
     abstract GetEnumerator : unit -> IEnumerator<KeyValuePair<Guid, CardMetadataBuilderBase.SectionContainerInfo>> 
    override GetEnumerator : unit -> IEnumerator<KeyValuePair<Guid, CardMetadataBuilderBase.SectionContainerInfo>> 
#### Возвращаемое значение
[IEnumerator](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerator-1)<[KeyValuePair](https://learn.microsoft.com/dotnet/api/system.collections.generic.keyvaluepair-2)<[Guid](https://learn.microsoft.com/dotnet/api/system.guid),
[CardMetadataBuilderBase.SectionContainerInfo](T_Tessa_Cards_Metadata_CardMetadataBuilderBase_SectionContainerInfo.htm)>>  
An
[IEnumerator](https://learn.microsoft.com/dotnet/api/system.collections.ienumerator)
object that can be used to iterate through the collection.
#### Реализации
[IEnumerable<T>.GetEnumerator()](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1.getenumerator#system-
collections-generic-ienumerable-1-getenumerator)  
##  __См. также
#### Ссылки
[CardMetadataBuilderBase.MetadataContainer -
](T_Tessa_Cards_Metadata_CardMetadataBuilderBase_MetadataContainer.htm)
[Tessa.Cards.Metadata - пространство имён](N_Tessa_Cards_Metadata.htm)
