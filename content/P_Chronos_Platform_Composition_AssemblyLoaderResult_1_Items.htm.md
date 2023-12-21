# AssemblyLoaderResult<TMetadata>.Items - свойство
Вся экспортированная метаинформация.
##  __Definition
 **Пространство имён:**
[Chronos.Platform.Composition](N_Chronos_Platform_Composition.htm)  
 **Сборка:** Chronos.Platform (в Chronos.Platform.dll) Версия: 3.6.0.17
C# __Копировать
     public IReadOnlyList<IMetadataExportItem<TMetadata>> Items { get; }
VB __Копировать
     Public ReadOnly Property Items As IReadOnlyList(Of IMetadataExportItem(Of TMetadata))
    	Get
C++ __Копировать
     public:
    virtual property IReadOnlyList<IMetadataExportItem<TMetadata>^>^ Items {
    	IReadOnlyList<IMetadataExportItem<TMetadata>^>^ get () sealed;
    }
F# __Копировать
     abstract Items : IReadOnlyList<IMetadataExportItem<'TMetadata>> with get
    override Items : IReadOnlyList<IMetadataExportItem<'TMetadata>> with get
#### Значение свойства
[IReadOnlyList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist-1)<[IMetadataExportItem](T_Chronos_Platform_Composition_IMetadataExportItem_1.htm)<[TMetadata](T_Chronos_Platform_Composition_AssemblyLoaderResult_1.htm)>>
#### Реализации
[IAssemblyLoaderResult<TMetadata>.Items](P_Chronos_Platform_Composition_IAssemblyLoaderResult_1_Items.htm)  
##  __Заметки
Значение свойства никогда не равно null.
## __См. также
#### Ссылки
[AssemblyLoaderResult<TMetadata> \-
](T_Chronos_Platform_Composition_AssemblyLoaderResult_1.htm)
[Chronos.Platform.Composition - пространство
имён](N_Chronos_Platform_Composition.htm)
