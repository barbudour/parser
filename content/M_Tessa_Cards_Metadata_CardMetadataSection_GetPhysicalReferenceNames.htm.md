# CardMetadataSection.GetPhysicalReferenceNames - метод
Возвращает имена физических колонок, которые являются ссылками на родительские
коллекционные или древовидные секции. Такие колонки указывают на RowID
родительских секций.
## __Definition
 **Пространство имён:** [Tessa.Cards.Metadata](N_Tessa_Cards_Metadata.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public ReadOnlyCollection<string> GetPhysicalReferenceNames()
VB __Копировать
     Public Function GetPhysicalReferenceNames As ReadOnlyCollection(Of String)
C++ __Копировать
     public:
    ReadOnlyCollection<String^>^ GetPhysicalReferenceNames()
F# __Копировать
     member GetPhysicalReferenceNames : unit -> ReadOnlyCollection<string> 
#### Возвращаемое значение
[ReadOnlyCollection](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.readonlycollection-1)<[String](https://learn.microsoft.com/dotnet/api/system.string)>  
Имена физических колонок, которые являются ссылками на родительские
коллекционные или древовидные секции.
## __Заметки
Метод эффективно работает только в случае, если объект защищён от изменений
вызовом метода [Seal()](M_Tessa_Cards_CardSerializableObject_Seal.htm).
## __См. также
#### Ссылки
[CardMetadataSection - ](T_Tessa_Cards_Metadata_CardMetadataSection.htm)
[Tessa.Cards.Metadata - пространство имён](N_Tessa_Cards_Metadata.htm)
