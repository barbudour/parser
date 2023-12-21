# IDataSourceMetadata - интерфейс
Описание интерфейса предоставляющего доступ к метаданным источника данных
(представления)
## __Definition
 **Пространство имён:** [Tessa.Views](N_Tessa_Views.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IDataSourceMetadata : ICloneable
VB __Копировать
     Public Interface IDataSourceMetadata
    	Inherits ICloneable
C++ __Копировать
     public interface class IDataSourceMetadata : ICloneable
F# __Копировать
     type IDataSourceMetadata = 
        interface
            interface ICloneable
        end
Implements
    [ICloneable](https://learn.microsoft.com/dotnet/api/system.icloneable)
##  __Свойства
[Alias](P_Tessa_Views_IDataSourceMetadata_Alias.htm)|  Gets Псевдоним элемента  
---|---  
[Appearance](P_Tessa_Views_IDataSourceMetadata_Appearance.htm)|  Gets
Псевдоним внешнего вида строки представления  
[Appearances](P_Tessa_Views_IDataSourceMetadata_Appearances.htm)|  Gets
Настройки внешнего вида представления  
[Caption](P_Tessa_Views_IDataSourceMetadata_Caption.htm)|  Gets Заголовок
элемента  
[Columns](P_Tessa_Views_IDataSourceMetadata_Columns.htm)|  Gets Возвращает
список метаданных столбцов  
[DefaultSortColumn](P_Tessa_Views_IDataSourceMetadata_DefaultSortColumn.htm)|
Gets Алиас колонки по умолчанию  
[DefaultSortDirection](P_Tessa_Views_IDataSourceMetadata_DefaultSortDirection.htm)|
Gets Направление сортировки  
[DefaultSortingColumns](P_Tessa_Views_IDataSourceMetadata_DefaultSortingColumns.htm)|
Gets Список столбцов для сортировки  
[EnableAutoWidth](P_Tessa_Views_IDataSourceMetadata_EnableAutoWidth.htm)|
Gets a value indicating whether Признак автоматического расчета ширины
столбцов представления  
[ExpandingIconName](P_Tessa_Views_IDataSourceMetadata_ExpandingIconName.htm)|
Gets Имя значка в развернутом состоянии  
[ExportDataPageLimit](P_Tessa_Views_IDataSourceMetadata_ExportDataPageLimit.htm)|
Gets количество строк запрашиваемых в режиме пагинации при выгрузке данных  
[Extensions](P_Tessa_Views_IDataSourceMetadata_Extensions.htm)|  Gets
возвращает список имен типов расширений  
[IconName](P_Tessa_Views_IDataSourceMetadata_IconName.htm)|  Gets Имя значка в
свернутом состоянии  
[Id](P_Tessa_Views_IDataSourceMetadata_Id.htm)|  Gets Идентификатор  
[MultiSelect](P_Tessa_Views_IDataSourceMetadata_MultiSelect.htm)|  Gets a
value indicating whether Признак возможности множественного выбора строк в
представлении. True - возможно выбрать множество строк. False - возможно
выбрать одну строку.(режим по умолчанию)  
[PageLimit](P_Tessa_Views_IDataSourceMetadata_PageLimit.htm)|  Gets количество
строк возвращаемых в режиме пейджинга  
[Paging](P_Tessa_Views_IDataSourceMetadata_Paging.htm)|  Gets Поддержка
постраничного вывода  
[Parameters](P_Tessa_Views_IDataSourceMetadata_Parameters.htm)|  Gets
возвращает список метаданных параметров доступных в компоненте  
[ParametersValues](P_Tessa_Views_IDataSourceMetadata_ParametersValues.htm)|
Gets Возвращает список значений параметров заданных в метаданных источника
данных  
[References](P_Tessa_Views_IDataSourceMetadata_References.htm)|  Gets список
ссылок представления  
[RowCounterVisible](P_Tessa_Views_IDataSourceMetadata_RowCounterVisible.htm)|
Gets a value indicating whether Признак необходимости расчета и отображения
количества строк  
[RowCountSubset](P_Tessa_Views_IDataSourceMetadata_RowCountSubset.htm)|  Gets
Алиас подмножества используемого для расчета количество строк, которые
доступны в обрабатываемом представлении.  
[SelectionMode](P_Tessa_Views_IDataSourceMetadata_SelectionMode.htm)|  Gets
Режим выделения элементов представления  
[SourceType](P_Tessa_Views_IDataSourceMetadata_SourceType.htm)|  Gets
Возвращает тип источника данных  
[Subsets](P_Tessa_Views_IDataSourceMetadata_Subsets.htm)|  Gets Возвращает
список подмножеств  
## __Методы
[Clone](https://learn.microsoft.com/dotnet/api/system.icloneable.clone#system-
icloneable-clone)| Creates a new object that is a copy of the current
instance.  
(Унаследован от
[ICloneable](https://learn.microsoft.com/dotnet/api/system.icloneable))  
---|---  
[GetViewMetadata](M_Tessa_Views_IDataSourceMetadata_GetViewMetadata.htm)|
Возвращает адаптируемые метаданные  
[IsSpecialSubset](M_Tessa_Views_IDataSourceMetadata_IsSpecialSubset.htm)|
Осуществляет проверку является ли подмножество с псевдонимом alias системным  
##  __Методы расширения
[IsEmptySource](M_Tessa_Views_Workplaces_DataSourceMetadataHelper_IsEmptySource.htm)|
Осуществляет проверку является ли источник metadata нулевой ссылкой или
недоступным источником метаданных  
(Определяется
[DataSourceMetadataHelper](T_Tessa_Views_Workplaces_DataSourceMetadataHelper.htm))  
---|---  
##  __См. также
#### Ссылки
[Tessa.Views - пространство имён](N_Tessa_Views.htm)
