# MetadataExportItem<TMetadata>.ImplementedInterfaceTypes - свойство
Типы интерфейсов, которые реализует экспортированный тип. Типы всех
проверяемых интерфейсов должны быть указаны при экспорте.
## __Definition
 **Пространство имён:**
[Chronos.Platform.Composition](N_Chronos_Platform_Composition.htm)  
 **Сборка:** Chronos.Platform (в Chronos.Platform.dll) Версия: 3.6.0.17
C# __Копировать
     public IReadOnlyList<Type> ImplementedInterfaceTypes { get; }
VB __Копировать
     Public ReadOnly Property ImplementedInterfaceTypes As IReadOnlyList(Of Type)
    	Get
C++ __Копировать
     public:
    virtual property IReadOnlyList<Type^>^ ImplementedInterfaceTypes {
    	IReadOnlyList<Type^>^ get () sealed;
    }
F# __Копировать
     abstract ImplementedInterfaceTypes : IReadOnlyList<Type> with get
    override ImplementedInterfaceTypes : IReadOnlyList<Type> with get
#### Значение свойства
[IReadOnlyList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist-1)<[Type](https://learn.microsoft.com/dotnet/api/system.type)>
#### Реализации
[IMetadataExportItem<TMetadata>.ImplementedInterfaceTypes](P_Chronos_Platform_Composition_IMetadataExportItem_1_ImplementedInterfaceTypes.htm)  
##  __См. также
#### Ссылки
[MetadataExportItem<TMetadata> \-
](T_Chronos_Platform_Composition_MetadataExportItem_1.htm)
[Chronos.Platform.Composition - пространство
имён](N_Chronos_Platform_Composition.htm)
