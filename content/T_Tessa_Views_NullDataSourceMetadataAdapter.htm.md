# NullDataSourceMetadataAdapter - класс
Пустой источник метаданных
## __Definition
 **Пространство имён:** [Tessa.Views](N_Tessa_Views.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
    [SerializableAttribute]
    [DataContractAttribute]
    public sealed class NullDataSourceMetadataAdapter : IDataSourceMetadata, 
    	ICloneable
VB __Копировать
    <SerializableAttribute>
    <DataContractAttribute>
    Public NotInheritable Class NullDataSourceMetadataAdapter
    	Implements IDataSourceMetadata, ICloneable
C++ __Копировать
    [SerializableAttribute]
    [DataContractAttribute]
    public ref class NullDataSourceMetadataAdapter sealed : IDataSourceMetadata, 
    	ICloneable
F# __Копировать
     [<SealedAttribute>]
    [<SerializableAttribute>]
    [<DataContractAttribute>]
    type NullDataSourceMetadataAdapter = 
        class
            interface IDataSourceMetadata
            interface ICloneable
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ NullDataSourceMetadataAdapter
Implements
    [ICloneable](https://learn.microsoft.com/dotnet/api/system.icloneable), [IDataSourceMetadata](T_Tessa_Views_IDataSourceMetadata.htm)
##  __Свойства
[Alias](P_Tessa_Views_NullDataSourceMetadataAdapter_Alias.htm)|  Gets
Псевдоним элемента  
---|---  
[Appearance](P_Tessa_Views_NullDataSourceMetadataAdapter_Appearance.htm)|
Gets Псевдоним внешнего вида строки представления  
[Appearances](P_Tessa_Views_NullDataSourceMetadataAdapter_Appearances.htm)|
Gets Настройки внешнего вида представления  
[Caption](P_Tessa_Views_NullDataSourceMetadataAdapter_Caption.htm)|  Gets
Заголовок элемента  
[Columns](P_Tessa_Views_NullDataSourceMetadataAdapter_Columns.htm)|
Возвращает список метаданных столбцов  
[DefaultSortColumn](P_Tessa_Views_NullDataSourceMetadataAdapter_DefaultSortColumn.htm)|
Gets Алиас колонки по умолчанию  
[DefaultSortDirection](P_Tessa_Views_NullDataSourceMetadataAdapter_DefaultSortDirection.htm)|
Gets Направление сортировки  
[DefaultSortingColumns](P_Tessa_Views_NullDataSourceMetadataAdapter_DefaultSortingColumns.htm)|
Gets Список столбцов для сортировки  
[EnableAutoWidth](P_Tessa_Views_NullDataSourceMetadataAdapter_EnableAutoWidth.htm)|
Gets a value indicating whether Признак автоматического расчета ширины
столбцов представления  
[ExpandingIconName](P_Tessa_Views_NullDataSourceMetadataAdapter_ExpandingIconName.htm)|
Gets Имя значка в развернутом состоянии  
[ExportDataPageLimit](P_Tessa_Views_NullDataSourceMetadataAdapter_ExportDataPageLimit.htm)|
Gets количество строк запрашиваемых в режиме пейджинга при выгрузке данных  
[Extensions](P_Tessa_Views_NullDataSourceMetadataAdapter_Extensions.htm)|
Gets возвращает список имен типов расширений  
[IconName](P_Tessa_Views_NullDataSourceMetadataAdapter_IconName.htm)|  Gets
Имя значка в свернутом состоянии  
[Id](P_Tessa_Views_NullDataSourceMetadataAdapter_Id.htm)|  Gets Идентификатор  
[Instance](P_Tessa_Views_NullDataSourceMetadataAdapter_Instance.htm)|  Gets
Экземпляр объекта  
[MultiSelect](P_Tessa_Views_NullDataSourceMetadataAdapter_MultiSelect.htm)|
Gets a value indicating whether Признак возможности множественного выбора
строк в представлении. True - возможно выбрать множество строк. False -
возможно выбрать одну строку.(режим по умолчанию)  
[PageLimit](P_Tessa_Views_NullDataSourceMetadataAdapter_PageLimit.htm)|  Gets
количество строк возвращаемых в режиме пейджинга  
[Paging](P_Tessa_Views_NullDataSourceMetadataAdapter_Paging.htm)|  Gets
Поддержка пролистывания  
[Parameters](P_Tessa_Views_NullDataSourceMetadataAdapter_Parameters.htm)|
Возвращает список метаданных параметров доступных в компоненте  
[ParametersValues](P_Tessa_Views_NullDataSourceMetadataAdapter_ParametersValues.htm)|
Возвращает список значений параметров заданных в метаданных источника данных  
[References](P_Tessa_Views_NullDataSourceMetadataAdapter_References.htm)|
Gets список ссылок представления  
[RowCounterVisible](P_Tessa_Views_NullDataSourceMetadataAdapter_RowCounterVisible.htm)|
Gets a value indicating whether Признак необходимости расчета и отображения
количества строк  
[RowCountSubset](P_Tessa_Views_NullDataSourceMetadataAdapter_RowCountSubset.htm)|
Gets Алиас подмножества используемого для расчета количество строк, которые
доступны в обрабатаываемом представлении.  
[SelectionMode](P_Tessa_Views_NullDataSourceMetadataAdapter_SelectionMode.htm)|
Gets Режим выделения элементов представления  
[SourceType](P_Tessa_Views_NullDataSourceMetadataAdapter_SourceType.htm)|
Gets Возвращает тип источника данных  
[Subsets](P_Tessa_Views_NullDataSourceMetadataAdapter_Subsets.htm)|
Возвращает список подмножеств  
## __Методы
[Clone](M_Tessa_Views_NullDataSourceMetadataAdapter_Clone.htm)|  Создает новый
объект, который является копией текущего экземпляра.  
---|---  
[Equals](M_Tessa_Views_NullDataSourceMetadataAdapter_Equals.htm)|  Определяет,
равен ли заданный объект
[Object](https://learn.microsoft.com/dotnet/api/system.object) текущему
объекту [Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Переопределяет
[Object.Equals(Object)](https://learn.microsoft.com/dotnet/api/system.object.equals#system-
object-equals\(system-object\)))  
[Finalize](https://learn.microsoft.com/dotnet/api/system.object.finalize#system-
object-finalize)| Allows an object to try to free resources and perform other
cleanup operations before it is reclaimed by garbage collection.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetHashCode](M_Tessa_Views_NullDataSourceMetadataAdapter_GetHashCode.htm)|
Играет роль хэш-функции для определенного типа.  
(Переопределяет
[Object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode#system-
object-gethashcode))  
[GetType](https://learn.microsoft.com/dotnet/api/system.object.gettype#system-
object-gettype)| Gets the
[Type](https://learn.microsoft.com/dotnet/api/system.type) of the current
instance.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetViewMetadata](M_Tessa_Views_NullDataSourceMetadataAdapter_GetViewMetadata.htm)|
Возвращает адаптируемые метаданные  
[IsSpecialSubset](M_Tessa_Views_NullDataSourceMetadataAdapter_IsSpecialSubset.htm)|
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
##  __Операторы
[Equality(NullDataSourceMetadataAdapter,
NullDataSourceMetadataAdapter)](M_Tessa_Views_NullDataSourceMetadataAdapter_op_Equality.htm)|
The ==.  
---|---  
[Inequality(NullDataSourceMetadataAdapter,
NullDataSourceMetadataAdapter)](M_Tessa_Views_NullDataSourceMetadataAdapter_op_Inequality.htm)|
The !=.  
## __Методы расширения
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
