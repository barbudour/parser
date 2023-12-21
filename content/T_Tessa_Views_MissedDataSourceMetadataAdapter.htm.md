# MissedDataSourceMetadataAdapter - класс
Адаптер отсутствующих метаданных
## __Definition
 **Пространство имён:** [Tessa.Views](N_Tessa_Views.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
    [SerializableAttribute]
    [DataContractAttribute]
    public sealed class MissedDataSourceMetadataAdapter : IDataSourceMetadata, 
    	ICloneable
VB __Копировать
    <SerializableAttribute>
    <DataContractAttribute>
    Public NotInheritable Class MissedDataSourceMetadataAdapter
    	Implements IDataSourceMetadata, ICloneable
C++ __Копировать
    [SerializableAttribute]
    [DataContractAttribute]
    public ref class MissedDataSourceMetadataAdapter sealed : IDataSourceMetadata, 
    	ICloneable
F# __Копировать
     [<SealedAttribute>]
    [<SerializableAttribute>]
    [<DataContractAttribute>]
    type MissedDataSourceMetadataAdapter = 
        class
            interface IDataSourceMetadata
            interface ICloneable
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ MissedDataSourceMetadataAdapter
Implements
    [ICloneable](https://learn.microsoft.com/dotnet/api/system.icloneable), [IDataSourceMetadata](T_Tessa_Views_IDataSourceMetadata.htm)
##  __Конструкторы
[MissedDataSourceMetadataAdapter](M_Tessa_Views_MissedDataSourceMetadataAdapter__ctor.htm)|
Initializes a new instance of the MissedDataSourceMetadataAdapter class.
Инициализирует новый экземпляр класса
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
---|---  
##  __Свойства
[Alias](P_Tessa_Views_MissedDataSourceMetadataAdapter_Alias.htm)|  Псевдоним
элемента  
---|---  
[Appearance](P_Tessa_Views_MissedDataSourceMetadataAdapter_Appearance.htm)|
Псевдоним внешнего вида строки представления  
[Appearances](P_Tessa_Views_MissedDataSourceMetadataAdapter_Appearances.htm)|
Настройки внешнего вида представления  
[Caption](P_Tessa_Views_MissedDataSourceMetadataAdapter_Caption.htm)|
Заголовок элемента  
[Columns](P_Tessa_Views_MissedDataSourceMetadataAdapter_Columns.htm)|
Возвращает список метаданных столбцов  
[DefaultSortColumn](P_Tessa_Views_MissedDataSourceMetadataAdapter_DefaultSortColumn.htm)|
Алиас колонки по умолчанию  
[DefaultSortDirection](P_Tessa_Views_MissedDataSourceMetadataAdapter_DefaultSortDirection.htm)|
Направление сортировки  
[DefaultSortingColumns](P_Tessa_Views_MissedDataSourceMetadataAdapter_DefaultSortingColumns.htm)|
Gets Список столбцов для сортировки  
[EnableAutoWidth](P_Tessa_Views_MissedDataSourceMetadataAdapter_EnableAutoWidth.htm)|
Признак автоматического расчета ширины столбцов представления  
[ExpandingIconName](P_Tessa_Views_MissedDataSourceMetadataAdapter_ExpandingIconName.htm)|
Имя значка в развернутом состоянии  
[ExportDataPageLimit](P_Tessa_Views_MissedDataSourceMetadataAdapter_ExportDataPageLimit.htm)|
Количество строк запрашиваемых в режиме пейджинга при выгрузке данных  
[Extensions](P_Tessa_Views_MissedDataSourceMetadataAdapter_Extensions.htm)|
Список имен типов расширений  
[IconName](P_Tessa_Views_MissedDataSourceMetadataAdapter_IconName.htm)|  Имя
значка в свернутом состоянии  
[Id](P_Tessa_Views_MissedDataSourceMetadataAdapter_Id.htm)|  Идентификатор  
[MultiSelect](P_Tessa_Views_MissedDataSourceMetadataAdapter_MultiSelect.htm)|
Признак возможности множественного выбора строк в представлении. True -
возможно выбрать множество строк. False - возможно выбрать одну строку.(режим
по умолчанию)  
[OriginalSourceType](P_Tessa_Views_MissedDataSourceMetadataAdapter_OriginalSourceType.htm)|
Тип исходного источника данных.  
[PageLimit](P_Tessa_Views_MissedDataSourceMetadataAdapter_PageLimit.htm)|
Количество строк возвращаемых в режиме пейджинга  
[Paging](P_Tessa_Views_MissedDataSourceMetadataAdapter_Paging.htm)|  Поддержка
пролистывания  
[Parameters](P_Tessa_Views_MissedDataSourceMetadataAdapter_Parameters.htm)|
Возвращает список метаданных параметров доступных в компоненте  
[ParametersValues](P_Tessa_Views_MissedDataSourceMetadataAdapter_ParametersValues.htm)|
Возвращает список значений параметров заданных в метаданных источника данных  
[References](P_Tessa_Views_MissedDataSourceMetadataAdapter_References.htm)|
Список ссылок представления  
[RowCounterVisible](P_Tessa_Views_MissedDataSourceMetadataAdapter_RowCounterVisible.htm)|
Признак необходимости расчета и отображения количества строк  
[RowCountSubset](P_Tessa_Views_MissedDataSourceMetadataAdapter_RowCountSubset.htm)|
Алиас подмножества используемого для расчета количество строк, которые
доступны в обрабатаываемом представлении.  
[SelectionMode](P_Tessa_Views_MissedDataSourceMetadataAdapter_SelectionMode.htm)|
Режим выделения элементов представления  
[SourceType](P_Tessa_Views_MissedDataSourceMetadataAdapter_SourceType.htm)|
Возвращает тип источника данных  
[Subsets](P_Tessa_Views_MissedDataSourceMetadataAdapter_Subsets.htm)|
Возвращает список подмножеств  
## __Методы
[Clone](M_Tessa_Views_MissedDataSourceMetadataAdapter_Clone.htm)|  Создает
новый объект, который является копией текущего экземпляра.  
---|---  
[Equals](https://learn.microsoft.com/dotnet/api/system.object.equals#system-
object-equals\(system-object\))| Determines whether the specified object is
equal to the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[Finalize](https://learn.microsoft.com/dotnet/api/system.object.finalize#system-
object-finalize)| Allows an object to try to free resources and perform other
cleanup operations before it is reclaimed by garbage collection.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetHashCode](https://learn.microsoft.com/dotnet/api/system.object.gethashcode#system-
object-gethashcode)| Serves as the default hash function.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetType](https://learn.microsoft.com/dotnet/api/system.object.gettype#system-
object-gettype)| Gets the
[Type](https://learn.microsoft.com/dotnet/api/system.type) of the current
instance.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetViewMetadata](M_Tessa_Views_MissedDataSourceMetadataAdapter_GetViewMetadata.htm)|
Возвращает адаптируемые метаданные  
[IsSpecialSubset](M_Tessa_Views_MissedDataSourceMetadataAdapter_IsSpecialSubset.htm)|
Осуществляет проверку является ли подмножество с псевдонимом alias системным  
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
##  __Методы расширения
[Get](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Get.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
---|---  
[InternalMarkerCanvas](M_Tessa_UI_Views_Charting_Annotations_AnnotationInternalsAccessor_InternalMarkerCanvas.htm)|
Возвращает маркер аннотации  
(Определяется
[AnnotationInternalsAccessor](T_Tessa_UI_Views_Charting_Annotations_AnnotationInternalsAccessor.htm))  
[Invoke](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Invoke.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
[IsEmptySource](M_Tessa_Views_Workplaces_DataSourceMetadataHelper_IsEmptySource.htm)|
Осуществляет проверку является ли источник metadata нулевой ссылкой или
недоступным источником метаданных  
(Определяется
[DataSourceMetadataHelper](T_Tessa_Views_Workplaces_DataSourceMetadataHelper.htm))  
[Set](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Set.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
##  __См. также
#### Ссылки
[Tessa.Views - пространство имён](N_Tessa_Views.htm)
