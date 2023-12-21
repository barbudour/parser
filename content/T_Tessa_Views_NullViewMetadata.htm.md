# NullViewMetadata - класс
Метаданные представления заменяющие значение null
## __Definition
 **Пространство имён:** [Tessa.Views](N_Tessa_Views.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class NullViewMetadata : ViewMetadata
VB __Копировать
     Public NotInheritable Class NullViewMetadata
    	Inherits ViewMetadata
C++ __Копировать
     public ref class NullViewMetadata sealed : public ViewMetadata
F# __Копировать
     [<SealedAttribute>]
    type NullViewMetadata = 
        class
            inherit ViewMetadata
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[ValidationObject](T_Tessa_Platform_Validation_ValidationObject.htm) __[ViewMetadataItem](T_Tessa_Views_Metadata_ViewMetadataItem.htm) __[NamedViewMetadataItem](T_Tessa_Views_Metadata_NamedViewMetadataItem.htm) __[ViewMetadata](T_Tessa_Views_Metadata_ViewMetadata.htm) __ NullViewMetadata
##  __Свойства
[Alias](P_Tessa_Views_Metadata_NamedViewMetadataItem_Alias.htm)|  Gets or sets
Псевдоним элемента метаданных  
(Унаследован от
[NamedViewMetadataItem](T_Tessa_Views_Metadata_NamedViewMetadataItem.htm))  
---|---  
[Appearance](P_Tessa_Views_Metadata_ViewMetadata_Appearance.htm)|  Gets or
sets Псевдоним внешнего вида строки представления  
(Унаследован от [ViewMetadata](T_Tessa_Views_Metadata_ViewMetadata.htm))  
[Appearances](P_Tessa_Views_Metadata_ViewMetadata_Appearances.htm)|  Gets
Настройки внешнего вида представления  
(Унаследован от [ViewMetadata](T_Tessa_Views_Metadata_ViewMetadata.htm))  
[AutoWidthRowLimit](P_Tessa_Views_Metadata_ViewMetadata_AutoWidthRowLimit.htm)|
Количество строк в наборе данных пределах которого работает автоматический
расчет ширини столбцов  
(Унаследован от [ViewMetadata](T_Tessa_Views_Metadata_ViewMetadata.htm))  
[Caption](P_Tessa_Views_Metadata_ViewMetadata_Caption.htm)|  Gets or sets the
Название представления.  
(Унаследован от [ViewMetadata](T_Tessa_Views_Metadata_ViewMetadata.htm))  
[Columns](P_Tessa_Views_Metadata_ViewMetadata_Columns.htm)|  Gets список
столбцов представления  
(Унаследован от [ViewMetadata](T_Tessa_Views_Metadata_ViewMetadata.htm))  
[ConnectionAlias](P_Tessa_Views_Metadata_ViewMetadata_ConnectionAlias.htm)|
Алиас строки подключения (из конфигурационного файла веб сервиса `app.json`) к
БД, на которой будет выполняться представление вместо дефолтной базы. В
конфигурационном файле можно указать подключение к любой СУБД. Если, например,
основная база - MSSQL, а подключение к базе Postgres, то запрос генерируется
по правилам Postgres; если же база какая-то другая (например, Oracle), то по
умолчанию используются правила генерации для MSSQL.
С помощью данного параметра можно прописать подключение к другой базе, в том
числе не к базе Tessa, а, например, к какой-то другой информационнной системе.
Укажите null или пустую строку, если используется соединение по умолчанию.
Также на алиас соединения влияет одноимённая настройка в метаинформации
представления.
Для использования этой настройки требуется модуль лицензии "Кластеризация". Он
включён в лицензии Enterprise.
(Унаследован от [ViewMetadata](T_Tessa_Views_Metadata_ViewMetadata.htm))  
[DefaultSortColumn](P_Tessa_Views_Metadata_ViewMetadata_DefaultSortColumn.htm)|
Gets or sets Псевдоним колонки по умолчанию  
(Унаследован от [ViewMetadata](T_Tessa_Views_Metadata_ViewMetadata.htm))  
[DefaultSortDirection](P_Tessa_Views_Metadata_ViewMetadata_DefaultSortDirection.htm)|
Gets or sets Направление сортировки  
(Унаследован от [ViewMetadata](T_Tessa_Views_Metadata_ViewMetadata.htm))  
[DefaultSortingColumns](P_Tessa_Views_Metadata_ViewMetadata_DefaultSortingColumns.htm)|
Gets Список столбцов по которым осуществляется сортировка  
(Унаследован от [ViewMetadata](T_Tessa_Views_Metadata_ViewMetadata.htm))  
[EnableAutoWidth](P_Tessa_Views_Metadata_ViewMetadata_EnableAutoWidth.htm)|
Gets or sets a value indicating whether Признак автоматического расчета ширины
столбцов представления  
(Унаследован от [ViewMetadata](T_Tessa_Views_Metadata_ViewMetadata.htm))  
[ExportDataPageLimit](P_Tessa_Views_Metadata_ViewMetadata_ExportDataPageLimit.htm)|
Gets or sets количество строк запрашиваемых в режиме пейджинга при выгрузке
данных  
(Унаследован от [ViewMetadata](T_Tessa_Views_Metadata_ViewMetadata.htm))  
[Extensions](P_Tessa_Views_Metadata_ViewMetadata_Extensions.htm)|  Gets
возвращает список имен типов расширений  
(Унаследован от [ViewMetadata](T_Tessa_Views_Metadata_ViewMetadata.htm))  
[GroupingColumn](P_Tessa_Views_Metadata_ViewMetadata_GroupingColumn.htm)|
Gets or sets Псевдоним столбца по которому включена группировка по умолчанию  
(Унаследован от [ViewMetadata](T_Tessa_Views_Metadata_ViewMetadata.htm))  
[Instance](P_Tessa_Views_NullViewMetadata_Instance.htm)|  Gets Возвращает
экземпляр объекта  
[IsSealed](P_Tessa_Views_Metadata_ViewMetadataItem_IsSealed.htm)| Признак
того, что объект был защищён от изменений.  
(Унаследован от
[ViewMetadataItem](T_Tessa_Views_Metadata_ViewMetadataItem.htm))  
[Kind](P_Tessa_Views_Metadata_ViewMetadata_Kind.htm)|  Gets or sets Вид
отображения представления  
(Унаследован от [ViewMetadata](T_Tessa_Views_Metadata_ViewMetadata.htm))  
[ModifiedDateTime](P_Tessa_Views_Metadata_ViewMetadata_ModifiedDateTime.htm)|  
(Унаследован от [ViewMetadata](T_Tessa_Views_Metadata_ViewMetadata.htm))  
[MultiSelect](P_Tessa_Views_Metadata_ViewMetadata_MultiSelect.htm)|  Gets or
sets a value indicating whether Признак возможности множественного выбора
строк в представлении. True - возможно выбрать множество строк. False -
возможно выбрать одну строку.(режим по умолчанию)  
(Унаследован от [ViewMetadata](T_Tessa_Views_Metadata_ViewMetadata.htm))  
[PageLimit](P_Tessa_Views_Metadata_ViewMetadata_PageLimit.htm)|  Gets or sets
количество строк возвращаемых в режиме пейджинга  
(Унаследован от [ViewMetadata](T_Tessa_Views_Metadata_ViewMetadata.htm))  
[Paging](P_Tessa_Views_Metadata_ViewMetadata_Paging.htm)|  Gets or sets
Поддержка страничного вывода  
(Унаследован от [ViewMetadata](T_Tessa_Views_Metadata_ViewMetadata.htm))  
[Parameters](P_Tessa_Views_Metadata_ViewMetadata_Parameters.htm)|  Gets
Параметры представления  
(Унаследован от [ViewMetadata](T_Tessa_Views_Metadata_ViewMetadata.htm))  
[QuickSearchParam](P_Tessa_Views_Metadata_ViewMetadata_QuickSearchParam.htm)|
Gets or sets Псевдоним параметра быстрого поиска  
(Унаследован от [ViewMetadata](T_Tessa_Views_Metadata_ViewMetadata.htm))  
[References](P_Tessa_Views_Metadata_ViewMetadata_References.htm)|  Gets список
ссылок представления  
(Унаследован от [ViewMetadata](T_Tessa_Views_Metadata_ViewMetadata.htm))  
[RowCounterVisible](P_Tessa_Views_Metadata_ViewMetadata_RowCounterVisible.htm)|
Gets or sets a value indicating whether Признак необходимости расчета и
отображения количества строк  
(Унаследован от [ViewMetadata](T_Tessa_Views_Metadata_ViewMetadata.htm))  
[RowCountSubset](P_Tessa_Views_Metadata_ViewMetadata_RowCountSubset.htm)|
Gets or sets Алиас подмножества используемого для расчета количество строк,
которые доступны в обрабатываемом представлении.  
(Унаследован от [ViewMetadata](T_Tessa_Views_Metadata_ViewMetadata.htm))  
[SelectionMode](P_Tessa_Views_Metadata_ViewMetadata_SelectionMode.htm)|  Gets
or sets Режим выделения элементов представления  
(Унаследован от [ViewMetadata](T_Tessa_Views_Metadata_ViewMetadata.htm))  
[Subsets](P_Tessa_Views_Metadata_ViewMetadata_Subsets.htm)|  Gets список
подзапросов представления  
(Унаследован от [ViewMetadata](T_Tessa_Views_Metadata_ViewMetadata.htm))  
[TreatAsSingleQuery](P_Tessa_Views_Metadata_ViewMetadata_TreatAsSingleQuery.htm)|
Признак выполнения запроса как обычный запрос на выборку без использования
серверного механизма кэширования представлений в виде хранимых процедур  
(Унаследован от [ViewMetadata](T_Tessa_Views_Metadata_ViewMetadata.htm))  
[TreeGroup](P_Tessa_Views_Metadata_ViewMetadata_TreeGroup.htm)|  Имя столбца
содержащего признак того, что строка содержит только информацию о группе  
(Унаследован от [ViewMetadata](T_Tessa_Views_Metadata_ViewMetadata.htm))  
[TreeGroupDisplayValue](P_Tessa_Views_Metadata_ViewMetadata_TreeGroupDisplayValue.htm)|
Имя столбца содержащего отображаемое имя группы  
(Унаследован от [ViewMetadata](T_Tessa_Views_Metadata_ViewMetadata.htm))  
[TreeGroupId](P_Tessa_Views_Metadata_ViewMetadata_TreeGroupId.htm)|  Имя
столбца содержащего идентификатор группы строки  
(Унаследован от [ViewMetadata](T_Tessa_Views_Metadata_ViewMetadata.htm))  
[TreeGroupParentId](P_Tessa_Views_Metadata_ViewMetadata_TreeGroupParentId.htm)|
Имя столбца содержащего идентификатор родительской группы  
(Унаследован от [ViewMetadata](T_Tessa_Views_Metadata_ViewMetadata.htm))  
[TreeHasChildrenColumn](P_Tessa_Views_Metadata_ViewMetadata_TreeHasChildrenColumn.htm)|
Gets or sets Алиас колонки из представления, которая должна содержать значение
типа bit, которое трактуется как признак наличия дочерних узлов. Если значение
= 1, система показывает плюсик для разворачивания элемента, если 0 - не
показывает. Необязательное, если не задано, то система будет показывать
плюсики у всех элементов дерева до первой попытки их развернуть, когда
выяснится, есть или нет на самом деле у него дочерние элементы. Параметр
обязателен при Kind: Tree.  
(Унаследован от [ViewMetadata](T_Tessa_Views_Metadata_ViewMetadata.htm))  
[TreeId](P_Tessa_Views_Metadata_ViewMetadata_TreeId.htm)|  Имя столбца
идентификатора строки  
(Унаследован от [ViewMetadata](T_Tessa_Views_Metadata_ViewMetadata.htm))  
[TreeParentId](P_Tessa_Views_Metadata_ViewMetadata_TreeParentId.htm)|  Имя
столбца идентификатора родительской строки  
(Унаследован от [ViewMetadata](T_Tessa_Views_Metadata_ViewMetadata.htm))  
[TreeRefParam](P_Tessa_Views_Metadata_ViewMetadata_TreeRefParam.htm)|  Gets or
sets Алиас параметра из текущего вью, который будет использоваться для
получения узлов дерева с определенным родителем. Для получения верхнего
уровня, в параметр передается NULL, для получения дочерних узлов - в параметр
передается значение из RefColumn, которое трактуется как идентификатор
текущего узла дерева. Параметр обязателен при Kind: Tree.  
(Унаследован от [ViewMetadata](T_Tessa_Views_Metadata_ViewMetadata.htm))  
[ValidationResult](P_Tessa_Views_Metadata_ViewMetadata_ValidationResult.htm)|
Gets or sets Информация о валидности представления  
(Унаследован от [ViewMetadata](T_Tessa_Views_Metadata_ViewMetadata.htm))  
##  __Методы
[CheckSealed](M_Tessa_Views_Metadata_ViewMetadataItem_CheckSealed.htm)|
Проверка защиты метаданных от изменения  
(Унаследован от
[ViewMetadataItem](T_Tessa_Views_Metadata_ViewMetadataItem.htm))  
---|---  
[Clone](M_Tessa_Views_Metadata_ViewMetadata_Clone.htm)|  Создает новый объект,
который является копией текущего экземпляра.  
(Унаследован от [ViewMetadata](T_Tessa_Views_Metadata_ViewMetadata.htm))  
[Deserialize](M_Tessa_Views_Metadata_ViewMetadata_Deserialize.htm)|  The
deserialize.  
(Унаследован от [ViewMetadata](T_Tessa_Views_Metadata_ViewMetadata.htm))  
[Equals](M_Tessa_Views_NullViewMetadata_Equals.htm)|  Определяет, равен ли
заданный объект [Object](https://learn.microsoft.com/dotnet/api/system.object)
текущему объекту
[Object](https://learn.microsoft.com/dotnet/api/system.object) .  
(Переопределяет
[Object.Equals(Object)](https://learn.microsoft.com/dotnet/api/system.object.equals#system-
object-equals\(system-object\)))  
[Finalize](https://learn.microsoft.com/dotnet/api/system.object.finalize#system-
object-finalize)| Allows an object to try to free resources and perform other
cleanup operations before it is reclaimed by garbage collection.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetHashCode](M_Tessa_Views_NullViewMetadata_GetHashCode.htm)|  Играет роль
хэш-функции для определенного типа.  
(Переопределяет
[Object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode#system-
object-gethashcode))  
[GetName](M_Tessa_Views_Metadata_NamedViewMetadataItem_GetName.htm)|
Возвращает имя объекта  
(Унаследован от
[NamedViewMetadataItem](T_Tessa_Views_Metadata_NamedViewMetadataItem.htm))  
[GetType](https://learn.microsoft.com/dotnet/api/system.object.gettype#system-
object-gettype)| Gets the
[Type](https://learn.microsoft.com/dotnet/api/system.type) of the current
instance.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetValidationName](M_Tessa_Views_Metadata_ViewMetadata_GetValidationName.htm)|
Возвращает строку, определяющую имя объекта, или null, если имя объекта ещё
неизвестно или объект не содержит имени.  
(Унаследован от [ViewMetadata](T_Tessa_Views_Metadata_ViewMetadata.htm))  
[InternalSeal](M_Tessa_Views_Metadata_ViewMetadata_InternalSeal.htm)|
Включение режимы защиты от изменения для коллекций объектов принадлежащих
классу  
(Унаследован от [ViewMetadata](T_Tessa_Views_Metadata_ViewMetadata.htm))  
[IsValid](M_Tessa_Platform_Validation_ValidationObject_IsValid.htm)| Выполняет
проверку объекта на валидность и возвращает признак того, что объект является
валидным.  
(Унаследован от
[ValidationObject](T_Tessa_Platform_Validation_ValidationObject.htm))  
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[OnDeserialized](M_Tessa_Views_Metadata_ViewMetadataItem_OnDeserialized.htm)|
Вызывается после процесса десериализации элемента метаданных Может
перекрываться в потомках  
(Унаследован от
[ViewMetadataItem](T_Tessa_Views_Metadata_ViewMetadataItem.htm))  
[OnDeserializedMethod](M_Tessa_Views_Metadata_ViewMetadataItem_OnDeserializedMethod.htm)|
Вызывается после десериализации элемента метаданных  
(Унаследован от
[ViewMetadataItem](T_Tessa_Views_Metadata_ViewMetadataItem.htm))  
[OnDeserializing](M_Tessa_Views_Metadata_ViewMetadataItem_OnDeserializing.htm)|
Вызывается перед десериализацией элемента метаданных Может перекрываться в
потомках  
(Унаследован от
[ViewMetadataItem](T_Tessa_Views_Metadata_ViewMetadataItem.htm))  
[OnDeserializingMethod](M_Tessa_Views_Metadata_ViewMetadataItem_OnDeserializingMethod.htm)|
Вызывается перед десериализацией элемента метаданных  
(Унаследован от
[ViewMetadataItem](T_Tessa_Views_Metadata_ViewMetadataItem.htm))  
[OnSerialized](M_Tessa_Views_Metadata_ViewMetadataItem_OnSerialized.htm)|
Вызывается после окончания процесса сериализации элемента метаданных. Может
перекрываться в потомках  
(Унаследован от
[ViewMetadataItem](T_Tessa_Views_Metadata_ViewMetadataItem.htm))  
[OnSerializedMethod](M_Tessa_Views_Metadata_ViewMetadataItem_OnSerializedMethod.htm)|
Вызывается после окончания процесса сериализации элемента метаданных.  
(Унаследован от
[ViewMetadataItem](T_Tessa_Views_Metadata_ViewMetadataItem.htm))  
[OnSerializing](M_Tessa_Views_Metadata_ViewMetadataItem_OnSerializing.htm)|
Вызывается перед началом процесса сериализации элемента метаданных. Может
перекрываться в потомках  
(Унаследован от
[ViewMetadataItem](T_Tessa_Views_Metadata_ViewMetadataItem.htm))  
[OnSerializingMethod](M_Tessa_Views_Metadata_ViewMetadataItem_OnSerializingMethod.htm)|
Вызывается перед началом процесса сериализации элемента метаданных.  
(Унаследован от
[ViewMetadataItem](T_Tessa_Views_Metadata_ViewMetadataItem.htm))  
[Seal](M_Tessa_Views_Metadata_ViewMetadataItem_Seal.htm)| Защищает объект от
изменений.  
(Унаследован от
[ViewMetadataItem](T_Tessa_Views_Metadata_ViewMetadataItem.htm))  
[Serializing](M_Tessa_Views_Metadata_ViewMetadata_Serializing.htm)|  The
serializing.  
(Унаследован от [ViewMetadata](T_Tessa_Views_Metadata_ViewMetadata.htm))  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[Validate()](M_Tessa_Platform_Validation_ValidationObject_Validate.htm)|
Выполняет валидацию объекта и всех его дочерних объектов.  
(Унаследован от
[ValidationObject](T_Tessa_Platform_Validation_ValidationObject.htm))  
[Validate(IValidationResultBuilder)](M_Tessa_Platform_Validation_ValidationObject_Validate_1.htm)|
Выполняет валидацию текущего объекта и всех его дочерних объектов.  
(Унаследован от
[ValidationObject](T_Tessa_Platform_Validation_ValidationObject.htm))  
[ValidateInternal](M_Tessa_Views_Metadata_ViewMetadata_ValidateInternal.htm)|
Выполняет валидацию текущего объекта и всех его дочерних объектов.  
(Унаследован от [ViewMetadata](T_Tessa_Views_Metadata_ViewMetadata.htm))  
##  __Поля
[isDeserializing](F_Tessa_Views_Metadata_ViewMetadataItem_isDeserializing.htm)|
Признак десериализации объекта  
(Унаследован от
[ViewMetadataItem](T_Tessa_Views_Metadata_ViewMetadataItem.htm))  
---|---  
[isSerializing](F_Tessa_Views_Metadata_ViewMetadataItem_isSerializing.htm)|
Признак сериализации объекта  
(Унаследован от
[ViewMetadataItem](T_Tessa_Views_Metadata_ViewMetadataItem.htm))  
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
[Set](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Set.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
##  __См. также
#### Ссылки
[Tessa.Views - пространство имён](N_Tessa_Views.htm)
