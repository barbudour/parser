# IApplicationCatalogRegistry.Catalogs - свойство
Gets Возвращает список компонентов контейнера расположенных непосредственно в
самом контейнере.
## __Definition
 **Пространство имён:** [Tessa.Applications](N_Tessa_Applications.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
    [NotNullAttribute]
    ReadOnlyObservableCollection<IApplicationCatalog> Catalogs { get; }
VB __Копировать
    <NotNullAttribute>
    ReadOnly Property Catalogs As ReadOnlyObservableCollection(Of IApplicationCatalog)
    	Get
C++ __Копировать
    [NotNullAttribute]
    property ReadOnlyObservableCollection<IApplicationCatalog^>^ Catalogs {
    	ReadOnlyObservableCollection<IApplicationCatalog^>^ get ();
    }
F# __Копировать
     [<NotNullAttribute>]
    abstract Catalogs : ReadOnlyObservableCollection<IApplicationCatalog> with get
#### Значение свойства
[ReadOnlyObservableCollection](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.readonlyobservablecollection-1)<[IApplicationCatalog](T_Tessa_Applications_IApplicationCatalog.htm)>
##  __См. также
#### Ссылки
[IApplicationCatalogRegistry -
](T_Tessa_Applications_IApplicationCatalogRegistry.htm)
[Tessa.Applications - пространство имён](N_Tessa_Applications.htm)
